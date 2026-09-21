# Lesson 31 — Hypothesis Testing

We are now entering one of the most important parts of statistical inference:

$$
\boxed{\text{Hypothesis Testing}}
$$

Don't worry about the terminology yet. We will build it from **zero**.

The central question is:

> **Given the data I observed, is a particular claim still reasonably plausible, or does the data provide evidence against it?**

This is especially important in **science, experiments, ML, and quantum physics**.

---

# 1. Start With a Scientific Claim 🔬

Imagine a manufacturer says:

> "Our sensor has an average measurement error of 0."

You don't know whether that's true.

You collect measurements:

$$
x_1,x_2,\ldots,x_n
$$

and calculate:

$$
\bar{x}=0.8
$$

Now what?

You cannot immediately say:

> "The manufacturer's claim is false."

Why?

Because even if the true mean were actually:

$$
\mu=0
$$

a random sample might produce:

$$
\bar{x}=0.8
$$

because of sampling variability.

So we need a systematic procedure for deciding how strongly the data contradicts a claim.

That procedure is:

$$
\boxed{\text{Hypothesis Testing}}
$$

---

# 2. The Courtroom Analogy ⚖️

A very useful mental model is a courtroom.

Imagine:

> Someone is presumed innocent unless the evidence provides sufficient reason to reject that presumption.

In hypothesis testing, we start with a **baseline assumption**.

That is called the:

$$
\boxed{\text{Null Hypothesis}}
$$

We then ask:

> **If the null hypothesis were true, how surprising would our observed data be?**

This is the key question.

---

# 3. The Two Hypotheses

We generally define two competing statements.

## Null Hypothesis

Written:

$$
\boxed{H_0}
$$

It represents the baseline/reference claim.

---

## Alternative Hypothesis

Written:

$$
\boxed{H_A}
$$

or:

$$
H_1
$$

It represents the alternative we're investigating.

---

# 4. Simple Example

Suppose a machine is supposed to produce components with average diameter:

$$
10\text{ mm}
$$

We want to investigate whether the true average is different.

We write:

$$
\boxed{H_0:\mu=10}
$$

and:

$$
\boxed{H_A:\mu\neq10}
$$

Read them as:

> \(H_0\): the population mean is 10 mm.

> \(H_A\): the population mean is not 10 mm.

---

# 5. Why Do We Start With \(H_0\)?

Because we need a reference model.

We're essentially asking:

> "Assume the baseline claim is true. Would the data we observed look unusual?"

If the answer is:

> Not particularly unusual.

Then we don't have strong evidence against \(H_0\).

If the answer is:

> Extremely unusual.

Then we have evidence against \(H_0\).

So the logic is:

$$
\boxed{
H_0
\rightarrow
\text{What data should look like if }H_0\text{ were true?}
}
$$

Then:

$$
\boxed{
\text{Compare actual data to that expectation}
}
$$

---

# 6. Example

Suppose:

$$
H_0:\mu=100
$$

You take a sample:

$$
n=100
$$

and find:

$$
\bar{x}=102
$$

Is 102 far from 100?

Not necessarily.

We need to know how much the sample mean normally fluctuates.

Suppose:

$$
\sigma=10
$$

Then:

$$
SE=\frac{\sigma}{\sqrt n}
$$

$$
SE=\frac{10}{10}=1
$$

Our sample mean is:

$$
102
$$

while the null hypothesis predicts:

$$
100
$$

Difference:

$$
102-100=2
$$

In standard-error units:

$$
\frac{102-100}{1}=2
$$

So the observation is:

$$
\boxed{2\text{ standard errors above the null}}
$$

Now we have a way to quantify how unusual the result is.

---

# 7. Test Statistic

That quantity is called a:

$$
\boxed{\text{Test Statistic}}
$$

For a simple known-\(\sigma\) mean test:

$$
\boxed{
Z=
\frac{\bar{x}-\mu_0}
{\sigma/\sqrt n}
}
$$

Let's decode it.

### \(\bar{x}\)

Observed sample mean.

### \(\mu_0\)

Mean specified by the null hypothesis.

### \(\sigma\)

Population standard deviation.

### \(n\)

Sample size.

### \(Z\)

How many standard errors the observed mean is away from the null value.

---

# 8. The Mental Model

Think of the test statistic as a **distance meter**.

Suppose:

$$
H_0:\mu=100
$$

and:

$$
\bar{x}=102
$$

The raw difference is:

$$
2
$$

But 2 units could mean very different things depending on uncertainty.

### Case A

$$
SE=10
$$

Then:

$$
Z=\frac2{10}=0.2
$$

Very small.

### Case B

$$
SE=1
$$

Then:

$$
Z=\frac2{1}=2
$$

Much more unusual.

### Case C

$$
SE=0.2
$$

Then:

$$
Z=\frac2{0.2}=10
$$

Extremely far from the null in standard-error units.

Therefore:

$$
\boxed{
\text{Difference alone is not enough}
}
$$

We need to compare the difference with its expected variability.

---

# 9. This Connects Directly to Standard Error

Remember:

$$
SE=\frac{\sigma}{\sqrt n}
$$

And now:

$$
Z=
\frac{\bar{x}-\mu_0}{SE}
$$

So:

$$
\boxed{
\text{Hypothesis testing}
=
\text{Observed difference}
\div
\text{uncertainty}
}
$$

That's a powerful intuition.

---

# 10. What Is a Large Test Statistic?

Suppose:

$$
Z=0.1
$$

The observation is very close to what \(H_0\) predicts.

But suppose:

$$
Z=5
$$

That's much farther away.

Generally, for a two-sided test:

$$
|Z|\text{ large}
$$

means:

> The observed result is far from what we'd expect under \(H_0\).

While:

$$
|Z|\text{ small}
$$

means:

> The observed result is relatively close to what we'd expect under \(H_0\).

---

# 11. The Standard Normal Distribution Returns

Remember:

$$
Z\sim N(0,1)
$$

under the null hypothesis, when the Normal approximation is appropriate.

Imagine:

```text
                         H₀ distribution
                              |
                         _____|_____
                      __/           \__
                    _/                 \_
___________________/_____________________\________________
                 -3    -2    0    +2    +3
```

Most observations are near:

$$
0
$$

Very large positive or negative values are relatively unusual.

---

# 12. Rejection Regions

We can define regions of the distribution where results would be considered sufficiently unusual according to a chosen significance level.

For a common two-sided test with:

$$
\alpha=0.05
$$

the critical values for a standard Normal test are approximately:

$$
-1.96
$$

and:

$$
+1.96
$$

So conceptually:

```text
        Reject          Do not reject          Reject
           ↓                  ↓                   ↓

───────────|──────────────────|──────────────────|──────────
         -1.96                0                 +1.96
```

If:

$$
Z<-1.96
$$

or:

$$
Z>1.96
$$

the result falls in the conventional 5% rejection region.

---

# 13. Significance Level \(\alpha\)

We choose a significance level:

$$
\boxed{\alpha}
$$

before performing the test.

A common choice is:

$$
\alpha=0.05
$$

Other common choices:

$$
0.01,\quad0.05,\quad0.10
$$

The significance level controls the long-run Type I error rate of the testing procedure under its assumptions.

We'll discuss Type I error shortly.

---

# 14. What Does \(\alpha=0.05\) Mean?

It does **not** mean:

> "There is a 5% probability that \(H_0\) is true."

That's a very common mistake.

Instead, roughly speaking:

> If \(H_0\) is true and we repeatedly use this test procedure, the probability of rejecting \(H_0\) incorrectly is controlled at 5%, under the test's assumptions.

That's the idea of the:

$$
\boxed{\text{Type I error rate}}
$$

---

# 15. Reject vs Fail to Reject

This wording is important.

If the test statistic falls in the rejection region, we say:

$$
\boxed{\text{Reject }H_0}
$$

Otherwise:

$$
\boxed{\text{Fail to reject }H_0}
$$

We generally **do not** say:

> "Accept \(H_0\)."

Why?

Because failing to find sufficient evidence against \(H_0\) is not the same thing as proving \(H_0\) is true.

---

# 16. A Simple Example

Suppose:

$$
H_0:\mu=100
$$

$$
H_A:\mu\neq100
$$

Given:

$$
\bar{x}=102
$$

$$
\sigma=10
$$

$$
n=100
$$

Then:

$$
SE=1
$$

and:

$$
Z=\frac{102-100}{1}
$$

$$
Z=2
$$

For a two-sided test at:

$$
\alpha=0.05
$$

the critical values are approximately:

$$
\pm1.96
$$

Since:

$$
2>1.96
$$

the test statistic falls in the rejection region.

Therefore:

$$
\boxed{\text{Reject }H_0}
$$

under this testing procedure.

---

# 17. But What Does That Actually Mean?

It means:

> The observed result is sufficiently unusual under the null hypothesis according to the pre-specified 5% testing procedure.

It does **not** mean:

> "There is a 95% probability that the alternative hypothesis is true."

That's a different statement.

Always distinguish:

$$
\boxed{\text{Evidence against }H_0}
$$

from:

$$
\boxed{\text{Probability that }H_0\text{ is true}}
$$

They are not the same thing.

---

# 18. Type I Error

Now we need to understand errors.

Suppose:

$$
H_0
$$

is actually true.

But our test rejects it.

That's:

$$
\boxed{\text{Type I Error}}
$$

Symbolically:

$$
\boxed{
\text{Type I Error}
=
\text{Reject }H_0
\text{ when }H_0\text{ is true}
}
$$

Its controlled rate is:

$$
\alpha
$$

under the assumptions of the test.

---

# 19. Type II Error

The other possibility:

$$
H_0
$$

is actually false.

But we fail to reject it.

That's:

$$
\boxed{\text{Type II Error}}
$$

Symbolically:

$$
\boxed{
\text{Type II Error}
=
\text{Fail to reject }H_0
\text{ when }H_0\text{ is false}
}
$$

Its probability is often denoted:

$$
\boxed{\beta}
$$

---

# 20. The Four Possibilities

Think of this table:

| Reality       | Our decision | Result            |
| ------------- | ------------ | ----------------- |
| \(H_0\) true  | Don't reject | Correct           |
| \(H_0\) true  | Reject       | **Type I error**  |
| \(H_0\) false | Reject       | Correct           |
| \(H_0\) false | Don't reject | **Type II error** |

So:

$$
\boxed{\alpha=P(\text{Type I error})}
$$

and:

$$
\boxed{\beta=P(\text{Type II error})}
$$

under the relevant assumptions.

---

# 21. Statistical Power

Now we get another important concept:

$$
\boxed{\text{Power}}
$$

Power is:

$$
\boxed{
1-\beta
}
$$

It represents the probability of correctly rejecting \(H_0\) when a particular alternative is true.

High power means the test is more capable of detecting a real effect of a specified size.

---

# 22. What Increases Statistical Power?

Generally, power can increase with:

### Larger sample size

$$
n\uparrow
$$

which reduces:

$$
SE=\frac{\sigma}{\sqrt n}
$$

---

### Larger true effect

If the true difference from the null is larger, it becomes easier to detect.

---

### Lower variability

Smaller:

$$
\sigma
$$

means smaller standard error.

---

### Larger \(\alpha\)

Using a less stringent significance threshold can increase power, but also increases the allowed Type I error rate.

So there are tradeoffs.

---

# 23. Example of Sample Size

Suppose:

$$
\mu_0=100
$$

and true mean is:

$$
\mu=102
$$

If our standard error is huge:

$$
SE=10
$$

then the difference:

$$
2
$$

is tiny relative to the uncertainty.

But if:

$$
SE=0.5
$$

then:

$$
\frac2{0.5}=4
$$

The same physical difference becomes much easier to detect.

This is why:

$$
\boxed{\text{Sample size matters}}
$$

---

# 24. One-Sided vs Two-Sided Tests

There are different forms of hypotheses.

## Two-sided

We're asking whether the parameter is simply different.

$$
H_0:\mu=100
$$

$$
H_A:\mu\neq100
$$

Possible differences:

$$
\mu<100
$$

or:

$$
\mu>100
$$

---

## Right-tailed

We're specifically asking whether the parameter is larger.

$$
H_0:\mu\le100
$$

$$
H_A:\mu>100
$$

---

## Left-tailed

We're specifically asking whether the parameter is smaller.

$$
H_0:\mu\ge100
$$

$$
H_A:\mu<100
$$

The choice should be based on the scientific question and specified appropriately—not chosen after looking at the data simply to obtain a preferred conclusion.

---

# 25. Why Does This Matter?

Suppose you're testing whether a new treatment changes a measurement.

If you're genuinely interested in **any change**, use a two-sided formulation:

$$
H_A:\mu\neq\mu_0
$$

