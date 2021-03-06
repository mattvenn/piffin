% Reaction Timer
% Piffin
%

# Reaction timer

One of the simplest programs and circuits we can make with an LED and a button is a reaction timer.

## What will be learnt

In this lesson, students will learn how to:

* create a basic circuit
* control input and output with the Raspberry Pi
* store and retrieve data using variables
* using libraries

Advanced students can progress to:

* conditional statements
* loops
* file input and output

## Facilities

* 1 Raspberry Pi per 2 or 3 students
* 1 Piffin experimenter kit per 2 or 3 students

## Time frame

2 hours assuming that Raspberry Pis are setup and students already have logins.

# Lesson Plan

## What do we need?

Discuss what we need for a reaction timer. We need at least the following:

* a light that we react to
* a button we press
* a variable - either to store the time when the light goes on, or to count the time as it elapses
* a way of counting time
* a way of making a random interval - this is important for checking a real reaction

## Build the circuit: 1 LED and 1 button

### Parts list

* 1 LED
* 1 button
* 3 male to female wires, 1 male to male wire
* 1 resistor

### Circuit Diagram

Follow the diagram to build the circuit. Common problems are:

* if an LED doesn't light, check the short leg is connected to ground (the black wire in the diagram).
* the input and output of the button should be on the top left and bottom right
* check the components are inserted properly, with their legs deeply inserted into the breadboard

\ ![1 LED and 1 button](1led1button.png)

## Write a program that can listen to the LED and light the button

Challenge the students to use the code in the button and light directories to make a program that satisfies the following:

* set up the LED as output
* set up the button as an input
* when the button is pressed, the light comes on
* when the button is released, the light goes out

## We need to wait a random length of time and then measure a time interval

Introduce the idea of libraries. We don't want to have to write everything from scratch. Though it can be good to do this to learn how to do things from first principles.

### Time library

Introduce the time library. Use ipython and demonstrate the following

~~~ {.python .numberLines}
#import the library
import time

#sleep for 5 seconds
time.sleep(5)

#get the system time
time.time()
~~~

Ask the students how they could measure how long something takes. We'd need to store the current time in a variable, then subtract that from the current time when the task is done:

~~~ {.python .numberLines}
#store time in a variable
time_start = time.time()

#do a task
time_taken = time.time() - time_start
print(time_taken)
~~~

### Random library

Introduce the random library:

~~~ {.python .numberLines}
#import library
import random
#pick a random number between 4 and 10
random.randint(4,10)
~~~

This should provide everything the students need to know to write the reaction timer program.

## Write the main program

See reaction.py for a worked example with comments.

***reaction.py

# Extension activities

Advance students can work on the following:

## Take 3 readings and get an average

* Use a loop to repeat the test a number of times
* Store the results in a list
* Average the results and print it

## Depending on how your time, display different messages

Use a conditional statement to print various messages:

~~~ {.python .numberLines}
if time > 1:
    print("pretty slow, could try harder")
else:
    print("nice reactions! Do you play a lot of sport?")
~~~

## Store the best scores and show them at startup

* Use file IO to store the previous results
TODO!

# Homework

TODO!

# Additional Resources

TODO!

* Reaction timers
* LEDs and resistors
* Latest version of this document
* Conditional statements
* File IO
* Loops
