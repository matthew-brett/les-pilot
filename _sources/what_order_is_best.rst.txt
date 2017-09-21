###################
What order is best?
###################

.. code-links:: clear

Here I have a list of 4 numbers:

.. nbplot::

    >>> my_numbers = [-1, 5, 10, 21]

Here I have another list of 4 numbers:

.. nbplot::

    >>> your_numbers = [3, 0, -10, 15]

Here is a function, that takes each element in the two lists, multiplies them,
and retuns the sum.

.. nbplot::

    >>> def list_product(first_list, second_list):
    ...     product = 0
    ...     for i in range(len(first_list)):
    ...         value = first_list[i] * second_list[i]
    ...         product = product + value
    ...     return product

Let's see the ``list_product`` for our two lists:

.. nbplot::

    >>> list_product(my_numbers, your_numbers)
    212

Now - here is your problem.  You can shuffle the second list,
``your_numbers``, in any way you like.  What is the right order for the
numbers in ``your_numbers``, to give the highest value for the
``list_product``?

For example, here I'm doing a random shuffle of the list:

.. nbplot::

    >>> #: The random module
    >>> import random

.. nbplot::
    :hide-from: all
    :show-to: doctest

    >>> random.seed(1966)

.. nbplot::

    >>> random.shuffle(your_numbers)
    >>> your_numbers
    [15, 0, -10, 3]

And I calculate the list product again:

.. nbplot::

    >>> list_product(my_numbers, your_numbers)
    -52

See if you can find the best ordering to give the highest sum.

If you've done that, see if you can find the best ordering for the *lowest*
sum.
