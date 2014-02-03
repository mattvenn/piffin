# Logging into the Pi and starting Idle

After the Pi has been plugged together and turned on, you should see a black screen full of white text that ends with `raspberrypi login:`
The username and password are all lower case:

* username: `pi`
* password: `raspberry`

While typing the password you won't see any characters appearing, this is to stop people from knowing how long your password is.

After logging in, start the [GUI](../glossary.html#gui) by typing `startx`. Then double click on the Idle icon on the desktop.

# Simple LED

Follow the diagram to build the circuit. Common problems are:

* If the LED doesn't light, check the short leg is connected to ground (the black wire in the diagram).
* Check the components are inserted properly, with their legs deeply inserted into the breadboard

\ ![Simple LED circuit](1ledbasic.png)

# Python stopwatch

Here is the program your teacher used to time your Raspberry Pi building skills. This time you'll type it to time yourself taking apart the circuit.

The numbers on the left are line numbers and don't need to be typed in.
The codes on the right are Python commands and they have to be copied exactly as written. Make sure you copy all the symbols, and that everything is in the correct case.

***stopwatch.py

# How to safely pack away

* Log out,
* Type `sudo halt`,
* Wait until the lights go out,
* Unplug the cables and pack into the box.

