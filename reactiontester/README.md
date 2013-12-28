# Reaction timer

One of the simplest programs and circuits we can make with an LED and a button is a reaction timer.

This lesson works through:

* a basic circuit
* controlling input and output with the raspberry pi
* data using variables

Advanced students can progress to:

* conditional statements
* loops
* file IO

# Lesson Plan

## What do we need?

Discuss what we need for a reaction timer. We need at least the following:

* a light that we react to
* a button we press
* a variable - either to store the time when the light goes on, or to count the time as it elapses
* a way of counting time
* a way of making a random interval - this is important for checking a real reaction

## Build the circuit: 1 led and 1 button

Follow the diagram to build the circuit. Things to look out for are:

* reversed LEDs (they only work one way) 
* the input and output of the switch should be on the top left and bottom right

![1 LED and 1 button](1\ led,\ 1\ switch.png)

## Write a program that can listen to the led and light the button

Challenge the students to use the code in the button and light directories to make a program that satisfies the following:

* set up the LED as output
* set up the button as an input
* when the button is pressed, the light comes on
* when the button is released, the light goes out

## We need to wait a random length of time and then measure a time interval

Introduce the idea of libraries. We don't want to have to write everything from scratch. Though it can be good to do this to learn how to do things from first principles.

### Time library

Introduce the time library. Use ipython and demonstrate the following

    #import the library
    import time

    #sleep for 5 seconds
    time.sleep(5)

    #get the system time
    time.time()

Ask the students how they could measure how long something takes. We'd need to store the current time in a variable, then subtract that from the current time when the task is done:

    #store time in a variable
    time_start = time.time()

    #do a task
    time_taken = time.time() - time_start
    print(time_taken)

### Random library

Introduce the random library:

    #import library
    import random
    #pick a random number between 4 and 10
    random.randint(4,10)

This should provide everything the students need to know to write the reaction timer program.

## Write the main program

See reaction.py for a worked example with comments.

# Enhancements

Advance students can work on the following:

## Take 3 readings and get an average

* Use a loop to repeat the test a number of times
* Store the results in a list
* Average the results and print it

## Depending on how your time, display different messages

* Use a conditional statement to print various messages:

    if time > 1:
        print("pretty slow, could try harder")
    else:
        print("nice reactions! Do you play a lot of sport?")

## Store the best scores and show them at startup

* Use file IO to store the previous results
