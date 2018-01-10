#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.output(4, 0)
GPIO.output(17, 0)
GPIO.output(27, 0)
#class DevNull:
 #   def write(self, msg):
#        pass sys.stderr = DevNull()
# The callback for when the client receives a CONNACK response from the 
# server.
def on_connect(
    client,
    userdata,
    flags,
    rc,
    ):
    time.sleep(3)
    print("Connected with result code " + str(rc))
    time.sleep(3)
    # Subscribing in on_connect() means that if we lose the connection 
    # and reconnect then subscriptions will be renewed.
    client.subscribe("node")
    print("Subscribed to topic with result code " + str(rc))
    print("Ready for receiving messages")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    message = str(msg.payload)
    msgs = message.split("'")[1]
    # set up pin 17 GPIO.setup(18, GPIO.OUT) # set up pin 18 
    # GPIO.output(4, 1) # turn on pin 17 GPIO.output(18, 1) # turn on 
    # pin 18 print(str(msg.payload))
    if msgs == "up":
        print("Trigger message received. Status: up")
        GPIO.output(17,1)
        time.sleep(10)
        GPIO.output(17,0)
    else:

        print("Trigger message received. Status: down")
        GPIO.output(27,1)
        time.sleep(10)
        GPIO.output(27,0)
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("10.77.97.14", 1883)
# Blocking call that processes network traffic, dispatches callbacks and 
# handles reconnecting. Other loop*() functions are available that give 
# a threaded interface and a manual interface.
client.loop_forever()
