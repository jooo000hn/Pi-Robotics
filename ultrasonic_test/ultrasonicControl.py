#!/usr/bin/env python
# Ultrasonic Control for Raspberry Pi with HC-SR04 

#-------------------------------------------------------------------------------
#### Imports ####

import time
import numpy as np
import RPi.GPIO as GPIO 

#### Constants ####

#-------------------------------------------------------------------------------
# GPIO Mode (BOARD/BCM)
GPIO.setmode(GPIO.BOARD)

# Assign GPIO pins to variables
_ULTRASONIC_TRIG=12
_ULTRASONIC_ECHO=32

# Set up ultrasonic pins
GPIO.setup(_ULTRASONIC_TRIG, GPIO.OUT)
GPIO.setup(_ULTRASONIC_ECHO, GPIO.IN)

#### Objects ####

#-------------------------------------------------------------------------------
class UltrasonicControl(object):
    # Make sure there is only one instance of UltrasonicControl  

    _instances=[]

    # Initialize the object
    def __init__(self):
        if ( len(self._instances)>1 ):
            print("ERROR: One instance of UltrasonicControl is running already.")
            exit(1)
        self._instances.append(self)									

#-------------------------------------------------------------------------------        
    # Read DISTANCE ahead of the robot. We are taking 5 readings, removing outliers and averaging the rest of the values.
    def distance(self):

        # set Trigger to HIGH
        GPIO.output(_ULTRASONIC_TRIG, True)
     
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(_ULTRASONIC_TRIG, False)
     
        StartTime = time.time()
        StopTime = time.time()
     
        # save StartTime
        while GPIO.input(_ULTRASONIC_ECHO) == 0:
            StartTime = time.time()
     
        # save time of arrival
        while GPIO.input(_ULTRASONIC_ECHO) == 1:
            StopTime = time.time()
     
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
     
        return distance
        
        