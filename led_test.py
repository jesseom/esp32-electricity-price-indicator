# This is my LED testing python file

import machine
import time

wifi_on_led = machine.Pin(2, machine.Pin.OUT)
wifi_off_led = machine.Pin(15, machine.Pin.OUT)
connecting_led =machine.Pin(4, machine.Pin.OUT)

expensive_led = machine.Pin(17, machine.Pin.OUT)
moderate_led = machine.Pin(18, machine.Pin.OUT)
cheap_led = machine.Pin(19, machine.Pin.OUT)

def set_led(led, state):
    led.value(state)
    
while True:
    set_led(wifi_on_led, 1)
    set_led(wifi_off_led, 1)
    set_led(connecting_led, 1)
    
    set_led(expensive_led, 1)
    set_led(moderate_led, 1)
    set_led(cheap_led, 1)