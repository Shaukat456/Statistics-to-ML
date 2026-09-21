# Lesson 13 — Probability Distributions

We now know:

- what probability is,
- what an outcome is,
- what a random variable is.

The next question is:

> **If a random variable can take many possible values, how do we describe all of its probabilities together?**

The answer is:

$$
\boxed{\text{Probability Distribution}}
$$

This is a **very important concept for Machine Learning**.

---

# 1. The Basic Idea

Suppose we roll a die.

Our random variable is:

$$
X=\text{number shown on the die}
$$

Possible values:

$$
1,2,3,4,5,6
$$

For a fair die:

$$
P(X=1)=\frac16
$$

$$
P(X=2)=\frac16
$$

and so on.

Instead of discussing each probability separately, we can describe the **whole collection**:

$$
\boxed{
\text{Distribution of }X
}
$$

So:

> **A probability distribution tells us how probability is spread across the possible values of a random variable.**

---

# 2. Think of a Probability Distribution as a "Probability Map"

Imagine you're asking:

> "Where is the probability located?"

For a die:

```text
X:       1    2    3    4    5    6
         │    │    │    │    │    │
P(X):   1/6  1/6  1/6  1/6  1/6  1/6
```

This is a probability map.

It tells us:

- possible values,
- and how much probability belongs to each value.

---

# 3. Why Do We Need Distributions?

Imagine you are studying exam scores.

Suppose you collect:

$$
55,60,62,65,67,70,71,72,74,75,78,80,81,85,90
$$

You might ask:

- Where are most scores concentrated?
- Are low scores common?
- Are high scores common?
- Is the data spread out?
- What score is most likely?
- How unusual is a score of 99?

A probability distribution gives us a mathematical framework for answering these kinds of questions.

---

# 4. Distributions Come in Two Major Forms

Because random variables come in two major types, distributions do too.

```text id="w0d6u7"
             Probability Distribution
                       │
              ┌────────┴────────┐
              │                 │
          Discrete           Continuous
              │                 │
             PMF               PDF
```

The distinction is fundamental.

---

# 5. Discrete Probability Distribution

A discrete random variable has countable possible values.

Example:

$$
X=\text{number on a die}
$$

Possible values:

$$
1,2,3,4,5,6
$$

We can assign a probability to each exact value.

For example:

$$
P(X=4)=\frac16
$$

This is described using a:

$$
\boxed{\text{PMF}}
$$

---

# 6. PMF — Probability Mass Function

PMF stands for:

$$
\boxed{\text{Probability Mass Function}}
$$

It tells us:

$$
\boxed{P(X=x)}
$$

for a discrete random variable.

In simple words:

> **PMF tells us how much probability is assigned to each possible discrete value.**

---

# 7. Example of a PMF

Fair die:

| \(x\) | \(P(X=x)\) |
| ----: | ---------: |
|     1 |    \(1/6\) |
|     2 |    \(1/6\) |
|     3 |    \(1/6\) |
|     4 |    \(1/6\) |
|     5 |    \(1/6\) |
|     6 |    \(1/6\) |

And:

$$
\sum_xP(X=x)=1
$$

because all possible outcomes together account for 100% probability.

---

# 8. A Non-Uniform Distribution

The probabilities don't have to be equal.

Suppose we have a strange six-sided die:

| \(X\) | Probability |
| ----: | ----------: |
|     1 |        0.05 |
|     2 |        0.10 |
|     3 |        0.15 |
|     4 |        0.20 |
|     5 |        0.20 |
|     6 |        0.30 |

Check:

$$
0.05+0.10+0.15+0.20+0.20+0.30=1
$$

So this is also a valid probability distribution.

It says:

> 6 is more likely than 1.

---

# 9. A Crucial Rule for PMFs

For a valid discrete probability distribution:

$$
\boxed{P(X=x)\geq0}
$$

and:

$$
\boxed{\sum_xP(X=x)=1}
$$

So probabilities:

- cannot be negative,
- must collectively add to 1.

---

# 10. Continuous Probability Distributions

Now consider:

$$
X=\text{height of a randomly selected person}
$$

Possible values could include:

$$
170
$$

$$
170.1
$$

