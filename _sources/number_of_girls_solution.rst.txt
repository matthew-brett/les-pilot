.. vim: ft=rst

###############################
Three girls in a family of four
###############################

.. code-links:: clear

.. nbplot::

    >>> #: We need the random module
    >>> import random

We need a function to give us a boy (0) or a girl (1) following the real
proportions of p=0.513 of a male child in the UK.  We will use the function we
wrote in :doc:`loops_and_functions`:

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

If you didn't do this before, use a ``while`` loop to make another family from
boy or girl choices.  See :doc:`loops_and_functions` for inspiration:

.. nbplot::

    >>> #- Make a family from boy or girl choices, using a while loop.
    >>> a_family = []
    >>> counter = 0
    >>> while counter < 4:
    ...     a_family.append(girl_or_boy())
    ...     counter = counter + 1
    >>> sum(a_family)
    2

Now you know how to make one family.  Now you're going to make 1000 families.

First make an empty list to collect the number of girls in each family.

Then use another ``while`` loop to make 1000 families.  Careful of your
counters, for each loop. For each family, calculate the number of girls, using
the code you just wrote above.  Collect the number of girls in your list.

Finally, use the ``count`` method of the list, to count the number of families
with 3 girls.

.. nbplot::

    >>> #- Make a list to store the number of girls in each family
    >>> number_of_girls = []
    >>> #- Use a while loop to make 1000 families.
    >>> #- For each family, calculate the number of girls
    >>> #- Store in the list
    >>> sample_counter = 0
    >>> while sample_counter < 1000:
    ...     a_family = []
    ...     family_counter = 0
    ...     while family_counter < 4:
    ...         a_family.append(girl_or_boy())
    ...         family_counter = family_counter + 1
    ...     number_of_girls.append(sum(a_family))
    ...     sample_counter = sample_counter + 1
    >>> #- Count the number of families with 3 girls
    >>> number_of_girls.count(3)
    232

Finally, divide the number of families with 3 girls, by the number of families
you made (1000) to give the estimated probability of a family of four having
three girls:

.. nbplot::

    >>> #- divide the number of familes with 3 girls by the number of families
    >>> number_of_girls.count(3) / 1000
    0.232
