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
                 (session_id integer, timestamp text, orientation integer, location_x integer, location_y integer, fsd_location_x integer, fsd_location_y integer, rsd_location_x integer, rsd_location_y integer, lsd_location_x integer, lsd_location_y integer, bsd_location_x integer, bsd_location_y integer, direction text, movement_value integer)''')

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
        session += 1

    return session


def algorithm(session_id):
    print "Starting..."

    # Initialise variables
    min_distance = 15
    rotation_amount = 2
    straight_amount = 2
    location_x = 0
    location_y = 0
    orientation = 0

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
            if orientation == 0:
                # Set location co-ordinates to y - 1
                location_y += 1
            elif orientation == 90:
                location_x += 1
            elif orientation == 180:
                location_y -= 1
            elif orientation == 270:
                location_x -= 1
            else:
                print "Orientation error!"
            # Do nothing to orientation

            # Set LED matrix to forwards arrow
            led("Forward")
            # Log sensor readings, movement decision, movement distance and timestamp
            logger(session_id, timestamp, orientation, location_x, location_y, fsd, rsd, lsd, bsd, "Forward", straight_amount)
            # Call move forwards method and tell the motors to move forwards
            move("Forward", straight_amount)

        elif (rsd or lsd) > min_distance:
            if rsd > lsd:
                # Don't change location, just change orientation for next movement

                # Set orientation relative to current orientation
                if orientation == 0:
                    orientation = 90
                elif orientation == 90:
                    orientation = 180
                elif orientation == 180:
                    orientation = 270
                elif orientation == 270:
                    orientation = 0
                else:
                    print "Error in orientation setting"
                # Set LED matrix to right arrow
                led("Right")
                # Log sensor readings, movement decision, movement distance and timestamp
                logger(session_id, timestamp, orientation, location_x, location_y, fsd, rsd, lsd, bsd, "Right", straight_amount)
                # Turn Right
                move("Right", rotation_amount)

            else:
                # Don't change location, just change orientation for next movement

                # Set orientation relative to current orientation
                if orientation == 0:
                    orientation = 270
                elif orientation == 90:
                    orientation = 0
                elif orientation == 180:
                    orientation = 90
                elif orientation == 270:
                    orientation = 180
                else:
                    print "Error in orientation setting"
                # Set LED matrix to left arrow
                led("Left")
                # Log sensor readings, movement decision, movement distance and timestamp
                logger(session_id, timestamp, orientation, location_x, location_y, fsd, rsd, lsd, bsd, "Left", straight_amount)
                # Turn Left
                move("Left", rotation_amount)

        elif bsd > min_distance:
            if orientation == 0:
                # Set location co-ordinates to y - 1
                location_y -= 1
            elif orientation == 90:
                location_x -= 1
            elif orientation == 180:
                location_y += 1
            elif orientation == 270:
                location_x += 1
            else:
                print "Orientation error!"
            # Do nothing to orientation

            # Set LED matrix to reverse arrow
            led("Reverse")
            # Log sensor readings, movement decision, movement distance and timestamp
            logger(session_id, timestamp, orientation, location_x, location_y, fsd, rsd, lsd, bsd, "Reverse", straight_amount)
            # Do Reverse
            move("Reverse", straight_amount)

        else:
            # Set LED matrix to exclaimation mark
            led("Halt")
            # Log data about point where robot got suck
            logger(session_id, timestamp, orientation, location_x, location_y, fsd, rsd, lsd, bsd, "Halt", straight_amount)


# Run database preparation
database()
# Get session id
# session_id = session_id()
session_id = 1
# Run algorithm
algorithm(session_id)