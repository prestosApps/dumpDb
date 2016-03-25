#!/usr/bin/env python

import sqlite3
import datetime
import json

conn = sqlite3.connect('/var/lib/dumpDb/dump1090.db')
cursor = conn.cursor()

epoch = datetime.datetime(1970,1,1)
today = datetime.date.today()
todayStart = datetime.datetime.combine(today, datetime.time.min)
todayEnd = datetime.datetime.combine(today, datetime.time.max)

start = (todayStart - epoch).total_seconds()
end = (todayEnd - epoch).total_seconds()

cursor.execute('select hexcode, count(hexcode) from aircraft where timeSeen between ? and ? group by hexcode', (start, end))

row = cursor.fetchall()

conn.close()

print json.dumps(row)
