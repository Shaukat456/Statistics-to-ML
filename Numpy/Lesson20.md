# Lesson 20 — Distribution Shape & Skewness

We have learned how to describe data using:

- Mean
- Median
- Mode
- Range
- Variance
- Standard deviation
- Percentiles
- Quartiles
- IQR
- Outlier detection

But there's still a major question:

> **What does the overall shape of the data look like?**

This is extremely important in **statistics, EDA, ML, and scientific computing**.

---

# 1. What Is a Distribution?

A **distribution** tells us how values are spread across their possible range.

Imagine measuring the heights of 1,000 people.

You don't just have:

```text
170
165
181
...
```

You can ask:

> How many people have heights around 160?

> How many around 170?

> How many around 180?

> Are most values concentrated somewhere?

That's the **distribution**.

A histogram is one common way to visualize it.

---

# 2. The Mountain Analogy 🏔️

Imagine that your data is a landscape.

```text
Frequency
   │
   │             /\
   │            /  \
   │           /    \
   │          /      \
   │_________/________\________
             Values →
```

The height of the mountain represents:

> **How many observations occur around that region.**

High mountain:

$$
\Rightarrow
$$

many observations.

Low region:

$$
\Rightarrow
$$

few observations.

So a distribution's **shape** tells us how the observations are arranged.

---

# 3. Histogram

Suppose we have exam scores.

A histogram groups values into ranges called **bins**.

For example:

```text
Score       Number of students

0–10       █
10–20      ██
20–30      ███
30–40      █████
40–50      ███████
50–60      █████████
60–70      ███████
70–80      ████
80–90      ██
90–100     █
```

The overall pattern gives us the distribution shape.

---

# 4. Why Does Shape Matter?

Consider these two datasets:

### Dataset A

```text
10 20 30 40 50 60 70 80 90
```

The values are spread fairly evenly.

### Dataset B

```text
10 10 10 10 10 10 20 50 100
```

The values are concentrated heavily toward the low end.

These datasets behave differently statistically.

Their:

- means
- medians
- variance
- percentiles
- outliers

can all behave differently.

So before applying statistical methods, it is useful to understand the **shape of the distribution**.

---

# 5. The Most Important Shapes

We'll focus on:

1. Symmetric
2. Right-skewed
3. Left-skewed
4. Uniform
5. Bimodal / multimodal

Let's start with the most important one.

---

# 6. Symmetric Distribution

A distribution is approximately **symmetric** when its left and right sides have similar shapes.

Imagine folding the graph in half.

```text
             /\
            /  \
           /    \
          /      \
_________/________\_________
              │
             center
```

The left side roughly mirrors the right side.

---

# 7. Normal Distribution

The most famous symmetric distribution is the:

$$
\boxed{\text{Normal distribution}}
$$

also called the:

$$
\boxed{\text{Gaussian distribution}}
$$

It looks approximately like:

```text
                 /\
               /    \
             /        \
           /            \
_________/________________\_________
```

It is extremely important in statistics, physics, measurement science, and ML.

---

# 8. Mean, Median and Mode in a Symmetric Distribution

For an ideal symmetric unimodal distribution:

$$
\boxed{\text{Mean}\approx\text{Median}\approx\text{Mode}}
$$

For a perfectly symmetric normal distribution:

$$
\boxed{\mu=\text{median}=\text{mode}}
$$

where:

$$
\mu
$$

means the population mean.

This gives us an important clue about distribution shape.

---

# 9. Right-Skewed Distribution

Now imagine most values are relatively small, but a few values extend far toward the right.

```text
Frequency
   │
   │       /\
   │      /  \
   │     /    \
   │____/      \________________
   │
   └────────────────────────────→
                         long right tail
```

This is called:

$$
\boxed{\text{Right-skewed}}
$$

or:

$$
\boxed{\text{Positively skewed}}
$$

Why "right"?

Because the long tail extends toward the **right**.

---

# 10. Example: Income

Consider incomes:

$$
[20k,22k,24k,25k,27k,30k,35k,40k,500k]
$$

Most people are clustered around:

$$
20k-40k
$$

but one extremely high income extends far to the right.

Therefore the distribution is strongly right-skewed.

This is common with:

- income
- wealth
- house prices
- transaction amounts
- response times.

---

# 11. What Happens to the Mean?

Remember:

> The mean is sensitive to extreme values.

Suppose:

$$
[10,11,12,13,14,100]
$$

The large value `100` pulls the mean toward the right.

The median is much less affected.

So in a typical right-skewed distribution:

$$
\boxed{\text{Mean}>\text{Median}}
$$

and often:

$$
\text{Median}>\text{Mode}
$$

So the common pattern is:

$$
\boxed{\text{Mode}<\text{Median}<\text{Mean}}
$$

