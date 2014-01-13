# Quiz Buttons

A useful example of using buttons - we can make the equipment we need to play a quiz game.

# Progression

## What do we need for quiz game buttons?

## Build the circuitry: 3 buttons, 3 LEDs

## Write a program to test the buttons and lights

## Write a program that waits for a button press, then lights that LED and disables the other LEDs

# Further enhancements

how to reduce code?

* make the LED on, sleep, off code become a function, where the LED pin is passed as an argument

## Play a sound

find a .wav sound file. Each player could have their own sound.

    import os
    os.system('aplay sound.wav')

## Reduce CPU usage with interrupts

Have a look at button_int.py in the button directory. This shows how to use interrupts instead of polling.
