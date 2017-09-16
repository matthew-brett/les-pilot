.. vim: ft=rst

###############################
Three girls in a family of four
###############################

.. code-links:: clear

.. nbplot::

    >>> #: We need the random module
    >>> import random

Now we need a function to do a coin toss.  Assume that probability of heads
is 0.5.  The function returns 1 for head and 0 for a tail:

.. nbplot::

    >>> #: A function for a single coin toss
    >>> def coin_toss():
    ...     random_no = random.random()
    ...     if random_no <= 0.5:
    ...         return 1
    ...     return 0

Test the function a few times:

.. nbplot::
    :hide-from: all
    :show-to: doctest

    >>> random.seed(1966)

Test the ``coin_toss`` function a few times.  It should come up with a few 1s
and a few 0s.

.. nbplot::

    >>> #- Test the coin toss a few times
    >>> coin_toss()
    0
    >>> coin_toss()
    0
    >>> coin_toss()
    0
    >>> coin_toss()
    0
    >>> coin_toss()
    1
    >>> coin_toss()
    0

Now make a list, called `a_family`, and collect four coin tosses:

.. nbplot::

    >>> #- Make a list, and collect four coin tosses
    >>> a_family = []
    >>> a_family.append(coin_toss())
    >>> a_family.append(coin_toss())
    >>> a_family.append(coin_toss())
    >>> a_family.append(coin_toss())
    >>> a_family
    [1, 1, 1, 0]

Let's take 1 from the coin toss to mean a girl.  Sum up the results of the
four coin tosses to say how many girls in this family.

.. nbplot::

    >>> #- Sum the list to give the number of girls in this family
    >>> sum(a_family)
    3

If you didn't do this before, use a ``for i in range(...)`` loop to make
another family from coin tosses.  See :doc:`programs_in_python` for
inspiration:

.. nbplot::

    >>> #- Make a family from coin tosses, using a for loop.
    >>> a_family = []
    >>> for i in range(4):
    ...     a_family.append(coin_toss())
    >>> sum(a_family)
    1

Now you know how to make one family.  Now you're going to make 1000 families.

First make an empty list to collect the number of girls in each family.

Then use another ``for s in range(...)`` loop to make 1000 families.  For each
family, calculate the number of girls, using the code you just wrote above.
Collect the number of girls in your list.

Finally, use the ``count`` method of the list, to count the number of families
with 3 girls.

.. nbplot::

    >>> #- Make a list to store the number of girls in each family
    >>> number_of_girls = []
    >>> #- Use a for loop to make 1000 families.
    >>> #- For each family, calculate the number of girls
    >>> #- Store in the list
    >>> for s in range(1000):
    ...     a_family = []
    ...     for i in range(4):
    ...         a_family.append(coin_toss())
    ...     number_of_girls.append(sum(a_family))
    >>> #- Count the number of families with 3 girls
    >>> number_of_girls.count(3)
    259

Finally, divide the number of families with 3 girls, by the number of families
you made (1000) to give the estimated probability of a family of four having
three girls:

.. nbplot::

    >>> #- divide the number of familes with 3 girls by the number of families
    >>> number_of_girls.count(3) / 1000
    0.259
