# Led logic here
import config
import machine
import time

price_green_led = machine.Pin(config.PRICE_GREEN_PIN, machine.Pin.OUT)
price_yellow_led = machine.Pin(config.PRICE_YELLOW_PIN, machine.Pin.OUT)
price_red_led = machine.Pin(config.PRICE_RED_PIN, machine.Pin.OUT)

wifi_green_led = machine.Pin(config.WIFI_GREEN_PIN, machine.Pin.OUT)
wifi_orange_led = machine.Pin(config.WIFI_ORANGE_PIN, machine.Pin.OUT)
wifi_red_led = machine.Pin(config.WIFI_RED_PIN, machine.Pin.OUT)

def set_led(led, state):
    led.value(state)
    
def display_price_category(category):
    set_led(price_green_led, config.OFF)
    set_led(price_yellow_led, config.OFF)
    set_led(price_red_led, config.OFF)
    
    if category == "cheap":
        set_led(price_green_led, config.ON)
    elif category == "moderate":
        set_led(price_yellow_led, config.ON)
    else:
        set_led(price_red_led, config.ON)
    