# This file is executed on every boot (including wake-boot from deepsleep)

import webrepl
import network
import time

from configs.secretConfigs import WiFi_ssid, WiFi_password

def connectToWiFi(ssid, password):
    station = network.WLAN(network.STA_IF)

    if station.isconnected():
        print('Already connected to network')

    if not station.isconnected():
        print('Connecting to network...')
        station.active(True)
        station.connect(ssid, password)
        # print('Network config:', station.ifconfig())

    if not station.isconnected():
        print('Network connection failed')

    print('Network connection: ', station.isconnected(), '\nNetwork config:', station.ifconfig())

time.sleep(1)
connectToWiFi(WiFi_ssid, WiFi_password)

webrepl.start()
