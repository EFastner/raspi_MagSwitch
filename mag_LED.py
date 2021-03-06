#DESCRIPTION: Monitors a magnetic switch and turns on LED when a change of state is detected 

import RPi.GPIO as GPIO
import time
import signal
import sys

#Define a function to turn off LED and clean up the GPIO board
def cleanlights(signal, frame):
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()
    print("\n")
    sys.exit(0)

#Set Broadcom mode to address GPIO pins by number
GPIO.setmode(GPIO.BCM)

#Set the GPIO pin number that the mag strip is set to
MAG_SWITCH_PIN = 24

#Set the GPIO pin number that the LED is set to
LED_PIN = 18

#Set up GPIO pin for the switch
GPIO.setup(MAG_SWITCH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#Set up GPIO pin for the LED
GPIO.setup(LED_PIN, GPIO.OUT)

#Create a blank variable for the prior state to compare with the new state 
old_state = None

#Set the cleanup handler to turn off the LED after keyboard interupt
signal.signal(signal.SIGINT, cleanlights)

while True:
    #Define what state the switch is in
    switch_state = GPIO.input(MAG_SWITCH_PIN)
    
    #Run after a state change is detected
    if old_state != switch_state:
        #If the switch detects a magnet
        if switch_state == 0:
            print("Magnet Detected")
            
            #Turn on Light
            GPIO.output(LED_PIN, GPIO.HIGH)
            
            #Set the old_state variable to the current state
            old_state = switch_state
        #If the switch does not detect a magnet
        else:
            print("No Magnet Detected")
            
            #Turn off light
            GPIO.output(LED_PIN, GPIO.LOW)

            #Set the old_state variable to the current state
            old_state = switch_state

    time.sleep(.1)
