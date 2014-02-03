% The Reaction Timer
% PIffIN
%

# The Reaction Timer

Now we've learnt how to setup the Pi, write some simple programs, flash an LED and detect a button - we're ready to start making some cool stuff! 

The last 2 lessons focus on building a reaction timer and then running a class competition to see who has the fastest reactions.

Students have mostly copied code and made minor modifications. This time we'll work together to plan a program and to turn it into Python using pseudo code.

# Learning objectives

Students learn:

* To plan a program by analysing a problem and using pseudo code,
* Commenting code is useful as a development aid,
* To use the `random` library,
* To use the `break` keyword to break out of a loop.

# Resources

* 15 Pis and equipment,
* 8 copies of the [Program cards](program_cards.pdf),
* 15 [copies of the handout](lesson-5-handout.html),
* 15 [copies of the cheat sheet](../cheatsheet.html),
* Pens and paper.

## What do we need for a reaction timer? : 25 minutes

Ask what hardware is needed? We react to the LED and push a button.
The LED has to light after a random time so we can't predict it.
Discuss with the class how the software will work. 

## Pseudo code

Tell the students to get into groups of 4 and use the program cards to lay out a program sequence (from top to bottom).
They'll need to use the blank ones to add their own variable names or extra codes.

After a few minutes ask 2 members of each team to walk around and get ideas from the other teams. They can ask questions, and the remaining members answer them.

### Example code

My variable names are written in blue.

\ ![Example pseudo code](reaction_code_cards.png)

If you're feeling shaky with Python, then you can ask the whole class to agree to follow one team's program structure. This will make it easier to debug code later. Then take a photo and show it on the projector or ask someone to copy it onto the white board. Make sure you save it for the next lesson!

### Convert pseudo code to Python comments

Ask students to get back in pairs, open a new program with Idle and save it as `reaction.py`.

Ask students to copy the code structure into their program, starting each line with a `#` so it becomes a comment.
The lines will change colour to remind them it's a comment.

It should end up something like this:

~~~ python
#pick a random number and store in sleep_time

#sleep for sleep_time seconds

#turn on the led 

#store the current time in start_time

#in a loop:
    #if the button is pressed:
        #break out of the loop

#work out how long they took by subtracting the start_time now from the time now

#print out how long they took
~~~

## Extra Python

We've introduced 2 commands with the program cards that we haven't covered yet in Python. These are also included in the handouts.

### Generating a random number

Here we import a new library called `random` and then use `randint()` to produce a random number between 1 and 5:

***random_demo.py

### Ending a loop

Here we use `break` to end the `while` loop:

***breakloop_demo.py

## Build reaction timer software : 30 minutes

Students work in pairs to convert the comments into Python code. They can reference any of the programs they've saved so far. They should write the Python below the comment, and leave the comment in for reference.

Ask them to start at the top and to test each line of code at a time by saving and running the code.

If students get stuck, remind them to look at their previous programs:

* `stopwatch` for getting the time, delaying, printing and storing variables,
* `flash` for turning on and off LEDs,
* `button` for detecting a button press.

## Reference code

***reaction.py

## Pack away : 5 minutes

Pack away the Pi.

# Homework

Continue with the homework project from the last week. Students convert the software description they came up with to comments, and then start working on converting the comments into Python code.

# Outcome

All students:

* Understand what components are necessary for a reaction timer,
* Have helped to write a program using the program cards,
* Have helped to start converting the program cards into Python.

Most students:

* Understand that analysis of the problem first makes it easier to turn into code later.
