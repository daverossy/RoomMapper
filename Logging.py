__author__ = 'David Rossiter'

# Import required modules
import sqlite3


def logger(session_id, timestamp, fsd, rsd, lsd, bsd, direction, movement_value):
    # Connect to SQLite database or create database if not already existing
    conn = sqlite3.connect('mapping.db')

    # Connection
    c = conn.cursor()

    # Insert a row of data
    c.execute('''INSERT INTO mapping (session_id, timestamp, fsd, rsd, lsd, bsd, direction, movement_value) VALUES (?, ?, ?, ?, ?, ?, ?)''', (session_id, timestamp, fsd, rsd, lsd, bsd, direction, movement_value))

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

