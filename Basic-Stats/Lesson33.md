# Lesson 33 — Statistical Significance, Effect Size & the Full Inference Picture

We have just learned **p-values**. Now we need to answer an important question:

> If a result is statistically significant, does that automatically mean it is important?

**No.**

This lesson connects:

$$
\boxed{
\text{p-value}
+
\text{effect size}
+
\text{uncertainty}
+
\text{sample size}
}
$$

into one complete picture.

---

# 1. What Does "Statistically Significant" Mean?

Suppose we perform a hypothesis test.

We choose:

$$
\alpha=0.05
$$

and obtain:

$$
p=0.02
$$

Since:

$$
p<\alpha
$$

we say:

$$
\boxed{\text{The result is statistically significant at the 5% level.}}
$$

This means the observed result is sufficiently inconsistent with \(H_0\), according to the specified test and assumptions, to reject \(H_0\) at that threshold.

It **does not** mean:

> "The result is important."

That's a different question.

---

# 2. Statistical Significance vs Practical Significance

Imagine a medicine reduces blood pressure by:

$$
0.1\text{ mmHg}
$$

Suppose we have millions of observations.

We might obtain:

$$
p<0.001
$$

So the effect could be statistically distinguishable from zero.

But:

$$
0.1\text{ mmHg}
$$

may be too small to matter practically.

So:

$$
\boxed{
\text{Statistical significance}
\neq
\text{Practical significance}
}
$$

---

# 3. The Two Questions

When analyzing data, ask two separate questions.

### Question 1 — Is there evidence of a difference?

Hypothesis testing helps answer this.

$$
H_0:\Delta=0
$$

$$
H_A:\Delta\neq0
$$

---

### Question 2 — How large is the difference?

That's where **effect size** becomes important.

$$
\boxed{\text{Effect size}}
$$

describes the magnitude of the difference or relationship.

---

# 4. Simple Effect Size

Suppose two groups have means:

$$
\mu_A=80
$$

and:

$$
\mu_B=75
$$

Then the difference is:

$$
\Delta=80-75=5
$$

So:

$$
\boxed{\Delta=5}
$$

is a simple effect size.

It tells us **how much the groups differ**.

The p-value tells us something different:

> How surprising would a difference this extreme be under the null hypothesis?

---

# 5. Example: Two Studies

Let's compare two hypothetical studies.

## Study A

Difference:

$$
\Delta=5
$$

Sample size:

$$
n=20
$$

Suppose:

$$
p=0.20
$$

Not statistically significant at:

$$
\alpha=0.05
$$

---

## Study B

Difference:

$$
\Delta=5
$$

Sample size:

$$
n=100,000
$$

Suppose:

$$
p<0.001
$$

Notice something interesting.

The **effect is the same**:

$$
\Delta=5
$$

but the evidence can differ because the amount of data differs.

This is why:

$$
\boxed{\text{p-value depends on both effect and uncertainty/sample size}}
$$

---

# 6. Why Sample Size Matters

Remember:

$$
SE=\frac{\sigma}{\sqrt n}
$$

As \(n\) increases:

$$
SE\downarrow
$$

The test statistic is approximately:

$$
Z=
\frac{\text{observed difference}}
{\text{standard error}}
$$

Therefore, for a fixed nonzero difference:

$$
SE\downarrow
$$

means:

$$
|Z|\uparrow
$$

which can produce:

$$
p\downarrow
$$

So:

$$
\boxed{
\text{More data can make tiny effects statistically significant.}
}
$$

---

# 7. A Very Important Example

Imagine a machine-learning model improves accuracy from:

$$
90.000\%
$$

to:

$$
90.010\%
$$

Difference:

$$
0.010\%
$$

With an enormous test set, this might be statistically significant.

But ask:

> Is a \(0.010\%\) improvement useful enough to justify the additional complexity or computational cost?

That's not a p-value question.

That's a **practical/engineering question**.

---

# 8. Effect Size Gives Us the Missing Information

Instead of reporting only:

$$
p=0.001
$$

we should ideally report something like:

$$
\boxed{
\text{effect estimate}
+
\text{uncertainty}
+
p\text{-value}
}
$$

For example:

$$
\Delta=5.2
$$

with:

$$
95\%\ CI=[2.1,8.3]
$$

and:

$$
p=0.002
$$

Now we know much more.

We know:

- estimated effect = \(5.2\)
- plausible range according to the CI = \(2.1\) to \(8.3\)
- evidence against the null is strong under the test = \(p=0.002\)