$$
170.01
$$

$$
170.001
$$

and infinitely many others.

We cannot make a table containing every possible value.

So we use a different mathematical tool:

$$
\boxed{\text{PDF}}
$$

---

# 11. PDF — Probability Density Function

PDF means:

$$
\boxed{\text{Probability Density Function}}
$$

A PDF describes how probability is **distributed across a continuous range**.

This is where an important distinction appears.

For a continuous random variable:

$$
\boxed{P(X=x)=0}
$$

for an exact point in the ideal mathematical model.

Instead, we ask:

$$
\boxed{P(a<X<b)}
$$

For example:

$$
P(170<X<180)
$$

meaning:

> What is the probability that the person's height lies between 170 and 180 cm?

---

# 12. The "Area" Mental Model

This is one of the most important things to understand.

Imagine a curve:

```text
Probability
density
   │
   │              /\
   │             /  \
   │           /      \
   │         /          \
   │_______/______________\______ Height
          160 170 180 190
```

The **area under the curve** represents probability.

So:

$$
P(170<X<180)
$$

is the area under the curve between 170 and 180.

---

# 13. Why Is a PDF Not Directly a Probability?

This is a common beginner mistake.

If:

$$
f(x)=0.03
$$

you should **not automatically say**:

> "There is a 3% probability of \(X=x\)."

For a continuous variable, \(f(x)\) is **density**, not the probability of that exact point.

Probability comes from an interval:

$$
P(a<X<b)
$$

which mathematically is:

$$
\boxed{
P(a<X<b)=\int_a^b f(x)\,dx
}
$$

Don't worry if the integral looks unfamiliar.

We'll build the calculus required later.

For now remember:

> **Discrete → probability at values.**

> **Continuous → probability over intervals / area under density.**

---

# 14. PMF vs PDF

This distinction is extremely important.

|                  | Discrete         | Continuous                  |
| ---------------- | ---------------- | --------------------------- |
| Random variable  | Countable values | Continuous range            |
| Function         | PMF              | PDF                         |
| Example          | Number of cars   | Temperature                 |
| Exact \(P(X=x)\) | Can be > 0       | 0 in ideal continuous model |
| Probability      | Sum              | Area                        |

Mental shortcut:

$$
\boxed{\text{PMF = Mass}}
$$

$$
\boxed{\text{PDF = Density}}
$$

---

# 15. CDF — Another Very Important Distribution Function

Now we introduce:

$$
\boxed{\text{CDF}}
$$

CDF stands for:

$$
\boxed{\text{Cumulative Distribution Function}}
$$

It answers:

> **What is the probability that \(X\) is less than or equal to \(x\)?**

Mathematically:

$$
\boxed{
F(x)=P(X\leq x)
}
$$

This definition is extremely important.

---

# 16. Example of a CDF

Suppose:

$$
X=\text{die result}
$$

Then:

$$
F(3)=P(X\leq3)
$$

Possible values:

$$
1,2,3
$$

Therefore:

$$
F(3)=
\frac16+\frac16+\frac16
$$

$$
\boxed{F(3)=\frac12}
$$

So the CDF tells us the **accumulated probability up to a point**.

---

# 17. CDF Mental Model

Think of filling a glass with probability.

Start:

$$
0
$$

As \(x\) increases, probability accumulates.

```text
x increases →

Probability
1.0 |                    ______
    |                  /
    |                /
0.5 |            ___/
    |          /
    |        /
0.0 |_______/
    +--------------------------→ x
```

The CDF can never decrease.

It starts near:

$$
0
$$

and eventually reaches:

$$
1
$$

---

# 18. PMF, PDF, CDF Together

Think of them as three different questions.

### PMF

> "How much probability is assigned to this discrete value?"

$$
P(X=x)
$$

### PDF

> "How densely is probability distributed around this continuous region?"

$$
f(x)
$$

### CDF

> "How much probability has accumulated up to \(x\)?"

$$
F(x)=P(X\leq x)
$$

---

# 19. The Most Famous Distribution: Normal Distribution

Now we arrive at one of the most important distributions in statistics and ML.

$$
\boxed{\text{Normal Distribution}}
$$

Also called:

$$
\boxed{\text{Gaussian Distribution}}
$$

It looks approximately like a bell:

```text
Density
   │
   │                  /\
   │                /    \
   │              /        \
   │            /            \
   │__________/________________\____
                     μ
                     │
                   center
```

This is called the **bell curve**.

---

# 20. Why Is the Normal Distribution Important?

Many real-world measurements are approximately normal under appropriate conditions.

Examples can include:

- measurement errors
- biological measurements
- noise
- manufacturing variation
- physical measurements

And the Normal distribution appears throughout:

- statistics
- regression
- hypothesis testing
- Bayesian modeling
- Gaussian processes
- signal processing
- scientific computing
- ML

But be careful:

> Not every real-world dataset is normally distributed.

The Normal distribution is important, not universally applicable.

---

# 21. Mean and Standard Deviation Control the Normal Distribution

A Normal distribution is characterized by:

$$
\boxed{\mu}
$$

and:

$$
\boxed{\sigma}
$$

where:

- \(\mu\) = mean
- \(\sigma\) = standard deviation

We haven't formally learned standard deviation yet, but intuitively:

> **\(\mu\) controls the center.**

> **\(\sigma\) controls the spread.**

---

# 22. Changing the Mean

Imagine:

$$
\mu=50
$$

The distribution is centered around 50.

If:

$$
\mu=100
$$

the entire distribution shifts toward 100.

The shape can remain the same; its location changes.

So:

$$
\boxed{\mu=\text{location/center}}
$$

---

# 23. Changing the Standard Deviation

Now suppose:

$$
\sigma=5
$$

The distribution is relatively narrow.

If:

$$
\sigma=20
$$

the distribution becomes wider.

So:

$$
\boxed{\sigma=\text{spread}}
$$

Mental picture:

```text
Small σ:          Large σ:

     /\                /\
    /  \              /  \
   /    \            /    \
__/      \__      __/      \__
```

More accurately, the larger-\(\sigma\) curve is broader and lower at the center.

---

# 24. The 68–95–99.7 Rule

For a Normal distribution, approximately:

### Within 1 standard deviation

$$
\mu\pm\sigma
$$

contains about:

$$
\boxed{68\%}
$$

of observations.

### Within 2 standard deviations

$$
\mu\pm2\sigma
$$

contains about:

$$
\boxed{95\%}
$$

### Within 3 standard deviations

$$
\mu\pm3\sigma
$$

contains about:

$$
\boxed{99.7\%}
$$

Visual:

```text
              Normal Distribution

                    /\
                   /  \
                  /    \
             ____/      \____
            |      |      |
          μ-σ      μ      μ+σ
             ←  ~68%  →

        μ-2σ ←---- ~95% ----→ μ+2σ

      μ-3σ ←------ ~99.7% ------→ μ+3σ
```

This rule is extremely useful for developing intuition about spread and unusual observations.

---

# 25. Standard Normal Distribution

A particularly useful Normal distribution has:

$$
\boxed{\mu=0}
$$

and:

$$
\boxed{\sigma=1}
$$

This is called the **standard normal distribution**.

We often represent it with:

$$
Z
$$

Then:

$$
Z\sim N(0,1)
$$

The symbol:

$$
\sim
$$

means:

> "is distributed according to"

So:

$$
Z\sim N(0,1)
$$

means:

> \(Z\) follows a Normal distribution with mean 0 and standard deviation 1.

---

# 26. Why Standardization Matters

Later we'll learn:

$$
\boxed{
z=\frac{x-\mu}{\sigma}
}
$$

This tells us:

> How many standard deviations away from the mean is \(x\)?

For example:

$$
\mu=70
$$

$$
\sigma=10
$$

Suppose:

$$
x=90
$$

Then:

$$
z=\frac{90-70}{10}
$$

$$
=2
$$

So 90 is:

$$
\boxed{2\text{ standard deviations above the mean}}
$$

This idea becomes important in:

- data preprocessing
- anomaly detection
- statistics
- ML
- scientific data analysis.

---

# 27. Probability Distribution and Machine Learning

Now let's connect the concept directly to ML.

Suppose you build a model that predicts house prices.

The actual price might be affected by:

