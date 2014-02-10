# Lesson 3 Handout

## Tips for the `flash.py` program

To print something, use this Python code:

~~~ python
print("hello")
~~~

## Controlling the GPIOs with Python

The first line imports the new library, the second sets the library so we can refer to the pins by their physical number, and the 3rd turns off some distracting warnings: 

~~~ {.python}
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
~~~

Now we store the pin number in a variable, so it's easy to change later, and then set that pin to be an output:

~~~ {.python}
led_pin = 8
GPIO.setup(led_pin, GPIO.OUT)
~~~

Finally, we can turn an LED on with this line:

~~~ {.python}
GPIO.output(led_pin, True)
~~~

And off with this line:

~~~ {.python}
GPIO.output(led_pin, False)
~~~

## Running a program as the super user

* Close Idle,
* Open lxterminal (double click on lxterminal icon on the desktop),
* Type `gksudo idle` and press enter,
* A warning window will pop up which you can ignore,
* Now open your program as before and use `f5` to run.

## LED circuit

Follow the diagram to build the circuit. Common problems are:

* If an LED doesn't light, check the short leg is connected to ground (the black wire in the diagram),
* check the components are inserted properly, with their legs deeply inserted into the breadboard,
* The green wire from the Raspberry Pi must be connected to pin 8.

\ ![LED circuit](1led.png)