---

# 9. Confidence Interval Is Extremely Important

Remember:

$$
\boxed{
\text{Estimate}\pm\text{Margin of Error}
}
$$

Suppose:

$$
\hat\theta=5
$$

and:

$$
95\%\ CI=[2,8]
$$

This tells us much more than simply:

$$
p<0.05
$$

The p-value gives us a measure related to incompatibility with a null value.

The CI gives us information about:

$$
\boxed{\text{magnitude + uncertainty}}
$$

---

# 10. Example: Same p-value, Different Effects

Imagine two experiments.

### Experiment A

$$
\Delta=0.1
$$

$$
p=0.001
$$

### Experiment B

$$
\Delta=10
$$

$$
p=0.001
$$

The p-values are identical.

But the effects are completely different.

Therefore:

$$
\boxed{
p\text{-value alone does not tell you effect magnitude}
}
$$

---

# 11. Effect Size in Standardized Form

Sometimes raw differences aren't directly comparable.

For example:

- exam scores
- blood pressure
- reaction time
- temperature
- measurement amplitude

all have different units.

We can standardize an effect.

One common measure is **Cohen's \(d\)**.

A simplified form is:

$$
\boxed{
d=\frac{\bar{x}_1-\bar{x}_2}{s_{\text{pooled}}}
}
$$

where:

- \(\bar{x}\_1\) = mean of group 1
- \(\bar{x}\_2\) = mean of group 2
- \(s\_{\text{pooled}}\) = pooled standard deviation

The idea is:

> How many standard deviations apart are the groups?

---

# 12. Intuition for Cohen's \(d\)

Suppose:

$$
\bar{x}_1=80
$$

$$
\bar{x}_2=75
$$

and:

$$
s_{\text{pooled}}=10
$$

Then:

$$
d=\frac{80-75}{10}
$$

$$
d=0.5
$$

So the groups differ by about:

$$
\boxed{0.5\text{ standard deviations}}
$$

This gives us a scale-independent description of the effect.

---

# 13. Don't Memorize "Small = 0.2, Medium = 0.5..."

You may encounter rules such as:

$$
d=0.2,\quad0.5,\quad0.8
$$

being described as small, medium, and large.

These are rough conventions, not universal laws.

What counts as an important effect depends heavily on:

- scientific field
- measurement
- cost
- application
- consequences of errors

So don't treat effect-size thresholds as universal truth.

---

# 14. Statistical Significance Depends on Three Things

A useful mental model is:

$$
\boxed{
\text{Evidence strength}
\sim
\frac{\text{Effect}}{\text{Uncertainty}}
}
$$

And uncertainty depends strongly on:

$$
n
$$

and:

$$
\sigma
$$

For a simple mean test:

$$
Z=
\frac{\bar{x}-\mu_0}
{\sigma/\sqrt n}
$$

Notice the three ingredients:

### Numerator

$$
\bar{x}-\mu_0
$$

Observed difference.

### Denominator

$$
\frac{\sigma}{\sqrt n}
$$

Uncertainty.

### Result

$$
Z
$$

Standardized evidence.

---

# 15. The Entire Hypothesis-Testing Picture

We can now build the complete mental model.

```text
                 DATA
                   │
                   ▼
           Estimate / Statistic
                   │
                   ▼
             Difference
                   │
                   ▼
             Standard Error
                   │
                   ▼
          Test Statistic
                   │
                   ▼
             p-value
                   │
             ┌─────┴─────┐
             ▼           ▼
          small         large
             │           │
             ▼           ▼
       evidence       insufficient
       against H₀     evidence against H₀
```

But we still need another branch:

```text
                 DATA
                   │
                   ▼
              Effect Size
                   │
                   ▼
          "How large is it?"
```

And another:

```text
                 DATA
                   │
                   ▼
          Confidence Interval
                   │
                   ▼
        "How uncertain is it?"
```

So a complete analysis considers:

$$
\boxed{
\text{Effect Size}
+
\text{Uncertainty}
+
\text{Statistical Evidence}
}
$$

---

# 16. Statistical Significance Does Not Mean "Truth"

Suppose:

$$
p=0.001
$$

We should **not** interpret this as:

> "We proved the alternative hypothesis."

A statistical test doesn't magically prove a scientific theory.

It tells us how compatible the observed data are with the null model under the assumptions of the test.

Scientific conclusions require:

- experimental design
- measurement quality
- assumptions
- possible confounders
- effect size
- uncertainty
- replication
- domain knowledge

---

# 17. Type I Error

We already introduced this.

A Type I error is:

$$
\boxed{
\text{Reject }H_0\text{ when }H_0\text{ is actually true}
}
$$

The significance level:

$$
\alpha
$$

controls the long-run Type I error rate under the test's assumptions.

For example:

$$
\alpha=0.05
$$

means the testing procedure has a 5% Type I error rate in the long run when the null is true, under the assumptions.

It does **not** mean:

> "There is a 5% chance I made a mistake in this particular experiment."

---

# 18. Type II Error

A Type II error is:

$$
\boxed{
\text{Fail to reject }H_0
\text{ when }H_0\text{ is false}
}
$$

Its probability is:

$$
\beta
$$

Therefore statistical power is:

$$
\boxed{
\text{Power}=1-\beta
}
$$

Power answers roughly:

> If a real effect of a specified size exists, how likely is our test to detect it?

---

# 19. What Increases Statistical Power?

Generally:

### Larger sample

$$
n\uparrow
$$

→

$$
SE\downarrow
$$

→ more ability to detect effects.

### Larger effect

$$
|\Delta|\uparrow
$$

→ easier to distinguish from noise.

### Lower variability

$$
\sigma\downarrow
$$

→ smaller uncertainty.

### Higher \(\alpha\)

Makes rejection easier, but increases Type I error risk.

So there are tradeoffs.

---

# 20. Physics Example 🔬

Suppose an experiment predicts:

$$
\theta=2.00
$$

and we observe:

$$
\hat\theta=2.05
$$

There are several questions:

### Question 1

Is:

$$
2.05
$$

different from:

$$
2.00
$$

statistically?

→ Hypothesis test / p-value.

### Question 2

How large is the difference?

$$
\Delta=0.05
$$

→ Effect size.

### Question 3

How uncertain is our estimate?

→ Confidence interval / standard error.

### Question 4

Would a difference of \(0.05\) matter physically?

→ Domain knowledge.

This is scientific reasoning.

---

# 21. Quantum Physics Example ⚛️

Suppose a quantum experiment estimates:

$$
\langle A\rangle=2.04
$$

while theory predicts:

$$
\langle A\rangle=2
$$

We shouldn't immediately conclude:

> "The theory is wrong."

Instead:

$$
\boxed{
\text{Difference}=0.04
}
$$

Then determine:

$$
SE
$$

and perhaps:

$$
95\%\ CI
$$

and a hypothesis test:

$$
H_0:\langle A\rangle=2
$$

$$
H_A:\langle A\rangle\neq2
$$

Then calculate:

$$
p
$$

But even if:

$$
p<0.05
$$

we still need to investigate:

- experimental noise
- systematic errors
- model assumptions
- calibration
- finite measurement effects
- whether the theoretical model applies

This is especially important in real experimental physics.

---

# 22. Your Quantum Decoherence Connection

This is where your statistics foundation starts becoming directly relevant to your FYP.

Suppose your model predicts a waiting-time distribution:

$$
w(\tau|\theta)
$$

and you collect:

$$
\tau_1,\tau_2,\ldots,\tau_n
$$

You might want to determine:

$$
\theta=\gamma
$$

where \(\gamma\) could represent a decay rate in an appropriate model.

You now have several different statistical questions.

### Estimation

> What value of \(\gamma\) best explains the data?

$$
\hat\gamma
$$

### Uncertainty

> How precisely can we estimate \(\gamma\)?

$$
SE(\hat\gamma)
$$

or a confidence interval.

### Hypothesis testing

> Is a particular value \(\gamma_0\) compatible with the data?

$$
H_0:\gamma=\gamma_0
$$

### p-value

> How unusual would our observed statistic be if \(\gamma=\gamma_0\)?

### Fisher Information

> How much information about \(\gamma\) is contained in the measurement distribution?

This is the bridge to the Fisher Information material you previously studied.

---

# 23. The Bigger Statistical Picture

You can now see statistics as a sequence of questions:

$$
\boxed{
\text{What happened?}
}
$$

→ Descriptive statistics

$$
\boxed{
\text{What might be true?}
}
$$

→ Estimation

$$
\boxed{
\text{How uncertain are we?}
}
$$

→ Standard Error / Confidence Intervals

$$
\boxed{
\text{Is this result unusual under a specific hypothesis?}
}
$$

