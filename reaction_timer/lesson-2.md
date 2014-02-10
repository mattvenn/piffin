% Lesson 2 - Elementary electronics & Python Stopwatch
% Piffin
%

# Elementary electronics & Python Stopwatch

In this lesson the students will learn how to follow a diagram to build a circuit that lights a single LED. 
They'll also learn how to write and run a Python program. They'll be using the SD card they installed from last time. It's a good idea to have a few spare SD cards that have already been installed in case something went wrong in the last lesson.

# Learning objectives

Students will learn:

* How to follow a breadboard circuit diagram,
* How to use Idle to run a simple Python program.

# Resources

* 15 Pis and equipment,
* LED, wires.
* 15 [copies of the handout](lesson-2-handout.html),
* A few small cross head screwdrivers (optional),
* Some spare NOOBS cards in case the ones from last week didn't work.

# Lesson Plan

## Finish building holder : 5 minutes

Last time the students stuck on the breadboard and the rubber feet to the holder. Now they're going to attach the Pi to the holder. Finish following the instructions to mount the Pi. Gently tighten the screws with the screw driver or do it by hand.

## Setup Pi : 5 minutes

Load your stopwatch python program and tell the students they're going to try and beat the best records from last lesson. Read out the times and when everyone is ready start the clock.

Record the results and ask what takes the time, and how it can be shortened. Try and get the students to start working to share best practice as this will be extremely useful later.

## Elementary electronics : 20 minutes

Explain [how a breadboard works](../glossary.html#breadboard) using the glossary.

Explain that the students should follow the diagram in their handout to build a simple LED circuit. For now, the Raspberry Pi is just powering the LED using its internal power supply. We are unable to switch the LED on and off with this circuit.

It doesn't matter what colour wires students use.

While the students start building the circuit, look around the room to check that the Pis have all booted to the desktop. If not then turn off the power, and replace the SD card with one you know works.

### Extension activity

Use a button to switch the LED. Show this picture for advanced students to follow:

\ ![1 LED and 1 button](1led1buttonbasic.png)

## Python stopwatch : 20 minutes

Tell students to start Idle (not Idle3), and create a new program by clicking `file->new`.

Ask students to explain how the stopwatch program works. Make some predictions.

Then ask the students to copy out the stopwatch program from the handout into this new window.

When everyone has finished, they need to save their files. Ask them to save their file as `stopwatch.py`

After all students have saved, ask them to press `f5` to run the program. If they've correctly typed the program they should see the stopwatch counting up in seconds.

Check everyone's screen to see this has happened. If student's predictions were wrong, discuss what is happening when the code runs.

Ask them to time themselves taking apart the circuit and putting the parts away in the correct bags.

### Extension activity

Ask students to change the stopwatch so it counts in tenths of a second instead of quarters.

## Pack away : 5 minutes

Pack away the Pi as before.

# Homework

Come up with a project that requires 2 or more LEDs. Explain what will happen and draw a circuit diagram.

# Outcome

All students:

* Can start the Pi, log in and get the graphical environment running.
* Can follow a simple diagram to build a working electronic circuit.
* Can copy a Python program and run it.

Most students:

* Have modified their program to count in tenths of a second.

Some students:

* Have used a button in their circuit.