- size
- location
- number of rooms
- age
- neighborhood
- noise
- factors you haven't measured.

Instead of assuming:

$$
Y=f(X)
$$

perfectly, we often think:

$$
\boxed{Y=f(X)+\epsilon}
$$

where:

$$
\epsilon
$$

represents random variation/noise.

We can then make assumptions about the distribution of \(\epsilon\).

For example:

$$
\epsilon\sim N(0,\sigma^2)
$$

This means the noise is modeled as Normally distributed with mean zero and variance \(\sigma^2\).

This assumption appears in classical regression.

---

# 28. Classification Also Uses Distributions

Suppose:

$$
Y\in\{\text{Cat},\text{Dog}\}
$$

A model can estimate:

$$
P(Y=\text{Cat}\mid X)
$$

and:

$$
P(Y=\text{Dog}\mid X)
$$

This is a **conditional probability distribution**.

The model is essentially saying:

> Given the input \(X\), how is probability distributed across possible outputs \(Y\)?

This is a fundamental perspective on probabilistic classification.

---

# 29. Distribution of Data vs Distribution of a Variable

This distinction is important.

Suppose you collect:

$$
2,4,3,5,1
$$

Those are observed data.

The **random variable** could represent the quantity before observation.

The **distribution** describes how that variable behaves probabilistically.

Think:

```text id="y3k2t9"
Underlying process
       ↓
 Random Variable X
       ↓
 Probability Distribution
       ↓
 Possible outcomes
       ↓
 Actual observations
       ↓
      DATA
```

Statistics often works backward:

$$
\boxed{
\text{Data}
\rightarrow
\text{infer properties of distribution}
}
$$

Machine learning often does something related:

$$
\boxed{
\text{Data}
\rightarrow
\text{learn patterns}
\rightarrow
\text{predict}
}
$$

---

# 30. Distribution in Quantum Physics

This becomes particularly interesting for your physics background.

Suppose an observable \(X\) is measured.

The measurement can produce different values.

Quantum mechanics gives probabilities for those outcomes.

For a discrete measurement:

$$
P(X=x_i)
$$

For a continuous observable, such as position:

$$
P(a<X<b)
$$

The wavefunction can produce a probability density:

$$
\boxed{
p(x)=|\psi(x)|^2
}
$$

and normalization requires:

$$
\boxed{
\int_{-\infty}^{\infty}|\psi(x)|^2dx=1
}
$$

Notice the conceptual similarity:

```text
Classical probability:
PDF → area → probability

Quantum mechanics:
|ψ(x)|² → area/integral → probability
```

The mathematical interpretation has important quantum-specific details, but this is a useful bridge.

---

# 31. The Deep Connection: Σ and ∫

We previously learned:

$$
\sum
$$

for adding discrete quantities.

For continuous quantities, we encounter:

$$
\int
$$

which you can initially think of as:

> **continuous accumulation.**

So:

### Discrete

$$
\sum_i P(X=x_i)=1
$$

### Continuous

$$
\int_{-\infty}^{\infty}f(x)\,dx=1
$$

This is a beautiful mathematical connection.

```text
DISCRETE                  CONTINUOUS

Σ                          ∫
│                          │
Add individual values      Accumulate continuously
│                          │
PMF                        PDF
│                          │
Probability                Probability
```

We'll eventually need calculus to fully understand the continuous case.

---

# 32. Common Beginner Mistakes

### Mistake 1

Thinking:

> "Distribution means graph."

Not necessarily.

A graph is a **visual representation** of a distribution.

The distribution itself is the mathematical description of probability across possible values.

---

### Mistake 2

Thinking all distributions are Normal.

No.

There are many distributions:

- Bernoulli
- Binomial
- Poisson
- Uniform
- Normal
- Exponential
- and many others.

We'll learn the important ones gradually.

---

### Mistake 3

Thinking PDF value = probability.

For continuous variables:

$$
f(x)
$$

is density.

Probability comes from an interval:

$$
P(a<X<b)
$$

---

### Mistake 4

Thinking random variable means "random number generator."

Not exactly.

It is a mathematical variable representing the uncertain outcome of a random process.

---

# 🧠 The Entire Lesson in One Picture

