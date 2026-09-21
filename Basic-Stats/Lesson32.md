# Lesson 32 — p-values

We now reach one of the **most misunderstood concepts in statistics**:

$$
\boxed{\text{p-value}}
$$

You have already learned almost everything needed to understand it:

$$
\text{Probability}
\rightarrow
\text{Random Variables}
\rightarrow
\text{Distributions}
\rightarrow
\text{Sampling Distribution}
\rightarrow
\text{SE}
\rightarrow
\text{CLT}
\rightarrow
\text{Confidence Intervals}
\rightarrow
\text{Hypothesis Testing}
$$

Now the p-value will fit naturally into that chain.

---

# 1. First: What Question Are We Asking?

Suppose:

$$
H_0:\mu=100
$$

You collect data and obtain:

$$
\bar{x}=102
$$

You calculate:

$$
Z=2
$$

Now we know the observation is **2 standard errors away** from the null value.

But we want to ask:

> **If \(H_0\) were actually true, how unusual would a result this extreme be?**

That is essentially what the p-value measures.

---

# 2. The Core Definition

For a hypothesis test, the p-value is:

$$
\boxed{
P(\text{result at least as extreme as observed}\mid H_0\text{ is true})
}
$$

That's the key definition.

Let's break every part down.

### "result"

The statistic we observed.

### "at least as extreme"

Results that are at least as far from the null expectation as what we observed, according to the test's direction.

### "\(H_0\) is true"

We calculate this probability **assuming the null hypothesis**.

---

# 3. The Most Important Mental Model

Think of \(H_0\) as a world.

Suppose:

$$
H_0:\mu=100
$$

Imagine we temporarily enter the world where:

$$
\mu=100
$$

is true.

Then we ask:

> "How often would we see a result this extreme or more extreme?"

That probability is the p-value.

So:

$$
\boxed{
H_0\text{ world}
\rightarrow
\text{observe extreme result}
\rightarrow
\text{calculate how rare it is}
}
$$

---

# 4. Example With a Coin 🪙

Suppose someone claims a coin is fair:

$$
H_0:p=0.5
$$

You flip it:

$$
100
$$

times.

Suppose you observe:

$$
70
$$

heads.

That's quite different from the expected:

$$
50
$$

heads.

The question isn't simply:

> "70 is different from 50, therefore the coin isn't fair."

Instead:

> **If the coin really were fair, how unusual would getting 70 or more heads be?**

For a two-sided test, we'd also consider outcomes comparably extreme in the other direction, such as 30 or fewer heads.

That probability is related to the p-value.

---

# 5. Small p-value

Suppose:

$$
p\text{-value}=0.002
$$

That means:

> Assuming \(H_0\) is true, results at least as extreme as the observed result have probability about 0.2% under the specified testing procedure.

That's relatively unusual under \(H_0\).

---

# 6. Large p-value

Suppose:

$$
p\text{-value}=0.40
$$

That means:

> Assuming \(H_0\) is true, results at least as extreme as the observed result are not particularly rare under the specified test.

So the data don't provide strong evidence against \(H_0\) by that criterion.

---

# 7. The Most Important Misunderstanding 🚨

A p-value is **NOT**:

$$
\boxed{P(H_0\text{ is true})}
$$

For example:

$$
p=0.03
$$

does **not** mean:

> "There is a 3% probability that \(H_0\) is true."

That's incorrect.

The p-value conditions on the null:

$$
\boxed{
P(\text{data as/extremer}\mid H_0)
}
$$

It does not directly give:

$$
\boxed{
P(H_0\mid\text{data})
}
$$

Those are different probabilities.

---

# 8. Why Are They Different?

Remember conditional probability from our early probability lesson.

We learned:

$$
P(A|B)
$$

means:

> probability of \(A\) given \(B\).

The p-value has the structure:

$$
P(\text{data}\mid H_0)
$$

But the probability that the hypothesis is true given data would be:

$$
P(H_0\mid\text{data})
$$

These are not generally equal.

