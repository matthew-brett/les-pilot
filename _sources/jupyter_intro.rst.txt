####################################
Introduction to the Jupyter Notebook
####################################

.. code-links:: clear

********************
A Notebook has cells
********************

As you can see, the Jupyter Notebook runs in your web browser.

It consists of *cells*. This is a text cell.  The cell below is a code cell.

You can mix code and text cells in any order.

To move from one cell to the next, you can use Shift-Enter. When you do
this inside a code cell, it will execute, and move to the next cell.

Press Shift-Enter now, to move out of this cell to the next, then Shift-Enter
again to run the text cell, and move again.

.. nbplot::

    >>> a = 10

It doesn't look as if anything has happened, but when you did Shift-Enter in
the cell above, the Jupyter Notebook sent the code off to be executed by
`Python <https://python.org>`_.  Python is a programming language with a
simple syntax that many universities use for teaching.  There is also a large
community of scientists and tech companies that use Python for data analysis.

The code cell above takes the *number* 10, and puts it into a *variable*
called ``a``. Now, when we use the variable ``a``, it will carry the value 10.
We say that the *variable* ``a`` has the *value* 10.

We often want to see the values of variables, and the Notebook makes it easy
to do that. We put the variable who value we want to see on its own at the end
of a cell. The Notebook detects that we have done that, and shows us the
value.  Here we display the value of the variable ``a``:

.. nbplot::

    >>> a
    10

