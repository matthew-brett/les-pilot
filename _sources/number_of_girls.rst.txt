.. vim: ft=rst

###############################
Three girls in a family of four
###############################

.. code-links:: clear

.. nbplot::

    >>> #: We need the random module
    >>> import random

We need a function to give us a boy (0) or a girl (1) following the real
proportions of p=0.513 of a male child in the UK [#male-births]_.  We will use
the function we wrote in :doc:`loops_and_functions`:

.. nbplot::

    >>> def girl_or_boy():
    ...     # Return 1 for a girl, 0 for a boy
    ...     random_no = random.random()
    ...     if random_no < 0.513:
    ...         # A boy
    ...         our_result = 0
    ...     else:
    ...         # A girl
    ...         our_result = 1
    ...     return our_result

Test the function a few times:

.. nbplot::
    :hide-from: all
    :show-to: doctest

    >>> random.seed(1966)

Test the ``girl_or_boy`` function a few times.  It should come up with a few
1s and a few 0s.

.. nbplot::

    >>> #- Test the boy / girl function a few times
    >>> girl_or_boy()
    1
    >>> girl_or_boy()
    1
    >>> girl_or_boy()
    1
    >>> girl_or_boy()
    1
    >>> girl_or_boy()
    0
    >>> girl_or_boy()
    1

Now make a list, called `a_family`, and collect four boy or girl choices:

.. nbplot::

    >>> #- Make a list, and collect four boy or girl choices
    >>> a_family = []
    >>> a_family.append(girl_or_boy())
    >>> a_family.append(girl_or_boy())
    >>> a_family.append(girl_or_boy())
    >>> a_family.append(girl_or_boy())
    >>> a_family
    [0, 0, 0, 1]

Remember 1 means a girl.  Sum up the results of the four coin tosses to say
how many girls in this family.

.. nbplot::

    >>> #- Sum the list to give the number of girls in this family
    >>> sum(a_family)
    1

If you didn't do this before, use a ``for`` loop to make another family from
boy or girl choices.  See :doc:`loops_and_functions` for inspiration:

.. nbplot::

    >>> #- Make a family from boy or girl choices, using a for loop.
    >>> a_family = []
    >>> for i in range(4):
    ...     a_family.append(girl_or_boy())
    >>> sum(a_family)
    2

We know how to make one family.  Now we make 1000 families.

First make an empty list to collect the number of girls in each family.

Then use another ``for`` loop to make 1000 families.  For each family,
calculate the number of girls, using the code you just wrote above.  Collect
the number of girls in your list.

We use the ``count`` method of the list, to count the number of families with
3 girls.

.. nbplot::

    >>> #- Make a list to store the number of girls in each family
    >>> number_of_girls = []
    >>> #- Use a for loop to make 1000 families.
    >>> #- For each family, calculate the number of girls
    >>> #- Store in the list
    >>> for i in range(1000):
    ...     a_family = []
    ...     for j in range(4):
    ...         a_family.append(girl_or_boy())
    ...     number_of_girls.append(sum(a_family))
    >>> #- Count the number of families with 3 girls
    >>> number_of_girls.count(3)
    232

Finally, we divide the number of families with 3 girls, by the number of
families you made (1000) to give the estimated probability of a family of four
having three girls:

.. nbplot::

    >>> #- divide the number of familes with 3 girls by the number of families
    >>> number_of_girls.count(3) / 1000
    0.232

.. [#male-births] `Official UK government statistics
   <https://www.gov.uk/government/statistics/gender-ratios-at-birth-in-great-britain-2010-to-2014>`_
   give the birth ratio as 105.3. This the number of boys born for every 100
   girls.