This is closely related to the distinction:

$$
P(D|T)\neq P(T|D)
$$

that we discussed when learning conditional probability.

---

# 9. A Visual Example

Suppose:

$$
H_0:\mu=100
$$

and our observed test statistic is:

$$
Z=2
$$

For a two-sided test, we care about both tails:

```text id="9qkz8r"
                         H₀ distribution

                         │
                    _____│_____
                 __/           \__
               _/                 \_
______________/_____________________\______________
       ← tail       0          tail →
                  -2          +2
```

The p-value is the probability represented by the relevant tail regions.

For:

$$
Z=2
$$

the two-sided Normal p-value is approximately:

$$
\boxed{0.0455}
$$

So roughly 4.55% of outcomes under the standard Normal null distribution would be at least as extreme as:

$$
|Z|=2
$$

---

# 10. One-Sided vs Two-Sided p-values

This is important.

Suppose:

$$
Z=2
$$

### Right-sided test

If:

$$
H_A:\mu>\mu_0
$$

we care about the right tail:

$$
P(Z\ge2)
$$

which is approximately:

$$
0.0228
$$

---

### Two-sided test

If:

$$
H_A:\mu\neq\mu_0
$$

we care about both tails:

$$
P(|Z|\ge2)
$$

which is approximately:

$$
0.0455
$$

So:

$$
\boxed{
\text{Alternative hypothesis determines which outcomes count as "extreme."}
}
$$

---

# 11. Why Do We Say "At Least As Extreme"?

Suppose our observed:

$$
Z=2
$$

We don't just ask:

> "What is the probability of getting exactly \(Z=2\)?"

For a continuous distribution, the probability of getting exactly one point is effectively zero.

Instead, we consider the region:

$$
Z\ge2
$$

for a right-tailed test.

Or:

$$
|Z|\ge2
$$

for a two-sided test.

Therefore:

$$
\boxed{
p\text{-value}=
\text{probability of the observed result or something more extreme}
}
$$

under \(H_0\).

---

# 12. p-value and the Rejection Rule

We previously learned about:

$$
\alpha
$$

Suppose:

$$
\alpha=0.05
$$

Then a common decision rule is:

$$
\boxed{
p<\alpha
\Rightarrow
\text{Reject }H_0
}
$$

and:

$$
\boxed{
p\ge\alpha
\Rightarrow
\text{Fail to reject }H_0
}
$$

For example:

### Case A

$$
p=0.01
$$

and:

$$
\alpha=0.05
$$

Since:

$$
0.01<0.05
$$

we reject \(H_0\).

---

### Case B

$$
p=0.30
$$

Since:

$$
0.30>0.05
$$

we fail to reject \(H_0\).

---

# 13. What Does "Statistically Significant" Mean?

If:

$$
p<\alpha
$$

we often say:

$$
\boxed{\text{statistically significant}}
$$

at significance level \(\alpha\).

For example:

$$
p=0.03
$$

with:

$$
\alpha=0.05
$$

is statistically significant at the 5% level.

But remember:

$$
\boxed{
\text{statistically significant}
\neq
\text{scientifically important}
}
$$

We'll discuss this more in the next lesson.

---

# 14. Let's Derive a p-value From Our Previous Example

Remember:

$$
H_0:\mu=100
$$

$$
\bar{x}=102
$$

$$
\sigma=10
$$

$$
n=100
$$

We calculated:

$$
SE=1
$$

Therefore:

$$
Z=
\frac{102-100}{1}
$$

$$
Z=2
$$

For a two-sided test:

$$
p=P(|Z|\ge2)
$$

Using the standard Normal distribution:

$$
P(Z\ge2)\approx0.0228
$$

and because there are two tails:

$$
p\approx2(0.0228)
$$

$$
\boxed{p\approx0.0455}
$$

At:

$$
\alpha=0.05
$$

we have:

$$
0.0455<0.05
$$

so we reject:

$$
H_0
$$

under this testing procedure.

---

# 15. p-value vs Confidence Interval

