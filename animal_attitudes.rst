.. vim: ft=rst

############################
Attitudes to animal research
############################

.. code-links:: clear

Here we are going to try to analyze the data from this survey:

https://www.ipsos.com/ipsos-mori/en-uk/attitudes-animal-research-2016

You can download the raw data from here:

https://discover.ukdataservice.ac.uk/catalogue?sn=8059

To be helpful, I have unpacked the tab-delimited data file for you, and also
converted the data dictionary document to a PDF:

* :download:`tab-delimited data file
  <ols_animal_research_survey_data_2016.tab>`;
* :download:`data dictionary PDF file
  <ols_animal_research_survey_data_2016_ukda_data_dictionary.pdf>`.

Download the data file to the directory containing this Notebook.

.. nbplot::

    >>> #: Load pandas
    >>> import pandas as pd

.. nbplot::

    >>> #: Read file into data frame
    >>> df = pd.read_table('ols_animal_research_survey_data_2016.tab')

Display the data frame:

.. nbplot::

    >>> #: Display the data frame
    >>> df
            ID  Q1  Q2a  Q2b  Q3a  Q3b  Q3c  Q3d  Q3e  Q3f   ...    Empstat  qual  \
    0    10150   2    1    2    5    1    1    1    5    3   ...          3     1 ...
    1    10170   1    1    1    1    1    1    5    2    1   ...          3     3 ...
    2    10190   3    2    2    3    1    5    1    5    2   ...          2     2 ...
    3    10210   3    2    3    3    2    3    3    4    2   ...          3     2 ...
    4    10230   3    3    3    2    2    2    3    4    2   ...          3     2 ...
    5    10250   3    2    3    3    2    2    2    4    2   ...          1     1 ...
    ...
    <BLANKLINE>
    [987 rows x 248 columns]

Show the list of the all the column names:

.. nbplot::

    >>> #- Show the column names
    >>> df.columns
    Index(['ID', 'Q1', 'Q2a', 'Q2b', 'Q3a', 'Q3b', 'Q3c', 'Q3d', 'Q3e', 'Q3f',
           ...
           'Empstat', 'qual', 'marstat', 'access', 'Income', 'Broadsheet',
           'MidMarket', 'Tabloid', 'NoPpr', 'weight'],
          dtype='object', length=248)

Have a look at the data dictionary.  Find the name of the column containing
the variable with label "Sources of balanced information about use of:
Universities".  Keep a note of that.

Now find the name of the column with label "Sources of balanced information
about use of: Animal protection organisations".  Keep a note of that too.

Finally, find the column for "Sources of balanced information about use of:
Politicians / MPs".  Note as well.

Use indexing to select make a new data frame containing only these three
columns from the original data frame.  It will look something like ``questions
=df[`` followed by the names of the columns you just found.  Have a look at
:doc:`brexit` for inspiration.

.. nbplot::

    >>> #- Select only the two columns we found above.
    >>> #- Something like
    >>> #- questions = df[ something here ]
    >>> questions = df[['Q7_1', 'Q7_2', 'Q7_6']]

Check that your new ``questions`` data frame has the column names you
expected.

.. nbplot::

    >>> #- Show the column names for the new "questions" data frame
    >>> questions.columns
    Index(['Q7_1', 'Q7_2', 'Q7_6'], dtype='object')

Rename the columns to ``"trust_uni"``, ``"trust_protectors"``,
``"trust_politicians"``.   See :doc:`brexit` for inspiration.

.. nbplot::

    >>> #- Rename the columns of the new data frame to:
    >>> #- "trust_uni", "trust_protectors", "trust_politicians"
    >>> questions.columns = ['trust_uni', 'trust_protectors', 'trust_politicians']
    >>> questions.columns
    Index(['trust_uni', 'trust_protectors', 'trust_politicians'], dtype='object')

.. mpl-interactive::

Import the plotting library, using the same conventions as in :doc:`brexit`:

.. nbplot::

    >>> #- Import the plotting library
    >>> import matplotlib.pyplot as plt

Plot a histogram of the values for the question about trusting universities.

.. nbplot::

    >>> #- A histogram of the values for the trust universities question
    >>> plt.hist(questions['trust_uni']);
    (...)

Plot a histogram of the values for the question about trusting Animal
Protection Organizations:

.. nbplot::

    >>> #- A histogram of the values for the trust APOs question
    >>> plt.hist(questions['trust_protectors']);
    (...)

Do you think there is a substantial difference between these histograms?   How
would you check?

Plot the histogram for the trust in politicians.  Is there a difference
between this question and the other two?  How would you check?

.. nbplot::

    >>> #- A histogram of the values for the trust APOs question
    >>> plt.hist(questions['trust_politicians']);
    (...)

Save the reduced data frame in case we want to use it later:

.. nbplot::

    >>> questions.to_csv('animal_questions.csv', index=False)
