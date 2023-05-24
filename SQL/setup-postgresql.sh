#!/bin/bash

set -e

sudo apt update -y
sudo apt install postgresql -y
sudo service postgresql start
sudo -u postgres psql -c "create user faculty"
sudo -u postgres psql -c "create schema input"
sudo -u postgres psql -c "grant all on schema input to faculty"
sudo -u postgres psql -c "grant all on all tables in schema input to faculty"
