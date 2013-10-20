# flashing an LED

Flashing an LED is a good first example. The code is commented well, so be sure to read that.

# Connections

add an LED and a resistor in series to pin 8 of the header. There is an example circuit on the workshop resources. If the LED doesn't turn on, it may be because the pin isn't turned on already (see the section below), or because the circuit is broken.

If the circuit is broken, check that the connections on the breadboard are as they are in the diagram. 

If you think the wires are correct, check the LED is the right way round - they only light one way round.

# Turning all outputs on with the all_on.py script

This can be run at the beginning of a workshop to ensure that all the Pi's outputs are switched on. This helps with debugging the electrical circuits.

Run it by typing this on the command line:
    
    sudo python all_on.py
