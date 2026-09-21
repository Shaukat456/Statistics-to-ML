# Lesson 18 — Percentiles & Quartiles

We now move from **mean, median, mode, and range** to a very important question:

> **“Where does a particular value stand compared with the rest of the data?”**

This is exactly what **percentiles** help us answer.

---

# 1. Why Do We Need Percentiles?

Suppose we have exam scores:

$$
[40,50,55,60,65,70,75,80,90,95]
$$

We can calculate:

- Mean
- Median
- Range

But suppose I tell you:

> “Ali scored 80.”

You might ask:

**Is 80 a good score?**

The number `80` alone doesn't tell us much.

But if I say:

> **80 is at the 80th percentile**

now we have context.

It means approximately:

> **80% of the observations are at or below that value.**

So percentiles answer:

> **“How does this value compare with the rest of the data?”**

---

# 2. First: Sort the Data

Percentiles are based on **position**.

Therefore, we usually start by sorting the data.

For example:

$$
[70,40,90,20,60]
$$

Sort it:

$$
[20,40,60,70,90]
$$

Now we know the relative positions.

Think of students standing in a line from lowest score to highest score:

```text
Lowest                              Highest
  ↓                                    ↓

20 → 40 → 60 → 70 → 90
```

Percentiles tell us **where we are in this line**.

---

# 3. What Is a Percentile?

A **percentile** is a value that tells us the position of an observation within a dataset.

For example:

### 90th percentile

The 90th percentile is a value such that approximately:

$$
90\%
$$

of observations are at or below it.

Similarly:

### 25th percentile

Approximately:

$$
25\%
$$

of observations are at or below it.

### 50th percentile

Approximately:

$$
50\%
$$

of observations are at or below it.

---

# 4. The Most Important Mental Model

Imagine **100 students standing in order from lowest score to highest score**.

```text
0%                                      100%
|-----------------------------------------|
Lowest                                  Highest
```

Now:

### 25th percentile

You're around:

```text
|---------●-------------------------------|
         25%
```

### 50th percentile

```text
|----------------●------------------------|
                 50%
```

### 75th percentile

```text
|--------------------------●--------------|
                           75%
```

### 90th percentile

```text
|------------------------------------●----|
                                     90%
```

So:

> **Percentile = position in the ordered population of data.**

---

# 5. Percentile Is NOT Percentage

This is extremely important.

These two words sound similar but mean different things.

### Percentage

Describes a **proportion of something**.

Example:

You answered 80 out of 100 questions correctly:

$$
\frac{80}{100}\times100=80\%
$$

Your accuracy is **80%**.

---

### Percentile

Describes **position relative to other observations**.

Suppose your score is at the 80th percentile.

That means:

> Your score is higher than or equal to approximately 80% of the observations.

You did **not necessarily score 80%**.

You could have scored 65%, but if most people scored lower, 65% could be the 80th percentile.

### Remember:

> **Percentage = how much you have.**

> **Percentile = where you stand.**

---

# 6. The 50th Percentile

This one is extremely important.

The:

$$
50^{th}\text{ percentile}
$$

is the **median**.

So:

$$
\boxed{P_{50}=\text{Median}}
$$

Why?

Because the median divides ordered data into two halves.

```text
50%                    50%
|----------------------|-------------------|
                      ↑
                    Median
```

Therefore:

> **Median = 50th percentile.**

---

# 7. Let's Use a Simple Dataset

Consider:

$$
X=[10,20,30,40,50,60,70,80,90,100]
$$

There are:

$$
n=10
$$

observations.

They are already sorted.

Think of them as 10 people standing in increasing order.

```text
10   20   30   40   50   60   70   80   90   100
↑                         ↑
low                       middle
```

---

# 8. The 50th Percentile

The 50th percentile is the median.

There are 10 observations, so the middle lies between:

$$
50
$$

and

$$
60
$$

Therefore:

$$
P_{50}=\frac{50+60}{2}=55
$$

So:

$$
\boxed{P_{50}=55}
$$

---

# 9. What Are Quartiles?

Now we divide the data into **four parts**.

That's where the word **quartile** comes from.

> **Quart = four**

So quartiles divide ordered data into roughly four sections.

There are three important quartiles:

| Quartile | Percentile | Meaning       |
| -------- | ---------: | ------------- |
| \(Q_1\)  |       25th | First quarter |
| \(Q_2\)  |       50th | Middle        |
| \(Q_3\)  |       75th | Third quarter |

Therefore:

$$
\boxed{Q_1=P_{25}}
$$