Notice that the Notebook made a new type of display after the cell, with the
prompt in red, and starting with ``Out[``. Every code cell has a number, such
as 1, or 2. The Notebook labels the cell with its number.  The code that will
be executed has the label ``In[`` followed by the cell number, meaning
*Input*. If there is a variable on its own at the end, that will generate an
*Output* cell, labeled with ``Out[`` followed by the cell number.

Our code cells can have lines that do some work, followed by a variable on its
own, so we can see its value. Like this:

.. nbplot::

    >>> b = 5
    >>> b
    5

****************************
The Notebook as a calculator
****************************

To get output from the cell, we don't actually need to have a variable on its
own. We can put any *expression* on the last line. An expression is anything
that returns a value.  So ``b`` on its own returns a value, which is the value
of ``b`` - in this case 5. But we can also do something like this:

.. nbplot::

    >>> (10 + 5 + 1) / 4
    4.0

Notice, we didn't use any variables. ``(10 + 5 + 1) / 4`` is an expression -
some code that returns a value.

This means that we can use the Notebook as a simple calculator. You've
already seen ``+`` and ``/`` and the parentheses. You also have ``*`` for
multiply, and ``-`` for subtract, and ``**`` for to-the-power-of.  For
example, here's :math:`10^4`:

.. nbplot::

    >>> 10 ** 4
    10000

Try calculating :math:`6 (2^3) / 4` (it should equal 12):

.. nbplot::

    >>> 6 * 2 ** 3 / 4
    12.0

Try :math:`1024^2 / 2^{16}`

.. nbplot::

    >>> 1024 ** 2 / 2**16
    16.0

We can also use variables in our calculations. For example, we might be
interested in the result of :math:`2 x^2 + 3x + 10`. We want to calculate what
answer we get for :math:`x = 2`.

.. nbplot::

    >>> x = 2
    >>> x
    2

.. nbplot::

    >>> 2 * x ** 2 + 3 * x + 10
    24

Now we can simply get the answer for :math:`x = 7`, or any other value
of :math:`x`:

.. nbplot::

    >>> x = 7
    >>> 2 * x ** 2 + 3 * x + 10
    129

******************************
Comments begin with a hash (#)
******************************

The code cells in this Notebook, and all the Notebooks we'll use in the class,
will be in the Python programming language. In that language (and many
others), a line beginning with ``#`` is a *comment*, which means that Python
does not do anything with that line, and it just serves to explain the code.

.. nbplot::

    >>> # This is a comment.  It doesn't do anything.
    >>> # This is another comment.  It is just for your reading pleasure.
    >>> # The line below sets the variable c to have value 10.
    >>> c = 10
    >>> # The last line is an expression, and so we see an output of this expression
    >>> # after the cell.
    >>> c
    10

********************
Strings contain text
********************

So far we have only seen numbers. Another type of information that Python can
store and use, is text. Python calls text data: *strings*. For example, here I
set the variable ``my_name`` to the *string* ``'Matthew'``. Notice the quotes
around the string. The quotes tell Python that this is text (string) data:

.. nbplot::

    >>> my_name = 'Matthew'
    >>> my_name
    'Matthew'

You can use single quotes (``'``) to go round strings, or double quotes
(``"``). It doesn't matter to Python, it recognizes you want to make a
string.

.. nbplot::

    >>> # I'm setting your_name to the string 'Alphonse' using single quotes
    >>> your_name = 'Alphonse'
    >>> your_name
    'Alphonse'

.. nbplot::

    >>> # But I could have used double quotes, it ends up the same to Python.
    >>> third_name = "Alphonse"
    >>> third_name
    'Alphonse'

************************
Functions process things
************************

Python also has *functions*. It is easiest to explain a function by example.
``len`` is a function, returning the length of something. Here we get the
length of the string:

.. nbplot::

    >>> len('Alphonse')
    8

The result that Python returned from ``len`` is the number of characters in
the string ``'Alphonse'``. The variable ``your_name`` also points to the
string ``'Alphonse'``, so we get the same result from calling ``len`` on the
variable ``your_name``:

.. nbplot::

    >>> len(your_name)
    8

The function has a name - ``len``. We call it, by using its name and then an
opening parenthesis, and then the *arguments* that we want to send to the
function, and then a closing parenthesis.

In this case the function ``len`` accepts only one argument, which is the
thing we want the length of.

Now try setting the variable ``my_name`` to a string containing your first
(given) name. Then get the Notebook to tell you how many characters there are
in your name. Here's how I would do that, in the cell below. You can edit the
cell to put your name in there instead.

.. nbplot::

    >>> my_name = 'Matthew'
    >>> len(my_name)
    7

There are functions which work on numbers as well. For example, the function
``max`` accepts two (or more) numbers, and returns the maximum:

.. nbplot::

    >>> max(10, 4)
    10

*****
Lists
*****

Python has other useful types of data. One very useful type is the *list*.
Here is a list of two numbers:

.. nbplot::

    >>> my_list = [10, 4]
    >>> my_list
    [10, 4]

Notice the square brackets around the list items, and a comma between the
items.

What do you think you will get calling ``len`` on this list? Try it.

.. nbplot::

    >>> # Try: len(my_list)

You can make an empty list by putting nothing between the brackets:

.. nbplot::

    >>> my_empty_list = []
    >>> my_empty_list
    []

Another thing we might want to do to a list is append a value.  We can do this
using the ``append`` *method* of the list.  A *method* is a function attached
to a value.  This is best seen in action:

.. nbplot::

    >>> my_list.append(7)
    >>> my_list
    [10, 4, 7]

.. nbplot::

    >>> my_list.append(1)
    >>> my_list
    [10, 4, 7, 1]

Notice that we *call* the method using the name of the list - here
``my_list``, followed by a dot, followed by the name of the method, here
``append``.  ``append`` is a function attached to ``my_list``.

Don't worry about the details at the moment, we will have many chances to get
used this this idea.

***********************
Careful of the brackets
***********************

You need square brackets - ``[`` and ``]`` to make a list.  If you use
parentheses ``()`` or curly brackets ``{}`` - you'll get something other than
a list - be careful.

******************************
Set equal to and test equal to
******************************

We have been setting the values of variables with the variable name (e.g.
`my_name`) followed by the equals character `=` and then the value. For
example:

.. nbplot::

    >>> # Setting variable my_name to have value "Matthew"
    >>> my_name = "Matthew"

This is the use of equal to mean "set the variable on the left equal to the
value on the right".

There is another use of "equal" which is to test whether something is equal to
something else.  This is called "test equals".  Python uses double equal signs
``==`` for that meaning of equals.  For example, here we test whether the
value of variable ``my_name`` is equal to the string `'John'`:

.. nbplot::

    >>> # Equal in the sense of test equal to
    >>> my_name == 'John'
    False

Notice that test-equal, with ``==``, is an expression, that returns the value
``True`` if the two sides are equal, and ``False`` if they are not:

.. nbplot::

    >>> # Equal in the sense of test equal to
    >>> my_name == 'Matthew'
    True

********
Packages
********

So far all the stuff we have seen uses functions that Python will always
give you. For example, ``len`` and ``max`` are always available to you,
whenever you start Python.

There are many other things that Python keeps in *modules*. Modules are
libraries of functions and other things, that you cannot use, until you
load them into Python. You load them into Python using the ``import``
command.

For example, we are soon going to be using the ``random`` module. This
is a module that gives us random numbers of various sorts. Before we can
use the ``random`` module, we have to ``import`` it - like this:

.. nbplot::

    >>> import random

Now we have the random module loaded, we can access its functions, by
typing the module name ``random``, followed by a dot, followed by the
function we want to use. For example, ``random`` has a function
``randint``, that returns a number between the first argument (the low
bound) and the second argument (the high bound). We can get a random
number between 0 and 10 like this:

.. nbplot::
    :hide-from: all
    :show-to: doctest

    >>> random.seed(1939)

.. nbplot::

    >>> random.randint(0, 10)
    9

.. _getting-help:

********
Exercise
********

Using what you have learned above, make a cell that creates an empty list,
then appends three random numbers between 0 and 100.

.. nbplot::

    >>> #- Make an empty list.
    >>> #- Make a random number between 0 and 100
    >>> #- Append it to the list
    >>> #- Do this three times
    >>> #- Show the new list with three numbers.

************
Getting help
************

Often we want to know what a function does, or how many arguments it takes.
The Notebook has a useful feature to help us. Type the name of the function
you are interested in, followed by ``?`` and press Shift-Enter. The Notebook
will show you pane of help on that function.  Try it now, for ``len`` and
``max``.

.. nbplot::

    >>> # Type (e.g):
    >>> #
    >>> # len?
    >>> #
    >>> # in the cell below

It is also common that we want to know what functions or other goodies there
are in a module.  The Notebook can help with that too.  In the code cell
below, try typing `random.` (note the trailing dot) and then, without pressing
Return, press the Tab key.  The Notebook shows you a list of functions and
other things inside the ``random`` module.  This is called "Tab completion".

.. nbplot::

    >>> # Type:
    >>> #
    >>> # random.
    >>> #
    >>> # followed by Tab, in the cell below
