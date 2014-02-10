% Lesson 1 - The Raspberry Pi
% PIffIN
%

# The Raspberry Pi

In this lesson, we'll learn what the Raspberry Pi is and practice setting it up and breaking it down. 
These lessons assume you won't be able to leave the Pi out and connected, so it's important to get the set up and break down time as fast as possible.
If you do have the facility to leave equipment setup, then take a little longer on the activities.

# Learning objectives

Students will learn:

* What the Pi is,
* What the various sockets are for,
* How to set up and take apart the Pi,
* How to get an SD card ready to use.

# Resources

* [Python and Idle installed](http://www.python.org/getit/releases/2.7.6/) on your presentation PC,
* 15 Raspberry Pis,
* 15 [NOOBS](http://www.raspberrypi.org/archives/4100) SD cards,
* 15 copies of the [Raspberry Pi quick setup guide](http://www.raspberrypi.org/wp-content/uploads/2012/04/quick-start-guide-v2_1.pdf),
* 15 [Piffin Lab Kits](http://www.piffin.co.uk/products/raspberry-pi-lab-kit) or equivalent.
* 15 [copies of the handout](lesson-1-handout.html)

# Lesson Plan

## Introduction to the Pi : 10 minutes

Show the students the Pi and ask if they know what it is. Explain that over the next few weeks they'll be learning how to use one, to write code on it, and to build circuits that will allow them to build a reaction timer. At the end of the sessions, everyone will compete to see who has the fastest reactions.

If you're not sure what the ports are yourself, [make sure you look at this picture!](http://www.raspberrypi.org/wp-content/uploads/2011/07/RaspiModelB.png)

Show [this unlabelled picture of the Pi](http://upload.wikimedia.org/wikipedia/commons/3/3d/RaspberryPi.jpg) and ask what the various parts are.
Make sure you show:

* HDMI for video,
* USB for keyboard and mouse,
* USB micro for power,
* SD socket for the disk,

## Setting up and breaking down : 20 minutes

We want to waste as little time as possible setting up and breaking down, so we're going to have a competition running over the whole 6 lessons to see how fast we can get it. You'll use the following program to do the timing.

***stopwatch.py

Tell the students you forgot your stop watch so you'll have to write one on the computer. Start Idle, create a new window and type the above code in. When you run the program the counter will start in the `shell`. You can adjust the size of the font using the `options -> configure idle` menu. Show the students what the output looks like and we'll be recording the shortest and longest time.

Ensure everyone is ready with their Pi equipment, and then start the program running. To end it you'll have to press `ctrl + c`.

Assign team numbers and write down how the fastest and slowest times it took to set up.

Remember where you saved the stopwatch program! We'll be using it again.

The result should be all the screens showing the NOOBS install screen, similar to below:

\ ![NOOBS](noobs.png)

## First booting : 15 minutes

Explain that the SD card that stores the operating system and all our files is currently not ready to use. We have to use the NOOBS interface to install the operating system. Here's how:

* Ask the students to tick the 4th box down next to *Raspian - Boot to Desktop*,
* Then click the top left icon that says *Install*.

This process takes about 10 minutes, so while we wait complete the following activities. Walk around the class and check that the installation is proceeding as expected. We need this to work so that next week we can login to the Pi.

* Ask the students to start assembling the holder (sticking on the feet and breadboard) - leave attaching the Pi until later. Ensure the students keep the little plastic screws safe in the bag.
* Ask the students to write their team number on the front of the Lab kit box,
* Ask if anyone has heard of or used Linux. Explain that Linux is a free [operating system](../glossary.html#operating-system). Android is a variant of Linux developed by Google.
* Explain that the Pi runs Linux, and so to use it we'll have to learn how to use it.

After Linux has been installed this screen will appear:

\ ![Raspi-Config](raspi-config.png)

Ask the students to press the tab key twice to highlight the `finish` text, and then press enter. The Pi will then reboot and load the desktop.

## Pack away : 5 minutes

Pack away the Pi:

* Click the red power button on the bottom right of the screen,
* Choose to `shut down`,
* Wait till only the red light shows on the Pi,
* Unplug the power cable,
* Unplug the other cables,
* Pack into the box.

These steps are included in the handout.

# Homework

Use the internet to research the parts of the Raspberry Pi. Fill in the picture in the handout.

# Outcome

All students:

* Understand the Raspberry Pi is a computer,
* Can set up the Pi from scratch.

Most students:

* Can set up the Pi in less than 3 minutes,
* Understand that Pi runs an operating system called Linux, which is installed on the SD card.