$$
\boxed{Q_2=P_{50}=\text{Median}}
$$

$$
\boxed{Q_3=P_{75}}
$$

---

# 10. Visualize the Quartiles

Imagine a road:

```text
0%             25%             50%             75%             100%
|---------------|---------------|---------------|----------------|
                ↑               ↑               ↑
               Q1              Q2              Q3
```

The three points divide the data into approximately four sections.

```text
     25%          25%          25%          25%
|------------|------------|------------|------------|
             Q1           Q2           Q3
```

This is the foundation of the **box plot**, which we'll encounter later.

---

# 11. Let's Find Quartiles Intuitively

Use:

$$
X=[10,20,30,40,50,60,70,80,90,100]
$$

The middle is:

$$
Q_2=55
$$

Now look at the lower half:

$$
[10,20,30,40,50]
$$

Its median is:

$$
Q_1=30
$$

The upper half:

$$
[60,70,80,90,100]
$$

Its median is:

$$
Q_3=80
$$

Therefore:

$$
\boxed{Q_1=30}
$$

$$
\boxed{Q_2=55}
$$

$$
\boxed{Q_3=80}
$$

---

# 12. What Does Q1 Actually Mean?

Suppose:

$$
Q_1=30
$$

This means approximately:

> **25% of observations are at or below 30.**

Similarly, if:

$$
Q_2=55
$$

then approximately:

> **50% of observations are at or below 55.**

And:

$$
Q_3=80
$$

means:

> **75% of observations are at or below 80.**

---

# 13. A Real-World Example: Salaries

Suppose we collect salaries from a company.

Imagine:

$$
Q_1=40,000
$$

$$
Q_2=55,000
$$

$$
Q_3=80,000
$$

Interpretation:

### \(Q_1=40,000\)

Approximately 25% of employees earn:

$$
\le \$40,000
$$

### \(Q_2=55,000\)

Approximately 50% earn:

$$
\le \$55,000
$$

### \(Q_3=80,000\)

Approximately 75% earn:

$$
\le \$80,000
$$

This tells us much more about the distribution than simply saying:

> "Average salary = $60,000."

---

# 14. Percentiles Give You Context

Suppose two students have:

- Student A = 85
- Student B = 75

It seems obvious that A performed better.

But imagine:

### Student A

$$
85 \rightarrow 55^{th}\text{ percentile}
$$

### Student B

$$
75 \rightarrow 80^{th}\text{ percentile}
$$

Why could this happen?

Because they may have taken different exams or come from different populations.

The **raw value** and the **relative position** answer different questions.

That's why percentiles are useful.

---

# 15. Percentile Position

Now let's understand how we actually locate a percentile.

There are multiple conventions for calculating percentile positions, especially when the desired position falls between observations.

For beginner intuition, let's first use the **nearest-rank idea**.

Suppose we have:

$$
n=10
$$

observations.

For the \(p\)-th percentile, a simple rank calculation is:

$$
\text{Rank}=\left\lceil\frac{p}{100}n\right\rceil
$$

where:

- \(p\) = desired percentile
- \(n\) = number of observations
- \(\lceil\ \rceil\) = round upward to the next whole number.

---

# 16. Example: 80th Percentile

Dataset:

$$
[10,20,30,40,50,60,70,80,90,100]
$$

We want:

$$
P_{80}
$$

Calculate:

$$
\frac{80}{100}\times10=8
$$

So rank:

$$
8
$$

The 8th value is:

$$
80
$$

Therefore, under this simple nearest-rank convention:

$$
\boxed{P_{80}=80}
$$

---

# 17. Another Example

Dataset:

$$
[10,20,30,40,50,60,70,80,90,100]
$$

Find the 30th percentile.

$$
\frac{30}{100}\times10=3
$$

The 3rd observation is:

$$
30
$$

So:

$$
\boxed{P_{30}=30}
$$

under this convention.

---

# 18. But There Is an Important Detail

Real statistical software does **not always use the exact same percentile convention**.

For example, NumPy's `np.percentile()` uses a method based on interpolation by default.

That means if the percentile falls between two observations, it may calculate a value **between** them.

So don't memorize one hand-calculation formula as the universal definition.

The important conceptual understanding is:

> **Percentile identifies a location in the ordered distribution.**

Later, when we properly learn NumPy, we'll study exactly how:

```python
np.percentile()
```

calculates it.

---

# 19. Percentile vs Quartile

This is another important distinction.

### Percentile

Can refer to any percentage position:

$$
P_1,P_2,P_3,\ldots,P_{99}
$$

For example:

$$
P_{90}
$$

