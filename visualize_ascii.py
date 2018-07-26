#!/usr/bin/python3

import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import matplotlib as mtp
mtp.use("TkAgg")
import math
import json
import copy
import numpy as np
import subprocess
from collections import deque
from copy import deepcopy

lastPosition = "x=0, y=0"
antennaStats = dict()
lastFrequencies = dict()
lastStrengths = dict()

def getAntennaString(sdr, ant):
    return "antenna_" + str(sdr) + "." + str(ant)

def dbmToBar(dbm):
    return "#" * round(130 + dbm)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    global antennaStats, lastFrequencies, lastStrengths
    for sdr in range(1,7):
        for ant in range(1,3):
            a = getAntennaString(sdr, ant)
            client.subscribe("/sdr/" + a + "/rssi")
            antennaStats[a] = 0
            lastFrequencies[a] = 0
            lastStrengths[a] = -1000 # haha

    client.subscribe("/sdr/signalStrengthPosition")

def on_message(client, userdata, msg):
    global lastPosition, antennaStats, lastFrequencies, lastStrengths
    # global antennas_strength_hist
    #print "on message"
    print(msg.topic+" "+str(msg.payload))
    if msg.topic == "/sdr/signalStrengthPosition":
        # print "got robot position"
        strpayload = msg.payload.decode('utf-8')
        robo_x = round(json.loads(strpayload)['x']/1000, 2)
        robo_y = round(json.loads(strpayload)['y']/1000, 2)
        lastPosition = "x=" + str(robo_x) + ", y=" + str(robo_y)
        # print('RX: ',robo_x,'RY: ',robo_y)
    else:
        # 1.1, 1.2, 2.1, ...: antenna = msg.topic[13:16]
        antenna = getAntennaString(msg.topic[13], msg.topic[15])
        antennaStats[antenna] += 1
        lastStrengths[antenna] = round(float(msg.payload), 2)
    # PRINT ALL DATA IN ASCII :)
    print(lastPosition)
    for sdr in range(1,7):
        for ant in range(1,3):
            a = getAntennaString(sdr,ant)
            print(a + ": " + str(antennaStats[a]) + ", " + str(lastFrequencies[a]) + "->" + str(lastStrengths[a]))
    for sdr in range(1,7):
        for ant in range(1,3):
            a = getAntennaString(sdr,ant)
            print(a + ": " + dbmToBar(lastStrengths[a]))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("gopher.phynetlab.com", 8883, 60)
client.loop_forever()
