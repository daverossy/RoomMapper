__author__ = 'David Rossiter'

from LED_System import led
import time

led("Forward")
time.wait(1)
led("Left")
time.wait(1)
time.wait(1)
led("Right")
time.wait(1)
led("Reverse")
time.wait(1)
led("Halt")
time.wait(1)
led("Complete")
time.wait(1)
led("Clear")