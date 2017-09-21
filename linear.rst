#############################################
Sampling distribution for linear relationship
#############################################

.. code-links:: clear

Test the null hypothesis that the observed linear relationship between
variables is compatible with the distribution of relationships when order of
the second variable is randomized.

See: :doc:`school_and_fertility`.

.. nbplot::

    >>> #: The random module
    >>> import random

    >>> def list_product(first_list, second_list):
    ...     product = 0
    ...     for i in range(len(first_list)):
    ...         value = first_list[i] * second_list[i]
    ...         product = product + value
    ...     return product

    >>> def linear_permute(measures_1, measures_2):
    ...     measures_1 = list(measures_1)
    ...     new_measures_2 = list(measures_2)
    ...     n_samples = 10000
    ...     observed = list_product(measures_1, measures_2)
    ...     sample_products = []
    ...     for i in range(n_samples):
    ...         random.shuffle(new_measures_2)
    ...         product = list_product(measures_1, new_measures_2)
    ...         sample_products.append(product)
    ...     return observed, sample_products

In action on the school, fertility data.

.. nbplot::

    >>> import pandas as pd
    >>> school_fertility = pd.read_csv('school_fertility.csv')
    >>> school = list(school_fertility['school'])
    >>> fertility = list(school_fertility['fertility'])
    >>> observed, distribution = linear_permute(school, fertility)
    >>> observed
    63210.978138184139

.. mpl-interactive::

.. nbplot::

    >>> import matplotlib.pyplot as plt
    >>> plt.hist(distribution)
    (...)
