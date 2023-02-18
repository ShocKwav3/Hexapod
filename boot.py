# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import webrepl
import network
import time

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
connectToWiFi('ssidOfAny2.4ghzWifi', 'wifiPassWord')
webrepl.start()