If the scientific question is specifically whether it **increases** the quantity:

$$
H_A:\mu>\mu_0
$$

The hypotheses must match the question.

---

# 26. Hypothesis Testing in Physics 🔬

Suppose a theoretical model predicts:

$$
\mu=9.81
$$

You perform an experiment.

Your sample gives:

$$
\bar{x}=9.95
$$

You could formulate:

$$
H_0:\mu=9.81
$$

versus:

$$
H_A:\mu\neq9.81
$$

Then determine how unusual:

$$
9.95
$$

would be under the null model, taking measurement variability into account.

This prevents us from declaring:

> "The theory is wrong!"

just because our finite sample isn't exactly equal to the theoretical prediction.

---

# 27. Quantum Example ⚛️

Suppose a quantum model predicts:

$$
\langle A\rangle=2.0
$$

Repeated measurements give:

$$
\bar A=2.12
$$

We might test:

$$
H_0:\langle A\rangle=2.0
$$

against:

$$
H_A:\langle A\rangle\neq2.0
$$

The question becomes:

> Is 2.12 sufficiently far from 2.0 relative to the statistical uncertainty of our measurements?

This is much more scientifically meaningful than simply comparing:

$$
2.12\neq2.0
$$

---

# 28. Connection to Quantum Trajectories

Suppose your experiment generates a stochastic record:

$$
x_1,x_2,\ldots,x_n
$$

For example, observations could involve photon detections or waiting times.

You might have a theoretical model:

$$
p(x|\theta)
$$

and a parameter:

$$
\theta
$$

You could ask:

$$
H_0:\theta=\theta_0
$$

versus:

$$
H_A:\theta\neq\theta_0
$$

Now the entire statistical foundation we've been building becomes relevant:

$$
\boxed{
\text{Probability Model}
\rightarrow
\text{Data}
\rightarrow
\text{Estimator}
\rightarrow
\text{Uncertainty}
\rightarrow
\text{Hypothesis Test}
}
$$

Later we'll connect this to likelihood and Fisher information.

---

# 29. ML Connection 🤖

Hypothesis testing appears throughout ML and data science.

Examples include testing:

- whether a feature is associated with an outcome
- whether two groups differ
- whether a model improvement is statistically distinguishable from noise
- whether a coefficient differs from zero
- whether observed performance differences could arise from sampling variability

For example, suppose:

```text
Model A accuracy = 91%
Model B accuracy = 92%
```

Can we immediately conclude:

> Model B is genuinely better?

No.

The difference is:

$$
1\%
$$

But we need to consider the uncertainty associated with the evaluation procedure.

A difference can be numerically nonzero without being statistically distinguishable from sampling variation.

---

# 30. Statistical Significance ≠ Practical Importance

This is extremely important in ML.

Suppose:

$$
n=10,000,000
$$

and Model B improves accuracy by:

$$
0.01\%
$$

A very large sample can make tiny differences statistically detectable.

But whether:

$$
0.01\%
$$

matters in practice is a separate question.

Therefore:

$$
\boxed{
\text{Statistical significance}
\neq
\text{Practical significance}
}
$$

We'll study this more deeply later.

---

# 31. The Big Connection to Confidence Intervals

Hypothesis testing and confidence intervals are closely related.

For a two-sided test at:

$$
\alpha=0.05
$$

there is a corresponding:

$$
95\%
$$

confidence interval.

For many standard settings:

> If the null value lies outside the 95% confidence interval, the corresponding two-sided hypothesis test rejects that null at the 5% level.

Example:

Suppose:

$$
95\%\ CI=[101,105]
$$

and:

$$
H_0:\mu=100
$$

Since:

$$
100
$$

is outside the interval, the corresponding two-sided 5% test rejects \(H_0\).

This is a powerful connection.

---

# 32. The Whole Statistical Inference Pipeline

Now look at what we've built:

```text id="q2i3d0"
              POPULATION
                  │
                  ↓
               SAMPLE
                  │
                  ↓
             STATISTICS
                  │
        ┌─────────┴─────────┐
        ↓                   ↓
    ESTIMATION         HYPOTHESIS TESTING
        │                   │
        ↓                   ↓
 Point / Interval       H₀ vs Hₐ
        │                   │
        ↓                   ↓
 Confidence             Test Statistic
 Interval                   │
                            ↓
                         p-value
                            │
                            ↓
                     Statistical Decision
```

