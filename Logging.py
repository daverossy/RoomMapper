__author__ = 'David Rossiter'

# Easiest to append each log record to a csv file, a database could be used

import csv


def logger(timestamp, fsd, rsd, lsd, bsd, direction, movement_value):
    with open('log.csv', 'w', newline='') as csvfile:
        log_writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        log_writer.writerow(timestamp, fsd, rsd, lsd, bsd, direction, movement_value)