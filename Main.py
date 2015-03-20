__author__ = 'David Rossiter'

import datetime
import time
from Logging import logger
from Sensors import sonar_reading
from Motors import move


def algorithm():
    print "Waiting to start..."

    # Initialise variables
    fsd = 0
    rsd = 0
    lsd = 0
    bsd = 0
    min_distance = 5
    rotation_amount = 2
    straight_amount = 2
    straight_travel_delay = 2
    rotation_travel_delay = 2

    # Run program while loop, will need a stop and start mechanism
    while True:
        # Get sonar readings
        fsd = sonar_reading("FSD")
        rsd = sonar_reading("RSD")
        lsd = sonar_reading("LSD")
        bsd = sonar_reading("BSD")

        # Get timestamp
        timestamp = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

        if fsd > min_distance:
            # Call move forwards method and tell the motors to move forwards
            move("Forward", straight_amount)
            # Log sensor readings, movement decision, movement distance and timestamp
            logger(timestamp, fsd, rsd, lsd, bsd, "Forward", straight_amount)
            # Add delay proportional to time taken for motors to complete travel
            # NEED TO FIGURE OUT TIME DELAY
            time.sleep(straight_travel_delay)

        elif (rsd | lsd) > min_distance:
            if rsd > lsd:
                # Do Right
                move("Right", rotation_amount)
                # Log sensor readings, movement decision, movement distance and timestamp
                logger(timestamp, fsd, rsd, lsd, bsd, "Right", rotation_amount)
                # Add delay proportional to time taken for motors to complete travel
                time.sleep(rotation_travel_delay)

            else:
                # Do Left
                move("Left", rotation_amount)
                # Log sensor readings, movement decision, movement distance and timestamp
                logger(timestamp, fsd, rsd, lsd, bsd, "Left", rotation_amount)
                # Add delay proportional to time taken for motors to complete travel
                time.sleep(rotation_travel_delay)

        elif bsd > min_distance:
            # Do Reverse
            move("Reverse", straight_amount)
            # Log sensor readings, movement decision, movement distance and timestamp
            logger(timestamp, fsd, rsd, lsd, bsd, "Reverse", straight_amount)
            # Add delay proportional to time taken for motors to complete travel
            time.sleep(straight_travel_delay)

        else:
            print "Error Raised, Stuck! Help!"
            logger(timestamp, fsd, rsd, lsd, bsd, "Stuck", straight_amount)