Remember our previous lesson.

We had:

$$
95\%\ CI
$$

and hypothesis testing.

For a two-sided test at:

$$
\alpha=0.05
$$

there is a close relationship:

$$
\boxed{
p<0.05
\iff
\text{null value is outside the corresponding 95% CI}
}
$$

under the same model and assumptions.

For example, suppose:

$$
95\%\ CI=[100.5,103.5]
$$

and we're testing:

$$
H_0:\mu=100
$$

Since:

$$
100
$$

is outside the interval, the corresponding two-sided test rejects \(H_0\).

---

# 16. p-value as a "Surprise Meter"

A useful beginner mental model:

$$
\boxed{\text{p-value = surprise meter under }H_0}
$$

### Large p-value

```text
H₀ predicts these kinds of results
             ↓
        ┌─────────┐
        │  DATA   │
        └─────────┘
        not unusual
```

### Small p-value

```text
H₀ predicts these kinds of results
             ↓
      DATA appears here
              ↓
        very unusual
```

So:

$$
\boxed{
\text{smaller p-value}
\Rightarrow
\text{stronger evidence against }H_0
}
$$

**within the framework and assumptions of the specified test.**

Notice that we're talking about evidence **against \(H_0\)**, not probability that \(H_0\) is false.

---

# 17. What a p-value Does NOT Tell You

A p-value does not directly tell you:

### ❌ Probability that \(H_0\) is true

$$
p\neq P(H_0)
$$

### ❌ Probability that \(H_A\) is true

$$
p\neq P(H_A)
$$

### ❌ Size of the effect

A tiny effect can have:

$$
p<0.001
$$

with enough data.

### ❌ Practical importance

Statistical significance doesn't automatically mean the effect matters scientifically or practically.

### ❌ Probability that your result is "due to chance"

That's an oversimplification and can be misleading.

---

# 18. A Very Important Example: Huge Sample

Suppose two models differ by:

$$
0.01\%
$$

in accuracy.

You have:

$$
n=100,000,000
$$

test examples.

Because the sample is enormous, the difference may produce a very small p-value.

You might get:

$$
p<0.001
$$

But the actual improvement:

$$
0.01\%
$$

could be practically irrelevant.

Therefore:

$$
\boxed{
\text{Small p-value}
\not\Rightarrow
\text{large effect}
}
$$

This is extremely important in ML.

---

# 19. Effect Size

To understand practical importance, we often also need:

$$
\boxed{\text{Effect Size}}
$$

Suppose:

$$
\mu_A=100
$$

and:

$$
\mu_B=100.1
$$

The difference is:

$$
0.1
$$

Now suppose the measurement uncertainty is tiny.

The result might be statistically significant.

But:

$$
0.1
$$

may or may not matter in the real application.

So a good scientific analysis considers both:

$$
\boxed{\text{Statistical evidence}}
$$

and:

$$
\boxed{\text{Magnitude / practical importance}}
$$

along with uncertainty and study design.

---

# 20. p-value and Sample Size

This is a very important relationship.

Suppose the true difference is:

$$
\Delta=1
$$

For small \(n\):

$$
SE
$$

may be large.

Then:

$$
Z=\frac{\Delta}{SE}
$$

may be small.

For large \(n\):

$$
SE\downarrow
$$

so:

$$
|Z|\uparrow
$$

and the p-value can become smaller.

Therefore:

$$
\boxed{
\text{Same effect}
+
\text{more data}
\rightarrow
\text{potentially smaller p-value}
}
$$

This is why you should never interpret a p-value without considering sample size.

---

# 21. Physics Example 🔬

Suppose a theory predicts:

$$
\mu=9.81
$$

Your experiment gives:

$$
\bar{x}=9.82
$$

The difference is:

$$
0.01
$$

Is that meaningful?

We need to know the uncertainty.

If:

$$
SE=1
$$

then:

$$
Z=0.01
$$

Very close to the null.

But if:

$$
SE=0.001
$$

then:

$$
Z=10
$$

Very far from the null.

Same raw difference:

$$
0.01
$$

but completely different statistical evidence.

Again:

$$
\boxed{
\text{Effect}/\text{uncertainty}
}
$$

is central.

---

# 22. Quantum Example ⚛️

Suppose a quantum model predicts:

$$
\langle A\rangle=2
$$

Experiment gives:

$$
\bar A=2.05
$$

If:

$$
SE=0.1
$$

then:

$$
Z=\frac{2.05-2}{0.1}=0.5
$$

The result isn't particularly far from the null.

But if:

$$
SE=0.005
$$

then:

$$
Z=10
$$

Now the result is extremely far from the null according to that model.

So simply saying:

> "The experimental value differs from theory"

is incomplete.

We need:

$$
\boxed{
\text{difference}
+
\text{uncertainty}
}
$$

---

# 23. Quantum Trajectory Connection

Suppose your quantum trajectory produces photon waiting times:

$$
\tau_1,\tau_2,\ldots,\tau_n
$$

You have a theoretical model:

$$
w(\tau|\theta)
$$

where:

$$
\theta
$$

might represent a physical parameter.

You could have:

$$
H_0:\theta=\theta_0
$$

and:

$$
H_A:\theta\neq\theta_0
$$

The data generate evidence about \(\theta\).

Eventually, rather than simply testing one parameter value, you may want to estimate:

$$
\hat\theta
$$

and determine how precisely you can estimate it.

That's where:

$$
\boxed{\text{Likelihood}}
$$

and:

$$
\boxed{\text{Fisher Information}}
$$

become extremely useful.

---

# 24. p-value and Fisher Information

These concepts are related, but they answer different questions.

### p-value

Asks:

> **How unusual is this observed result if \(H_0\) were true?**

### Fisher Information

Asks roughly:

> **How much information does the probability distribution contain about an unknown parameter?**

So:

$$
\boxed{
\text{Hypothesis testing}
\rightarrow
\text{evidence against a specified hypothesis}
}
$$

while:

$$
\boxed{
\text{Fisher Information}
\rightarrow
\text{precision/information about parameter estimation}
}
$$

This distinction will become very important for your quantum work.

---

# 25. The p-value Pipeline

Remember this:

```text id="n3iz7k"
H₀
 ↓
Assume H₀ is true
 ↓
Sampling distribution under H₀
 ↓
Observe test statistic
 ↓
Ask:
"How extreme is this result?"
 ↓
Calculate tail probability
 ↓
p-value
```

That's the whole conceptual pipeline.

---

# 26. Three Numbers You Must Never Confuse

### \(\alpha\)

Chosen **before** the test.

$$
\boxed{\text{significance threshold}}
$$

---

### Test statistic

Calculated from data.

Example:

$$
Z=2.3
$$

$$
\boxed{\text{distance from null in standardized units}}
$$

---

### p-value

Calculated from the test statistic and null distribution.

$$
p=0.021
$$

$$
\boxed{\text{tail probability under }H_0}
$$

So:

```text id="yq6q8s"
α
↓
chosen threshold

Z
↓
observed standardized distance

p
↓
how extreme that Z is under H₀
```

---

# 27. 🧠 Practice

### Q1

What does a p-value measure?

---

### Q2

True or false:

> A p-value of 0.03 means there is a 3% probability that \(H_0\) is true.

---

### Q3

Suppose:

$$
p=0.02
$$

and:

$$
\alpha=0.05
$$

What is the usual decision?

---

### Q4

Suppose:

$$
p=0.20
$$

and:

$$
\alpha=0.05
$$

Do we reject \(H_0\)?

---

### Q5

Which is smaller?

$$
p(Z\ge2)
$$

or:

$$
p(|Z|\ge2)
$$

for a standard Normal \(Z\)?

---

### Q6

Does a small p-value prove that the effect is practically important?

---

## Answers

### Q1

A p-value is the probability, **assuming \(H_0\) is true**, of obtaining a result at least as extreme as the observed result according to the specified test.

