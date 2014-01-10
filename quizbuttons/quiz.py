#import the libraries
import RPi.GPIO as GPIO

#setup the led and the switch
GPIO.setmode(GPIO.BOARD)

button_1_pin = 8
led_1_pin = 10

button_2_pin = 12
led_2_pin = 16

button_3_pin = 18
led_3_pin = 22

#set the button pins to be high to start, when we press it, the pin will read False.
GPIO.setup(button_1_pin,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_2_pin,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_3_pin,GPIO.IN, pull_up_down=GPIO.PUD_UP)

#set the led pins to be outputs, and turn them off
GPIO.setup(led_1_pin, GPIO.OUT)
GPIO.output(led_1_pin,False)
GPIO.setup(led_2_pin, GPIO.OUT)
GPIO.output(led_2_pin,False)
GPIO.setup(led_3_pin, GPIO.OUT)
GPIO.output(led_3_pin,False)

#wait for a button to be pressed...
while True:
    if GPIO.input(button_1_pin) == False:
        print("player 1!")
        GPIO.output(led_1_pin,False)
    if GPIO.input(button_2_pin) == False:
        print("player 2!")
        GPIO.output(led_2_pin,False)
    if GPIO.input(button_3_pin) == False:
        print("player 3!")
        GPIO.output(led_3_pin,False)
