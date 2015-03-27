__author__ = 'David Rossiter'

from Logging import logger
import time
import datetime

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