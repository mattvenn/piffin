#import the libraries
import time
import random
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

button_pin = 8
led_pin = 10

#set the button pin to be True to start,
#when we press the button, the pin will change to False.
GPIO.setup(button_pin,GPIO.IN, pull_up_down=GPIO.PUD_UP)

#set the led pin to be an output
GPIO.setup(led_pin, GPIO.OUT)
GPIO.output(led_pin,False)

#how long should we wait before turning on the led
sleep_time = random.randint(3,10)

#wait for our random time
time.sleep(sleep_time)

#turn on the led and store the current time in a variable
GPIO.output(led_pin, True)
start_time = time.time()

#wait for the button to be pressed...
while True:
    if GPIO.input(button_pin) == False:
        print("stopped!")
        #finish the while loop
        break

#work out how long they took:
reaction_time = time.time() - start_time
print("you got" + str(reaction_time) + "seconds")
