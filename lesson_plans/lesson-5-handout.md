# Missing pieces of Python

For our reaction timer, we need to generate a random number. This can be done using the `random` library. The following code prints out a random integer between 1 and 5:

~~~ python
import random
my_number = random.randint(1,5)
print(my_number)
~~~

We also need a way of ending a loop when something happens. Here's an example of ending a loop when the counter reaches 10:

~~~ python
counter = 0
while True:
    counter = counter + 1
    if counter == 10:
        break
~~~

When the conditional that is testing to see if counter == 10 becomes true, we break out of the loop using the `break` command.
