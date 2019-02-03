#DESCRIPTION: Monitors a magnetic switch and outputs the status as the state changes
#Magnet Detected: Green LED
#No Magnet Detected: Red LED

import RPi.GPIO as GPIO
import time
import signal
import sys

#Define a function to turn off RGB and clean up the GPIO board
def cleanlights(signal, frame):
    GPIO.cleanup()
    print("\n")
    sys.exit(0)

#Set Broadcom mode to address GPIO pins by number
GPIO.setmode(GPIO.BCM)

#Set the GPIO pin numbers for the RGB and add them to a list for easy setup
red_pin = 16
green_pin = 20
blue_pin = 21
chan_list = [16, 20, 21]

#Set the GPIO pin number that the mag strip is set to
MAG_SWITCH_PIN = 24

#Set up GPIO pin for the switch
GPIO.setup(MAG_SWITCH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#Set up GPIO pins for the RGB
GPIO.setup(chan_list, GPIO.OUT)

#Create a PWM for all lights
RED_LED = GPIO.PWM(red_pin, 100)
GREEN_LED = GPIO.PWM(green_pin, 100)
BLUE_LED = GPIO.PWM(blue_pin,100)

#Create a blank variable for the prior state to compare with the new state 
old_state = None

#Set the cleanup handler to turn off the LED after keyboard interupt
signal.signal(signal.SIGINT, cleanlights)

while True:
    #Define what state the switch is in
    switch_state = GPIO.input(MAG_SWITCH_PIN)
    
    #Run after a state change is detected
    if old_state != switch_state:
        #Stop any existing lights
        RED_LED.stop()
        GREEN_LED.stop()
        BLUE_LED.stop()

        #If the switch detects a magnet
        if switch_state == 0:
            print("Magnet Detected")
            
            #Turn on Green Light
            GREEN_LED.start(75)
            
            #Set the old_state variable to the current state
            old_state = switch_state
        
        #If the switch does not detect a magnet
        else:
            print("No Magnet Detected")
            
            #Turn on Red Light
            RED_LED.start(75)

            #Set the old_state variable to the current state
            old_state = switch_state

    time.sleep(.1)
