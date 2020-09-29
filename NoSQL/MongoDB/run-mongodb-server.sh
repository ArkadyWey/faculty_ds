#!/bin/sh

set -eu

sudo apt update
sudo apt install -y mongodb

for conda_env in Python2 Python3; do
    conda install -y pymongo -n "$conda_env" --yes
done

sudo mkdir -p /data/db
sudo mongod --quiet --fork --logpath /var/log/mongod.log