is the 90th percentile.

### Quartile

Specifically refers to the quarter divisions:

$$
Q_1,Q_2,Q_3
$$

Relationship:

$$
\boxed{Q_1=P_{25}}
$$

$$
\boxed{Q_2=P_{50}}
$$

$$
\boxed{Q_3=P_{75}}
$$

---

# 20. The Complete Picture

Imagine your entire dataset as a population standing in sorted order:

```text
0%                 25%                 50%                 75%                100%
|-------------------|-------------------|-------------------|-------------------|
                    Q1                  Q2                  Q3
                    ↓                   ↓                   ↓
                  25th                50th                75th
                percentile          percentile           percentile
```

And:

$$
Q_2=\text{Median}
$$

This gives us a powerful way of describing a dataset.

---

# 21. Why Is This Important in Machine Learning?

Suppose you're working with a dataset containing:

```text
Age
Salary
Temperature
Vehicle Speed
Sensor Reading
```

You might want to know:

> "What values are typical?"

Mean helps.

But you may also ask:

> "Where are the lower 25% of values?"

That's \(Q_1\).

> "Where is the middle?"

That's \(Q_2\).

> "Where are the upper 25%?"

That's \(Q_3\).

---

# 22. ML Application — Understanding Feature Distributions

Imagine a feature:

```text
House Price
```

Suppose:

$$
Q_1=100k
$$

$$
Q_2=150k
$$

$$
Q_3=250k
$$

You immediately get information about the distribution.

Instead of looking at thousands of numbers individually, you have a compact summary.

This is extremely useful during:

> **EDA — Exploratory Data Analysis**

---

# 23. ML Application — Outlier Detection

Percentiles become especially powerful when combined with:

$$
Q_1
$$

and:

$$
Q_3
$$

This leads to:

$$
\boxed{\text{IQR}=Q_3-Q_1}
$$

IQR stands for:

> **Interquartile Range**

We'll study this properly in the **next lesson**.

It becomes one of the important tools for detecting outliers.

---

# 24. ML Application — Robust Statistics

Suppose a dataset contains:

```text
10
11
12
13
14
15
16
10000
```

The value `10000` is extremely large compared with the others.

The mean can be heavily affected.

Percentiles and quartiles focus more on **relative position within the ordered data**, which can make them useful for understanding data with extreme values.

This is one reason they're common in EDA.

---

# 25. Physics Example

Suppose you're measuring photon arrival times.

You collect:

$$
t_1,t_2,t_3,\ldots,t_n
$$

Maybe you're interested in the distribution of arrival times.

You could ask:

> "What time is below which 90% of the measurements fall?"

That's essentially a **90th percentile threshold**.

Similarly, if you're studying experimental noise amplitudes:

$$
A_1,A_2,\ldots,A_n
$$

you might ask:

> "What amplitude contains the lower 95% of measurements?"

Again, a percentile gives you a useful threshold.

This becomes particularly useful in scientific data analysis where distributions may not be nicely Gaussian.

---

# 26. NumPy Preview

Eventually you'll use:

```python
import numpy as np

x = np.array([10,20,30,40,50,60,70,80,90,100])

np.percentile(x, 25)
np.percentile(x, 50)
np.percentile(x, 75)
```

Conceptually:

```text
np.percentile(x, 25) → Q1
np.percentile(x, 50) → Q2 / Median
np.percentile(x, 75) → Q3
```

But remember our learning philosophy:

> **Don't memorize the function first. Understand the mathematics first.**

The NumPy function is simply a tool for performing the mathematical operation.

---

# 27. A Very Important Mental Model

Think of a **race**.

100 runners finish and are ordered from slowest to fastest.

If you're at the:

### 25th percentile

You are around the first quarter of the ordered group.

### 50th percentile

You're around the middle.

### 75th percentile

You're around three-quarters of the way through.

### 95th percentile

You're very close to the top end.

So:

> **Percentile is a position, not a score.**

---

# 28. Common Mistakes

### Mistake 1

Thinking:

> 80th percentile = 80% score.

❌ Wrong.

It means approximately 80% of observations are at or below that value.

---

### Mistake 2

Thinking:

> 75th percentile means the value is 75.

❌ Wrong.

The **percentile number** and the **data value** are different things.

For example:

$$
P_{75}=82
$$

means:

> The 75th percentile value is 82.

---

### Mistake 3

Thinking Q1 means "first observation."

❌ Wrong.

$$
Q_1=P_{25}
$$

It is the 25th-percentile location.

---

### Mistake 4

Thinking Q2 is something different from median.

❌

