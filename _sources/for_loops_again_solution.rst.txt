.. vim: ft=rst

###############
For loops again
###############

.. code-links:: clear

In :doc:`for_loops`, we saw that we can repeat something ``N`` times with a
``for`` loop, like this:

.. nbplot::

    >>> #: Doing something N times
    >>> N = 4   # or whatever number you like
    >>> for i in range(N):
    ...     # Do something
    ...     print('i is set equal to', i)
    ...
    i is set equal to 0
    i is set equal to 1
    i is set equal to 2
    i is set equal to 3

Now for a little more detail on how this works, and what else you can do with
the ``for`` loop.

Consider the start of the loop: ``for i in range(N):``.  What is happening, is
that Python collects all the values on the right hand side of the loop.  That
is, it collects all the values given by ``range(N)``.  We can see these values
by making a list out of them:

.. nbplot::

    >>> #: Collecting the values in range(N)
    >>> #: Remember N == 4
    >>> list(range(N))
    [0, 1, 2, 3]

So, Python collects the values (in this case) ``[0, 1, 2, 3]``, and it feeds
them, one by one into the loop, setting the value of ``i`` with the next value
from the right hand side.  So the loop above is the equivalent of:

.. nbplot::
    :hide-from: doctest

    >>> #: The exact equivalent of the loop above
    >>> i = 0
    >>> print('i is set equal to', i)
    i is set equal to 0
    >>> i = 1
    >>> print('i is set equal to', i)
    i is set equal to 1
    >>> i = 2
    >>> print('i is set equal to', i)
    i is set equal to 2
    >>> i = 3
    >>> print('i is set equal to', i)
    i is set equal to 3

So what is we used something else on the right hand side of ``for i in ...`` ?
Could we use any list?  Yes we could.

.. nbplot::

    >>> #: we can use any list on the right hand side
    >>> my_list = [0, 9, 1, 8]
    >>> for i in my_list:
    ...     print('i is set equal to', i)
    ...
    i is set equal to 0
    i is set equal to 9
    i is set equal to 1
    i is set equal to 8

Again, Python is taking the right hand side - now ``my_list``, and feeding
each value into the loop, by setting ``i`` to be the current value.

Now for the exercise.

First - modify the loop above, and rename the variable ``i`` to a different
name, say ``my_variable``.  Does it still work?

Next - you have a list.

.. nbplot::

    >>> #: Your list
    >>> the_list = [12, 4, 3, 1, 5]

Your job is to calculate the product of all the values of this list, using a
``for`` loop.  You should get:

.. nbplot::

    >>> #: the result you want
    >>> 12 * 4 * 3 * 1 * 5
    720

Now your turn.  Read the comments for hints.

.. nbplot::

    >>> #- Make a for loop to calculate product of all elements in the_list
    >>> #- You are going to start off with something like:
    >>> #-
    >>> #- product = 1
    >>> #- for i in <something you put here>:
    >>> product = 1
    >>> for i in the_list:
    ...     product = product * i
    ...
    >>> product
    720
