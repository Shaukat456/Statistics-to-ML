# Lesson 17 — Mean, Median, Mode & Range

We now move from **probability theory** toward **descriptive statistics**.

Until now, we were asking questions like:

> "What could happen, and with what probability?"

Now we start asking:

> **"I have actual data. How can I summarize it?"**

This is extremely important because ML begins with **data**, and before building a model, we need to understand the data.

---

# 1. Imagine You Receive a Dataset

Suppose you collect the exam scores of 7 students:

$$
[55,60,65,70,70,75,95]
$$

Looking at all seven numbers tells us something.

But imagine having:

$$
10,000
$$

students.

You don't want to inspect every number individually.

You want a few useful summary statistics.

The first ones are:

$$
\boxed{\text{Mean}}
$$

$$
\boxed{\text{Median}}
$$

$$
\boxed{\text{Mode}}
$$

$$
\boxed{\text{Range}}
$$

---

# 2. The Four Questions

Think of these as four different investigators examining the same dataset:

```text
                    DATA
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
     MEAN          MEDIAN         MODE
   "Average"     "Middle"      "Most common"
                     │
                     └────── RANGE
                           "How wide?"
```

Each answers a different question.

---

# 3. Mean — The Mathematical Average

You've already encountered the mean.

For:

$$
x_1,x_2,\ldots,x_n
$$

the mean is:

$$
\boxed{
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i
}
$$

In simple English:

> **Add all values and divide by the number of values.**

---

# 4. Example

Consider:

$$
[10,20,30,40,50]
$$

Add them:

$$
10+20+30+40+50=150.
$$

There are 5 values.

Therefore:

$$
\bar{x}=\frac{150}{5}=30.
$$

So:

$$
\boxed{\bar{x}=30}
$$

---

# 5. Mean as a "Balance Point" ⚖️

This is a powerful mental model.

Imagine each number is a weight placed on a number line.

For:

$$
[10,20,30,40,50]
$$

the mean is:

$$
30.
$$

The mean is the point where the distribution would theoretically balance.

```text id="wz2j5t"
10    20    30    40    50
●-----●-----⚖-----●-----●
            ↑
          Mean
```

This is why the mean is sometimes called the **center of mass** or balance point of the data.

---

# 6. But Mean Has a Problem...

Consider:

$$
[10,20,30,40,50]
$$

Mean:

$$
30.
$$

Now change the last value:

$$
[10,20,30,40,1000].
$$

Mean becomes:

$$
\frac{10+20+30+40+1000}{5}
$$

$$
=\frac{1100}{5}
$$

$$
=220.
$$

Whoa.

The mean jumped from:

$$
30\rightarrow220.
$$

Why?

Because the value:

$$
1000
$$

is extremely far away.

This is called an **outlier**.

---

# 7. Median

The median takes a completely different approach.

> **Sort the data and find the middle value.**

Consider:

$$
[10,20,30,40,50].
$$

Already sorted.

The middle value is:

$$
30.
$$

Therefore:

$$
\boxed{\text{Median}=30}
$$

---

# 8. Why Is Median Useful?

Now consider:

$$
[10,20,30,40,1000].
$$

The median is still:

$$
30.
$$

So:

$$
\boxed{\text{Median}=30}
$$

while:

$$
\boxed{\text{Mean}=220}.
$$

The median barely cares about the extreme value.

This makes median much more **robust to outliers** than the mean.

---

# 9. Odd Number of Values

Suppose:

$$
[3,7,9,12,15].
$$

There are:

$$
5
$$

values.

The middle is the 3rd value:

$$
\boxed{9}.
$$

So:

$$
\text{Median}=9.
$$

---

# 10. Even Number of Values

Now suppose:

$$
[3,7,9,12].
$$

There are 4 values.

There is no single middle value.

The two middle values are:

$$
7,\quad9.
$$

Take their average:

$$
\frac{7+9}{2}=8.
$$

Therefore:

$$
\boxed{\text{Median}=8}.
$$

---

# 11. Median Algorithm

For a dataset:

$$
[x_1,x_2,\ldots,x_n]
$$

### Step 1

Sort the data.

