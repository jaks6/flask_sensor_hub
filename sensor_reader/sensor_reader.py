#!/usr/bin/python
import sqlite3
import hat_sensors
import datetime
import time
import os


cur_path = os.path.dirname(os.path.realpath(__file__))

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect( cur_path + '/sqlite.db')
    rv.row_factory = sqlite3.Row
    print "Opened database successfully";
    return rv

def insert_to_db(avg):
    db.execute('insert into "values" (name, value, timestamp) values (?, ?, ?)',
                 ['avg_temp', avg, datetime.datetime.now()])

    db.execute('delete from "values" where timestamp <= datetime("now", "-1 minutes")')
    db.commit()

db = connect_db()
with open( cur_path + '/schema.sql',  mode='r') as f:
    db.cursor().executescript(f.read())
    print 'Initialized the database.'
db.commit()

print("Writing sensor values to DB.. Ctrl + C to stop.");
try:
    while(True):
        sensor_values = hat_sensors.get_values()
        avg = hat_sensors.avg_temp()
        insert_to_db(avg)
        time.sleep(2);
except KeyboardInterrupt:
    print " Closing DB..."
    db.close();
    print 'Finished.'