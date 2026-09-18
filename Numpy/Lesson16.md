# Lesson 16 — Expected Value & Variance

Today we are going to slow down and build **Expectation and Variance from absolute zero**.

These two concepts are everywhere in:

- Statistics
- Machine Learning
- Probability
- Data Science
- Physics
- Quantum Mechanics

You have already seen formulas such as:

$$
E[X]=p
$$

and

$$
\operatorname{Var}(X)=p(1-p)
$$

for Bernoulli, and:

$$
E[X]=np
$$

for Binomial.

But now we're going to understand **why**.

---

# 1. The Problem: How Do We Describe a Distribution?

Imagine I give you this probability distribution:

| Value of \(X\) | Probability |
| -------------: | ----------: |
|              0 |         0.2 |
|              1 |         0.5 |
|              2 |         0.3 |

You could draw the whole distribution.

But sometimes we want a few numbers that summarize it.

Two of the most important are:

### Expected value

> Where is the distribution centered?

### Variance

> How spread out is the distribution?

Think:

```text
             Distribution
                  │
          ┌───────┴───────┐
          ▼               ▼
      Expected          Variance
       Value             Spread
       "Center"          "How much?"
```

---

# 2. Expected Value: The Basic Idea

The word **expected** can be misleading.

It does **not** necessarily mean:

> "What will happen?"

Instead:

> **Expected value is the probability-weighted average of possible outcomes.**

Let's start with an everyday example.

---

# 3. A Simple Game 🎲

Imagine a game:

- 50% chance of winning $0
- 50% chance of winning $100

What is the average amount you'd expect per game over many repetitions?

A natural answer is:

$$
\$50.
$$

Why?

Because half the time you get 0 and half the time you get 100:

$$
\frac{0+100}{2}=50.
$$

But let's express this using probabilities.

$$
E[X]
=
0(0.5)+100(0.5)
$$

$$
=0+50
$$

$$
\boxed{E[X]=50}
$$

---

# 4. Why "Weighted Average"?

Normal average:

$$
\frac{x_1+x_2+x_3}{3}
$$

assumes every value is equally important.

But in probability, outcomes may have different probabilities.

So we multiply:

$$
\text{value}\times\text{probability}.
$$

Then add everything.

Therefore:

$$
\boxed{
E[X]=\sum_x xP(X=x)
}
$$

This is the fundamental formula for the expected value of a discrete random variable.

---

# 5. Decode the Formula

$$
E[X]=\sum_x xP(X=x)
$$

### \(E[X]\)

Expected value of \(X\).

### \(\sum\)

Add everything.

### \(x\)

A possible value of the random variable.

### \(P(X=x)\)

Probability that \(X\) takes that value.

So mentally:

> **Expected value = value × probability, for every possible value, then add.**

---

# 6. Example With Three Outcomes

Suppose:

| \(X\) | \(P(X)\) |
| ----: | -------: |
|     0 |      0.2 |
|     1 |      0.5 |
|     2 |      0.3 |

Then:

$$
E[X]
=
0(0.2)+1(0.5)+2(0.3)
$$

$$
=0+0.5+0.6
$$

$$
\boxed{E[X]=1.1}
$$

Notice something interesting:

\(X\) can only be:

$$
0,1,2
$$

but the expected value is:

$$
1.1.
$$

That's perfectly fine.

Expected value **doesn't have to be one of the possible outcomes**.

---

# 7. Long-Run Interpretation

This is one of the best ways to understand expectation.

Suppose:

$$
E[X]=1.1.
$$

If you perform the experiment:

- 10 times → average might not be 1.1
- 100 times → perhaps closer
- 10,000 times → typically much closer

In the long run:

$$
\text{average observed value}\rightarrow E[X].
$$

So:

> **Expected value is the long-run average outcome under repeated trials.**

This is especially useful in statistics.

---

# 8. Expected Value of a Bernoulli Variable

Remember Bernoulli:

$$
X\in\{0,1\}.
$$

And:

$$
P(X=1)=p
$$

$$
P(X=0)=1-p.
$$

Therefore:

$$
E[X]
=
0(1-p)+1(p)
$$

$$
\boxed{E[X]=p}
$$

This now makes intuitive sense.

If an event happens 70% of the time:

$$
p=0.7,
$$

then if we encode:

$$
\text{happens}=1
$$

and:

