#########################
Chi-squared by simulation
#########################

.. topics
    +=
    slicing
    np.any
    np.zeros
    indexing into an array

.. nbplot::

    >>> import numpy as np

We can make empty arrays like this:

.. nbplot::

    >>> new_array = np.zeros((2, 3))
    >>> new_array
    array([[ 0.,  0.,  0.],
           [ 0.,  0.,  0.]])

Use of ``np.all``:

.. nbplot::

    >>> np.all(new_array == 0)
    True
    >>> new_array[0, 0] = 99
    >>> new_array
    array([[ 99.,   0.,   0.],
           [  0.,   0.,   0.]])
    >>> np.all(new_array == 0)
    False

Make a table with the counts in it:

.. nbplot::

    >>> gs_table = np.array([[1, 9], [11, 3]])
    >>> gs_table
    array([[ 1,  9],
           [11,  3]])

The sum of all the values in the table.  This gives the total number of people
surveyed.

.. nbplot::

    >>> n = gs_table.sum()
    >>> n
    24

We can use *slicing* to get individual rows and columns.  Here we get the
first row:

.. nbplot::

    >>> # First row, and all the columns (there are only two)
    >>> men = gs_table[0, :]
    >>> men
    array([1, 9])

We can get the sum of this new row too, to get the total number of men:

.. nbplot::

    >>> n_men = men.sum()
    >>> n_men
    10

Here we get the first column:

.. nbplot::

    >>> # All the rows, and only the first column (there are only two)
    >>> studiers = gs_table[:, 0]
    >>> studiers
    array([ 1, 11])

The probabilities that an observation drawn from the $n$ observations at
random, will be a man:

.. nbplot::

    >>> p_man = n_men / n
    >>> p_man
    0.41666666666666669

The probabilities that an observation drawn from the $n$ observations at
random, will be a studier:

.. nbplot::

    >>> p_studier = studiers.sum() / n
    >>> p_studier
    0.5

.. nbplot::

    >>> import random

.. nbplot::
    :hide-from: all
    :show-to: doctest

    >>> random.seed(42)

.. nbplot::

    >>> def is_man():
    ...     if random.random() <= p_man:
    ...         return 1
    ...     return 0

.. nbplot::

    >>> n_repeats = 10000
    >>> people = []
    >>> for i in range(n_repeats):
    ...     people.append(is_man())
    >>> sum(people) / len(people)
    0.4166

.. nbplot::

    >>> def is_studier():
    ...     if random.random() <= p_studier:
    ...         return 1
    ...     return 0

.. nbplot::

    >>> people = []
    >>> for i in range(n_repeats):
    ...     people.append(is_studier())
    >>> sum(people) / len(people)
    0.4941

.. nbplot::

    >>> def make_table(n_observations):
    ...     new_table = np.zeros((2, 2))
    ...     for i in range(n_observations):
    ...         if is_man():
    ...             if is_studier():
    ...                 new_table[0, 0] += 1
    ...             else:
    ...                 new_table[0, 1] += 1
    ...         else: # A woman
    ...             if is_studier():
    ...                 new_table[1, 0] += 1
    ...             else:
    ...                 new_table[1, 1] += 1
    ...     return new_table

.. nbplot::

    >>> make_table(n)
    array([[ 8.,  4.],
           [ 7.,  5.]])

.. nbplot::

    >>> make_table(n)
    array([[ 5.,  4.],
           [ 7.,  8.]])

.. nbplot::

    >>> def make_similar_table(example_table):
    ...     n = example_table.sum()
    ...     row_totals = example_table.sum(axis=1)
    ...     column_totals = example_table.sum(axis=0)
    ...     while True:  # Run forever, until break
    ...         new_table = make_table(n)
    ...         if np.any(row_totals != new_table.sum(axis=1)):
    ...             continue
    ...         if np.any(column_totals != new_table.sum(axis=0)):
    ...             continue
    ...         break # the rows and columns are all equal to the original
    ...     return new_table

.. nbplot::

    >>> make_similar_table(gs_table)
    array([[ 7.,  3.],
           [ 5.,  9.]])

.. nbplot::

    >>> make_similar_table(gs_table)
    array([[ 3.,  7.],
           [ 9.,  5.]])

.. nbplot::

    >>> p_woman = 1 - p_man
    >>> p_not_study = 1 - p_studier
    >>> expected_probs = np.array([[p_man * p_studier, p_man * p_not_study],
    ...                            [p_woman * p_studier, p_woman * p_not_study]])
    >>> expected_table = expected_probs * n

.. nbplot::

    >>> def chi2(table):
    ...     o_minus_e = table - expected_table
    ...     oe2_e = o_minus_e ** 2 / expected_table
    ...     return oe2_e.sum()

.. nbplot::

    >>> actual_chi2 = chi2(gs_table)
    >>> actual_chi2
    10.971428571428572

.. nbplot::

    >>> simulated_table = make_similar_table(gs_table)
    >>> simulated_chi2 = chi2(simulated_table)
    >>> simulated_chi2
    0.68571428571428572

.. nbplot::

    >>> n_repeats = 10000
    >>> simulated_chi2s = []
    >>> for i in range(n_repeats):
    ...     simulated_table = make_similar_table(gs_table)
    ...     s_chi2 = chi2(simulated_table)
    ...     simulated_chi2s.append(s_chi2)

.. mpl-interactive::


.. nbplot::

    >>> import matplotlib.pyplot as plt

.. nbplot::

    >>> plt.hist(simulated_chi2s, bins=100)
    (...)

.. nbplot::

    >>> simulated_chi2s.sort()

.. nbplot::

    >>> first_as_big = n_repeats
    >>> for i in range(n_repeats):
    ...     if simulated_chi2s[i] >= actual_chi2:
    ...         first_as_big = i
    >>> first_as_big
    9999

.. nbplot::

    >>> number_as_big = n_repeats - first_as_big
    >>> proportion_as_big = number_as_big / n_repeats
    >>> print(proportion_as_big)
    0.0001
