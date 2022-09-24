import network
import time

wlan = network.WLAN(network.STA_IF)
while not wlan.isconnected():
    print('Waiting for Wi-Fi...')
    time.sleep(1)
   
import pixelblaze

