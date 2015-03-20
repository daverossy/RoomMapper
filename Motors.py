__author__ = 'David Rossiter'

# Import required libraries
import time
import RPi.GPIO as GPIO


def initialise_gpio():
    # Use BOARD GPIO references
    # instead of physical pin numbers
    GPIO.setmode(GPIO.BOARD)

    # Define GPIO signals to use
    # Left Stepper Motor Pins 7,11,12,13
    # Right Stepper Motor Pins 15,16,18,22
    step_pins = [7, 11, 12, 13]

    # Set all pins as output
    for pin in step_pins:
        print "Setup pins"
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, False)

    # Define some settings
    step_counter = 0
    wait_time = 0.5

    # Define advanced sequence
    # as shown in manufacturers data sheet
    step_count_2 = 8
    seq_2 = []
    seq_2 = range(0, step_count_2)
    seq_2[0] = [1, 0, 0, 0]
    seq_2[1] = [1, 1, 0, 0]
    seq_2[2] = [0, 1, 0, 0]
    seq_2[3] = [0, 1, 1, 0]
    seq_2[4] = [0, 0, 1, 0]
    seq_2[5] = [0, 0, 1, 1]
    seq_2[6] = [0, 0, 0, 1]
    seq_2[7] = [1, 0, 0, 1]

    # Choose a sequence to use
    seq = seq_2
    step_count = step_count_2

    # Start main loop
    while 1 == 1:
        for pin in range(0, 4):
            xpin = step_pins[pin]
            if seq[step_counter][pin] != 0:
                print " Step %i Enable %i" % (step_counter, xpin)
                GPIO.output(xpin, True)
        else:
            GPIO.output(xpin, False)

    step_counter += 1

    # If we reach the end of the sequence
    # start again
    if step_counter == step_count:
        step_counter = 0
    if step_counter < 0:
        step_counter = step_count

    # Wait before moving on
    time.sleep(wait_time)

    GPIO.cleanup()

def move(direction, movement):
    if direction == "Forward":
        # Move stepper motor forward for value of movement
    elif direction == "Right":
        # Move stepper motor right for value of movement
    elif direction == "Left":
        # Move stepper motor left for value of movement
    elif direction == "Reverse":
        # Move stepper motor in reverse for value of movement
    else:
        # Print error, selection of sensor location parameter is not valid
        print "Error in sensor selection!"
