__author__ = 'David Rossiter'

import RPi.GPIO as GPIO
import time


def sonar_reading(sensor):
    if sensor == "FSD":

    elif sensor == "RSD":

    elif sensor == "LSD":

    elif sensor == "BSD":

    else:
        # Print error, selection of sensor location parameter is not valid
        print "Error in sensor selection!"


def running():
    GPIO.setmode(GPIO.BCM)

    # Set pins used for sonar sensors
    trig = 23
    echo = 24

    print "Distance Measurement In Progress"

    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

    GPIO.output(trig, False)
    print "Waiting For Sensor To Settle"
    time.sleep(2)

    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    while GPIO.input(echo) == 0:
        pulse_start = time.time()

    while GPIO.input(echo) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    print "Distance:", distance, "cm"

    GPIO.cleanup()

    # Return Sonar Value
    return distance
