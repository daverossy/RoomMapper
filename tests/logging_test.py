__author__ = 'David Rossiter'

from Logging import logger
import time
import datetime
import sqlite3

# Logging Test

# Set test variables
ts = time.time()
session_id = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
timestamp = session_id
orientation = 0
location_x = 4
location_y = 2
fsd = 12.65
rsd = 10.25
lsd = 6.26
bsd = 4.64
straight_amount = 1

# Log sensor readings, movement decision, movement distance and timestamp
logger(session_id, timestamp, orientation, location_x, location_y, fsd, rsd, lsd, bsd, "Forward", straight_amount)

# Connect to SQLite database or create database if not already existing
conn = sqlite3.connect('mapping.db')

# Connection
c = conn.cursor()

# Create table if not already existing
c.execute('''CREATE TABLE IF NOT EXISTS mapping
                 (session_id text, timestamp text, orientation integer, location_x integer, location_y integer, fsd_location_x integer, fsd_location_y integer, rsd_location_x integer, rsd_location_y integer, lsd_location_x integer, lsd_location_y integer, bsd_location_x integer, bsd_location_y integer, direction text, movement_value integer)''')

# Commit changes
conn.commit()

print "\nEntire database contents:\n"
for row in c.execute("SELECT * FROM mapping"):
    print row

# Close connection
conn.close()