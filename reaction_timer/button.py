import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
import time

button_pin = 16

#set the pin to be high to start, low when pressed
GPIO.setup(button_pin,GPIO.IN, pull_up_down=GPIO.PUD_UP)

#check if the button is pressed
while True:
    if GPIO.input(button_pin) == False:
        print("button pressed")
    else:
        print("button not pressed")

    #small delay to reduce CPU usage
    time.sleep(0.1)