→ Hypothesis Testing / p-values

$$
\boxed{
\text{How large is the effect?}
}
$$

→ Effect Size

$$
\boxed{
\text{How much information is available about a parameter?}
}
$$

→ Fisher Information

---

# 24. One Giant Example

Let's put everything together.

Suppose a quantum experiment measures a quantity 100 times.

You obtain:

$$
\bar{x}=10.4
$$

Theory predicts:

$$
\mu_0=10
$$

Suppose:

$$
\sigma=2
$$

and:

$$
n=100
$$

### Step 1 — Standard Error

$$
SE=\frac{\sigma}{\sqrt n}
$$

$$
SE=\frac2{10}=0.2
$$

---

### Step 2 — Test Statistic

$$
Z=
\frac{10.4-10}{0.2}
$$

$$
Z=2
$$

---

### Step 3 — p-value

For a two-sided test:

$$
p\approx0.0455
$$

---

### Step 4 — Decision

If:

$$
\alpha=0.05
$$

then:

$$
p<\alpha
$$

so we reject \(H_0\) under this test.

---

### Step 5 — Effect

Raw difference:

$$
\Delta=10.4-10
$$

$$
\Delta=0.4
$$

---

### Step 6 — Interpret

We have evidence that the mean differs from 10 under the assumptions of the test.

But we should **not** automatically conclude:

> "The theory is wrong."

We need to consider:

- effect magnitude
- uncertainty
- systematic error
- experimental design
- model assumptions
- physical significance

This is how statistics supports scientific reasoning rather than replacing it.

---

# 🧠 The Ultimate Mental Model

When you see a statistical result, don't immediately look at the p-value.

Ask:

```text
1. What was measured?
       ↓
2. What is the estimated effect?
       ↓
3. How uncertain is the estimate?
       ↓
4. What is the null hypothesis?
       ↓
5. What does the sampling distribution look like?
       ↓
6. What is the test statistic?
       ↓
7. What is the p-value?
       ↓
8. Is it statistically significant?
       ↓
9. How large is the effect?
       ↓
10. Does the effect matter scientifically/practically?
```

That is a much stronger way of thinking than:

> "p < 0.05, therefore important."

---

# 🗺️ COMPLETE ROADMAP — LESSON 33

```text
PHASE 0 — MATHEMATICAL FOUNDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Numbers & Variables                  ✅
Arithmetic                           ✅
Fractions / Ratios / %               ✅
Powers / Roots / Logs                ✅
Algebra                              ✅
Functions                            ✅
Coordinates & Graphs                 ✅
Vectors                              ✅
Matrices                             ✅
Summation                            ✅
Basic Probability                    ✅


PHASE 1 — STATISTICS FOUNDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Data                                 ✅
Population vs Sample                 ✅
Mean / Median / Mode                 ✅
Variance / SD / Range                ✅
Percentiles / Quartiles              ✅
IQR / Outliers                       ✅
Distribution Shape                   ✅

Random Variables                     ✅
Probability Distributions            ✅
Bernoulli                            ✅
Binomial                             ✅
Expected Value                       ✅
Correlation                          ✅
Covariance                           ✅

Sampling Methods                     ✅
Sampling Distribution                ✅
Standard Error                       ✅
CLT                                  ✅
LLN                                  ✅
Confidence Intervals                 ✅
Statistical Inference                ✅
Hypothesis Testing                   ✅
p-values                             ✅
Statistical Significance             🔵 YOU ARE HERE
Effect Size                          🔵 YOU ARE HERE
Type I / Type II Errors              ✅
Statistical Power                    ✅


PHASE 2 — NUMPY FOUNDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NumPy / ndarray                      ⬜
Array creation                       ⬜
Shape / Dimensions                   ⬜
Data types                           ⬜
Indexing                             ⬜
Slicing                              ⬜
Reshaping                            ⬜
Flattening                           ⬜
Concatenation                        ⬜
Stacking                             ⬜
Broadcasting                         ⬜
Vectorization                        ⬜


PHASE 3 — STATISTICS WITH NUMPY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mean                                 ⬜
Median                               ⬜
Variance                             ⬜
Standard deviation                   ⬜
Percentiles                          ⬜
IQR                                  ⬜
Covariance                           ⬜
Correlation                          ⬜
Sampling simulations                 ⬜
Sampling distributions               ⬜
SE simulations                       ⬜
CLT simulations                      ⬜
LLN simulations                      ⬜
Confidence intervals                 ⬜
Hypothesis tests                     ⬜
p-values                             ⬜


PHASE 4 — LINEAR ALGEBRA + NUMPY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Vectors                              ⬜
Dot product                          ⬜
Norms / Distance                     ⬜
Matrices                             ⬜
Matrix multiplication                ⬜
Transpose                            ⬜
Inverse                              ⬜
Linear systems                       ⬜
Eigenvalues                          ⬜
Eigenvectors                         ⬜


PHASE 5 — NUMPY FOR ML
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Feature matrix X                     ⬜
Target y                             ⬜
Standardization                      ⬜
Normalization                        ⬜
Predictions                          ⬜
Errors                               ⬜
MSE / RMSE                           ⬜
Gradients                            ⬜
Vectorized ML                        ⬜


PHASE 6 — MACHINE LEARNING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Supervised Learning                  ⬜
Unsupervised Learning                ⬜
Regression                           ⬜
Classification                       ⬜
Linear Regression                    ⬜
Logistic Regression                  ⬜
KNN                                  ⬜
Decision Trees                       ⬜
Random Forest                        ⬜
SVM                                  ⬜
Clustering                           ⬜
Model Evaluation                     ⬜
Feature Engineering                  ⬜
Cross Validation                     ⬜
Hyperparameter Tuning                ⬜


PHASE 7 — ADVANCED ML
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Optimization                         ⬜
Gradient Descent                     ⬜
Regularization                       ⬜
PCA                                  ⬜
Neural Networks                      ⬜
Deep Learning                        ⬜
CNNs                                 ⬜
Transformers                         ⬜


PHASE 8 — SCIENTIFIC / QUANTUM ML
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Scientific Computing                 ⬜
Numerical Methods                    ⬜
Scientific Data Analysis             ⬜
Quantum States                       ⬜
Quantum Measurement                  ⬜
Quantum Probability                  ⬜
Quantum ML                            ⬜
```

