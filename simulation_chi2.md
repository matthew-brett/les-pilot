---
# YAML metadata
title: "On simulation and Chi2"
bibliography: les_pilot.bib
---

# Introduction from [@lin2015revisit]

The following is a slightly amended version of the introductory text from
[@lin2015revisit].

Let the individuals of a population be classified according to two qualitative
variables (or attributes), say A and B, into a and b classes respectively.
Let $A_1, A_2, ... A_a$ be the classes of A, and $B_1, B_2, ... B_b$ be the
classes of B. Let $\pi_{ij}$ be the proportion of members of the population
belonging to the $i$th class of A and $j$th class of B simultaneously.

Thus, the structure of the population is as follows:

The objective here is to test the independence of A and B, i.e., test

$$
H_0 : \quad \pi_{ij} = \pi_{i\cdot} \pi_{{\cdot}j} \forall(i, j) \text{ vs. }
H_1 : \quad \pi_{ij} \ne \pi_{i\cdot} \pi_{{\cdot}j} \text{ for some } (i, j)
$$ {#eq:h0}

A sample of size n is drawn randomly from the population where all draws are
independent. Let $X_{ij}$ be the number of sample observations belonging to
$(A_i, B_j)$-cell.  The marginal frequencies for $i$th row and $j$th column
are obtained as:

$$
X_{i\cdot} = \sum_{j=1}^{j=b} X_{ij} \text{ and }
X_{{\cdot}j} \sum_{i=1}^{i=a} X_{ij}
$$

As a result, the maximum likelihood estimates of the marginal probabilities
are given by:

$$
\hat{\pi}_{i\cdot} = X_{i\cdot} / n \text{ and }
\hat{\pi}_{{\cdot}j} = X_{{\cdot}j} / n
$$

If the rows and columns are independent, then the *expected value* $E_{ij}$
for $X_{ij}$ is:

$$
E_{ij} = n \hat{\pi}_{i\cdot} \hat{\pi}_{{\cdot}j} \\
$$

Further, the usual (Pearson’s) Chi-square test statistic is defined as:

$$
Q_1 = \sum_{i=1}^{i=a} \sum_{j=1}^{j=b} (X_{ij} - E_{ij})^2 / E_{ij}
$$

which, under $H_0$ follows $\chi^2_{(i-1), (j-1)}$ asymptotically, which
means, as $n \to \infty$, $P(Q_1 \le u) \to P(\chi^2_{(i-1), (j-1)} \le u)$
for all $u > 0$ when $H_0$ is satisfied.

# What is the null distribution for the Chi-square test?

See this [SAS blog post about assumptions for contingency
tables](http://blogs.sas.com/content/iml/2015/10/14/sim-2x2-model.html]).

In essence, we can simulate a new table, using the maximum likelihood
probabilities from the original table: $\hat{\pi}_{i\cdot}$ and
$\hat{\pi}_{{\cdot}j}$.  Call the new simulated table $S$ and call the entries
in this new table $S_{ij}$.  We can calculate Chi-squared from many of these
new tables to get a null distribution of the Chi-squared value.  But:

* should we restrict the samples $S$ to have the same row and column counts as
  the original table --- $X_{i\cdot}, X_{{\cdot}j}$?  (This is what the SAS
  blog post implies).
* if we do not restrict the row and column totals, should we use the original
  $E_{ij}$ values, or should we recalculate for the new table $S$ to give
  $E^s_{ij}$ expected values for this particular table?

I believe that [@lin2015revisit] does not restrict, and does recalculate. It's
not clear to me what [@amiri2011efficiency] does.  [@agresti1979exact]
restricts.  There is a detailed section on "Conditional versus Unconditional
Tests" in [@agresti2003categorical], chapter 3, where "conditional" refers to
the restrict option above.

See also:

* [Monte-Carlo simulations in
SAS](http://blogs.sas.com/content/iml/2015/10/28/simulation-exact-tables.html)
* [Post to R mailing list about contingency
  tables](http://r.789695.n4.nabble.com/Simulating-contingency-table-Basic-question-help-please-td882712.html)


# Bibliography