$$
\boxed{Q_2=\text{Median}}
$$

---

# 29. Percentile vs Mean vs Median

Let's put them together.

| Statistic  | Main question                                  |
| ---------- | ---------------------------------------------- |
| Mean       | What is the average?                           |
| Median     | What is the middle value?                      |
| Percentile | Where does a value stand relative to the data? |
| Quartile   | Where are the 25%, 50%, and 75% divisions?     |
| Range      | How far apart are minimum and maximum?         |

This is an important transition:

```text
Mean
 ↓
Center

Median
 ↓
Middle

Percentiles
 ↓
Relative position

Quartiles
 ↓
25% / 50% / 75%

IQR
 ↓
Middle 50% spread
```

---

# 30. One Dataset — Everything Together

Consider:

$$
X=[10,20,20,30,40,50,60,70,80,100]
$$

There are 10 observations.

We can ask different questions.

### Mean

$$
\bar{x}=\frac{10+20+20+30+40+50+60+70+80+100}{10}
$$

$$
\bar{x}=48
$$

### Median

Middle two:

$$
40,\ 50
$$

Therefore:

$$
Q_2=\text{Median}=45
$$

### Quartiles

Using the simple median-of-halves intuition:

Lower half:

$$
[10,20,20,30,40]
$$

so:

$$
Q_1=20
$$

Upper half:

$$
[50,60,70,80,100]
$$

so:

$$
Q_3=70
$$

Thus:

$$
\boxed{Q_1=20,\quad Q_2=45,\quad Q_3=70}
$$

And notice:

$$
Q_1=20
$$

means approximately 25% of observations are at or below this region.

$$
Q_2=45
$$

is the median.

$$
Q_3=70
$$

marks the 75th-percentile region.

---

# 31. The Big Mental Map 🧠

Remember this:

```text
                  ORDER THE DATA
                        │
                        ▼
               [lowest → highest]
                        │
                        ▼
                  PERCENTILES
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
        P25           P50           P75
         │             │             │
         ▼             ▼             ▼
         Q1            Q2            Q3
                       │
                       ▼
                    MEDIAN
```

And then:

```text
Q1 ───────── Q2 ───────── Q3
│             │             │
25%           50%           75%
```

Next comes:

$$
\boxed{IQR=Q_3-Q_1}
$$

which tells us about the **spread of the middle 50% of the data**.

---

# 32. Practice — Don't Look at the Answers Immediately

### Q1

What does the 90th percentile mean?

---

### Q2

What percentile is the median?

---

### Q3

What are the three quartiles?

---

### Q4

What is the relationship between quartiles and percentiles?

---

### Q5

Dataset:

$$
[10,20,30,40,50,60,70,80,90,100]
$$

Using our simple nearest-rank convention, what is the 80th percentile?

---

### Q6

What's the difference between:

> 80% accuracy

and

> 80th percentile?

---

### Q7

If:

$$
Q_1=25
$$

what does that tell us?

---

### Q8

If:

$$
Q_3=90
$$

what percentile does 90 represent?

---

# Answers

### Q1

Approximately 90% of observations are at or below that value.

### Q2

$$
\boxed{50^{th}}
$$

### Q3

$$
\boxed{Q_1,Q_2,Q_3}
$$

### Q4

$$
Q_1=P_{25}
$$

$$
Q_2=P_{50}
$$

$$
Q_3=P_{75}
$$

### Q5

Rank:

$$
0.80(10)=8
$$

8th value:

$$
\boxed{80}
$$

### Q6

**80% accuracy** = 80 out of every 100 predictions were correct.

**80th percentile** = the value is around the level at or below which 80% of observations lie.

### Q7

Approximately 25% of observations are at or below 25.

### Q8

$$
\boxed{75^{th}\text{ percentile}}
$$

---

# 🔑 Lesson 18 Summary

You should now understand:

$$
\boxed{\text{Percentile = relative position in ordered data}}
$$

$$
\boxed{P_{50}=\text{Median}}
$$

$$
\boxed{Q_1=P_{25}}
$$

$$
\boxed{Q_2=P_{50}}
$$

$$
\boxed{Q_3=P_{75}}
$$

And the most important distinction:

> **Percentage tells you how much. Percentile tells you where you stand.**

The next concept naturally builds directly from this:

# Lesson 19 — IQR & Outlier Detection

We'll take:

$$
Q_1,\ Q_2,\ Q_3
$$

and discover how they let us measure the **middle 50% of the data**, construct the **box-plot idea**, and identify potential **outliers**—one of the most important concepts in EDA and ML data preprocessing.
