# Lesson 23 — Population vs Sample & Sampling

We are now entering one of the **most important ideas in statistics and machine learning**.

So far, we have been calculating things like mean, variance, covariance, and correlation. But there is a big question:

> **Where does our data come from?**

If we understand this properly, later concepts like **confidence intervals, hypothesis testing, standard error, and the Central Limit Theorem** will become much easier.

---

# 1. The Big Problem

Imagine we want to know:

> What is the average height of all university students in Pakistan?

There may be **millions of students**.

Can we measure every single student's height?

Technically possible, but extremely expensive and impractical.

Instead, we might measure 1,000 students.

Now we have two different things:

**All students** → Population

**1,000 selected students** → Sample

This is the foundation of sampling.

---

# 2. Population

A **population** is the complete group we are interested in studying.

For example:

- All university students in Pakistan
- All cars manufactured by a company
- All photons detected during an experiment
- All patients with a particular condition
- All images that a self-driving system might encounter
- All possible measurements from a physical system

Let's call population size:

$$
N
$$

So if there are 10 million students:

$$
N=10,000,000
$$

---

# 3. Sample

A **sample** is a smaller subset taken from the population.

For example:

$$
\text{Population}=10,000,000\text{ students}
$$

We select:

$$
n=1,000\text{ students}
$$

Those 1,000 students are our **sample**.

Notice the notation:

$$
N=\text{population size}
$$

$$
n=\text{sample size}
$$

Usually:

$$
n<N
$$

---

# 4. The Best Analogy: Ocean and Cup of Water 🌊🥤

Imagine there is a huge ocean.

You want to know:

> "Is this water salty?"

You don't need to drink the entire ocean.

You take one cup:

🌊 **Ocean** → Population

🥤 **Cup of water** → Sample

You analyze the cup and use that information to understand the ocean.

But there is an important condition:

> **The cup should reasonably represent the ocean.**

If you somehow take water from a freshwater river flowing into the ocean, your conclusion may be wrong.

This is exactly what **sampling bias** can do.

---

# 5. Population Parameter vs Sample Statistic

This distinction is extremely important.

Suppose the true average height of **every student** in the population is:

$$
\mu=170\text{ cm}
$$

Here:

$$
\mu
$$

is the **population mean**.

It is called a **parameter**.

---

Now suppose we randomly select 1,000 students and calculate:

$$
\bar{x}=169.7\text{ cm}
$$

This is the **sample mean**.

It is called a **statistic**.

So:

| Population            | Sample           |
| --------------------- | ---------------- |
| Entire group          | Subset           |
| Size \(N\)            | Size \(n\)       |
| Mean \(\mu\)          | Mean \(\bar{x}\) |
| Variance \(\sigma^2\) | Variance \(s^2\) |
| Parameter             | Statistic        |

### Remember:

> **Parameter describes the population.**
> **Statistic describes the sample.**

---

# 6. Why Do We Care About the Sample?

Because usually:

$$
\mu
$$

is unknown.

We want to know it.

But we can't measure the entire population.

So we collect a sample and calculate:

$$
\bar{x}
$$

Then use:

$$
\bar{x}\approx\mu
$$

The sample statistic becomes an **estimate** of the population parameter.

This is one of the central ideas of statistics:

$$
\boxed{\text{Sample data}\rightarrow\text{Estimate population properties}}
$$

---

# 7. Example

Suppose the actual population is:

$$
[10,20,30,40,50,60,70,80,90,100]
$$

The population mean is:

$$
\mu=
\frac{10+20+30+40+50+60+70+80+90+100}{10}
$$

Therefore:

$$
\mu=55
$$

Now suppose we don't have access to all 10 values.

We randomly select:

$$
[20,40,60,80,100]
$$

Our sample mean is:

$$
\bar{x}
=
\frac{20+40+60+80+100}{5}
$$

$$
\bar{x}=60
$$

Our estimate is:

$$
\bar{x}=60
$$

while the true population mean is:

$$
\mu=55
$$