```text id="h4a2zv"
                     RANDOM VARIABLE X
                             │
                             ↓
                  PROBABILITY DISTRIBUTION
                             │
                  ┌──────────┴──────────┐
                  │                     │
              DISCRETE              CONTINUOUS
                  │                     │
                 PMF                   PDF
                  │                     │
          P(X = x)                 Density
                  │                     │
               SUM Σ                  AREA ∫
                  │                     │
                  └──────────┬──────────┘
                             ↓
                            CDF
                       P(X ≤ x)
                             │
                             ↓
                       STATISTICS
                             │
                             ↓
                   MACHINE LEARNING
                             │
               ┌─────────────┼─────────────┐
               │             │             │
          Classification   Regression    Uncertainty
               │             │             │
        P(Y|X)          Y=f(X)+ε       Noise models
```

---

# 🎯 What You Should Know Before Moving On

Make sure these are clear:

### 1. Probability distribution

$$
\boxed{\text{Describes how probability is distributed over possible values}}
$$

### 2. PMF

For discrete variables:

$$
\boxed{P(X=x)}
$$

### 3. PDF

For continuous variables:

$$
\boxed{\text{Probability density}}
$$

Probability comes from area over an interval.

### 4. CDF

$$
\boxed{F(x)=P(X\leq x)}
$$

### 5. Normal distribution

Characterized by:

$$
\mu,\sigma
$$

where:

$$
\mu=\text{center}
$$

$$
\sigma=\text{spread}
$$

### 6. Standard Normal

$$
\boxed{Z\sim N(0,1)}
$$

---

# 📝 Practice

Try these before checking the answers.

### Q1

What is a probability distribution?

---

### Q2

A random variable represents the number of defective products in a batch.

Is it discrete or continuous?

---

### Q3

A random variable represents the temperature of a laboratory.

Is it discrete or continuous?

---

### Q4

For a discrete random variable:

$$
P(X=1)=0.2
$$

$$
P(X=2)=0.3
$$

$$
P(X=3)=0.5
$$

Is this a valid probability distribution?

Why?

---

### Q5

What does this mean?

$$
F(10)=P(X\leq10)
$$

---

### Q6

What is the difference between PMF and PDF?

---

### Q7

If:

$$
X\sim N(100,15^2)
$$

what are the mean and standard deviation?

---

### Q8

If:

$$
\mu=50,\qquad\sigma=5
$$

what is the z-score of:

$$
x=60
$$

?

---

# Answers

### Q1

A probability distribution describes how probability is spread across the possible values of a random variable.

### Q2

**Discrete**, because defective products are counted.

### Q3

**Continuous**, because temperature is measured and can take values across a continuous range.

### Q4

Yes.

Because:

$$
0.2+0.3+0.5=1
$$

and all probabilities are non-negative.

### Q5

It means:

> The probability that \(X\) is less than or equal to 10.

### Q6

**PMF** describes probabilities for discrete values.

**PDF** describes probability density for continuous variables; probabilities come from areas over intervals.

### Q7

Given:

$$
X\sim N(100,15^2)
$$

we have:

$$
\boxed{\mu=100}
$$

and:

$$
\boxed{\sigma=15}
$$

Remember: the second parameter is often written as the **variance** \(\sigma^2\), not the standard deviation.

### Q8

$$
z=\frac{x-\mu}{\sigma}
$$

$$
=\frac{60-50}{5}
$$

$$
=\boxed{2}
$$

So 60 is 2 standard deviations above the mean.

---

## 🔑 One Sentence to Remember

> **A random variable tells us what can vary; a probability distribution tells us how likely its possible values are.**

And now we have built the foundation needed for one of the most important probability distributions in ML:

$$
\boxed{\text{Bernoulli Distribution}}
$$

### Next lesson: Bernoulli Distribution → Binomial Distribution

We'll start with the simplest possible random experiment—**one yes/no trial**—and from that build:

$$
\text{Bernoulli}
\rightarrow
\text{multiple trials}
\rightarrow
\text{Binomial}
\rightarrow
\text{classification}
\rightarrow
\text{logistic regression}
$$

This will be our first major bridge from probability into actual ML.