This is a useful rule of thumb, not an absolute law for every dataset.

---

# 12. The "Rope Pull" Analogy

Imagine three people representing the mean, median and mode.

The distribution has a very long tail on the right.

```text
Mode      Median                 Mean
 ●----------●---------------------●
                              →
                         long tail
```

The extreme values on the right are like people pulling a rope.

The **mean gets pulled toward the extreme values**.

The median doesn't move nearly as much.

That's why:

> **Right-skew → mean tends to be pulled right.**

---

# 13. Left-Skewed Distribution

Now reverse the situation.

Most observations are high, but a few very small values create a long tail toward the left.

```text
Frequency
   │
   │                         /\
   │                        /  \
   │                       /    \
___│______________________/      \____
   │
   └────────────────────────────────→
      long left tail
```

This is:

$$
\boxed{\text{Left-skewed}}
$$

also called:

$$
\boxed{\text{Negatively skewed}}
$$

---

# 14. Example: An Easy Exam

Imagine an exam where almost everyone scores very highly:

$$
[70,80,85,88,90,92,94,95,20]
$$

Most values are high.

But one very low score creates a long left tail.

Therefore:

> The distribution is left-skewed.

The low extreme value pulls the mean toward the left.

Typically:

$$
\boxed{\text{Mean}<\text{Median}}
$$

and often:

$$
\boxed{\text{Mean}<\text{Median}<\text{Mode}}
$$

Again, treat these as common patterns rather than universal rules.

---

# 15. The Easiest Way to Remember Skewness

Forget the complicated terminology for a moment.

Look at the **tail**.

### Tail goes right:

$$
\boxed{\text{Right-skewed}}
$$

### Tail goes left:

$$
\boxed{\text{Left-skewed}}
$$

The direction is determined by the **tail**, not where the peak is.

```text
Right skew:

       /\
      /  \________________
     /
----|--------------------→
                 RIGHT TAIL


Left skew:

________________/\
               /  \
--------------/----\------→
← LEFT TAIL
```

---

# 16. Don't Make This Common Mistake

People sometimes think:

> "The peak is on the left, so it's left-skewed."

❌ Not necessarily.

Look at the **tail**.

If the tail extends to the right:

$$
\boxed{\text{Right-skewed}}
$$

regardless of where the peak is.

---

# 17. Uniform Distribution

Now consider a completely different shape.

Suppose values are approximately equally likely:

```text
Frequency
   │
   │ █ █ █ █ █ █ █ █
   │ █ █ █ █ █ █ █ █
   │ █ █ █ █ █ █ █ █
   └────────────────────→
```

This resembles a rectangle.

This is a:

$$
\boxed{\text{Uniform distribution}}
$$

In a continuous uniform distribution:

$$
X\sim U(a,b)
$$

where:

- \(a\) = lower bound
- \(b\) = upper bound.

Every value within the interval has equal density.

---

# 18. Bimodal Distribution

Now imagine you have **two peaks**.

```text
Frequency
   │
   │       /\             /\
   │      /  \           /  \
   │     /    \         /    \
___│____/______\_______/______\____
   └──────────────────────────────→
```

This is called:

$$
\boxed{\text{Bimodal}}
$$

because:

> **Bi = two**

> **Modal = modes/peaks**

So there are two prominent modes.

---

# 19. Why Could Two Peaks Exist?

Suppose we measure heights of:

- children
- adults

and combine them into one dataset.

We might get two groups:

```text
Children                    Adults
    /\                         /\
   /  \                       /  \
__/    \_____________________/    \__
```

The two peaks may indicate that the dataset contains **different subpopulations**.

This is extremely useful during EDA.

A bimodal distribution can make you ask:

> "Are these actually two different groups mixed together?"

---

# 20. Multimodal Distribution

If there are more than two prominent peaks:

$$
\boxed{\text{Multimodal}}
$$

For example:

```text
      /\       /\          /\
     /  \     /  \        /  \
____/    \___/    \______/    \____
```

This might indicate several subgroups.

---

# 21. Why Distribution Shape Matters in ML

Imagine you're analyzing a feature:

$$
X=\text{Salary}
$$

You calculate:

$$
\text{Mean}=80,000
$$

But if the distribution is heavily right-skewed, the mean might not represent the "typical" person very well.

The median might be more informative.

This affects:

- feature analysis
- preprocessing
- transformations
- outlier analysis
- model assumptions
- interpretation.

---

# 22. Skewed Features and Log Transformation

Suppose a feature looks like:

```text
Most values: small
Few values: enormous
```

That's common with things like:

- income
- population
- transaction value
- website traffic.

A common transformation is:

$$
x'=\log(x)
$$

This compresses very large values.

For example:

$$
10\rightarrow\log(10)
$$