---

# 🔗 When Do We Connect This to NumPy?

**Very soon.**

We've now built the conceptual foundation needed for statistical computation.

The transition will be:

$$
\boxed{
\text{Statistics}
\rightarrow
\text{NumPy}
}
$$

But we won't forget the mathematics.

For example, you'll already know:

$$
\bar{x}=\frac1n\sum_{i=1}^nx_i
$$

Then NumPy will simply give us an efficient computational way to perform it:

```python
np.mean(x)
```

You've already learned:

$$
\sigma^2=\frac1N\sum_{i=1}^N(x_i-\mu)^2
$$

Then:

```python
np.var(x)
```

Covariance:

$$
\operatorname{Cov}(X,Y)
$$

→

```python
np.cov(x, y)
```

Correlation:

$$
r=
\frac{\operatorname{Cov}(X,Y)}
{\sigma_X\sigma_Y}
$$

→

```python
np.corrcoef(x, y)
```

And the really valuable part will be **simulation**.

We'll use NumPy to actually watch:

$$
\text{LLN}
$$

$$
\text{CLT}
$$

$$
\text{Sampling distributions}
$$

$$
\text{Confidence intervals}
$$

and

$$
\text{Hypothesis testing}
$$

happen computationally.

So you won't just memorize statistics—you'll **see it happen**.

---

# 🧠 Final Lesson Paragraph

> **Statistical significance tells us about evidence against a specified null hypothesis, while effect size tells us how large the observed effect is and confidence intervals tell us about its uncertainty. A small p-value does not automatically mean that an effect is large or practically important; with sufficiently large samples, even extremely small effects can become statistically significant because \(SE=\sigma/\sqrt n\) decreases as sample size increases. Conversely, a meaningful effect may fail to reach statistical significance when data are limited or highly variable. A complete statistical analysis therefore considers the estimated effect, its uncertainty, the hypothesis test and p-value, sample size, assumptions, and practical or scientific importance. We also connected Type I error \(\alpha\), Type II error \(\beta\), and statistical power \(1-\beta\) to the same framework. In physics and quantum experiments, this distinction is crucial: a measured deviation from a theoretical prediction must be evaluated relative to experimental uncertainty before drawing conclusions. For the quantum-decoherence problem, the same framework will eventually let us move from measured photon-counting or waiting-time data to parameter estimation, hypothesis testing, likelihoods, and ultimately Fisher Information. We have now completed the major introductory statistical-inference foundation, and we are approaching the transition into NumPy, where all of these mathematical concepts will become actual computations and simulations.**
