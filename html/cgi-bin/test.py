#!/usr/bin/env python

import sqlite3

conn = sqlite3.connect('/var/lib/dumpDb/dump1090.db')
cursor = conn.cursor()

cursor.execute('select totalAircraftSeen, aircraftSeenToday, lastUpdated from stats')
response = cursor.fetchone()

conn.close()

print str(response[0]) + "," + str(response[1]) + "," + response[2] 
