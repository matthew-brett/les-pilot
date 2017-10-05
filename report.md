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
  discipline, until the start their final year projects.

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

The second of these arguments gives a further motivation to teach code - in
order to make statistical reasoning more accessible to students who do not
have a substantial background in mathematics.

# Prior art

There are now sevaral books and courses teaching statistics and data science
to readers who can already write Python or R code - Think Stats, Statistics is
Easy, Data science from Scratch.



Teaching this way has become much easier with the development of interactive
code and data notebooks, such as the [Jupyter Notebook](https://jupyter.org)
and [R Studio](https://www.rstudio.com).

In the second semester of 2015, Berkeley started a cross-university
introduction to data science now called [Computational and Inferential
Thinking](https://www.inferentialthinking.com). They used the Jupyter Notebook
to write the course book, and teach the course.  The material uses no
mathematical formulae, but instead uses simple computer code to express the
same ideas.

# References
