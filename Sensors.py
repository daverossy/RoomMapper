__author__ = 'David Rossiter'

import RPi.GPIO as GPIO
import time

def sonarReading(Sensor):
    if Sensor == "FSD":
        # Get sonar reading for front sensor
    elif Sensor == "RSD":
        # Get sonar reading for right sensor
    elif Sensor == "LSD":
        # Get sonar reading for left sensor
    elif Sensor == "BSD":
        # Get sonar reading for back sensor
    else:
        # Print error, selection of sensor location parameter is not valid
        print "Error in sensor selection!"


    GPIO.setmode(GPIO.BCM)

    # Set pins used for sonar sensors
    TRIG = 23
    ECHO = 24

    print "Distance Measurement In Progress"

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

    GPIO.output(TRIG, False)
    print "Waiting For Sensor To Settle"
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
      pulse_start = time.time()

    while GPIO.input(ECHO)==1:
      pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    print "Distance:",distance,"cm"

    GPIO.cleanup()

    # Return Sonar Value
    return distance
