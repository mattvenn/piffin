# Glossary

## argument

An argument is a parameter we pass to a function. If we want to use the `time.sleep()` function, we have to pass an argument to specify how long to sleep for. In this case, 5 seconds:

~~~ python
time.sleep(5)
~~~

## breadboard

A board that makes it easy to assemble temporary electronic circuits. 

\ ![breadboard](documentation/breadboard.png)

### Side columns

* The 2 columns on either side are electrically connected vertically along their length. So the red wire on the left is connected to the yellow wire. 

### Middle rows

* The middle columns are connected horizontally, so the yellow wire connects to the resistor. 

* The bank of 5 columns on the left (A-E) are separate to those on the right (F-J).

## circuit

A circuit is made up of different components electrically connected together. The [breadboard](#breadboard) example above shows a circuit made up of wires, a resistor and an LED.

## CLI

Stands for Command Line Interface. Where we type the commands on a keyboard. The only graphics are textual characters. Often seen as scary or old, the GUI is actually a very powerful way of interacting with a computer, and very common with the [Linux](#linux) operating system.

## conditional

A program is made of a sequence of instructions. If we only have a sequence then every time the program runs, the same thing happens. We use a conditional if we want the program to do different things depending on its environment. For example; switching off a light when it gets bright.

Here's an example in python. The condition being tested is `brightness > 50`

~~~ python
if brightness > 50:
    turn_off_light()
~~~

## current

Current is the movement of electricity through the components. It is measured in Amps or A for short. There is only current if there is a difference in [voltage](#voltage)

## function

A function is a set of computer instructions that are grouped together so we can easily run them over and over again. We use them because they can save time and space in the program. 

## GPIO

Stands for General Purpose Input Output. The Raspberry Pi has 17 GPIOs available in the row of gold pins in the corner. We have to switch them between either being an input or an output.

## ground

Ground means 0 [volts](#voltage).

## GUI

Stands for Graphical User Interface. This is the type of interface we're usually most used to - using a mouse to move a pointer, dragging and dropping. As opposed to a [CLI](#CLI)
## LED
## library
## Linux
## loop
## operator
## Pseudo code
## resistor
## terminal
## variable

A variable allows us to store data, update the data, and retrieve the data.
Think of a variable as a computer's short term memory. For a computer to repeat a task 10 times, it needs to remember how many times the task has already been completed. 

We store that number in a variable (line 1), update it every time we run the loop (line 4), and retrieve it when we want to check if we need to keep running the loop (line 2).

***var_demo.py

## operating system (OS)

The software that runs on a computer that allows us to log in, read files, start programs, connect to the internet. All the boring but vital stuff. Examples include:

* Linux,
* Android,
* Mac OSX,
* Microsoft Windows.

## voltage

For a [current](#current) to flow, we need a difference in voltage. The electricity flows from the higher voltage to the lower voltage.
