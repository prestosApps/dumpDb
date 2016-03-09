import os
import sqlite3

db_filename = '/var/lib/dumpTest/dump1090.db'
schema_filename = '/usr/local/bin/dumpTest/schema.sql'

db_is_new = not os.path.exists(db_filename)

conn = sqlite3.connect(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        with open(schema_filename, 'rt') as f:
            schema = f.read()
            conn.executescript(schema)
    else:
        print 'Database already exists. Setup skipped.'