### Step 2

If \(n\) is odd:

Take the middle value.

### Step 3

If \(n\) is even:

Average the two middle values.

Mental model:

> **Median = person standing exactly in the middle of a queue.**

---

# 12. Mean vs Median

Let's compare.

Dataset:

$$
[10,20,30,40,50]
$$

Mean:

$$
30
$$

Median:

$$
30.
$$

No problem.

Now:

$$
[10,20,30,40,1000]
$$

Mean:

$$
220
$$

Median:

$$
30.
$$

This teaches us something important:

> **Mean uses the actual numerical magnitude of every observation.**

> **Median mainly depends on the ordering of observations.**

Therefore, extreme values can strongly affect mean but often have much less effect on median.

---

# 13. Mode

Now we ask a third question:

> **Which value occurs most frequently?**

Suppose:

$$
[2,3,3,4,5,3,6].
$$

Count the values:

```text id="m2y6k1"
2 → 1 time
3 → 3 times
4 → 1 time
5 → 1 time
6 → 1 time
```

Therefore:

$$
\boxed{\text{Mode}=3}
$$

because 3 occurs most often.

---

# 14. Mode Is Different

Mean:

> mathematical average

Median:

> middle value

Mode:

> most frequently occurring value

For example:

$$
[1,2,2,2,3,4,5]
$$

gives:

$$
\text{Mean}=?
$$

$$
\text{Median}=2
$$

$$
\text{Mode}=2.
$$

The mean is:

$$
\frac{19}{7}\approx2.71.
$$

So the three don't have to be the same.

---

# 15. Can There Be More Than One Mode?

Yes.

Consider:

$$
[1,1,2,2,3,4].
$$

1 appears twice.

2 appears twice.

Therefore the dataset has two modes:

$$
\boxed{1\text{ and }2}.
$$

This is called **bimodal**.

If several values tie for the highest frequency, a dataset can be **multimodal**.

---

# 16. Range

Now we want to know:

> **How wide is the dataset?**

The simplest measure is the range.

$$
\boxed{
\text{Range}=\text{Maximum}-\text{Minimum}
}
$$

Example:

$$
[10,20,30,40,50].
$$

Maximum:

$$
50.
$$

Minimum:

$$
10.
$$

Therefore:

$$
\text{Range}=50-10=40.
$$

---

# 17. Range Mental Model

Imagine a ruler:

```text id="k73e1h"
10────────────────────────50
↑                          ↑
Min                        Max

<--------- Range --------->
             40
```

So:

> **Range tells you the total width covered by the data.**

---

# 18. Range Has a Weakness

Suppose:

$$
[10,20,30,40,50].
$$

Range:

$$
40.
$$

Now:

$$
[10,20,30,40,1000].
$$

Range:

$$
990.
$$

One outlier dramatically changes the range.

So range is easy to understand but can be very sensitive to extreme values.

Later we'll learn a more robust measure:

$$
\boxed{\text{IQR}}
$$

(interquartile range).

---

# 19. One Dataset — Four Investigators

Let's put everything together.

Dataset:

$$
[10,20,20,30,40,100]
$$

### Mean

$$
\frac{10+20+20+30+40+100}{6}
=
\frac{220}{6}
$$

$$
\boxed{\text{Mean}\approx36.67}
$$

### Median

The two middle values are:

$$
20,\quad30.
$$

Therefore:

$$
\boxed{\text{Median}=25}
$$

### Mode

20 appears twice.

Therefore:

$$
\boxed{\text{Mode}=20}
$$

### Range

$$
100-10=90.
$$

Therefore:

$$
\boxed{\text{Range}=90}
$$

So:

```text id="t6q4jr"
Mean    → 36.67  → average
Median  → 25     → middle
Mode    → 20     → most common
Range   → 90     → total width
```

---

# 20. Why Does ML Care?

Suppose you have a dataset of house prices:

$$
\$100k,\ \$120k,\ \$130k,\ \$150k,\ \$5M.
$$

The $5M house is an extreme observation.

If you calculate the mean, it can be pulled upward significantly.

The median might better represent a "typical" house price in such a skewed dataset.

This matters during:

- Exploratory Data Analysis (EDA)
- outlier investigation
- feature understanding
- data cleaning
- preprocessing
- feature engineering.

---

# 21. Mean in ML

Suppose a feature is:

$$
\text{Age}
$$

with:

$$
[20,25,30,35,40].
$$

Mean:

$$
30.
$$

Later, standardization uses:

$$
z=\frac{x-\mu}{\sigma}.
$$

Notice the mean appears directly.

So mean is fundamental to ML preprocessing.

---

# 22. Median in ML

Median is especially useful when data is **skewed**.

Imagine salaries:

```text id="3qjp0u"
$30k
$32k
$35k
$38k
$40k
$42k
$2M
```

The $2M salary can pull the mean upward.

The median remains much more representative of the center of the ordered observations.

This doesn't mean:

> "Always use median."

Instead:

> **Choose the summary statistic according to the structure and purpose of the data.**

---

# 23. Mode in ML

Mode becomes particularly useful with **categorical data**.

Suppose:

```text id="x6cb5j"
Red
Blue
Blue
Green
Blue
Red
```

Mode:

$$
\boxed{\text{Blue}}
$$

This can help when understanding categorical features.

For example:

- most common city
- most common product category
- most common class
- most common device type.

---

# 24. Range in ML

Range gives a quick sense of scale.

Suppose:

### Feature A

$$
[1,2,3,4,5]
$$

Range:

$$
4.
$$

### Feature B

$$
[1000,2000,3000,4000,5000]
$$

Range:

$$
4000.
$$

The features have very different numerical scales.

This can become important for algorithms that depend on distances or optimization.

Later, when we study **feature scaling**, this will become very important.

---

# 25. A Critical Concept: Mean ≠ Typical in Every Dataset

Suppose:

$$
[1,1,1,1,100].
$$

Mean:

$$
\frac{104}{5}=20.8.
$$

Would you say 20.8 is a "typical" observation?

Probably not.

Most observations are:

$$
1.
$$

Median:

$$
1.
$$

Mode:

$$
1.
$$

This shows why we shouldn't automatically assume:

$$
\boxed{\text{mean}=\text{typical value}}
$$

The shape of the data matters.

---

# 26. Connection to Distribution Shape

Later we'll learn about **skewness**.

For now, just develop this intuition.

### Symmetric distribution

Mean and median can be close.

```text id="i5nguh"
       •
     • • •
   • • • • •
───────┼───────
      center
```

### Right-skewed distribution

A few very large values pull the mean rightward.

```text id="w2s4o1"
      •
    • •
  • •
 •
───────────────────────→
```

So often:

$$
\text{Mean}>\text{Median}
$$

in strongly right-skewed data.

### Left-skewed

The opposite can happen:

$$
\text{Mean}<\text{Median}.
$$

These are useful intuitions, not universal rules for every dataset.

---

# 27. Connection to Probability

This connects beautifully with our previous lessons.

A **probability distribution** describes how likely different values are.

Expected value:

$$
E[X]
$$

is essentially the theoretical probability-weighted center.

When we collect actual data:

$$
x_1,x_2,\ldots,x_n
$$

we calculate the sample mean:

$$
\bar{x}
=
\frac1n\sum_{i=1}^{n}x_i.
$$

So:

```text id="g4sp0r"
Probability distribution
        │
        ▼
Expected value E[X]
        │
        │ observe samples
        ▼
Actual dataset
        │
        ▼
Sample mean x̄
```

This is a major bridge between **probability and statistics**.

---

# 28. Physics Connection

Imagine measuring the position of a particle many times:

$$
x_1,x_2,\ldots,x_n.
$$

You might calculate:

$$
\bar{x}
$$

to estimate the average measured position.

In quantum mechanics, the theoretical expectation value is:

$$
\langle x\rangle.
$$

For a continuous wavefunction:

$$
\boxed{
\langle x\rangle
=
\int x|\psi(x)|^2dx
}
$$

Notice the structure:

$$
\text{value}\times\text{probability density}
$$

integrated over all possible values.

That's conceptually the continuous analogue of:

$$
E[X]=\sum_xxP(X=x).
$$

