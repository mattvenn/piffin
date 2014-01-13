# Flashing an LED

Flashing an LED is a good first example of controlling something in the real world with a computer. Once we can control an LED we can move on to things like motors and buzzers.

## What will be learnt

* create a basic circuit
* control output with the raspberry pi
* looping
* using the time library

## Facilities

* 1 raspberry pi per 2 or 3 students
* 1 piffin experimenter kit per 2 or 3 students

## Time frame

1 hour assuming that raspberry pis are setup and students already have logins.

# Lesson Plan

## What do we need?

Ask the students to think about what is needed to flash a light on and off. It's straight forward, but there are a few things that need to be considered.

* a loop, so the LED will continue flashing
* pausing a short moment - without a pause the LED will flash so fast it will just look dim!
* being able to control the pins on the raspberry pi with python

## Writing a python program with Idle

### Idle

If you've not used Idle before, it's a programming environment that makes it easier for us to write python programs. When you start it up, you get the 'shell', which let's us easily experiment with single python commands. As soon as we press enter, the python command will run. Try typing in some basic maths operators:

~~~
10 + 10
5 * 25
~~~

The shell is a great way to show a concept quickly, and then get the students to copy what you've done to see on their own computer.

When we want to move onto writing longer programs, we can make a new window (file->new) and then write our code using an editor. Before we can run it, we need to save it as a new file (don't forget to add the .py extension). Then press f5 to run the program. Check the [Additional Resources](#Idle) for some links to Idle resources.

### looping

Before we add the electronics, let's get a python program running that creates the loop and the time delay. Use the shell to show a loop:

~~~
while True:
    print("hello world!")
~~~

Show the students the CPU monitor in the bottom right hand corner, it goes really high when the program is running, because the Pi is printing 'hello world!' as fast as it can!

### the time library

If we want to slow it down, we can use the time library. Libraries allow us to use code written by other people - so we don't need to write everything ourselves.

Show the students how to import the time library in the shell:

~~~
import time
time.sleep(5)
~~~

You may also notice that if you wait after typing 

    time.

Idle will show you the different functions we can use from the time library.

### putting it together

Ask the students to start writing a new program (using the file->new) menu. The program should:

* loop the following forever:
    * print 'hello' on one line
    * wait 1 second
    * print 'world' on one line
    * wait 1 second

The code will look something like this:

~~~
import time

while True:
    print("hello")
    time.sleep(1)
    print("world")
    time.sleep(1)
~~~

Now if we can control an LED as well as printing, we'll be done!

## Build the circuit

### Parts list

* 2 LEDs
* 2 resistors
* 3 male to female wires

### Circuit diagram

![2 LEDs](2leds.png)

### Controlling the LEDs from python 

We need to use another library to control the LEDs. Get the students to add these lines to the top of their hello world code.

The first line imports the new library, and the second sets the library so we can refer to the pins by their physical number: 

    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)

Now we store the pin number in a variable, so it's easy to change later, and then set that pin to be an output:

    led_pin = 8
    GPIO.setup(led_pin, GPIO.OUT)

Finally, we can turn an LED on with this line:

    GPIO.output(led_pin, True)

And off with this line:

    GPIO.output(led_pin, False)

Challenge your students to finish the program themselves. If you get stuck, here is a working example:

***flash.py

# Extension activities

## Running the program from the command line

Open a terminal and use cd to navigate to the directory where the code is stored. We then need to use 2 commands to run the program:

* `sudo` - this lets us run the program as an admin user
* `python` - needed to run the python program

We can run the program as a super user by typing them one after the other 

    sudo python flash.py

# Homework

# Additional Resources

## Idle

* blah

## Turning all outputs on with the all_on.py script

This can be run at the beginning of a workshop to ensure that all the Pi's outputs are switched on. This helps with debugging the electrical circuits.

Run it by typing this on the command line:

    sudo python all_on.py
