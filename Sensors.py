__author__ = 'David Rossiter'

import RPi.GPIO as GPIO
import time
# Set GPIO to board pin numbers
GPIO.setmode(GPIO.BOARD)

# Set no errors for pins already being used
GPIO.setwarnings(False)

# Set pin number variables
front_trig = 29
front_echo = 22
left_trig = 18
left_echo = 16
right_trig = 15
right_echo = 13
back_trig = 12
back_echo = 11

GPIO.cleanup()


def sonar_reading(sensor):
    # If sensor select is front then get front measurement
    if sensor == "FSD":
        GPIO.setup(front_trig, GPIO.OUT)
        GPIO.setup(front_echo, GPIO.IN)

        GPIO.output(front_trig, False)
        # time.sleep(2)

        GPIO.output(front_trig, True)
        time.sleep(0.00001)
        GPIO.output(front_trig, False)

        while GPIO.input(front_echo) == 0:
            pulse_start = time.time()

        while GPIO.input(front_echo) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance, 2)

        # Return sonar distance
        return distance

        GPIO.cleanup()

    elif sensor == "RSD":
        GPIO.setup(right_trig, GPIO.OUT)
        GPIO.setup(right_echo, GPIO.IN)

        GPIO.output(right_trig, False)
        # time.sleep(2)

        GPIO.output(right_trig, True)
        time.sleep(0.00001)
        GPIO.output(right_trig, False)

        while GPIO.input(right_echo) == 0:
            pulse_start = time.time()

        while GPIO.input(right_echo) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance, 2)

        # Return sonar distance
        return distance

        GPIO.cleanup()

    elif sensor == "LSD":
        GPIO.setup(left_trig, GPIO.OUT)
        GPIO.setup(left_echo, GPIO.IN)

        GPIO.output(left_trig, False)
        # time.sleep(2)

        GPIO.output(left_trig, True)
        time.sleep(0.00001)
        GPIO.output(left_trig, False)

        while GPIO.input(left_echo) == 0:
            pulse_start = time.time()

        while GPIO.input(left_echo) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance, 2)

        # Return sonar distance
        return distance

        GPIO.cleanup()

    elif sensor == "BSD":
        GPIO.setup(back_trig, GPIO.OUT)
        GPIO.setup(back_echo, GPIO.IN)

        GPIO.output(back_trig, False)
        # time.sleep(2)

        GPIO.output(back_trig, True)
        time.sleep(0.00001)
        GPIO.output(back_trig, False)

        while GPIO.input(back_echo) == 0:
            pulse_start = time.time()

        while GPIO.input(back_echo) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance, 2)

        # Return sonar distance
        return distance

        GPIO.cleanup()

    else:
        # Print error, selection of sensor location parameter is not valid
        print "Error in sensor selection!"
