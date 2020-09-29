#!/bin/sh

set -eu

wget -O - https://debian.neo4j.org/neotechnology.gpg.key | sudo apt-key add -
echo 'deb https://debian.neo4j.org/repo stable/' | sudo tee -a /etc/apt/sources.list.d/neo4j.list
sudo apt-get update

sudo apt-get install neo4j=1:3.5.5 -y

pip install neomodel

sudo neo4j-admin set-initial-password password
sudo neo4j start