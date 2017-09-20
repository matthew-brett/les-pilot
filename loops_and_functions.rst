#################################
Conditionals, functions and loops
#################################

.. code-links:: clear

In this Notebook, we work out how to simulate a coin toss in Python.  Then we
wrap up the coin toss logic into our own function.  Lastly, we work out how to
do many coin tosses and collect the result.

************
Conditionals
************

We want our Python code to do the equivalent of a coin toss.  We want to run
the code, and get a random answer, that is 1 50% of the time (representing a
Head), and 0 50% of the time (representing a Tail).

Let's start by getting a random number that can be any value, with equal
likelihood, all the way between 0 and 1.  We think first of the ``random``
module:

.. nbplot::

    >>> import random

We can explore the functions inside the random module by tab completion (see
:ref:`getting-help`).  We can also look at the `documentation for the random
module <https://docs.python.org/3.6/library/random.html>`_.  We discover that
the ``random`` function in the ``random`` module does what we want:

.. nbplot::
    :hide-from: all
    :show-to: doctest

    >>> random.seed(1966)

.. nbplot::

    >>> # Get a random number between 0 and 1
    >>> random.random()
    0.889900600711181

.. nbplot::

    >>> # Get another random number between 0 and 1
    >>> random.random()
    0.9602318110750124

To do our coin toss, we can look at the random number.  If it is < 0.5, we can
decide this is a 0 (for Tails), and if it is >= 0.5, we will say it is a 1
(for Heads).  This is a "if, then" type statement, called a *conditional*.
It's called a conditional because we do something only if a condition is met.
The condition here is that the random number is < 0.5.  A conditional in
Python looks like this:

.. nbplot::

    >>> random_no = random.random()
    >>> # Next we see the condition that is being tested
    >>> if random_no < 0.5:
    ...     # Tails
    ...     our_result = 0
    ... else:
    ...     # Heads
    ...     our_result = 1

There are a couple of important things to notice here. The conditional starts
with ``if``, followed by the condition, here ``random_no < 0.5``.  There must
be a colon (`:`) at the end of the line, and this signals the start of the
statements that should run if the condition is True.

The statement to execute if the condition is True, is ``our_result = 0``.
Notice that this statement is *indented* by four spaces.  It is this
indentation that tells Python that the statement should run only if the
condition is True.  You can put many statements to run if the condition is
True, but they must all be indented in the same way.  Luckily the Notebook and
other code editors usually guess what we want and do the indentation for us.

Next we see a line ``else:``.  Notice that this line is *not* indented.  That
is because we want this line to run if the condition is False.  Remember, the
indented lines above run only when the condition is True.

Notice again that the ``else:`` has a colon at the end, to say that more
indented lines will follow.  These lines only run if the condition is False.

To recap, the indented lines after the ``if`` and before the ``else`` run only
if the condition is True.  The indented lines after the ``else:`` only run if
the condition is False.

You don't have to have an ``else:`` part of a conditional block - you can just
have the ``if`` part.  For example, this code would do the same as the code
above:

.. nbplot::

    >>> random_no = random.random()
    >>> # Default to Heads
    >>> our_result = 1
    >>> # We have the "if" part, but no "else:" part.
    >>> if random_no < 0.5:
    ...     # Tails
    ...     our_result = 0

*********
Functions
*********

In :doc:`jupyter_intro`, we saw functions in action, such as ``len`` and
``max``.

These are functions that Python provides for us.

We can also write our own functions.

We're going to wrap up our logic for the coin toss into a function, and call
the function ``coin_toss``.  Like ``random.random`` our function ``coin_toss``
will accept no arguments.  It will return a 0 50% of the time and a 1 50% of
the time.

We make a function like this:

.. nbplot::

    >>> def coin_toss():
    ...     random_no = random.random()
    ...     if random_no < 0.5:
    ...         our_result = 0
    ...     else:
    ...         our_result = 1
    ...     return our_result

The function starts with the word ``def`` which tells Python we are defining a
function.  Next follows the name of the function, followed by, in our case,
parentheses.  You specify what arguments the function should have, in the
parentheses. In our case, our function as no arguments, so there is nothing
between the parentheses.

