import json
import sqlite3
import urllib2
import datetime
import time

receiver = urllib2.urlopen('http://192.168.1.79/dump1090/data/receiver.json')
response = urllib2.urlopen('http://192.168.1.79/dump1090/data/aircraft.json')

receiverData = json.load(receiver)
data = json.load(response)

history = receiverData.get('history',0)
print "Receiver History: ", history

conn = sqlite3.connect('/var/lib/dumpDb/dump1090.db')
cursor = conn.cursor()

for i in range(history):
    label = 'http://192.168.1.79/dump1090/data/history_'
    historyUrl = label + str(i) + '.json'
    historyResponse = urllib2.urlopen(historyUrl)
    historyJson = json.load(historyResponse)

    print 'Processing: ' + str(i)

    for a in historyJson['aircraft']:
        if a.get('mlat') == None:
            mlat = 0
        else:
            mlat = 1
        cursor.execute("insert into aircraft values (null,?,?,?,?,?,?,?,?,?,?,?,?,?)", (a.get('hex',''), a.get('squawk',''), a.get('flight',''), a.get('lat',0), a.get('lon',0), a.get('altitude',0), a.get('vertRate',0), a.get('track',0), a.get('speed',0), a.get('messages',0), mlat, historyJson.get('now',0), a.get('rssi',0)))

#Remove duplicate entries from the database
print 'Deleting duplicates...'
cursor.execute("delete from aircraft where _id not in(select min(_id) from aircraft group by hexcode, squawk, flight, lat, lon, altitude, vertRate, track, speed, messages, rssi)")    
conn.commit()

#Get basic stats data
cursor.execute('select count(distinct(hexcode)) from aircraft')
totalAircraftSeen = cursor.fetchone()[0]
cursor.execute('delete from stats')

epoch = datetime.datetime(1970,1,1)
today = datetime.date.today()
todayStart = datetime.datetime.combine(today, datetime.time.min)
todayEnd = datetime.datetime.combine(today, datetime.time.max)

start = (todayStart - epoch).total_seconds()
end = (todayEnd - epoch).total_seconds()

cursor.execute('select count(distinct(hexcode)) from aircraft where timeSeen between ? and ?', (start, end))
aircraftSeenToday = cursor.fetchone()[0]
print aircraftSeenToday

updateTime = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')

cursor.execute('insert into stats (totalAircraftSeen, aircraftSeenToday, lastUpdated) values (?,?,?)', (totalAircraftSeen, aircraftSeenToday,updateTime,))

conn.commit()

conn.close()
print 'Done...'
