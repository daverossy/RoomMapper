__author__ = 'David Rossiter'

# Easiest to append each log record to a csv file, a database could be used

import csv

def logger(Timestamp,FSD,RSD,LSD,BSD,Direction,StraightAmount):
    with open('log.csv', 'w', newline='') as csvfile:
    logWriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    logWriter.writerow(Timestamp,FSD,RSD,LSD,BSD,Direction,StraightAmount)