Next there follows a series of statements that are indented.  These statements
are the *body* of the function.  They are the code that gets run when the
function gets called.

We return the result with the ``return`` statement.  Here we are returning a 0
if a random number was < 0.5, and a 1 otherwise.

Let's call the function a few times to see if the results are plausible:

.. nbplot::

    >>> # Notice, we pass no arguments
    >>> coin_toss()
    0

.. nbplot::

    >>> coin_toss()
    1

.. nbplot::

    >>> coin_toss()
    0

********
Exercise
********

Up until now, we've assumed that the chance that a child is a boy is 0.5.  Now
assume the proportion of boys born in the UK is 0.513 [#male-births]_.

Here is a new copy of the ``coin_toss`` function, but renamed.  Like the
``coin_toss`` function, it returns 0 50% of the time, and 1 the rest of the
time.  Modify the function to return 0 (for a boy) 51.3% of the time, and 1
(for a girl) 48.7% of the time:

.. nbplot::

    >>> def girl_or_boy():
    ...     # Return 1 for a girl, 0 for a boy
    ...     random_no = random.random()
    ...     if random_no < 0.5:
    ...         our_result = 0
    ...     else:
    ...         our_result = 1
    ...     return our_result

You can try your function out a few times with the cell below:

.. nbplot::

    >>> girl_or_boy()
    0

.. _on-loops:

*****
Loops
*****

We often want to repeat some code many times.  We could type the same code
over and over again, but this would be messy, error-prone and boring.  No,
what we want, is a loop.

A loop is a set of statements that we can repeat several times.

One type of Python loop uses ``while``.

While loops
===========

For our trials, we need to do four coin tosses, and collect the results.  We
can do this with a ``while`` loop, like this:

.. nbplot::

    >>> # We use a counter to keep track of how many times we've run
    >>> counter = 0
    >>> coin_tosses = []
    >>> while counter < 4:
    ...     result = coin_toss()
    ...     coin_tosses.append(result)
    ...     counter = counter + 1
    ...
    >>> coin_tosses
    [0, 1, 1, 1]

The ``while`` loop, like the ``if`` statement, tests a condition, here
``counter < 4``.  Like the ``if`` statement, there are indented statements
after the condition test, that only run if the condition test is True.  The
difference is that a while loop keeps running the indented statements until
the condition is True.  So, the first time through, when ``counter`` is set to
0, the condition will be True (0 is less than 4), and the body of the while
loop executes.  But, when the while loop finishes running ``counter = counter
+ 1`` at the end of the block, it goes back and checks the conditional again.
Now ``counter`` is 1, but this is still less than 4, and so we proceed to run
``result = coin_toss()`` and the rest of the statements in the body.  We do
this until the condition is False, and then the while loop stops and the
program continues after the end of the while loop.

*************
Sum and count
*************

``sum`` is a function, like ``len`` or ``max``:

.. nbplot::

    >>> my_list = [3, 5, 1]
    >>> sum(my_list)
    9

``count`` is a method of a list.  As y'all remember, a method is a function
attached to something, in this case, a list.

.. nbplot::

    >>> my_list = [3, 5, 1, 3]
    >>> my_list.count(3)
    2
    >>> my_list.count(1)
    1

********
Exercise
********

Using the ``while`` loop above as a template, make a list of 10000 samples
from the ``girl_or_boy`` function you wrote above.  Calculate how many of
these samples are girls (have value of 1) (hint: ``sum`` might be useful).
What proportion of the samples are girls?  How close is this to the number you
were expecting?  Here's a copy of the ``while`` loop above, for you to use as
a template:

.. nbplot::

    >>> # A copy of the while loop above for you to edit
    >>> counter = 0
    >>> coin_tosses = []
    >>> while counter < 4:
    ...     result = coin_toss()
    ...     coin_tosses.append(result)
    ...     counter = counter + 1
    ...
    >>> coin_tosses
    [0, 1, 0, 0]

.. [#male-births] `Official UK government statistics
   <https://www.gov.uk/government/statistics/gender-ratios-at-birth-in-great-britain-2010-to-2014>`_
   give the birth ratio as 105.3. This the number of boys born for every 100
   girls.