$$
\text{doesn't happen}=0,
$$

the long-run average of those 0/1 values will be approximately:

$$
0.7.
$$

That's why:

$$
\boxed{E[X]=p}.
$$

---

# 9. Expected Value of Binomial

Now remember:

$$
X=X_1+X_2+\cdots+X_n
$$

where every \(X_i\) is Bernoulli.

Each one has:

$$
E[X_i]=p.
$$

A very important property is:

$$
E[X_1+X_2+\cdots+X_n]
=
E[X_1]+E[X_2]+\cdots+E[X_n].
$$

Therefore:

$$
E[X]=p+p+\cdots+p
$$

\(n\) times.

So:

$$
\boxed{E[X]=np}.
$$

For example:

$$
n=100,\qquad p=0.8
$$

gives:

$$
E[X]=100(0.8)=80.
$$

Meaning:

> Across many repetitions of the 100-trial experiment, the average number of successes approaches 80.

---

# 10. Now: Variance

Expected value tells us about the **center**.

But center isn't enough.

Consider these two datasets:

### Dataset A

$$
4,5,5,5,6
$$

### Dataset B

$$
0,2,5,8,10
$$

Both are centered around approximately 5.

But they clearly behave differently.

Dataset A:

> Values are close to the center.

Dataset B:

> Values are spread out.

We need a way to measure that spread.

That's **variance**.

---

# 11. The Core Idea of Variance

Variance asks:

> **How far are the values from the mean, on average?**

Imagine the mean is your home.

Each observation is somewhere around your home.

Variance measures:

> How far away are the observations?

Mental picture:

```text
              Values

     • • •
       •
------- MEAN ----------------

     •              •
                 •
                         •
```

Small spread → small variance.

Large spread → large variance.

---

# 12. First Calculate the Difference From the Mean

Suppose:

$$
X=[2,4,6].
$$

The mean is:

$$
\mu=\frac{2+4+6}{3}=4.
$$

Now calculate each deviation:

$$
2-4=-2
$$

$$
4-4=0
$$

$$
6-4=2.
$$

So:

$$
[-2,0,2].
$$

These are called **deviations from the mean**.

---

# 13. Why Can't We Just Average Deviations?

Let's try:

$$
\frac{-2+0+2}{3}=0.
$$

Oops!

We got:

$$
0.
$$

But the data clearly isn't perfectly concentrated at the mean.

The problem is that positive and negative deviations cancel.

For example:

$$
-10+10=0.
$$

So we need to remove the negative sign.

There are two common possibilities:

### Absolute value

$$
|x-\mu|
$$

or:

### Square

$$
(x-\mu)^2.
$$

Statistics commonly uses the **square**.

---

# 14. Why Square?

Suppose:

$$
x-\mu=-3.
$$

Square it:

$$
(-3)^2=9.
$$

And:

$$
3^2=9.
$$

So both sides of the mean contribute positively.

Also, larger deviations become disproportionately larger:

$$
1^2=1
$$

$$
2^2=4
$$

$$
5^2=25.
$$

So being far away from the mean gets strongly penalized.

This idea becomes extremely important in Machine Learning.

---

# 15. Variance Formula

For a population:

$$
\boxed{
\sigma^2=
\frac{1}{N}
\sum_{i=1}^{N}(x_i-\mu)^2
}
$$

Don't worry about the notation.

Let's decode it.

### \(x_i\)

One observation.

### \(\mu\)

Mean.

### \(x_i-\mu\)

Distance/deviation from mean.

### \((x_i-\mu)^2\)

Squared deviation.

### \(\sum\)

Add all squared deviations.

### \(N\)

Number of observations.

### Divide by \(N\)

Take the average.

So:

> **Variance = average squared distance from the mean.**

---

# 16. Full Example

Data:

$$
X=[2,4,6].
$$

Mean:

$$
\mu=4.
$$

Deviations:

$$
[-2,0,2].
$$

Square them:

$$
[4,0,4].
$$

Add:

$$
4+0+4=8.
$$

Divide by 3:

$$
\frac83\approx2.67.
$$

Therefore:

$$
\boxed{\sigma^2\approx2.67}.
$$

That's the variance.

---

# 17. Standard Deviation

Variance has a small problem.

We squared the units.

If the original measurement is in:

$$
\text{meters}
$$

then variance is in:

$$
\text{meters}^2.
$$

That isn't always intuitive.

So we take the square root.

This gives us **standard deviation**:

$$
\boxed{
\sigma=\sqrt{\sigma^2}
}
$$

For our example:

$$
\sigma=\sqrt{2.67}
$$

approximately:

$$
\boxed{1.63}.
$$

So:

```text
Variance
   ↓ square root
Standard deviation
```

---

# 18. Variance vs Standard Deviation

Think of it this way:

### Variance

The mathematical quantity that measures squared spread.

$$
\sigma^2
$$

### Standard deviation

The square root of variance.

$$
\sigma
$$

Standard deviation is often easier to interpret because it has the **same units as the original data**.

---

# 19. Why Do We Care About Variance in ML?

Suppose we have a feature:

$$
\text{Age}
$$

with values:

$$
20,21,22,23,24.
$$

Very little variation.

Another feature:

$$
\text{Income}
$$

might be:

$$
20,000,\ 50,000,\ 100,000,\ 500,000.
$$

Huge variation.

Variance helps us understand:

> How much does a feature vary?

This becomes important for:

- feature scaling
- standardization
- detecting unusual values
- understanding distributions
- statistical modeling
- PCA
- Gaussian models
- regression
- uncertainty analysis.

---

# 20. Standardization Preview

Later we'll study:

$$
\boxed{
z=\frac{x-\mu}{\sigma}
}
$$

This is called **standardization**.

Notice what appears:

- mean \(\mu\)
- standard deviation \(\sigma\)

That's why understanding expectation, variance, and standard deviation is essential before serious ML preprocessing.

---

# 21. Variance in Machine Learning Loss

Remember MSE:

$$
MSE=
\frac1n
\sum_{i=1}^{n}(y_i-\hat y_i)^2.
$$

Look at the squared error:

$$
(y_i-\hat y_i)^2.
$$

This has the same fundamental idea as variance:

$$
(x_i-\mu)^2.
$$

Both measure squared deviations.

Variance asks:

> How far are observations from their mean?

MSE asks:

> How far are predictions from their true values?

That's a very useful connection.

---

# 22. Expected Value in Physics

Expectation is everywhere in physics.

For a classical random variable \(X\):

$$
E[X].
$$

In quantum mechanics, expectation values are also fundamental.

For an observable represented by operator \(\hat A\):

$$
\boxed{
\langle A\rangle
=
\langle\psi|\hat A|\psi\rangle
}
$$

This represents the expected measurement value under repeated measurements of identically prepared systems.

So the idea you've just learned—

> **weighted average over possible outcomes**

—has a deep connection to quantum measurement.

---

# 23. Quantum Example

Suppose a measurement has two possible outcomes:

$$
0,\quad1
$$

with probabilities:

$$
P(0)=|\alpha|^2
$$

and:

$$
P(1)=|\beta|^2.
$$

The expected value is:

$$
E[X]
=
0|\alpha|^2
+
1|\beta|^2.
$$

Therefore:

$$
\boxed{
E[X]=|\beta|^2
}
$$

if the outcomes themselves are numerically encoded as 0 and 1.

Again:

> The expected measurement value is a probability-weighted average of the possible outcomes.

---

# 24. A Very Important Conceptual Distinction

Don't confuse:

### Mean of observed data

with:

### Expected value of a random variable.

They are closely related but conceptually different.

Suppose:

$$
X
$$

is a random variable describing a population/process.

Its theoretical expected value is:

$$
E[X].
$$

Now you collect observations:

$$
x_1,x_2,\ldots,x_n.
$$

Their sample mean is:

$$
\boxed{
\bar x=
\frac1n\sum_{i=1}^{n}x_i
}
$$

The sample mean is used to **estimate** the population expected value.

So:

$$
\boxed{
\text{Expected value} \rightarrow \text{theoretical quantity}
}
$$

$$
\boxed{
\text{Sample mean} \rightarrow \text{quantity calculated from observed data}
}
$$

This distinction will become extremely important later.

---

# 25. Population Variance vs Sample Variance

You will eventually encounter two formulas.

### Population variance

$$
\boxed{
\sigma^2=
\frac1N\sum_{i=1}^{N}(x_i-\mu)^2
}
$$

### Sample variance

$$
\boxed{
s^2=
\frac1{n-1}
\sum_{i=1}^{n}(x_i-\bar{x})^2
}
$$

Why \(n-1\) instead of \(n\)?

That's connected to **estimating a population variance from a sample**, and we'll study it properly later.

For now remember:

> **Population and sample variance are related but are not the same calculation.**

Don't memorize the \(n-1\) explanation yet.

---

# 26. One Amazing Mental Model 🧠

Imagine a target:

```text
                 •
            •    │    •
                 │
       •─────────🎯────────•
                 │
            •    │    •
                 │
```

### Expected value / mean

Where is the **center of gravity**?

🎯

### Variance

How widely are the points scattered around that center?

So:

$$
\boxed{\text{Mean = center}}
$$

$$
\boxed{\text{Variance = spread}}
$$

$$
\boxed{\text{Standard deviation = spread in original units}}
$$

---

# 27. The Three Most Important Equations

### Expected value

$$
\boxed{
E[X]=\sum_xxP(X=x)
}
$$

### Variance

$$
\boxed{
\operatorname{Var}(X)
=
E[(X-\mu)^2]
}
$$

where:

$$
\mu=E[X].
$$

### Standard deviation

$$
\boxed{
\sigma=\sqrt{\operatorname{Var}(X)}
}
$$

---

# 28. The Alternative Variance Formula

You'll often see:

$$
\boxed{
\operatorname{Var}(X)=E[X^2]-(E[X])^2
}
$$

This might look unrelated to:

$$
E[(X-\mu)^2].
$$

But they're the same.

Let's prove it.

Start:

$$
\operatorname{Var}(X)=E[(X-\mu)^2].
$$

Expand:

$$
(X-\mu)^2=X^2-2X\mu+\mu^2.
$$

Therefore:

$$
E[(X-\mu)^2]
=
E[X^2-2X\mu+\mu^2].
$$

Using linearity:

$$
=E[X^2]-2\mu E[X]+\mu^2.
$$

But:

$$
E[X]=\mu.
$$

So:

$$
=E[X^2]-2\mu^2+\mu^2
$$

and therefore:

$$
\boxed{
\operatorname{Var}(X)=E[X^2]-\mu^2
}
$$

Since:

$$
\mu=E[X],
$$

we get:

$$
\boxed{
\operatorname{Var}(X)=E[X^2]-(E[X])^2
}
$$

This formula will appear frequently in statistics and ML.

---

# 29. Let's Connect Everything

We started with:

### Probability

$$
P(X=x)
$$

Then:

### Expected value

$$
E[X]
$$

tells us the center.

Then:

### Variance

$$
\operatorname{Var}(X)
$$

tells us the spread.

Then:

### Standard deviation

$$
\sigma
$$

gives spread in original units.

So:

```text
Probability Distribution
        │
        ├───────────────┐
        ▼               ▼
     Expected         Variance
      Value             │
        │               ▼
      Center       Standard Deviation
                      Spread
```

---

# 30. Practice

Try these before looking at the answers.

### Q1

A random variable has:

| \(X\) | \(P(X)\) |
| ----: | -------: |
|     0 |      0.2 |
|     1 |      0.5 |
|     2 |      0.3 |

Calculate:

$$
E[X].
$$

---

### Q2

For:

$$
X\sim\mathrm{Bernoulli}(0.8)
$$

calculate:

$$
E[X].
$$

---

### Q3

For:

$$
X\sim\mathrm{Bernoulli}(0.8)
$$

calculate:

$$
\operatorname{Var}(X).
$$

---

### Q4

A Binomial random variable has:

$$
n=50,\qquad p=0.6.
$$

Find:

$$
E[X].
$$

---

### Q5

For the data:

$$
[2,4,6]
$$

find:

1. Mean
2. Deviations from mean
3. Squared deviations
4. Population variance
5. Population standard deviation

---

### Q6

Explain in your own words:

> Why don't we simply average the deviations from the mean to calculate spread?

---

# Answers

### Q1

$$
E[X]
=
0(0.2)+1(0.5)+2(0.3)
$$

$$
=1.1.
$$

---

### Q2

For Bernoulli:

$$
E[X]=p
$$

so:

$$
\boxed{E[X]=0.8}
$$

---

### Q3

$$
\operatorname{Var}(X)=p(1-p)
$$

$$
=0.8(0.2)
$$

$$
\boxed{0.16}
$$

---

### Q4

$$
E[X]=np
$$

$$
=50(0.6)
$$

$$
\boxed{30}
$$

---

### Q5

Data:

$$
[2,4,6]
$$

Mean:

$$
\mu=4.
$$

Deviations:

$$
[-2,0,2].
$$

Squared deviations:

$$
[4,0,4].
$$

Population variance:

$$
\sigma^2=\frac{4+0+4}{3}
$$

$$
\boxed{\sigma^2=\frac83\approx2.67}
$$

Standard deviation:

$$
\sigma=\sqrt{2.67}
$$

$$
\boxed{\sigma\approx1.63}
$$

---

### Q6

Because positive and negative deviations cancel:

$$
(-2)+0+(2)=0.
$$

Squaring makes every deviation positive:

$$
(-2)^2=4,\qquad 2^2=4.
$$

Therefore squared deviations allow us to measure spread without cancellation.

---

# 🧠 Final Mental Map

You should now be able to look at a distribution and think:

```text
              DISTRIBUTION
                   │
          ┌────────┴────────┐
          ▼                 ▼
      EXPECTATION         VARIANCE
          │                 │
          ▼                 ▼
        CENTER             SPREAD
                            │
                            ▼
                    STANDARD DEVIATION
```

And remember:

$$
\boxed{\text{Expected Value = probability-weighted average}}
$$

$$
\boxed{\text{Variance = average squared deviation from the mean}}
$$

$$
\boxed{\text{Standard Deviation = square root of variance}}
$$

This foundation is now strong enough to move into the next major part of statistics: **describing real datasets**—starting with **mean, median, mode, range, and then percentiles/quartiles/IQR**, before eventually implementing them with NumPy.
