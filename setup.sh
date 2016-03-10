#!/bin/bash

sudo mkdir /usr/local/bin/dumpDb
sudo mkdir /var/lib/dumpDb

cd ~/dumpDb
sudo cp * /usr/local/bin/dumpDb

cd /usr/local/bin/dumpDb
sudo rm setup.sh

sudo python /usr/local/bin/dumpDb/databaseSetup.py

(sudo crontab -l 2>/dev/null; echo -e "0 * * * * /usr/local/bin/dumpDb/loadData.py\n") | sudo crontab -
