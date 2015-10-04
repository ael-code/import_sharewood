#!/bin/bash

set -e

systemctl stop elasticsearch
rm -rf /var/lib/elasticsearch/elasticsearch/nodes/0/indices/sharewood
systemctl start elasticsearch
