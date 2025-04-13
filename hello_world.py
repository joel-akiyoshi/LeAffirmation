#!/usr/bin/env python3

import RPi.GPIO as GPIO

while True:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, GPIO.HIGH)