$$
100\rightarrow\log(100)
$$

$$
1000\rightarrow\log(1000)
$$

The distances between large values become compressed.

Conceptually:

```text
Original:

10 ---- 100 ----------- 1000 -------------------- 10000


After log:

1 ---- 2 ---- 3 ---- 4
```

This can make a highly skewed feature easier to analyze or model.

We will study transformations properly later.

---

# 23. Why This Matters for Neural Networks

Many ML algorithms work better when numerical features are represented on sensible scales.

Suppose one feature has:

$$
1,2,3,4,5
$$

while another has:

$$
1,000,000
$$

Understanding the distribution helps us decide whether transformations or scaling might be appropriate.

Later you'll learn:

$$
z=\frac{x-\mu}{\sigma}
$$

for standardization.

But remember:

> **Standardization changes scale; it does not automatically remove skewness.**

This distinction is important.

---

# 24. Distribution Shape and Probability

Earlier we learned:

$$
P(X=x)
$$

for discrete variables and:

$$
f(x)
$$

for continuous distributions.

Now we're looking at the **shape** of those probabilities/densities.

For example, a normal distribution:

$$
X\sim N(\mu,\sigma^2)
$$

has a bell-shaped distribution.

Here:

$$
\mu
$$

controls the center, while:

$$
\sigma
$$

controls the spread.

---

# 25. Normal Distribution — Deeper Connection

A normal distribution is written:

$$
\boxed{X\sim N(\mu,\sigma^2)}
$$

where:

- \(X\) = random variable
- \(N\) = normal distribution
- \(\mu\) = mean
- \(\sigma^2\) = variance.

Its probability density function is:

$$
f(x)=
\frac{1}{\sigma\sqrt{2\pi}}
e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$

Don't worry about memorizing this yet.

The important thing is to recognize the ingredients:

$$
e
$$

$$
(x-\mu)^2
$$

$$
\sigma^2
$$

These connect directly to concepts you've already learned:

- exponentials
- squares
- mean
- variance.

---

# 26. The 68–95–99.7 Rule

For a normal distribution:

Approximately:

$$
68\%
$$

of observations lie within:

$$
\mu\pm\sigma
$$

Approximately:

$$
95\%
$$

lie within:

$$
\mu\pm2\sigma
$$

Approximately:

$$
99.7\%
$$

lie within:

$$
\mu\pm3\sigma
$$

Visualize:

```text
             68%
          |-------|
       95%|-------|95%
     99.7%|-------|99.7%
-----------|---μ---|-----------
         -σ       +σ
```

We'll eventually use this for probability and standardization.

---

# 27. Scientific / Physics Example

Suppose a detector measures noise around:

$$
\mu=0
$$

with:

$$
\sigma=2
$$

If the noise is approximately Gaussian:

$$
X\sim N(0,4)
$$

then approximately 68% of measurements fall within:

$$
[-2,2]
$$

and approximately 95% within:

$$
[-4,4].
$$

This is why Gaussian distributions appear so frequently in measurement and experimental science.

---

# 28. Quantum / Experimental Connection

In experimental quantum physics, repeated measurements can generate distributions of measured quantities.

For example:

$$
x_1,x_2,\ldots,x_n
$$

could represent repeated measurements of an observable.

You might examine:

- mean
- variance
- histogram
- skewness
- tails
- outliers
- multimodality.

In quantum mechanics, a probability distribution can arise from:

$$
p(x)=|\psi(x)|^2
$$

for position measurement.

So the distribution shape is not just an ML concept—it is fundamental to experimental physics.

---

# 29. Important: Distribution vs Histogram

These are related but not identical.

### Distribution

The underlying statistical behavior/probability structure.

### Histogram

A visualization made from observed data.

Think:

> **Distribution = the underlying story.**

> **Histogram = a picture we create from our observations to inspect that story.**

A histogram is therefore an estimate/visual representation of the distribution, and its appearance can depend on choices such as bin width.

---

# 30. Distribution Shape Cheat Sheet

| Shape        | Main characteristic                                   |
| ------------ | ----------------------------------------------------- |
| Symmetric    | Left and right sides roughly similar                  |
| Normal       | Symmetric bell shape                                  |
| Right-skewed | Long tail toward larger values                        |
| Left-skewed  | Long tail toward smaller values                       |
| Uniform      | Values roughly equally distributed across an interval |
| Bimodal      | Two prominent peaks                                   |
| Multimodal   | Multiple prominent peaks                              |

---

# 31. The Most Important Relationships

For a typical right-skewed distribution:

$$
\boxed{\text{Mean}>\text{Median}}
$$

For a typical left-skewed distribution:

$$
\boxed{\text{Mean}<\text{Median}}
$$

For a symmetric unimodal distribution:

$$
\boxed{\text{Mean}\approx\text{Median}\approx\text{Mode}}
$$

Again:

> These are useful patterns, not mathematical guarantees for every dataset.

---

# 32. Your EDA Mental Model

When you receive a new numerical feature, don't immediately train a model.

Ask:

### Step 1 — Where is the center?

$$
\text{Mean, Median}
$$

### Step 2 — How spread out is it?

$$
\text{Range, Variance, SD, IQR}
$$

### Step 3 — Where are values positioned?

$$
\text{Percentiles, Quartiles}
$$

### Step 4 — What does the shape look like?

$$
\text{Symmetric? Skewed? Bimodal?}
$$

### Step 5 — Are there unusual observations?

$$
\text{Outliers}
$$

This is the beginning of **Exploratory Data Analysis**.

---

# 33. A Powerful EDA Checklist

For any numerical feature:

```text id="q7h8pd"
                FEATURE
                   │
                   ▼
             ┌───────────┐
             │   CENTER  │
             │ Mean/Med. │
             └─────┬─────┘
                   ↓
             ┌───────────┐
             │   SPREAD  │
             │ SD / IQR  │
             └─────┬─────┘
                   ↓
             ┌───────────┐
             │ POSITION  │
             │ Percentile│
             └─────┬─────┘
                   ↓
             ┌───────────┐
             │   SHAPE   │
             │ Skew/etc. │
             └─────┬─────┘
                   ↓
             ┌───────────┐
             │ OUTLIERS  │
             └───────────┘
```

You are building a statistical "X-ray vision" for data.

---

# 34. Practice

Try these yourself.

### Q1

What determines whether a distribution is right-skewed or left-skewed?

---

### Q2

If a distribution has a long tail toward large values, is it left-skewed or right-skewed?

---

### Q3

In a typical right-skewed distribution, which is generally larger?

$$
\text{Mean or Median?}
$$

---

### Q4

In a typical left-skewed distribution, which is generally smaller?

$$
\text{Mean or Median?}
$$

---

### Q5

What is the approximate relationship between mean, median and mode in a symmetric unimodal distribution?

---

### Q6

What does "bimodal" mean?

---

### Q7

Why might salary data be right-skewed?

---

### Q8

Why can a histogram be useful during EDA?

---

### Q9

Suppose measurements are:

$$
[1,2,2,2,3,3,3,20]
$$

Would you expect the distribution to be approximately symmetric or right-skewed?

---

### Q10

True or false:

> If a point is an outlier, it must be removed.

---

# Answers

### Q1

The direction of the **tail**.

### Q2

$$
\boxed{\text{Right-skewed}}
$$

### Q3

Typically:

$$
\boxed{\text{Mean}>\text{Median}}
$$

### Q4

Typically:

$$
\boxed{\text{Mean}<\text{Median}}
$$

### Q5

Approximately:

$$
\boxed{\text{Mean}\approx\text{Median}\approx\text{Mode}}
$$

### Q6

A distribution with two prominent peaks.

### Q7

Most people may have relatively moderate incomes while a smaller number of people have extremely high incomes, creating a long right tail.

### Q8

It provides a visual representation of how observed values are distributed and can reveal shape, skewness, concentration, and possible unusual values.

### Q9

Likely:

$$
\boxed{\text{Right-skewed}}
$$

because `20` creates a long right tail.

### Q10

**False.**

An outlier should generally be investigated before deciding how to handle it.

---

# 🧠 Final Mental Model

Imagine your dataset as a landscape:

```text
                 DISTRIBUTION
                      │
          ┌───────────┼───────────┐
          ↓           ↓           ↓
       CENTER       SPREAD       SHAPE
          │           │           │
       Mean/Med.   SD/IQR      Symmetry
                                  │
                         ┌────────┼────────┐
                         ↓        ↓        ↓
                       Normal   Right    Left
                                skew     skew
                                  │
                                  ↓
                              OUTLIERS
```

And remember the simplest rule:

> **Look at the tail, not the peak.**

Right tail → **right-skewed**

Left tail → **left-skewed**

---

## Where We Are

You now have a solid foundation for **univariate statistics**:

$$
\boxed{
\text{Data}
\rightarrow
\text{Probability}
\rightarrow
\text{Random Variables}
\rightarrow
\text{Distributions}
\rightarrow
\text{Center}
\rightarrow
\text{Spread}
\rightarrow
\text{Percentiles}
\rightarrow
\text{IQR}
\rightarrow
\text{Distribution Shape}
}
$$

The next major concept is **Correlation**.

We'll build it from zero:

> **"When one variable changes, does another variable tend to change with it?"**

We'll first understand this visually and intuitively, then mathematically derive the idea, and finally connect it to **NumPy and ML feature analysis**.
