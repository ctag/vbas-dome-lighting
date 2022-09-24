import uwebsockets.client
import os
import time
from machine import Pin

def pbwsclient():
    global gpio_pressed
    with uwebsockets.client.connect('ws://192.168.1.222:81') as websocket:

        while True:
            if gpio_pressed != "NONE":
                print("PRESSED: " + gpio_pressed)
                payload = '{"activeProgramId": "pabnMtKcMhgSMS6Cm"}' #X OFF - fallback
    
                #if gpio_pressed == "Pin(5)": payload = '{"activeProgramId": "pabnMtKcMhgSMS6Cm"}' #X OFF
                #if gpio_pressed == "Pin(4)": payload = '{"activeProgramId": "yLMLo9JMiTpJTHwgs"}' #VBAS House Lights
                #if gpio_pressed == "Pin(0)": payload = '{"activeProgramId": "HNtjeLWC3AJ9SBCc4"}' #VBAS Projector Color Bands
                #if gpio_pressed == "Pin(2)": payload = '{"activeProgramId": "SnrKHS7wm6R8Xr3E3"}' #VBAS Sunset
                #if gpio_pressed == "Pin(14)": payload = '{"activeProgramId": "SNotM9hqAdrkXNWLe"}' #VBAS Aurora
                #if gpio_pressed == "Pin(12)": payload = '{"activeProgramId": "wPnJGj5d5hzgeLbZD"}' #edgeburst
                #if gpio_pressed == "Pin(13)": payload = '{"activeProgramId": "Jc63nhxTkKZL9ckn3"}' #VBAS Night Vision Red
                #if gpio_pressed == "Pin(15)": payload = '{"activeProgramId": "xDpehSz2fg3KTrMF5"}' #VBAS Logo Blue

                if gpio_pressed == "Pin(2)": payload = '{"activeProgramId": "pabnMtKcMhgSMS6Cm"}' #X OFF
                if gpio_pressed == "Pin(4)": payload = '{"activeProgramId": "HNtjeLWC3AJ9SBCc4"}' #VBAS Projector Color Bands
                if gpio_pressed == "Pin(0)": payload = '{"activeProgramId": "SnrKHS7wm6R8Xr3E3"}' #VBAS Sunset

                
                print("> {}".format(payload))
                websocket.send(payload)
                gpio_pressed = "NONE"
    
            received = websocket.recv()
            print("< {}".format(received))
    
            time.sleep_ms(250)

def irq_callback(pin_object):
    global gpio_pressed
    gpio_pressed = str(pin_object)

gpio_pressed = "NONE"

for pin_number in [5, 4, 0, 2, 14, 12, 13, 15]:
    the_pin = Pin(pin_number, Pin.IN, Pin.PULL_UP)
    the_pin.irq(trigger=Pin.IRQ_FALLING, handler=irq_callback)

pbwsclient()

