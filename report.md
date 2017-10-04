---
# YAML metadata
title: "First pilot study on statistics with computing"
bibliography: les_pilot.bib
---

# Summary

This is a report of a pilot course teaching statistics through computing, run
over 10 hours of face-to-face teaching, from September 19th through the 21st.

In 10 hours, I taught:

* solving a simple probability problem through physical simulation, and
  simulation with simple programming;
* extending this problem to analyze responses from survey data;
* sample statistics and the sampling distribution (equivalent to standard
  error of mean);
* comparing groups by permutation testing (equivalent to t-tests);
* using permutation for paired tests (equivalent to paired t-tests);
* comparing measures by permutation (equivalent to correlation).

# Background

There has been a lot of recent discussion about teaching introductory
statistics, partly motivated by the recent success of data science methods.

A central article for this discussion is @cobb2015mere - "Mere Renovation is
Too Little Too Late: We Need to Rethink Our Undergraduate Curriculum from the
Ground Up”. There is [a page hosting the Cobb article and many comment papers
from distinguished teachers of
statistics](https://nhorton.people.amherst.edu/mererenovation).

To summarize the Cobb paper and comments on it: modern statistics courses
should:

* teach how to "think with data" [@horton2015think];
* make statistical reasoning accessible by teaching in terms of algorithms and
  computation instead of mathematics [@cobb2015mere; @hesterberg2015teachers].
  Courses should teach "computational thinking" [@temple_lang2015];
* use analysis with real data and open questions to give an "authentic data
  analysis experience" [@temple_lang2015] by "teaching through research"
  [@cobb2015mere].

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
