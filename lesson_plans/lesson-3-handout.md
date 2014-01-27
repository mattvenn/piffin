# Tips for the `flash.py` program

To print something, use this Python code:

~~~ python
print("hello")
~~~

# Controlling the GPIOs with Python

The first line imports the new library, and the second sets the library so we can refer to the pins by their physical number: 

~~~ {.python}
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
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

# LED circuit

Follow the diagram to build the circuit. Common problems are:

* if an LED doesn't light, check the short leg is connected to ground (the black wire in the diagram).
* check the components are inserted properly, with their legs deeply inserted into the breadboard

\ ![LED circuit](1led.png)

# Running a program as the super user

* Close Idle,
* Open a terminal (start menu->accessories->lxterminal),
* Type `gksudo idle` and press enter,
* A warning window will pop up which you can ignore,
* Now open your program as before and use `f5` to run.
