#DESCRIPTION: Monitors a magnetic switch and outputs the status every 5 seconds for 5 cycles

import RPi.GPIO as GPIO
import time

#Set Broadcom mode to address GPIO pins by number
GPIO.setmode(GPIO.BCM)

#Set the GPIO pin number that the mag strip is set to
MAG_SWITCH_PIN = 24

#Set up GPIO pin
GPIO.setup(MAG_SWITCH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

i = 1
cycles = 5

while i <= cycles:
    switch_state = GPIO.input(MAG_SWITCH_PIN)

    if switch_state == 0:
        print("Magnet Detected")
    else:
        print("No Magenet Detected")
    
    if i == cycles:
        break

    i += 1
    
    time.sleep(2)

