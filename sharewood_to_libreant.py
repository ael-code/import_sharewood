import csv
import requests
import json
import string

inputFile = "catalogo_sharewood.csv"
libreantIP = "localhost"
libreantPort = 5001
apiUrlPrefix = "/api/v1"

volumesUrl = "http://{}:{}{}/volumes/".format(libreantIP, libreantPort, apiUrlPrefix)


def beautify_row(row):
    row['_language'] = "it"
    row['title'] = string.capitalize(row['TITOLO'])
    row['authors'] = beautify_authors(row['AUTORE'])
    return json.dumps(row)

def beautify_authors(authors):
    return [string.capitalize(a) for a in string.split(authors)]


count=0
with open(inputFile) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        metadata = beautify_row(row)
        r = requests.post(volumesUrl, data={'metadata':metadata})
        if r.status_code is not 201:
            print r.text
            exit(1)
        print(reader.line_num)