---

### Q2

$$
\boxed{\text{False}}
$$

It does not mean:

$$
P(H_0)=0.03
$$

---

### Q3

Since:

$$
0.02<0.05
$$

we:

$$
\boxed{\text{Reject }H_0}
$$

under that testing procedure.

---

### Q4

Since:

$$
0.20>0.05
$$

we:

$$
\boxed{\text{Fail to reject }H_0}
$$

---

### Q5

The two-sided probability is larger:

$$
P(|Z|\ge2)
=
2P(Z\ge2)
$$

so:

$$
\boxed{
P(Z\ge2)<P(|Z|\ge2)
}
$$

---

### Q6

$$
\boxed{\text{No}}
$$

A small p-value concerns statistical evidence under the null model; practical importance depends on effect size, context, uncertainty, and other considerations.

---

# 🗺️ COMPLETE ROADMAP — LESSON 32

```text id="b7q7mg"
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
Hypothesis Testing                  ✅

p-values                            🔵 YOU ARE HERE
Statistical Significance            ⬜
Type I / Type II Errors             ✅
Statistical Power                   ✅
Effect Size                         🔵 introduced


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
p-value calculations                ⬜


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

# 🔗 We Are Almost at NumPy

At this point, you've built nearly the complete **introductory statistics foundation**.

We have:

$$
\boxed{
\text{Descriptive Statistics}
}
$$

↓

$$
\boxed{
\text{Probability}
}
$$

↓

$$
\boxed{
\text{Random Variables}
}
$$

↓

$$
\boxed{
\text{Distributions}
}
$$

↓

$$
\boxed{
\text{Sampling}
}
$$

↓

$$
\boxed{
\text{Sampling Distribution}
}
$$

↓

$$
\boxed{
SE
}
$$

↓

$$
\boxed{
CLT + LLN
}
$$

↓

$$
\boxed{
\text{Confidence Intervals}
}
$$

↓

$$
\boxed{
\text{Hypothesis Testing}
}
$$

↓

$$
\boxed{
p\text{-values}
}
$$

The next lesson will tie together:

$$
\boxed{\text{p-values + }\alpha+\text{ statistical significance + effect size}}
$$

Then we can close this core statistics block and begin the **NumPy Foundation**.

And when we start NumPy, we won't just learn:

```python
np.mean()
np.std()
np.cov()
```

as isolated commands.

We'll take the mathematics you've already learned and make NumPy **execute that mathematics**.

---

# 🧠 Final Lesson Paragraph

> **A p-value quantifies how unusual the observed result, or a result at least as extreme according to the specified test, would be if the null hypothesis \(H_0\) were true. It is fundamentally a conditional probability of the form \(P(\text{data as or more extreme}\mid H_0)\), not the probability that \(H_0\) is true. For a two-sided Normal test with \(Z=2\), for example, the p-value is \(P(|Z|\ge2)\approx0.0455\), while a right-sided test would use only \(P(Z\ge2)\approx0.0228\). The alternative hypothesis determines which outcomes count as extreme. When a pre-specified p-value is below a significance level such as \(\alpha=0.05\), we commonly reject \(H_0\); otherwise, we fail to reject it. A small p-value indicates stronger evidence against the null model within the assumptions of the test, but it does not tell us the probability that the null is true, the probability that the alternative is true, or whether an effect is practically important. Statistical significance must therefore be considered alongside effect size, uncertainty, sample size, and study design. In physics and quantum experiments, p-values can help assess whether deviations from theoretical predictions are unusually large relative to expected statistical fluctuations; in ML, they can help evaluate whether observed differences or associations are distinguishable from sampling variability. This completes another major piece of statistical inference and prepares us to connect the entire foundation to NumPy through simulations and computation.**

### Next:

$$
\boxed{\textbf{Lesson 33 — Statistical Significance, Effect Size \& the Full Inference Picture}}
$$

After that, we'll be ready to make the jump from **mathematics/statistics → NumPy**.
