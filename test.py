#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.output(3, 1)
GPIO.output(4, 1)
GPIO.output(2, 1)
GPIO.output(27, 0)