We haven't yet studied the final major piece:

$$
\boxed{p\text{-value}}
$$

That's next.

---

# 33. 🧠 Practice

### Q1

What is the null hypothesis?

A. Always the hypothesis we want to prove

B. A baseline/reference hypothesis tested against the data

C. The sample mean

D. The alternative hypothesis

---

### Q2

Suppose:

$$
H_0:\mu=50
$$

and:

$$
\bar{x}=53
$$

Does \(\bar{x}=53\) automatically prove \(H_0\) false?

---

### Q3

If:

$$
Z=0
$$

what does that mean?

---

### Q4

If:

$$
Z=4
$$

is the observation closer to or farther from the null prediction than:

$$
Z=1?
$$

---

### Q5

What is a Type I error?

---

### Q6

What is statistical power?

---

## Answers

### Q1

$$
\boxed{B}
$$

---

### Q2

No.

We need to consider the variability of the estimator.

---

### Q3

The observed statistic is exactly at the null value in standardized units.

---

### Q4

Farther.

$$
|4|>|1|
$$

---

### Q5

Rejecting \(H_0\) when \(H_0\) is actually true.

---

### Q6

$$
\boxed{
\text{Power}=1-\beta
}
$$

It is the probability of rejecting \(H_0\) when a specified alternative is true.

---

# 🗺️ COMPLETE ROADMAP — LESSON 31

```text id="kz5d4h"
╔══════════════════════════════════════════════╗
║        ML + STATISTICS LEARNING MAP         ║
╚══════════════════════════════════════════════╝

PHASE 0 — MATHEMATICAL FOUNDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Numbers & Variables                 ✅
Arithmetic                          ✅
Fractions / Ratios / %              ✅
Powers / Roots / Logs               ✅
Algebra                             ✅
Functions                           ✅
Coordinates & Graphs                ✅
Vectors                             ✅
Matrices                            ✅
Summation (Σ)                       ✅
Basic Probability                   ✅


PHASE 1 — STATISTICS FOUNDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

What is Data?                       ✅
Population vs Sample                ✅
Mean / Median / Mode                ✅
Range / Variance / SD               ✅
Percentiles / Quartiles             ✅
IQR / Outliers                      ✅
Distribution Shape                  ✅

Random Variables                    ✅
Probability Distributions           ✅
Bernoulli                           ✅
Binomial                            ✅
Expected Value                      ✅
Correlation                         ✅
Covariance                          ✅

Sampling Methods                    ✅
Sampling Distribution               ✅
Standard Error                      ✅
Central Limit Theorem               ✅
Law of Large Numbers                ✅
Confidence Intervals                ✅
Statistical Inference               ✅

Hypothesis Testing                  🔵 YOU ARE HERE
p-values                            ⬜
Statistical Significance            ⬜
Type I / Type II Errors             🔵 introduced
Statistical Power                   🔵 introduced


PHASE 2 — NUMPY FOUNDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NumPy & ndarray                     ⬜
Creating Arrays                     ⬜
Shape & Dimensions                  ⬜
Data Types                          ⬜
Indexing                            ⬜
Slicing                             ⬜
Reshaping                           ⬜
Flattening                          ⬜
Concatenation                       ⬜
Stacking                            ⬜
Broadcasting                        ⬜
Vectorization                       ⬜


PHASE 3 — STATISTICS WITH NUMPY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Mean                                ⬜
Median                              ⬜
Variance                            ⬜
Standard Deviation                  ⬜
Percentiles                         ⬜
IQR                                 ⬜
Covariance                          ⬜
Correlation                         ⬜
Sampling simulations                ⬜
Sampling distributions              ⬜
Standard Error simulations          ⬜
CLT simulations                     ⬜
LLN simulations                     ⬜
Confidence Intervals                ⬜
Hypothesis-testing simulations      ⬜


PHASE 4 — LINEAR ALGEBRA WITH NUMPY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Vectors                             ⬜
Vector Operations                   ⬜
Dot Product                         ⬜
Norms / Distance                    ⬜
Matrices                            ⬜
Matrix Multiplication               ⬜
Transpose                           ⬜
Inverse                             ⬜
Linear Systems                      ⬜
Eigenvalues                         ⬜
Eigenvectors                        ⬜


PHASE 5 — NUMPY FOR ML
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Feature Matrix X                   ⬜
Target Vector y                    ⬜
Train/Test Split                   ⬜
Normalization                      ⬜
Standardization                    ⬜
Dot Products                       ⬜
Predictions                        ⬜
Errors                             ⬜
MSE / RMSE                         ⬜
Gradients                          ⬜
Vectorized ML                      ⬜
Batch Computation                  ⬜


PHASE 6 — MACHINE LEARNING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Supervised Learning                ⬜
Unsupervised Learning              ⬜
Regression                         ⬜
Classification                     ⬜
Linear Regression                  ⬜
Logistic Regression                ⬜
KNN                                ⬜
Decision Trees                     ⬜
Random Forest                      ⬜
SVM                                ⬜
Clustering                         ⬜
Model Evaluation                   ⬜
Feature Engineering                ⬜
Cross Validation                   ⬜
Hyperparameter Tuning              ⬜


PHASE 7 — ADVANCED ML
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Optimization                       ⬜
Gradient Descent                   ⬜
Regularization                     ⬜
PCA                                ⬜
Neural Networks                    ⬜
Deep Learning                      ⬜
CNNs                               ⬜
Transformers                       ⬜


PHASE 8 — SCIENTIFIC / QUANTUM ML
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Scientific Computing               ⬜
Numerical Methods                  ⬜
Scientific Data Analysis           ⬜
Quantum States                     ⬜
Quantum Measurement                ⬜
Quantum Probability                ⬜
Quantum ML                         ⬜
```

