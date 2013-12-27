#import the libraries
import time
import RPi.GPIO as GPIO

#setup the led and the switch
GPIO.setmode(GPIO.BOARD)

button_pin = 8
r_led_pin = 10
a_led_pin = 12
g_led_pin = 16

#set the button pin to be high to start, when we press it, the pin will read False.
GPIO.setup(button_pin,GPIO.IN, pull_up_down=GPIO.PUD_UP)

#set the led pins to be outputs
GPIO.setup(r_led_pin, GPIO.OUT)
GPIO.setup(a_led_pin, GPIO.OUT)
GPIO.setup(g_led_pin, GPIO.OUT)

#turn off the R and A leds, and on the G
GPIO.output(r_led_pin, False)
GPIO.output(a_led_pin, False)
GPIO.output(g_led_pin, True)

#a variable to store what state the crossing is in
state = 'go'

#variables to store information about how long the lights should be on for
light_time = 2
flash_time = 0.5
flashes = 3

#function for stopping: green -> amber -> red
#and we'll start off with the green light on
def stop():
    #turn off green light
    GPIO.output(g_led_pin, False)

    #turn on amber and wait
    GPIO.output(a_led_pin, True)
    time.sleep(light_time)

    #turn off amber
    GPIO.output(a_led_pin, False)

    #turn on green
    GPIO.output(r_led_pin, True)
    

#function for starting: red -> amber flash -> green
#starting off with the red light on
def start():
    #turn off red light
    GPIO.output(r_led_pin, False)

    #flash amber light
    for i in range(flashes):
        GPIO.output(a_led_pin, True)
        time.sleep(flash_time)
        GPIO.output(a_led_pin, False)
        time.sleep(flash_time)

    #turn on green light
    GPIO.output(g_led_pin, True)


#forever: wait for the button to be pressed...
while True:
    #if the button is pressed, change the state, then we'll know next time
    #to call the other function
    if GPIO.input(button_pin) == False:
        if state == 'go':
            print "stopping"
            state = 'stopped'
            stop()
        else:
            print "starting"
            state = 'go'
            go()

    #let the processor have a break
    time.sleep(0.1)

