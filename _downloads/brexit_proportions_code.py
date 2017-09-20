""" Testing Brexit Proportions
"""
#: brexit proportion in survey
541 / (541 + 774)

#: The random module
import random

#: keep this for exercise built page
random.seed(1966)

#: function to return a Leave or Remain voter
def leave_or_remain():
    # Return 1 for Leave, 0 for Remain
    random_no = random.random()
    if random_no < 0.519:
        our_result = 1
    else:
        our_result = 0
    return our_result

#: call the fnction
#: remember the brackets at the end
leave_or_remain()

#: The statistic value from a single trial
def one_proportion():
    votes = []
    for i in range(1315):
        vote = leave_or_remain()
        votes.append(vote)
    brexits = sum(votes)
    return brexits / len(votes)

#: Result of one trial
one_proportion()

#: Number of trials
n_trials = 10000

#- Make a list to contain the proportion for each trial
#- Make 10000 trials.
#- For each trial, calculate the proportion and store it
#- You now have 10000 proportions.

#: The stuff you need for plotting a histogram
import matplotlib.pyplot as plt

#- plot the histogram of the sampling distribution
