__author__ = 'David Rossiter'

import datetime
from Logging import logger
from Sensors import sonarReading
from Motors import move

def algorithm():
    print "Waiting to start..."

    # Initalise Variables
    FSD = 0
    RSD = 0
    LSD = 0
    BSD = 0
    MinDistance = 5
    RotationAmount = 2
    StraightAmount = 2

    # Run program while loop, will need a stop and start mechanism
    while True:
        # Get sonar readings
        FSD = sonarReading("FSD")
        RSD = sonarReading("RSD")
        LSD = sonarReading("LSD")
        BSD = sonarReading("BSD")

        # Get timestamp
        Timestamp = datetime.datetime.fromtimestamp(Timestamp).strftime('%Y-%m-%d %H:%M:%S')

        if FSD > MinDistance:
            # Call move forwards method and tell the motors to move forwards
            move("Forward",StraightAmount)
            # Log sensor readings, movement decision, movement distance and timestamp
            logger(Timestamp,FSD,RSD,LSD,BSD,"Forward",StraightAmount)

        elif (RSD | LSD) > MinDistance:
            if RSD > LSD:
                # Do Right
                move("Right",RotationAmount)
                # Log sensor readings, movement decision, movement distance and timestamp
                logger(Timestamp,FSD,RSD,LSD,BSD,"Right",RotationAmount)
            else:
                # Do Left
                move("Left",RotationAmount)
                # Log sensor readings, movement decision, movement distance and timestamp
                logger(Timestamp,FSD,RSD,LSD,BSD,"Left",RotationAmount)

        elif BSD > MinDistance:
            # Do Reverse
            move("Reverse",StraightAmount)
            # Log sensor readings, movement decision, movement distance and timestamp
            logger(Timestamp,FSD,RSD,LSD,BSD,"Reverse",StraightAmount)

        else:
            print "Error Raised, Stuck! Help!"
            logger(Timestamp,FSD,RSD,LSD,BSD,"Stuck",StraightAmount)
