% Lesson 4 - Conditionals and buttons
% Piffin
%

# Conditionals & Detecting button presses

Now the class is moving onto buttons, they need to be able to use [conditions](../glossary.html#conditional) in Python. These let a program do different things depending on what's happening.

# Learning objectives

Students will learn:

* Conditional statements,
* How to write a conditional in Python,
* Build a button circuit,
* Detect a button press with Python.

# Resources

* 15 Pis and equipment,
* Button, wires,
* Some A4 sheets of paper, pens,
* 15 [copies of the handout](lesson-4-handout.html).

# Lesson Plan

## Conditional Tree : 15 minutes

You'll need some room to play this physical game. Outside works well!

* Ask the class for some True or False questions eg: Are you a boy?, Do you get driven to school?
* Get 3 of these questions, and write them each on a piece of paper,
* Get 3 volunteers to be the conditionals, they will each be assigned one of the above questions.

Stand the the conditionals so one is at the front, then the other 2 are behind in a v shape.
The rest of the class line up and one by one they go through the ‘tree’. Their personal answer will direct them to the next conditional. If the answer is True; go left, and if False; right.

### Tips

* Works well with a whole class, 
* Having cones at the points of a tree helps to structure the game. For 3 conditionals, you’d need 7 cones, 3 for the conditions and 4 for the possible outcomes, 
* Sometimes students forget which way to go, so having True and False with arrows on the paper can help.

## Setup the Pi : 5 minutes

Setup the Pi and get logged in.

## Detect a button with Python : 10 minutes

* Ask the students to look at the code in their handout and predict what will happen.
* Explain that the `if` and the `else` are doing the same task as the people in the conditional tree game. 
* This is the part that allows the code to do 2 different things depending on whether the button is pressed.
* Ask them to start Idle as the super user as before, and copy the code into a new file called `button.py`. 

## Build the circuit : 10 minutes

Ask the students to identify pin 16 on the Pi (8 down on the right hand side). Ask the students to build the circuit shown in the handout. 

## Run the code : 10 minutes

Ask the students to test their prediction by running the code.
Students will discover that the code only checks the button once. 
They'll have to hold the button before starting the program to ever see the message that the button is pressed.

Ask the students to modify the code, adding a loop so that the program is checking continuously if the button is pressed. If they are stuck as them to look at the loop in the `flash.py` or `stopwatch.py` examples. The [cheat sheet](../cheatsheet.html#loops) also has a looping example.

Once the students have done added a loop, ask them to look at the little box in the bottom right corner of the screen that shows CPU usage. They'll see that when they run the program the CPU is working at 100%!

### Extension Activity

They can reduce CPU usage by including a small delay in our loop. The smaller the delay the harder the Pi has to work. Ask the students to add a delay and experiment with delay times. If they forgot how to do a delay then they can check their `flash.py` code. Try different lengths of delay. Is there a problem with increasing the delay too much? If it's too big then they might miss a button press.

## Example code

This code adds the loop to continuously check the button, and reduces CPU usage by using `time.sleep()` to add a small delay.

***button.py

## Pack away : 5 minutes

Pack away the Pi.

# Homework

* Read this webpage on the one button audio book: [http://bit.ly/1-bab](http://bit.ly/1-bab),
* Come up with an idea for a project that involves an LED and a button. Draw a picture of the circuit and describe how the software will work.

# Outcome

All students:

* Understand what a conditional statement is,
* Have built a circuit that connects a button to the Pi,
* Have run some Python code that can detect a button press.

Most students:

* Understand that they need to check the button over and over with a loop.

Some students:

* Have reduced CPU usage by using a small delay in the loop.
