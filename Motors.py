# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

# Use GPIO pin numbers
GPIO.setmode(GPIO.BOARD)

# Set no errors for pins already being used
GPIO.setwarnings(False)

# Define GPIO pins order to use for each motor direction/side
forwards_left_step_pins = [40, 38, 37, 36]
forwards_right_step_pins = [31, 32, 33, 35]
right_left_step_pins = [40, 38, 37, 36]
right_right_step_pins = [35, 33, 32, 31]
left_left_step_pins = [36, 37, 38, 40]
left_right_step_pins = [31, 32, 33, 35]
reverse_left_step_pins = [36, 37, 38, 40]
reverse_right_step_pins = [35, 33, 32, 31]

# Define advanced sequence
# as shown in manufacturers data sheet
Seq = [[1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [1, 0, 0, 1]]


def move(direction, movement):
    if direction == "Forward":
        # Set all pins as output
        for pin in forwards_left_step_pins, forwards_right_step_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)

        stepcount = len(Seq)-1
        stepdir = 2 # Set to 1 or 2 for clockwise
        # Set to -1 or -2 for anti-clockwise

        # Read wait time from command line
        if len(sys.argv)>1:
            waittime = int(sys.argv[1])/float(1000)
        else:
            waittime = 0.004

        # Initialise variables
        stepcounter = 0

        # Start main loop
        for x in range(0, 251):
            for pin in range(0, 4):
                l_pin = forwards_left_step_pins[pin]
                r_pin = forwards_right_step_pins[pin]
                if Seq[stepcounter][pin] != 0:
                    GPIO.output(l_pin, True)
                    GPIO.output(r_pin, True)
                else:
                    GPIO.output(l_pin, False)
                    GPIO.output(r_pin, False)

            stepcounter += stepdir

            # If we reach the end of the sequence
            # start again
            if stepcounter >= stepcount:
                stepcounter = 0
            if stepcounter < 0:
                stepcounter = stepcount

            # Wait before moving on
            time.sleep(waittime)

        GPIO.output(forwards_left_step_pins, False)
        GPIO.output(forwards_right_step_pins, False)

    elif direction == "Right":
        # Set all pins as output
        for pin in right_left_step_pins, right_right_step_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)

        stepcount = len(Seq)-1
        stepdir = 2 # Set to 1 or 2 for clockwise
        # Set to -1 or -2 for anti-clockwise

        # Read wait time from command line
        if len(sys.argv)>1:
            waittime = int(sys.argv[1])/float(1000)
        else:
            waittime = 0.004

        # Initialise variables
        stepcounter = 0

        # Start main loop
        for x in range(0, 1951):
            for pin in range(0, 4):
                l_pin = right_left_step_pins[pin]
                r_pin = right_right_step_pins[pin]
                if Seq[stepcounter][pin] != 0:
                    GPIO.output(l_pin, True)
                    GPIO.output(r_pin, True)
                else:
                    GPIO.output(l_pin, False)
                    GPIO.output(r_pin, False)

            stepcounter += stepdir

            # If we reach the end of the sequence
            # start again
            if stepcounter >= stepcount:
                stepcounter = 0
            if stepcounter < 0:
                stepcounter = stepcount

            # Wait before moving on
            time.sleep(waittime)

        GPIO.output(right_left_step_pins, False)
        GPIO.output(right_right_step_pins, False)

    elif direction == "Left":
        # Set all pins as output
        for pin in left_left_step_pins, left_right_step_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)

        stepcount = len(Seq)-1
        stepdir = 2 # Set to 1 or 2 for clockwise
        # Set to -1 or -2 for anti-clockwise

        # Read wait time from command line
        if len(sys.argv)>1:
            waittime = int(sys.argv[1])/float(1000)
        else:
            waittime = 0.004

        # Initialise variables
        stepcounter = 0

        # Start main loop
        for x in range(0, 1951):
            for pin in range(0, 4):
                l_pin = left_left_step_pins[pin]
                r_pin = left_right_step_pins[pin]
                if Seq[stepcounter][pin] != 0:
                    GPIO.output(l_pin, True)
                    GPIO.output(r_pin, True)
                else:
                    GPIO.output(l_pin, False)
                    GPIO.output(r_pin, False)

            stepcounter += stepdir

            # If we reach the end of the sequence
            # start again
            if stepcounter >= stepcount:
                stepcounter = 0
            if stepcounter < 0:
                stepcounter = stepcount

            # Wait before moving on
            time.sleep(waittime)

        GPIO.output(left_left_step_pins, False)
        GPIO.output(left_right_step_pins, False)

    if direction == "Reverse":
        # Set all pins as output
        for pin in reverse_left_step_pins, reverse_right_step_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)

        stepcount = len(Seq)-1
        stepdir = 2 # Set to 1 or 2 for clockwise
        # Set to -1 or -2 for anti-clockwise

        # Read wait time from command line
        if len(sys.argv) > 1:
            waittime = int(sys.argv[1])/float(1000)
        else:
            waittime = 0.004

        # Initialise variables
        stepcounter = 0

        # Start main loop
        for x in range(0, 251):
            for pin in range(0, 4):
                l_pin = reverse_left_step_pins[pin]
                r_pin = reverse_right_step_pins[pin]
                if Seq[stepcounter][pin] != 0:
                    GPIO.output(l_pin, True)
                    GPIO.output(r_pin, True)
                else:
                    GPIO.output(l_pin, False)
                    GPIO.output(r_pin, False)

            stepcounter += stepdir

            # If we reach the end of the sequence
            # start again
            if stepcounter >= stepcount:
                stepcounter = 0
            if stepcounter < 0:
                stepcounter = stepcount

            # Wait before moving on
            time.sleep(waittime)

        GPIO.output(reverse_left_step_pins, False)
        GPIO.output(reverse_right_step_pins, False)

    else:
        # Print error, selection of sensor location parameter is not valid
        print "Error in motor selection!"
