% Flashing an LED
% Piffin
%

# Flash an LED with Python

Last time we made a simple LED circuit, but we didn't control it with the Pi, this time we'll do that by building a flashing LED circuit and program.

# Learning objectives

Students will learn:

* How to use the Pi to control a [GPIO](../glossary.html#gpio),
* looping,
* using the time library.

# Resources

* 15 Pis and equipment,
* LED, resistor, wires,
* Some A4 sheets of paper, pens,
* 15 [copies of the handout](lesson-3-handout.html).

## Setup Pi : 5 minutes

Use the stopwatch code to time your students, they should be pretty fast by now! You could time how long it takes until they have started Idle. The author managed 55 seconds to login, and 87 seconds to start Idle.

## Looping with Python : 10 minutes

The Raspberry Pi has many GPIOs (General Purpose Input/Output) that we can use. They can either be set as an input or an output.
Flashing an LED is a good first example of using the Pi's output to controlling something in the real world.
Once we can control an LED we can move on to things like motors and buzzers. 

Ask the students to think about what is needed to flash a light on and off:

1. being able to control the pins on the Raspberry Pi with python
2. pausing a short moment - without a pause the LED will flash so fast it will just look dim!
3. a loop, so the LED will continue flashing

Ask the students if they've seen any code that could something similar? The stopwatch program from last time has the loop, and it can pause. What it's missing is the ability to turn on and off the LED.

Ask the students to open the `stopwatch.py` program they used last time and save it as a new file `flash.py`. Then ask them to modify the program to the following:

* loop the following forever:
    * print 'LED on' on one line
    * wait 1 second
    * print 'LED off' on one line
    * wait 1 second

## Add the LED control : 10 minutes

We need to use another library to control the LEDs. Get the students to add these lines to the top of their `flash.py` code.

These lines are also in the handout.

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

Challenge your students to finish the program themselves. If they get stuck, see the example below.

***flash.py

## Running the program : 10 minutes

When it comes to testing the program there are a few things to bear in mind:

* We can only access the GPIOs as the super user.
* We'll get a warnings once we've used the GPIOs once.

We can ignore the warnings, but we need a way to run the program as the super user to get anything to work. 

* Close Idle,
* Open a terminal (start menu->accessories->lxterminal),
* Type `gksudo idle` and press enter,
* A warning window will pop up which you can ignore,
* Now open your program as before and use `f5` to run.

Remember that we expect a warning about the GPIO already being in use.

## Build the circuit : 15 minutes

Ask students to build the LED circuit in their handout. When their circuit is correct, their LED should start flashing.

### Extension activity

* The circuit has 2 LEDs, but we're only flashing one. Ask the students to modify the code to control the other LEDs

## Pack away : 5 minutes

Pack away the Pi.

# Homework

* Research Raspberry Pi GPIOs. How many digital ins and outs. How many analogue ins and outs. What is the difference between analogue and digital?
* Explain that the codes we've been writing so far have been sequential, in that the codes are executed one after the other. If we ever want our programs to do different things depending on what's happening around us we need to be able to make decisions in the code. These decisions are called [conditions](../glossary.html#conditional). Ask what conditions are there in making a cup of tea, walking home, doing homework?

# Outcome

All students:

* Will understand we can use a GPIO to control an LED,
* Will have modified a Python program.

Most students:

* Will have turned on and off an LED using Python.

Some students:

* Will have modified their code to flash 2 LEDs.
