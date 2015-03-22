__author__ = 'David Rossiter'

# Import required modules
import sqlite3
import numpy as np
import matplotlib.pyplot as plt


def mapping_generator():
    # Connect to SQLite database or create database if not already existing
    conn = sqlite3.connect('mapping.db')

    # Connection
    c = conn.cursor()

    # Insert a row of data
    c.execute("SELECT * FROM mapping")
    print(c.fetchall())

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


def scatter_plt():
    # the random data
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

    plt.savefig('foo.png')
    plt.savefig('foo.pdf')

    plt.show()

scatter_plt()