---

# 🔗 When Are We Connecting This to NumPy?

We're now **very close**.

The remaining core statistics concepts are:

$$
\boxed{p\text{-values}}
$$

and:

$$
\boxed{\text{Statistical Significance}}
$$

Then we'll transition into NumPy.

And when we do, we're going to make the connection explicit.

For example, today's calculation:

$$
Z=
\frac{\bar{x}-\mu_0}{\sigma/\sqrt n}
$$

will eventually become an actual computation on an array.

We'll generate thousands of random samples and see what happens when:

$$
H_0
$$

is true.

Then we'll see how often extreme results occur.

That computational experiment will make:

$$
\boxed{\alpha}
$$

$$
\boxed{\text{rejection region}}
$$

and:

$$
\boxed{p\text{-value}}
$$

much easier to understand.

The philosophy remains:

$$
\boxed{
\text{Understand}
\rightarrow
\text{Mathematics}
\rightarrow
\text{NumPy}
\rightarrow
\text{Simulation}
\rightarrow
\text{ML}
\rightarrow
\text{Scientific/Quantum Computing}
}
$$

---

# 🧠 Final Lesson Paragraph

> **Hypothesis testing is a formal framework for evaluating whether observed data provide sufficient evidence against a baseline hypothesis. We begin with a null hypothesis \(H_0\), which represents a reference claim, and an alternative hypothesis \(H_A\), which represents the possibility we are investigating. We then calculate a test statistic that measures how far the observed data are from what \(H_0\) predicts relative to the uncertainty of the estimate. For a simple Normal mean test, this can be expressed as \(Z=(\bar{x}-\mu_0)/(\sigma/\sqrt n)\). A large absolute test statistic indicates that the observation is farther from the null prediction in standardized units. A significance level \(\alpha\), often 0.05, defines the long-run Type I error rate of the testing procedure under its assumptions; a Type I error occurs when we reject a true \(H_0\), while a Type II error occurs when we fail to reject a false \(H_0\), with statistical power given by \(1-\beta\). We must say 'reject \(H_0\)' or 'fail to reject \(H_0\)' rather than treating failure to reject as proof that \(H_0\) is true. Hypothesis testing connects directly to confidence intervals, because a two-sided 5% test generally corresponds to a 95% confidence interval under the same assumptions. In physics and quantum experiments, this framework lets us ask whether observed deviations from theoretical predictions are larger than expected from statistical fluctuations; in ML, it helps distinguish observed differences in model performance or features from differences that could plausibly arise from sampling variability. The next concept, the p-value, will give us another way to quantify how unusual the observed result is under the null hypothesis.**

### Next:

$$
\boxed{\textbf{Lesson 32 — p-values}}
$$

We will build the p-value **very carefully**, because it is one of the most misunderstood concepts in statistics.
