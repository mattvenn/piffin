# Glossary

## Argument

Say we're programming a robot and we want it to take 5 steps forward, we might have a function called `forward()`, and we'd need to pass an argument to take 5 steps:

~~~ python
forward(5)
~~~

## Breadboard

A board that makes it easy to assemble temporary electronic circuits. 

\ ![breadboard](documentation/breadboard.png)

### Side columns

The 2 columns of 25 holes on the sides are connected from top to bottom, so that means:

* All the holes beneath the red wire on the left are connected,
* All the holes beneath the blue wire on the left are connected, 
* The red and blue holes are not connected to each other.

### Middle rows

The 30 rows of 5 holes in the middle are connected horizontally. The 2 banks of columns (A-E and F-J) are not connected, so:

* All the holes on row 10 under the yellow wire are connected,
* All the holes on row 11 under the green wire are connected,
* The yellow and green holes are not connected,
* The holes under the orange wire are not connected to the yellow holes.

## Circuit

A circuit is made up of different components electrically connected together. 

## CLI

Stands for Command Line Interface. Where we type the commands on a keyboard. The only graphics are textual characters. Often seen as scary or old, the GUI is actually a very powerful way of interacting with a computer, and very common with the [Linux](#linux) operating system.

## Conditional

A program is made of a sequence of instructions. If we only have a sequence then every time the program runs, the same thing happens. We use a conditional if we want the program to do different things depending on its environment. For example; switching off a light when it gets bright.

Here's an example in python. The condition being tested is `brightness > 50`

~~~ python
if brightness > 50:
    turn_off_light()
~~~

## Current

Current is the movement of electricity through the components. It is measured in Amps or A for short. There is only a flow of current if there is a difference in [voltage](#voltage)

## Function

A function is a set of computer instructions that are grouped together so we can easily run them over and over again. We use them because they can save time and space in the program. 

## GPIO

Stands for General Purpose Input Output. The Raspberry Pi has 17 GPIOs available in the row of gold pins in the corner. We have to switch them between either being an input or an output.

## Ground

Ground means 0 [volts](#voltage).

## GUI

Stands for Graphical User Interface. This is the type of interface we're usually most used to - using a mouse to move a pointer, dragging and dropping. As opposed to a [CLI](#CLI)

## LED

An electronic component that lights up when a [current](#current) passes through it.

## Library

A set of codes we can borrow for our program. Often written by someone else. Common examples include the `time`, `random` and `turtle` libraries.

## Linux

A type of operating system. Others you may have heard of are `Apple OSX`, `Microsoft windows` and `Android`. Linux is used on the Raspberry Pi.

## Loop

A way of repeating computer instructions. For example if we want to print out a repeated message we could do this:

***loop_demo.py

## Operator

Some examples of operators in Python:

* + to add
* * to multiply
* - to subtract
* / to divide
* = to assign a value to a variable

## Pseudo code

A way of trying out ideas by writing our ideas in something halfway between English and Python. For example:

~~~
In a loop:
    If the robot bumps into something:
        take a step back
    Otherwise
        take a step forwards
~~~

## Resistor

An electrical component that limits the movement of current. We need to use them with [LEDs](#led) to avoid damaging them.

## Terminal

In [Linux](#linux) we often do work by using a Terminal to type commands into the [CLI](#cli), as well as clicking on icons in the [GUI](#gui), 

## Variable

A variable allows us to store data, update the data, and retrieve the data.
Think of a variable as a computer's short term memory. For a computer to repeat a task 10 times, it needs to remember how many times the task has already been completed. 

We store that number in a variable (line 1), update it every time we run the loop (line 4), and retrieve it when we want to check if we need to keep running the loop (line 2).

***var_demo.py

## Operating System (OS)

The software that runs on a computer that allows us to log in, read files, start programs, connect to the internet. All the boring but vital stuff. Examples include:

* Linux,
* Android,
* Mac OSX,
* Microsoft Windows.

## Voltage

For a [current](#current) to flow, we need a difference in voltage. The electricity flows from the higher voltage to the lower voltage.
