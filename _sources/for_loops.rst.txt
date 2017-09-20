#########
For loops
#########

.. code-links:: clear

See: :doc:`loops_and_functions` for an introduction to ``while`` loops.

To start, let us redefine the function to do a coin toss:

.. nbplot::

    >>> import random

.. nbplot::
    :hide-from: all
    :show-to: doctest

    >>> random.seed(1939)

.. nbplot::

    >>> def coin_toss():
    ...     random_no = random.random()
    ...     if random_no < 0.5:
    ...         our_result = 0
    ...     else:
    ...         our_result = 1
    ...     return our_result

In :ref:`loops and functions <on-loops>`, we have already used ``while`` loops
to collect four coin toses.  Just to remind you, the ``while`` loop looks like
this:

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
    [1, 1, 0, 1]

In face, people writing Python code do not often use ``while`` loops.  That is
because Python has a particularly nice and general ``for`` loop.  Here is the
way we would write the ``while`` loop above, using a ``for`` loop:

.. nbplot::

    >>> coin_tosses = []
    >>> for i in range(4):
    ...     result = coin_toss()
    ...     coin_tosses.append(result)
    ...
    >>> coin_tosses
    [0, 0, 1, 0]

*************
The take-home
*************

If you want to repeat something N times in Python, then use a ``for`` loop,
that starts with something like ``for i in range(N):``.

That's the quick version.   If you want to understand more about the ``range``
and the ``i`` in that statement, read on.

***********
More detail
***********

Notice the use of ``range``.  The ``range`` function here gives us a sequence
of numbers, starting at 0, and going up to, but not including 4.  Therefore,
the ``range`` function is giving us 4 numbers, 0, 1, 2, 3:

.. nbplot::

    >>> list(range(4))
    [0, 1, 2, 3]

Now notice the line ``for i in range(4)``.  The for loop will take each of the
numbers 0 through 3, and put it into the variable we've named ``i``. This is
the *loop variable*.  You can see better what is going on if we collect the
loop variable value in the for loop, instead of doing the coin toss:

.. nbplot::

    >>> variable_values = []
    >>> for i in range(4):
    ...     variable_values.append(i)
    ...
    >>> variable_values
    [0, 1, 2, 3]

We can see the same thing, if we call the ``print`` function at each iteration
of the loop, to show the value of ``i``.   ``print`` displays the value as
text.

.. nbplot::

    >>> for i in range(4):
    ...     # Show the value of i at each iteration of the loop
    ...     print('Value of i is', i)
    ...
    Value of i is 0
    Value of i is 1
    Value of i is 2
    Value of i is 3