The estimate isn't exact.

And that's okay.

Statistics is largely about understanding:

> **How reliable is our estimate?**

---

# 8. Different Samples Give Different Answers

This is a VERY important realization.

Suppose we take another sample:

$$
[10,30,50,70,90]
$$

Then:

$$
\bar{x}=50
$$

Another sample:

$$
[20,30,60,70,100]
$$

gives:

$$
\bar{x}=56
$$

So:

$$
\bar{x}_1=60
$$

$$
\bar{x}_2=50
$$

$$
\bar{x}_3=56
$$

etc.

Why?

Because every sample contains different observations.

Therefore:

> **The sample mean is not always the same.**

This leads us to one of the most important concepts coming later:

# Sampling Distribution

---

# 9. Sampling Distribution — First Intuition

Imagine repeatedly taking samples of size 100.

For example:

```text
Population
    ↓
Sample 1 → mean = 51.2
Sample 2 → mean = 49.8
Sample 3 → mean = 50.4
Sample 4 → mean = 50.1
Sample 5 → mean = 51.0
Sample 6 → mean = 49.7
...
```

Now instead of looking at individual observations, we look at the **means of the samples**.

Those means themselves form a distribution.

That's the:

$$
\boxed{\text{Sampling distribution of the sample mean}}
$$

We'll study this deeply later.

---

# 10. Population Mean

For the entire population:

$$
\boxed{
\mu=\frac{1}{N}\sum_{i=1}^{N}x_i
}
$$

Where:

- \(\mu\) = population mean
- \(N\) = population size
- \(x_i\) = \(i\)-th population observation
- \(\sum\) = add all observations

---

# 11. Sample Mean

For a sample:

$$
\boxed{
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i
}
$$

Where:

- \(\bar{x}\) = sample mean
- \(n\) = sample size
- \(x_i\) = \(i\)-th sample observation

Compare:

$$
\mu=\frac1N\sum_{i=1}^{N}x_i
$$

versus

$$
\bar{x}=\frac1n\sum_{i=1}^{n}x_i
$$

Very similar formula.

The difference is **what group we're averaging**.

---

# 12. Population Variance vs Sample Variance

Remember variance?

Population variance:

$$
\boxed{
\sigma^2=
\frac1N
\sum_{i=1}^{N}(x_i-\mu)^2
}
$$

For a sample, we usually calculate:

$$
\boxed{
s^2=
\frac1{n-1}
\sum_{i=1}^{n}(x_i-\bar{x})^2
}
$$

Notice something strange:

Why:

$$
n-1
$$

instead of:

$$
n?
$$

This is extremely important.

---

# 13. Why \(n-1\)?

Let's build intuition rather than memorizing it.

Suppose we have three observations:

$$
x_1,x_2,x_3
$$

And suppose their sample mean is already known:

$$
\bar{x}=10
$$

Imagine we know:

$$
x_1=8
$$

$$
x_2=12
$$

Can \(x_3\) be anything?

No.

Because:

$$
\frac{8+12+x_3}{3}=10
$$

Therefore:

$$
20+x_3=30
$$

$$
x_3=10
$$

The third value is **forced**.

So after calculating the mean, only **two values were free to vary**.

That's:

$$
3-1=2
$$

This is called a **degree of freedom**.

For \(n\) observations, once we use the data to estimate the mean, we effectively have:

$$
\boxed{n-1}
$$

degrees of freedom.

---

# 14. Why Does This Matter?

If we divide the sample squared deviations by \(n\), we tend to underestimate the population variance.

Why?

Because the sample mean:

$$
\bar{x}
$$

was calculated from the same data.

The deviations from \(\bar{x}\) are therefore slightly constrained.

Using:

$$
n-1
$$

corrects this systematic tendency.

So:

$$
\boxed{
s^2=
\frac{\sum(x_i-\bar{x})^2}{n-1}
}
$$

is the usual **unbiased estimator of population variance** under the standard random-sampling assumptions.

For now, the mental model is:

> **We "spent" one degree of freedom estimating the mean.**

---

# 15. Sample Standard Deviation

Once we have sample variance:

$$
s^2
$$

sample standard deviation is:

$$
\boxed{s=\sqrt{s^2}}
$$

So:

```text
Sample
   ↓
Sample mean
   ↓
Sample variance
   ↓
Sample standard deviation
```

---

# 16. Random Sampling

Now comes another critical idea.

Suppose we have 100,000 students.

We need a sample of 1,000.

One approach is **random sampling**.

Every individual should have a reasonable, known chance of being selected according to the sampling design.

Why?

Because we want our sample to represent the population rather than deliberately selecting convenient observations.

---

# 17. Sampling Bias

Suppose you want to know:

> "What is the average daily study time of university students?"

But you only survey students inside a library.

You might get:

```text
Library students
→ studying a lot
→ likely higher study hours
```

Your sample could systematically differ from the population.

That's **sampling bias**.

### Another example

Suppose you want to estimate smartphone usage.

You survey only people attending a technology conference.

Again, your sample may not represent everyone.

---

# 18. Representative Sample

A sample is useful when it captures important characteristics of the population.

Think:

```text
Population
████████████████████

Good sample
████████

Bad sample
████████
       ↑
only one unusual region
```

The goal isn't necessarily to make the sample numerically identical to the population.

The goal is to avoid systematic distortions that make the sample unrepresentative.

---

# 19. Sample Size Matters

Imagine estimating the average height using:

$$
n=5
$$

versus:

$$
n=5,000
$$

Generally, larger samples provide more information.

For the sample mean, under standard independent sampling assumptions:

$$
SE(\bar X)=\frac{\sigma}{\sqrt n}
$$

This is called the **standard error**.

Don't worry about deriving it yet.

Just notice:

$$
n\uparrow
$$

means:

$$
\sqrt n\uparrow
$$

therefore:

$$
SE\downarrow
$$

So larger samples generally make the sample mean more stable.

---

# 20. A Beautiful Physical Analogy

Imagine measuring a quantum experiment.

Suppose a theoretical observable has expectation value:

$$
\langle A\rangle
$$

But experimentally, you don't get \(\langle A\rangle\) directly.

You perform measurements:

$$
A_1,A_2,A_3,\ldots,A_n
$$

Then calculate:

$$
\bar A=
\frac1n\sum_{i=1}^{n}A_i
$$

As the number of measurements increases, under appropriate conditions:

$$
\bar A\rightarrow\langle A\rangle
$$

So:

**Theoretical quantity**

$$
\langle A\rangle
$$

↓

**Repeated experimental measurements**

$$
A_1,A_2,\ldots,A_n
$$

↓

**Experimental estimate**

$$
\bar A
$$

This is exactly the population/sample idea.

---

# 21. Machine Learning Connection 🤖

Sampling is everywhere in ML.

Suppose the real-world population is:

> **All images that could ever be encountered by your autonomous driving system.**

You cannot collect every possible image.

Instead:

$$
\text{Real-world population}
$$

↓

$$
\text{Collected dataset}
$$

↓

$$
\text{Training sample}
$$

Your model learns from the sample and is expected to perform on previously unseen data.

This is one reason **dataset quality and representativeness** matter so much.

---

# 22. Train/Test Split

Suppose you have:

$$
100,000
$$

images.

You might split them into:

$$
80,000
$$

training examples and:

$$
20,000
$$

test examples.

Conceptually:

```text
Collected data
      │
      ├── Training data
      │
      └── Test data
```

The test set is intended to provide evidence about performance on unseen examples.

But remember:

> A test set is not automatically representative just because it is large.

If the training/test data come from a biased collection process, both can inherit that bias.

---

# 23. Scientific Computing Connection

Suppose your detector records photon arrival times:

$$
\tau_1,\tau_2,\tau_3,\ldots,\tau_n
$$

You want to estimate the underlying average waiting time:

$$
E[\tau]
$$