This is a very important connection between probability and quantum mechanics.

---

# 29. NumPy Preview

We are **not starting NumPy implementation yet**—we're still building the mathematical foundation.

But eventually these concepts become extremely easy to calculate with NumPy:

```python
import numpy as np

x = np.array([10, 20, 20, 30, 40, 100])

np.mean(x)
np.median(x)
np.min(x)
np.max(x)
```

And later:

```python
np.ptp(x)
```

can give the range.

The important principle remains:

> **First understand the mathematics. Then use NumPy to perform it efficiently.**

---

# 30. The Ultimate Mental Model 🧠

Imagine four people looking at the same dataset.

### 👨 Mean

> "I'll add everything and divide."

### 👩 Median

> "Line everyone up. I'll stand in the middle."

### 👨‍🔬 Mode

> "I'll count who appears most often."

### 📏 Range

> "I'll measure from the smallest to the largest."

So:

$$
\boxed{
\text{Mean = Average}
}
$$

$$
\boxed{
\text{Median = Middle}
}
$$

$$
\boxed{
\text{Mode = Most Common}
}
$$

$$
\boxed{
\text{Range = Maximum - Minimum}
}
$$

---

# 31. Summary Table

| Statistic | Main Question                  | Sensitive to Outliers?      |
| --------- | ------------------------------ | --------------------------- |
| Mean      | What's the arithmetic average? | Yes                         |
| Median    | What's the middle value?       | Much less                   |
| Mode      | What's most common?            | Usually not in the same way |
| Range     | How wide is the data?          | Yes                         |

---

# 32. Practice

### Q1

Calculate the mean:

$$
[2,4,6,8,10]
$$

---

### Q2

Calculate the median:

$$
[3,7,8,10,15]
$$

---

### Q3

Calculate the median:

$$
[3,7,8,10]
$$

---

### Q4

Find the mode:

$$
[2,3,3,4,5,3,6,2]
$$

---

### Q5

Find the range:

$$
[12,18,25,31,40]
$$

---

### Q6

Which is more affected by an extreme outlier: mean or median?

---

### Q7

Consider:

$$
[5,5,5,6,7,100].
$$

Calculate:

- Mean
- Median
- Mode
- Range

Then ask yourself:

> Which statistic best represents the center of this particular dataset, and why?

Don't worry about making a "universal" rule—the point is to reason about the data.

---

# 33. Answers

### Q1

$$
\frac{2+4+6+8+10}{5}
=
\boxed{6}
$$

### Q2

Middle value:

$$
\boxed{8}
$$

### Q3

Middle two:

$$
7,8
$$

Therefore:

$$
\frac{7+8}{2}
=
\boxed{7.5}
$$

### Q4

3 appears most often:

$$
\boxed{3}
$$

### Q5

$$
40-12=\boxed{28}
$$

### Q6

$$
\boxed{\text{Mean}}
$$

### Q7

Mean:

$$
\frac{5+5+5+6+7+100}{6}
=
\frac{128}{6}
\approx21.33
$$

Median:

$$
\frac{5+6}{2}=5.5
$$

Mode:

$$
5
$$

Range:

$$
100-5=95.
$$

Notice how the outlier \(100\) dramatically changes the mean and range, while the median and mode remain close to where most observations are concentrated.

---

# 🧠 Where We Are

Your statistics foundation is developing like this:

```text
Probability
     ↓
Random Variables
     ↓
Probability Distributions
     ↓
Bernoulli
     ↓
Binomial
     ↓
Expectation
     ↓
Variance
     ↓
        DESCRIPTIVE STATISTICS
              │
       ┌──────┼──────┐
       ▼      ▼      ▼
     Mean   Median  Mode
              │
              ▼
            Range
              │
              ▼
        Quartiles & Percentiles
              │
              ▼
             IQR
              │
              ▼
       Distribution Shape
              │
              ▼
        Correlation
              │
              ▼
          Covariance
```

**Next lesson:** **Percentiles & Quartiles** — we'll answer questions like:

> "What value is greater than 90% of the observations?"

and build the foundation for **IQR, box plots, outlier detection, and EDA**.
