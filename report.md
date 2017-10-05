---
# YAML metadata
title: "First pilot study on statistics with computing"
bibliography: les_pilot.bib
---

# Summary

This is a report of a pilot course teaching statistics through computing, run
over 10 hours of face-to-face teaching, from September 19th through the 21st.

The course web page is https://github.com/matthew-brett/les-pilot

We covered: solving simple probability through physical simulation and
computer simulation; loading and exploring real datasets; simulation for
comparing a population to a sample; comparing group means using permutation
(equivalent to a t-test); comparing responses within subject using permutation
(equivalent to a paired t-test); comparing continuous measures by permutation
(equivalent to correlation hypothesis test).

In the final 2 hour session I asked the students to try their own analysis on
the data of their choice, either their own data, or data from the datasets we
had used in class.

My impressions were:

* there was a large difference between students in their level of comfort with
  Python code;
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

There seems to be a general, if not universal feeling that we should be
thinking about ways to teach new students to use code; this will broaden the
range of data they can analyze, and give them more flexibility in analysis
methods.

Prominent teachers of statistics have also been reflecting on problems with
current undergraduate courses - see @cobb2015mere and commentaries on this paper at
https://nhorton.people.amherst.edu/mererenovation.  There appears to be some
consensus that the next generation of statistics courses should:

* make statistical reasoning accessible by teaching in terms of algorithms and
  computation instead of mathematics [@cobb2015mere; @hesterberg2015teachers].
  Courses should teach "computational thinking" [@temple_lang2015];
* teach how to "think with data" [@horton2015think];
* use analysis with real data and open questions to give an "authentic data
  analysis experience" [@temple_lang2015] by "teaching through research"
  [@cobb2015mere].

The first of these arguments gives another reason to teach with code.

# Prior art

Julian Simon advocated teaching statistics through resampling from the mid
sixties.  His book [-@simon1997resampling], which is [freely available
online](http://www.resample.com/intro-text-online), uses a simple custom
computer language to express resampling algorithms. He collected experimental
evidence that his approach was effective in teaching statistics to high school
students [-@simon1969new] and undergraduates [-@simon1976probability],
including those with "low skills and little interest in mathematics".

There are now several books that teach statistics through resampling to
readers who can already read and write Python code [@downey2014think;
@grus2015data; @shasha2010statistics].  There is a Matlab version of Simon's
resampling software, with a tutorial introduction to resampling
[@kaplan1999resampling]. @bruce2014introductory teaches resampling with
reference to several languages, including Simon's own, as well as R.

In 2015, Berkeley started an initiative to teach data science to
undergraduates of all disciplines using simple Python code. They use the
[Jupyter Notebook](https://jupyter.org) that allows the student to edit, enter
and run code from a web browser. The textbook is online at
https://www.inferentialthinking.com.  The course takes an interesting
approach, which is to get the students running the instructor's code very
early in the course, before explaining how the code works in any detail.

# The course

I combined elements from the resampling book of [@simon1997resampling] and the
Berkeley data science course.  All the teaching material after the initial
introduction was in the form of interactive Jupyter Notebooks, with the
students running the same code as I was, on their own laptops.  We used real
and complete open-access datasets for all the tutorials and exercises. These
were:

* a survey of political attitudes post Brexit;
* a survey on attitudes to animal research;
* a World Bank dataset on gender inequality.

The order of play was to:

* introduce the Jupyter Notebook;
* get and part-analyze the Brexit data, to discover that 41% of the survey
  respondents who told the interviewer their Brexit vote, admitted to voting
  Leave; our question - given that 52% voted Leave, did the survey company
  mess up with its sampling?
* we then back up and ask the students "If a family has four children, what
  are the chances that they have three girls and one boy?"
  [@simon1997resampling]. I introduce the idea of solving probability problems
  with simulation (Monte Carlo sampling) rather than the mathematics of
  probability.  We simulate with coin tosses and get something near the right
  answer;
* we can ask the computer to do this tedious process for us. Introduce the
  code necessary to express the coin-toss algorithm.  Run the coin-toss
  algorithm to get a similar answer;
* the Brexit 41% problem is a very similar problem.  Solve with simulation;
  show that 41% cannot plausibly have come about by random sampling from a
  population where 52% voted Leave; the samples we use to solve this problem
  introduce the idea of the sampling distribution;
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
  respondent);
* introduce the World Bank dataset.  Show scatterplot of youth childbirth
  rates per country against average years that that girls remain in school.
  Introduce idea of correlation. Generate random samples by shuffling one of
  the two vectors, and recalculating (surrogate for) correlation.

Along the way, the students needed to be able to read, and possibly modify:

* variable assignment: e.g. `a = 10`;
* appending to lists: e.g. `b.append(a)` where `b` is a list;
* if statements e.g. `if coin_toss == 1: # do something`;
* for loops e.g. `for i in range(1000): # do something`;
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
* the students can easily find language help and tutorials online.

# Discussion

I briefly referred to the feedback in the summary above.  The feedback
confirmed my suspicions in the later parts of the class, that the students
were, on average, finding it harder to read and modify the code than I had
hoped. They wanted to have more practice in learning the constructs they were
using, in order to fully understand them.

Teaching computer programming is difficult [@mccracken2001multi], but we only
need a small proportion of the material that should be taught on a programming
course.  We have no need to go into difficult topics like recursion or object
oriented programming.  The Jupyter Notebook greatly lowers the barrier to
running and writing code; it runs in the student's web browser after
installing a single software package.  What we need to teach might better be
called "scripting".  After this pilot, I am confident that, with more time and
more exercises, it is possible to teach the level of programming that the
students need in order to be able to understand the ideas, and see what tools
they will have available if they continue their learning.  If that succeeds,
we will have achieved two successes: the first is that we have introduced the
students to a tool of great power for their future work; the second is that
they will have a deeper and more general understanding of the principles of
statistics.

# References
