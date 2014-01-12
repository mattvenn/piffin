#import the library to control the GPIO pins
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

#import the time library
import time

led_pin = 8

#set the pin to be an output
GPIO.setup(led_pin, GPIO.OUT)

#in a loop:
while True:
    #turn on the led
    print('hello')
    GPIO.output(led_pin, True)
    #wait for 1 second
    time.sleep(1)

    #turn off the led
    print('world!')
    GPIO.output(led_pin, False)
    #sleep again
    time.sleep(1)
