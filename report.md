---
# YAML metadata
title: "First pilot study on statistics with computing"
bibliography: les_pilot.bib
---

# Summary

This is a report of a pilot course teaching statistics through computing, run
over 10 hours of face-to-face teaching, from September 19th through the 21st.

The course web page is https://github.com/matthew-brett/les-pilot

We covered:

* solving a simple probability problem through physical simulation, and
  simulation with simple programming;
* extending this problem to analyze responses from survey data;
* sample statistics and the sampling distribution (equivalent to standard
  error of mean);
* comparing groups by permutation testing (equivalent to t-tests);
* using permutation for paired tests (equivalent to paired t-tests);
* comparing measures by permutation (equivalent to correlation).

In the final 2 hour session I asked the students to try their own analysis on
the data of their choice, either their own data, or using the datasets from
the teaching and exercises.

I was therefore trying to cover most of basic statistics, at fundamental
level, as well as some Python coding; this was very ambitious for 10 hours
total work time.

My impressions were:

* there was a very large difference between students in their level of comfort
  with Python code;
* the only student who had written a lot of code before found the course too
  slow, but most found the course too fast;
* the students seemed to enjoy the final session, and to be surprised at the
  amount of analysis they were able to do.

Next time I plan to:

* explore ways of introducing code to those with no previous experience;
* simplify the initial simulation;
* add code exercises to practice the basic constructs they need;
* remove discussion of the paired test and correlation by permutation.  These
  follow naturally from the permutation test between groups.

# Background

My discussions with teachers in the four LES schools suggested that students:

* often do not have a deep understanding of statistics after their current
  courses;
* find it hard to see the relevance of statistics courses to their core
  discipline, until they start their final year projects.

There seems to be a general feeling that we should teach new students to use code, to broaden the range of data they can analyze, and give them more flexibility in analysis methods.

There has been a lot of discussion among teachers of statistics about problems
with current undergraduate courses - see @cobb2015mere - "Mere Renovation is
Too Little Too Late: We Need to Rethink Our Undergraduate Curriculum from the
Ground Up” and commentaries on this paper at
https://nhorton.people.amherst.edu/mererenovation.  There seems to be some
consensus that the next generation of statistics courses should:

* teach how to "think with data" [@horton2015think];
* make statistical reasoning accessible by teaching in terms of algorithms and
  computation instead of mathematics [@cobb2015mere; @hesterberg2015teachers].
  Courses should teach "computational thinking" [@temple_lang2015];
* use analysis with real data and open questions to give an "authentic data
  analysis experience" [@temple_lang2015] by "teaching through research"
  [@cobb2015mere].

The second of these arguments is another reason to teach code - in order to
make statistical reasoning more accessible to students who do not have a
substantial background in mathematics.

# Prior art

Julian Simon advocated teaching statistics through resampling from the mid
sixties.  His book [-@simon1997resampling], which is [freely available
online](http://www.resample.com/intro-text-online), uses a simple custom
computer language to express resampling algorithms. He collected experimental
evidence that his approach was effective in teaching statistics to high school
students [-@simon1969new] and undergraduates [-@simon1976probability],
including those with "low skills and little interest in mathematics".

There are now sevaral books that teach statistics through resampling
to readers who can already read and write Python code [@downey2014think;
@grus2015data; @shasha2010statistics].

In 2015, Berkeley started an initiative to teach data science to
undergraduates of all disciplines using simple Python code. They use the
[Jupyter Notebook](https://jupyter.org) to students to get started with
running code.  The textbook is online at https://www.inferentialthinking.com.
The course takes an interesting approach, which is to get the students running
the instructor's code very early in the course, before explaining how the code
works in any detail.

# The course

I chose to combine elements from the resampling course of
[@simon1997resampling] and the Berkeley data science course.  All the teaching
material after the initial introduction was in the form of interactive Jupyter
Notebooks, with the students running the same code as I was, on their own
laptops.  We used real full open-access datasets for all the tutorials and
exercises:

* A survey of political attitudes post Brexit;
* A survey on attitudes to animal research;
* A World Bank dataset on gender inequality.

The order of play was to:

* introduce the Jupyter Notebook;
* get and part-analyze the Brexit data, to discover that 41% of the survey
  respondents who told the interviewer their Brexit vote, admitted to voting
  Leave; our question - did the survey company mess up with its sampling?
* ask the students "If a family has four children, what are the chances that
  they have three girls and one boy?" [@simon1997resampling]. In trying to
  solve this problem, I introduce the idea of trying to solve probability
  problems with simulation (Monte Carlo sampling).  We simulate with coin
  tosses and get something near the right answer;
* we can ask the computer to do this tedious process for us, much more
  quickly.  Introduce the code necessary to express the coin-toss algorithm.
  Run the coin-toss algorithm to get a similar answer;
* return the the Brexit 41% problem; it's the same problem.  Solve with
  simulation; show that 41% cannot plausibly have come about by random
  sampling; introduce the sampling distribution;
* the histogram of the ages of the Leave voters looks different from that of
  the Remain voters; could this difference be due to sampling?  Introduce the
  permutation test for generating samples of mixed Leave and Remain voters.
  Show that the actual difference in Leave / Remain mean ages is outside the
  range of differences we see from these samples;
* introduce the survey on attitudes to Animal Research.  Respondents gave yes
  / no answers to a question on whether they trusted a) universities or b)
  animal protection organizations for advice on animal research.  Ask whether
  the difference in yes / no proportions for these answers could be due to
  sampling.  Explain sampling for the paired test (swap answers within
  subject).
* introduce World Bank Survey.  Show scatterplot of youth childbirth rates per
  country against average years that that girls remain in school.  Introduce
  idea of correlation. Generate random samples by shuffling one of the two
  vectors, and recalculating (surrogate for) correlation.

Along the way, the students needed to be able to read, and possibly modify:

* variable assignment: e.g. `a = 10`;
* appending to lists: e.g. `b.append(a)` where `b` is a list;
* if statements e.g. `if coin_toss == 1: # do something`.
* for loops e.g. `for i in range(1000): # do something
* using simple functions, defined in the Notebook, e.g.:

~~~~
def mean(my_list):
    return sum(my_list) / len(my_list)
~~~~

The aim was to express Simon's [-@simon1997resampling] custom language with a
small amount of simple Python code.  Although the result does involve more
lines of code than Simon's language, it does have the advantages that:

* it's easier to see exactly what the code is doing;
* the effort to explain how the code works is independently valuable to the
  students, as it introduces them to a general purpose language widely used
  for teaching and data science;
* the students can see that the choice of language is not obscure;
* the students can easily find language help and tutorials online.

# Feedback

I briefly referred to the feedback in the summary above.  The feedback
confirmed my suspicions in the later parts of the class, that the students
were, on average, finding it harder to read and modify the code than I had
hoped. They wanted to have more practice in learning the constructs they were
using, in order to fully understand them.

# Next time

Teaching computer programming is difficult [@mccracken2001multi].  However,
our task is not that task; we need to teach the small subset of computer
programming listed above.  This might be better called "scripting".  I
established from this course that we can explain the fundamental ideas of
statistics in a short time using these ideas, but we need to do more work to
make it easier for students to feel comfortable with the code that they need.
I imagine this will involve a combination of better, slower teaching of how
the code works, and more exercises for the students to so in class or at home.

# References
