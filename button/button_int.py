"""
author: matt venn
"""

#import the library
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

button_pin_1 = 16
button_pin_2 = 18

#set the pin to be high to start, low when pressed
GPIO.setup(button_pin_1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_pin_2,GPIO.IN, pull_up_down=GPIO.PUD_UP)

def my_callback(channel):  
    print("button!")

GPIO.add_event_detect(button_pin_1, GPIO.FALLING, callback=my_callback, bouncetime=300) 

while True:
    #wait for a bit to avoid high cpu usage
    time.sleep(1)


