__author__ = 'David Rossiter'

# Import required modules
import sqlite3


def logger(session_id, timestamp, orientation, location_x, location_y, fsd, rsd, lsd, bsd, direction, movement_value):
    if orientation == "0":
        # Set front sensor co-ordinates
        fsd_location_x = location_x
        fsd_location_y = location_y + fsd
        # Set right sensor co-ordinates
        rsd_location_x = location_x + rsd
        rsd_location_y = location_y
        # Set left sensor co-ordinates
        lsd_location_x = location_x - lsd
        lsd_location_y = location_y
        # Set rear sensor co-ordinates
        bsd_location_x = location_x
        bsd_location_y = location_y - bsd

        # Return values with sensor points unused but left in case used somewhere else
        # return fsd_location_x, fsd_location_y, rsd_location_x, rsd_location_y, \
        # lsd_location_x, lsd_location_y, bsd_location_x, bsd_location_y

    elif orientation == "90":
        # Set front sensor co-ordinates
        fsd_location_x = location_x + fsd
        fsd_location_y = location_y
        # Set right sensor co-ordinates
        rsd_location_x = location_x
        rsd_location_y = location_y - rsd
        # Set left sensor co-ordinates
        lsd_location_x = location_x
        lsd_location_y = location_y + lsd
        # Set rear sensor co-ordinates
        bsd_location_x = location_x - bsd
        bsd_location_y = location_y

    elif orientation == "180":
        # Set front sensor co-ordinates
        fsd_location_x = location_x
        fsd_location_y = location_y - fsd
        # Set right sensor co-ordinates
        rsd_location_x = location_x - rsd
        rsd_location_y = location_y
        # Set left sensor co-ordinates
        lsd_location_x = location_x + lsd
        lsd_location_y = location_y
        # Set rear sensor co-ordinates
        bsd_location_x = location_x
        bsd_location_y = location_y + bsd

    elif orientation == "270":
        # Set front sensor co-ordinates
        fsd_location_x = location_x - fsd
        fsd_location_y = location_y
        # Set right sensor co-ordinates
        rsd_location_x = location_x
        rsd_location_y = location_y + rsd
        # Set left sensor co-ordinates
        lsd_location_x = location_x
        lsd_location_y = location_y - lsd
        # Set rear sensor co-ordinates
        bsd_location_x = location_x + bsd
        bsd_location_y = location_y

    else:
        print "Error"

    # Connect to SQLite database or create database if not already existing
    conn = sqlite3.connect('mapping.db')

    # Connection
    c = conn.cursor()

    # Insert a row of data
    c.execute('''INSERT INTO mapping (session_id, timestamp, location_x, location_y, fsd_location_x, fsd_location_y, rsd_location_x, rsd_location_y, lsd_location_x, lsd_location_y, bsd_location_x, bsd_location_y, direction, movement_value) VALUES (?, ?, ?, ?, ?, ?, ?)''', (session_id, timestamp, location_x, location_y, fsd_location_x, fsd_location_y, rsd_location_x, rsd_location_y, lsd_location_x, lsd_location_y, bsd_location_x, bsd_location_y, direction, movement_value))

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

