#!/bin/bash

sudo mkdir /usr/local/bin/dumpDb
sudo mkdir /var/lib/dumpDb

cd ~/dump1090
sudo cp * /usr/local/bin/dumpDb

cd /usr/local/bin/dumpDb
sudo rm setup.sh

sudo python /usr/local/bin/dumpDb/databaseSetup.py
