##########################
More on working with lists
##########################

**************************
Concatenating lists with +
**************************

You can add lists together.

.. nbplot::

    >>> my_list = [11, 12, 13]
    >>> your_list = [5, 6, 7]
    >>> long_list = my_list + your_list
    >>> long_list
    [11, 12, 13, 5, 6, 7]

Adding lists with ``+`` makes a new list with the values from the first list
followed by the values from the second.

***********************************
Getting list elements with indexing
***********************************

You can also *index* lists to return list elements.

In Python, as for many other languages, the first element in the list is at
index 0:

.. nbplot::

    >>> # Indexing a list to get the first element (index 0)
    >>> long_list[0]
    11
    >>> # Indexing to get the second element (index 1)
    >>> long_list[1]
    12

**************************************
Getting parts of the list with slicing
**************************************

You can also take *slices* out of lists.  For example, here we ask for all the
elements in the list from (and including) index 1 (the second element).

.. nbplot::

    >>> # Everything from the second element (index 1)
    >>> # 1 is the "start index"
    >>> long_list[1:]
    [12, 13, 5, 6, 7]
    >>> # Everything from the fourth element (index 3)
    >>> long_list[3:]
    [5, 6, 7]

You can also ask for everything up to *but not including* a particular
element.  For example, here is everythin up to *but not including* the fourth
element (index 3).  Notice the colon followed by the number, which is called
the *stop index*.

.. nbplot::

    >>> # Everything up to but not including the fourth element
    >>> # 3 is the "stop index"
    >>> long_list[:3]
    [11, 12, 13]

So, if we want to split a list at element index 3, we would do this:

.. nbplot::

    >>> # Splitting a list at index 3
    >>> first_part = long_list[:3]
    >>> first_part
    [11, 12, 13]

.. nbplot::

    >>> second_part = long_list[3:]
    >>> second_part
    [5, 6, 7]

You can specify both the start index and the stop index, like this:

.. nbplot::

    >>> # Everything from index 1, up to, not including, index 3
    >>> long_list[1:3]
    [12, 13]

.. _list-shuffle:

****************************
Shuffling list element order
****************************

We find that we ofen want to shuffle the order of list elements, to have a
random order.

Python's ``random.shuffle`` function can do the shuffle for us:

.. nbplot::

    >>> import random

.. nbplot::
    :hide-from: all
    :show-to: doctest

    >>> random.seed(7)

``random.shuffle`` takes a list and shuffles it to a random order. Here I make
a small example list and shuffle it a few times to show that the order of the
list changes:

.. nbplot::

    >>> # A small example list
    >>> a_list = [1, 2, 3, 4, 5]
    >>> # Shuffle it
    >>> random.shuffle(a_list)
    >>> # The shuffled list has a different (random) order
    >>> a_list
    [5, 1, 4, 2, 3]

.. nbplot::

    >>> # Shuffling again gives a different order
    >>> random.shuffle(a_list)
    >>> a_list
    [4, 2, 1, 3, 5]

.. nbplot::

    >>> random.shuffle(a_list)
    >>> a_list
    [3, 1, 4, 2, 5]
