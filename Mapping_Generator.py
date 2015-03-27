__author__ = 'David Rossiter'

# Requires matlibplot to be installed
# Import required modules
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def data(session_id):
    # Connect to SQLite database or create database if not already existing
    conn = sqlite3.connect('mapping.db')

    # Connection
    conn.row_factory = dict_factory
    c = conn.cursor()

    # Select all records for the current session id
    c.execute("SELECT * FROM mapping WHERE session_id = ?", session_id)

    print c.fetchone()['timestamp']

    # Close connection
    conn.close()



def scatter_plot(session_id):
    # Get graph data from database for current session id
    #x, y = data(session_id)

    # Insert tuple of all points from database required in here!
    x = [0, 0, 0, 0, 0, 1, 1, 1, 2]
    y = [1, 2, 3, 4, 5, 5, 6, 7, 7]

    # definitions for the axes
    left, width = 0.1, 0.8
    bottom, height = 0.1, 0.8

    rect_scatter = [left, bottom, width, height]

    # start with a rectangular Figure
    plt.figure(1, figsize=(8, 8))

    axScatter = plt.axes(rect_scatter)

    # the scatter plot:
    axScatter.scatter(x, y)


    # now determine nice limits by hand:
    binwidth = 0.25
    xymax = np.max( [np.max(np.fabs(x)), np.max(np.fabs(y))] )
    lim = (int(xymax/binwidth) + 1) * binwidth

    axScatter.set_xlim((-1, lim))
    axScatter.set_ylim((-1, lim))

    # Generate timestamp
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H-%M-%S')

    # Export as PDF or PNG
    # plt.savefig(str(timestamp) + '.png')
    # plt.savefig(str(timestamp) + '.pdf')

    # Open in viewer
    plt.show()

data("1")
