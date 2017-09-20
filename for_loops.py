# $\newcommand{L}[1]{\| #1 \|}\newcommand{VL}[1]{\L{ \vec{#1} }}\newcommand{R}[1]{\operatorname{Re}\,(#1)}\newcommand{I}[1]{\operatorname{Im}\, (#1)}$
#
# ## For loops
#
# See: [Conditionals, functions and loops](https://matthew-brett.github.io/les-pilot/loops_and_functions.html) for an introduction to `while` loops.
#
# To start, let us redefine the function to do a coin toss:

import random

def coin_toss():
    random_no = random.random()
    if random_no < 0.5:
        our_result = 0
    else:
        our_result = 1
    return our_result

# Actually, people writing Python code do not often use `while` loops.  That
# is because Python has a particularly nice and general `for` loop.  Here is
# the way we would write the `while` loop above, using a `for` loop:

coin_tosses = []
for i in range(4):
    result = coin_toss()
    coin_tosses.append(result)

coin_tosses

# ## The take-home
#
# If you want to repeat something N times in Python, then use a `for` loop,
# that starts with something like `for i in range(N):`.
#
# That’s the quick version.   If you want to understand more about the `range`
# and the `i` in that statement, read on.
#
# ## More detail
#
# Notice the use of `range`.  The `range` function here gives us a sequence
# of numbers, starting at 0, and going up to, but not including 4.  Therefore,
# the `range` function is giving us 4 numbers, 0, 1, 2, 3:

list(range(4))

# Now notice the line `for i in range(4)`.  The for loop will take each of the
# numbers 0 through 3, and put it into the variable we’ve named `i`. This is
# the *loop variable*.  You can see better what is going on if we collect the
# loop variable value in the for loop, instead of doing the coin toss:

variable_values = []
for i in range(4):
    variable_values.append(i)

variable_values

# We can see the same thing, if we call the `print` function at each iteration
# of the loop, to show the value of `i`.   `print` displays the value as
# text.

for i in range(4):
    # Show the value of i at each iteration of the loop
    print('Value of i is', i)
