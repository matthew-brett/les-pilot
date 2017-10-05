from os.path import join as pjoin

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from numbers import Number
from collections import Counter
from textwrap import wrap


def bd(fn):
    return pjoin('feedback', fn)


responses = pd.read_csv(bd('student_feedback.csv'))


def default_bar(column_name, labels, plot_labels=None, figsize=None,
                wrapcols=0):
    if isinstance(labels, Number):
        n = labels
        labels = range(1, n + 1)
    else:
        n = len(labels)
    if plot_labels is None:
        plot_labels = labels
    if wrapcols:
        plot_labels = ['\n'.join(wrap(line, wrapcols))
                       for line in plot_labels]
    column = responses[column_name]
    counts = Counter(list(column))
    values = [counts[label] for label in labels]
    max_c = max(values)
    fig, ax = plt.subplots(figsize=figsize)
    ax.barh(range(n), values[::-1])
    ax = plt.gca()
    ax.set_xticks(range(max_c + 1))
    ax.set_xticklabels(range(max_c + 1))
    ax.set_yticks(range(n))
    ax.set_yticklabels(plot_labels[::-1])
    plt.subplots_adjust(left=0.2)
    return column


def responses_to_markdown(column_name, n_cols=76, header_level=2):
    column = responses[column_name]
    # Some lines may be NaN
    replies = ['> ' + '\n> '.join(wrap(line, n_cols)) for line in column
               if isinstance(line, str)]
    return '{} {}\n\n{}\n'.format(
        '#' * header_level,
        column_name,
        '\n\n'.join(replies))


fig = default_bar('The main reason I wanted to do this course was', [
    'I wanted to learn more about data analysis',
    'The 100 pound bursary',
    'The bursary and the learning were equally important.'],
    wrapcols=15)
plt.savefig(bd('fb_main_reason.png'))

default_bar('How much computer code have you written?', [
    "I've never written any code",
    "I've played with code but never wrote anything useful",
    "I have written a small amount of useful code.",
    "I have written a lot of useful code."
    ],
    wrapcols=15)
plt.savefig(bd('fb_code_written.png'))


col = default_bar('I had a better understanding of statistics after the course.', 5, 
           ['Agree - 1', '2', '3', '4', 'Disagree - 5'])
plt.text(5, 0, 'Mean: {:0.1f}'.format(np.mean(col)))
plt.savefig(bd('fb_better_statistics.png'))


col = default_bar('After the course, I feel more confident about doing my own data analysis', 5, 
               ['Disagree - 1', '2', '3', '4', 'Agree - 5'])
plt.text(3, 4, 'Mean: {:0.1f}'.format(np.mean(col)))
plt.savefig(bd('fb_confident.png'))


col = default_bar('Writing the statistical procedures in code made them harder to understand.', 5, 
               ['Agree - 1', '2', '3', '4', 'Disagree - 5'])
plt.text(4, 0, 'Mean: {:0.1f}'.format(np.mean(col)))
plt.savefig(bd('fb_code_helps.png'))


col = default_bar('About the pace of the course, was it:', 5,
            ['Too fast - 1', '2', '3', '4', 'Too slow - 5'])
plt.text(4, 0, 'Mean: {:0.1f}'.format(np.mean(col)))
plt.savefig(bd('fb_pace.png'))


with open(bd('fb_like_most.md'), 'wt') as fobj:
    fobj.write(responses_to_markdown(
        'What did you like most about the course?'
    ))

with open(bd('fb_could_change.md'), 'wt') as fobj:
    fobj.write(responses_to_markdown(
        'If there was one thing about the course you could change, what would it be?'
    ))

with open(bd('fb_other_suggestions.md'), 'wt') as fobj:
    fobj.write(responses_to_markdown(
        'Do you have any other suggestions for the next time we do this course?'
    ))
