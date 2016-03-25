#!/usr/bin/env python

import sqlite3
import datetime
import json
import cgi
import cgitb

cgitb.enable()
form = cgi.FieldStorage()

conn = sqlite3.connect('/var/lib/dumpDb/dump1090.db')
cursor = conn.cursor()

hexcode = (form.getvalue("hexcode"),)

cursor.execute('select * from aircraft where hexcode = ?', hexcode)

row = cursor.fetchall()

conn.close()

print json.dumps(row)
