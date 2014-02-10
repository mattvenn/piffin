% Lesson 3 - Flashing an LED
% Piffin
%

# Flash an LED with Python

Last time they made a simple LED circuit, but didn't control it with the Pi.
This time the students will control an LED with a Python program.
Once they can control an LED, the same technique can be used to control motors, speakers and other actuators.

# Learning objectives

Students will learn:

* How to use the Pi to control a [GPIO](../glossary.html#gpio),
* Looping,
* How to pause a Python program using the time library.

# Resources

* 15 Pis and equipment,
* LED, resistor, wires,
* Some A4 sheets of paper, pens,
* 15 [copies of the handout](lesson-3-handout.html).

## Setup Pi : 5 minutes

Use the stopwatch code to time your students, they should be pretty fast by now! You could time how long it takes until they have started Idle. The author managed to go from unplugged to typing code into Idle in 68 seconds.

## Looping with Python : 10 minutes

The Raspberry Pi has many GPIOs (General Purpose Input/Output) that we can use. They can either be set as an input or an output.
Flashing an LED is a good first example of using the Pi's output to controlling something in the real world.
Once they can control an LED we can move on to things like motors and buzzers. 

Ask the students to think about what is needed to flash a light on and off:

1. Being able to control the pins on the Raspberry Pi with python,
2. Pausing a short moment - without a pause the LED will flash so fast it will just look dim!
3. A loop, so the LED will continue flashing,
4. The physical circuit: an LED, resistor and some wires.

Ask the students if they've seen any code that could something similar? The stopwatch program from last time has the loop, and it can pause. What it's missing is the ability to turn on and off the LED.

Ask the students to open the `stopwatch.py` program they used last time and save it as a new file `flash.py`. Then ask them to modify the program to the following:

* loop the following forever:
    * print 'LED on' on one line
    * wait 1 second
    * print 'LED off' on one line
    * wait 1 second

Check that everyone has managed to get the program printing out the messages.

## Add the LED control : 10 minutes

We need to use another library to control the LEDs. Get the students to add these lines to the top of their `flash.py` code. They can leave in the printing lines, as they are helpful for debugging.

These lines are also in the handout.

The first line imports the new library, the second sets the library so they can refer to the pins by their physical number, and the 3rd turns off some distracting warnings: 

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

Challenge your students to finish the program themselves. If they get stuck, see the example below.

***flash.py

## Running the program : 10 minutes

Ask the students to run the program. It will fail with this error:

`RuntimeError: No access to /dev/mem.  Try running as root!`

This is because we can only access the GPIOs as the super user (root). Here's how to run Idle as the super user:

* Close Idle,
* Open lxterminal (double click on lxterminal icon on the desktop),
* Type `gksudo idle` and press enter,
* A warning window will pop up which you can ignore,
* Now open your program as before and use `f5` to run.

These instructions are also in the handout.

## Build the circuit : 15 minutes

Ask students to build the LED circuit in their handout. When their circuit is correct, their LED should start flashing.

Explain that the LED is connected to pin 8 because we set the `led_pin` variable to pin 8 in the software. If we wanted the LED on another pin, we'd have to make sure the hardware and the software matched up. We can use any pin that isn't marked `GND`, `3.3v` or `5v`. Ask the students to identify which is pin 8. They can use the etching on the Pi holder. It is the 4th pin down on the right hand side.

If you're not using our Pi mounting kits, then here's a picture of the GPIOs with `ground` (same as `GND`), `3.3v` or `5v` marked.

\ ![GPIOs](gpios.png)

Explain that the controlling an LED is just the first and simplest thing they can control. They can use the same technique for controlling motors, though they'd also need some kind of amplifier.

### Extension activities

* Make the LED flash the [morse code](http://en.wikipedia.org/wiki/Morse_code) of the student's initials.
* Move the LED onto another pin and change the software to match.
* Add an extra LED and update the software to flash both LEDs.

## Pack away : 5 minutes

Pack away the Pi. Remind students to follow the instructions in last lesson's handout.

# Homework

* Research Raspberry Pi GPIOs. How many digital ins and outs. How many analogue ins and outs. What is the difference between analogue and digital?
* Ask students to think of some things they'd like to control with a computer.

# Outcome

All students:

* Will understand they can use a GPIO to control an LED,
* Will have modified a Python program.

Most students:

* Will have turned on and off an LED using Python.

Some students:

* Will have modified their code to flash 2 LEDs.
