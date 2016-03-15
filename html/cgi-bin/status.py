#!/usr/bin/env python

import json
import urllib2
import datetime

receiver = urllib2.urlopen('http://192.168.1.79/dump1090/data/receiver.json')
stats = urllib2.urlopen('http://192.168.1.79/dump1090/data/stats.json')

receiverData = json.load(receiver)
statsData = json.load(stats)

version = receiverData.get('version','unknown')
timestamp =  statsData.get('total').get('start')

startDate = datetime.datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M')

print version + "," + startDate
