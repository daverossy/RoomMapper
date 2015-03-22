__author__ = 'David Rossiter'

import datetime
import time
from Logging import logger
from Sensors import sonar_reading
from Motors import move
from LED_System import led
import sqlite3


def database():
    # Connect to SQLite database or create database if not already existing
    conn = sqlite3.connect('mapping.db')

    # Connection
    c = conn.cursor()

    # Create table if not already existing
    c.execute('''CREATE TABLE IF NOT EXISTS mapping
                 (session_id integer,timestamp text, fsd real, rsd real, lsd real, bsd real, direction text, movement_value integer)''')

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


def session_id():
    # Connect to SQLite database or create database if not already existing
    conn = sqlite3.connect('mapping.db')
    # Connection
    c = conn.cursor()
    # Insert a row of data
    c.execute("SELECT max(session_id) FROM mapping")

    session = (c.fetchall())

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

    if session == null:
        session = 1
    else:
        session = session + 1

    return session


def algorithm(session_id):
    print "Starting..."

    # Initialise variables
    min_distance = 15
    rotation_amount = 2
    straight_amount = 2

    # Run program while loop, will need a stop and start mechanism
    while True:
        # Get sonar readings
        fsd = sonar_reading("FSD")
        rsd = sonar_reading("RSD")
        lsd = sonar_reading("LSD")
        bsd = sonar_reading("BSD")

        # Get timestamp
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        if fsd > min_distance:
            # Set LED matrix to forwards arrow
            led("Forward")
            # Log sensor readings, movement decision, movement distance and timestamp
            logger(session_id, timestamp, fsd, rsd, lsd, bsd, "Forward", straight_amount)
            # Call move forwards method and tell the motors to move forwards
            move("Forward", straight_amount)

        elif (rsd or lsd) > min_distance:
            if rsd > lsd:
                # Set LED matrix to right arrow
                led("Right")
                # Log sensor readings, movement decision, movement distance and timestamp
                logger(session_id, timestamp, fsd, rsd, lsd, bsd, "Right", rotation_amount)
                # Turn Right
                move("Right", rotation_amount)

            else:
                # Set LED matrix to left arrow
                led("Left")
                # Log sensor readings, movement decision, movement distance and timestamp
                logger(session_id, timestamp, fsd, rsd, lsd, bsd, "Left", rotation_amount)
                # Turn Left
                move("Left", rotation_amount)

        elif bsd > min_distance:
            # Set LED matrix to reverse arrow
            led("Reverse")
            # Log sensor readings, movement decision, movement distance and timestamp
            logger(session_id, timestamp, fsd, rsd, lsd, bsd, "Reverse", straight_amount)
            # Do Reverse
            move("Reverse", straight_amount)

        else:
            # Set LED matrix to exclaimation mark
            led("Halt")
            # Log data about point where robot got suck
            logger(session_id, timestamp, fsd, rsd, lsd, bsd, "Stuck", straight_amount)


# Run database preparation
database()
# Get session id
session_id = session_id()
# Run algorithm
algorithm(session_id)