Your experimental estimate is:

$$
\bar{\tau}
=
\frac1n
\sum_{i=1}^{n}\tau_i
$$

As you collect more observations, your estimate generally becomes more stable.

This is fundamental in experimental physics.

---

# 24. NumPy Preview

We haven't formally entered the NumPy implementation stage yet, but you should recognize the connection.

```python
import numpy as np

sample = np.array([10, 20, 30, 40, 50])

mean = np.mean(sample)

variance = np.var(sample, ddof=1)

std = np.std(sample, ddof=1)
```

The important detail is:

```python
ddof=1
```

which corresponds to the \(n-1\) denominator for the usual sample variance/standard deviation.

We'll properly study NumPy later.

---

# 25. The Most Important Mental Model

Keep this picture in your head:

```text
                REAL WORLD
                    │
                    ▼
               POPULATION
                    │
             impossible to
             observe entirely
                    │
                    ▼
                 SAMPLE
                    │
                    ▼
              STATISTICS
          ┌─────────┼─────────┐
          ▼         ▼         ▼
        mean     variance  correlation
          │
          ▼
       ESTIMATE
          │
          ▼
   POPULATION PARAMETER
```

For example:

$$
\boxed{
\bar{x}\rightarrow\mu
}
$$

$$
\boxed{
s^2\rightarrow\sigma^2
}
$$

$$
\boxed{
s\rightarrow\sigma
}
$$

The arrow means **estimate**, not necessarily exact equality.

---

# 26. Parameter vs Statistic — Memorize This

### Population

$$
\mu,\quad\sigma^2,\quad\sigma
$$

are parameters.

### Sample

$$
\bar{x},\quad s^2,\quad s
$$

are statistics.

A very useful memory trick:

> **Greek letters often represent population quantities.**
>
> **Latin symbols often represent sample quantities.**

This is a common convention, not an absolute law.

---

# 27. Quick Practice 🧠

### Q1

A university has 50,000 students. You select 500 students.

What is:

- Population?
- Sample?
- \(N\)?
- \(n\)?

---

### Q2

The true average height of all students is:

$$
\mu=171\text{ cm}
$$

A sample gives:

$$
\bar{x}=170.5\text{ cm}
$$

Which is the parameter?

Which is the statistic?

---

### Q3

Why is sample variance normally calculated using:

$$
n-1
$$

instead of:

$$
n?
$$

---

### Q4

You want to estimate the average salary of workers in a city, but you survey only people entering an expensive shopping mall.

What potential problem exists?

---

### Q5

You perform 100 photon measurements and calculate:

$$
\bar{x}
$$

Then perform 10,000 measurements and calculate another:

$$
\bar{x}
$$

Which estimate would generally be expected to have less sampling variability, assuming comparable independent sampling conditions?

---

# Answers

**Q1**

Population:

$$
50,000\text{ students}
$$

Sample:

$$
500\text{ students}
$$

$$
N=50,000,\qquad n=500
$$

**Q2**

Population parameter:

$$
\mu=171
$$

Sample statistic:

$$
\bar{x}=170.5
$$

**Q3**

Because estimating the sample mean uses one degree of freedom, and dividing by \(n-1\) gives the usual unbiased estimator of population variance.

**Q4**

Potential **sampling bias**. People entering that particular mall may not represent the city's workers.

**Q5**

Generally the estimate based on 10,000 measurements, because larger sample sizes tend to reduce sampling variability.

---

# 🔑 Final Mental Picture

Don't memorize this lesson as isolated definitions.

Think:

> **Population = the whole ocean.**
>
> **Sample = the cup we take from it.**
>
> **Parameter = what is actually true about the ocean.**
>
> **Statistic = what we calculate from the cup.**
>
> **Inference = using the cup to learn about the ocean.**

And this creates the next major question:

> **If different samples produce different statistics, how exactly do those statistics behave?**

That takes us to **Sampling Methods → Sampling Distribution → Standard Error → Central Limit Theorem (CLT)**.
