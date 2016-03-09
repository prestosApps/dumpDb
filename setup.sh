#!/bin/bash

sudo mkdir /usr/local/bin/dumpTest
sudo mkdir /var/lib/dumpTest

cd ~/dump1090
sudo cp * /usr/local/bin/dumpTest

cd /usr/local/bin/dumpTest
sudo rm setup.sh

sudo python /usr/local/bin/dumpTest/databaseSetup.py
