# Lesson 21 — Correlation

Now we reach one of the **most important concepts in statistics and Machine Learning**:

> **How are two variables related to each other?**

For example:

- Does study time increase exam score?
- Does house size relate to house price?
- Does temperature relate to electricity usage?
- Does one sensor reading change when another changes?
- Does one physical measurement correlate with another?

The mathematical tool we use to measure **linear relationship** is called **correlation**.

---

# 1. Start With a Simple Question

Suppose we record:

| Student | Study Hours | Score |
| ------- | ----------: | ----: |
| A       |           1 |    50 |
| B       |           2 |    55 |
| C       |           3 |    65 |
| D       |           4 |    70 |
| E       |           5 |    80 |

Look at the pattern:

```text
Study Hours ↑
      ↓
Score tends to ↑
```

As study hours increase, score generally increases.

We would say:

> There is a **positive relationship** between study hours and score.

But how strong is that relationship?

That's where correlation comes in.

---

# 2. The Scatter Plot Mental Model

Imagine plotting every student as a point.

- x-axis = study hours
- y-axis = score

```text
Score
  ↑
80|                  ●
75|
70|             ●
65|         ●
60|
55|     ●
50| ●
  +--------------------------→ Study Hours
    1   2   3   4   5
```

The points generally move **upward**.

That suggests:

$$
\boxed{\text{Positive correlation}}
$$

---

# 3. What Is Correlation?

At a high level:

> **Correlation measures the direction and strength of a linear relationship between two variables.**

There are three major possibilities:

### Positive correlation

$$
X\uparrow \Rightarrow Y\uparrow
$$

### Negative correlation

$$
X\uparrow \Rightarrow Y\downarrow
$$

### Little/no linear correlation

Changes in \(X\) don't show a clear linear pattern in \(Y\).

---

# 4. Positive Correlation

Imagine:

$$
X=[1,2,3,4,5]
$$

and:

$$
Y=[2,4,6,8,10]
$$

As \(X\) increases:

$$
Y
$$

also increases.

Graphically:

```text id="7s94fa"
Y
↑
10|                 ●
  |
 8|             ●
  |
 6|         ●
  |
 4|     ●
  |
 2| ●
  +--------------------→ X
```

This is a very strong positive linear relationship.

In fact:

$$
\boxed{r=1}
$$

for Pearson correlation.

We'll derive what \(r\) means shortly.

---

# 5. Negative Correlation

Now:

$$
X=[1,2,3,4,5]
$$

$$
Y=[10,8,6,4,2]
$$

As \(X\) increases, \(Y\) decreases.

```text id="m9v8rj"
Y
↑
10| ●
  |
 8|     ●
  |
 6|         ●
  |
 4|             ●
  |
 2|                 ●
  +--------------------→ X
```

This is:

$$
\boxed{\text{Negative correlation}}
$$

and in this perfect linear example:

$$
\boxed{r=-1}
$$

---

# 6. No Linear Correlation

Consider:

$$
X=[1,2,3,4,5]
$$

but:

$$
Y=[8,2,7,3,9]
$$

There's no obvious straight-line pattern.

```text id="b4k8cv"
Y
↑
9|                 ●
8| ●
7|         ●
6|
5|
4|             ●
3|
2|     ●
 +--------------------→ X
```

The Pearson correlation could be close to:

$$
0
$$

meaning:

> There is little or no **linear** relationship.

⚠️ Very important:

$$
r\approx0
$$

does **not** necessarily mean there is absolutely no relationship.

We'll see why later.

---

# 7. The Correlation Coefficient

The most common correlation measure you'll encounter is the:

$$
\boxed{\text{Pearson correlation coefficient}}
$$

It is usually represented by:

$$
\boxed{r}
$$

or sometimes:

$$
\boxed{\rho}
$$

depending on whether we're talking about sample or population correlation.

For now, think of:

$$
r
$$

as a **relationship meter**.

---

# 8. The Range of Correlation

Pearson correlation satisfies:

$$
\boxed{-1\le r\le1}
$$

This is extremely important.

```text id="z0u8w5"
-1              0              +1
│---------------│---------------│
Strong          No             Strong
negative        linear         positive
                relationship
```

Interpretation:

### \(r=+1\)

Perfect positive linear relationship.

### \(r=-1\)

Perfect negative linear relationship.

### \(r=0\)

No linear correlation.

### \(r=+0.8\)

Strong positive linear relationship.

### \(r=-0.8\)

Strong negative linear relationship.

### \(r=+0.2\)

Weak positive linear relationship.

---

# 9. Important: Correlation Has Two Things

Correlation tells us:

## Direction

Positive or negative.

## Strength

How closely the points follow a straight-line relationship.

For example:

$$
r=0.9
$$

means strong positive linear association.

While:

$$
r=-0.9
$$

means strong negative linear association.

Notice:

$$
|0.9|=|-0.9|=0.9
$$

The **magnitude** tells us strength.

The **sign** tells us direction.

---

# 10. The Absolute Value Trick

A useful mental model:

$$
\boxed{|r|=\text{strength}}
$$

while:

$$
\boxed{\text{sign of }r=\text{direction}}
$$

For example:

| \(r\) | Direction | Strength      |
| ----: | --------- | ------------- |
| +0.95 | Positive  | Very strong   |
| +0.30 | Positive  | Weak          |
|     0 | None      | None linearly |
| -0.30 | Negative  | Weak          |
| -0.95 | Negative  | Very strong   |

These descriptions are approximate conventions, not universal cutoffs.

---

# 11. But How Do We Actually Calculate Correlation?

Now we get to the mathematics.

The Pearson correlation coefficient is:

$$
\boxed{
r=
\frac{
\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})
}{
\sqrt{
\sum_{i=1}^{n}(x_i-\bar{x})^2
}
\sqrt{
\sum_{i=1}^{n}(y_i-\bar{y})^2
}
}
}
$$

Don't panic. 😄

It looks complicated because several ideas we've already learned are combined.

Let's unpack it.

---

# 12. First: What Are \(x_i\) and \(y_i\)?

Suppose:

$$
X=[1,2,3,4,5]
$$

and:

$$
Y=[2,4,6,8,10]
$$

Then:

$$
x_1=1,\quad x_2=2,\ldots
$$

and:

$$
y_1=2,\quad y_2=4,\ldots
$$

The subscript \(i\) simply identifies which observation we're talking about.

---

# 13. What Are \(\bar{x}\) and \(\bar{y}\)?

They're the means.

For \(X\):

$$
\bar{x}=\frac{1+2+3+4+5}{5}=3
$$

For \(Y\):

$$
\bar{y}=\frac{2+4+6+8+10}{5}=6
$$

So:

$$
\boxed{\bar{x}=3}
$$

$$
\boxed{\bar{y}=6}
$$

---

# 14. Why Subtract the Mean?

Correlation wants to know:

> Do \(X\) and \(Y\) move together relative to their own averages?

So we calculate:

$$
x_i-\bar{x}
$$

and:

$$
y_i-\bar{y}
$$

These are called **deviations from the mean**.

---

# 15. Build a Table

Let's calculate everything.

$$
X=[1,2,3,4,5]
$$

$$
Y=[2,4,6,8,10]
$$

Means:

$$
\bar{x}=3
$$

$$
\bar{y}=6
$$

Now:

| \(x_i\) | \(y_i\) | \(x_i-\bar{x}\) | \(y_i-\bar{y}\) |
| ------: | ------: | --------------: | --------------: |
|       1 |       2 |              -2 |              -4 |
|       2 |       4 |              -1 |              -2 |
|       3 |       6 |               0 |               0 |
|       4 |       8 |              +1 |              +2 |
|       5 |      10 |              +2 |              +4 |

Now something interesting happens.

---

# 16. Look at the Signs

For the first observation:

$$
(-2)(-4)=+8
$$

Both deviations are negative.

For the second:

$$
(-1)(-2)=+2
$$

Again both are negative.

For the fourth:

$$
(+1)(+2)=+2
$$

Both positive.

For the fifth:

$$
(+2)(+4)=+8
$$

Again both positive.

So when \(X\) and \(Y\) move in the **same direction**, their deviation product is positive.

---

# 17. What If They Move Oppositely?

Suppose:

$$
X
$$

is above its mean:

$$
x_i-\bar{x}>0
$$

but:

$$
Y
$$

is below its mean:

$$
y_i-\bar{y}<0
$$

Then:

$$
(+)(-) = -
$$

The product becomes negative.

So:

```text id="jzv0v1"
X above mean
       +
       │
       │
       ↓
       Y below mean
       -

       (+)(-) = negative
```

That's exactly what we need.

---

# 18. The Core Idea Behind Correlation

This is the heart of Pearson correlation:

> **Check whether the two variables tend to deviate from their means in the same direction or opposite directions.**

Same direction:

$$
(+)(+)=+
$$

or:

$$
(-)(-)=+
$$

→ positive relationship.

Opposite directions:

$$
(+)(-) = -
$$

→ negative relationship.

This is why the numerator contains:

$$
\boxed{
\sum(x_i-\bar{x})(y_i-\bar{y})
}
$$

---

# 19. What Is Covariance?

And now we reach an important connection.

The quantity:

$$
\sum(x_i-\bar{x})(y_i-\bar{y})
$$

is closely related to **covariance**.

Covariance asks:

> **Do two variables tend to move together?**

This will be our **next major lesson**.

For now:

$$
\boxed{\text{Covariance = directional co-movement}}
$$

Correlation takes this idea and **normalizes it** so that the result always lies between:

$$
-1
$$

and:

$$
+1.
$$

---

# 20. Why Does Correlation Need Normalization?

Imagine measuring:

- height in meters
- height in centimeters

The numerical values are completely different.

Covariance changes with the scale of the variables.

Correlation removes that scale dependence.

That's why the denominator contains:

$$
\sqrt{\sum(x_i-\bar{x})^2}
$$

and:

$$
\sqrt{\sum(y_i-\bar{y})^2}
$$

These are related to the spread of \(X\) and \(Y\).

Conceptually:

$$
\boxed{
\text{Correlation}
=
\frac{\text{co-movement}}{\text{individual spread}}
}
$$

This is a very useful mental model.

---

# 21. Let's Understand the Formula as a Story

Instead of memorizing the formula, imagine two dancers:

- Dancer X
- Dancer Y

We watch how each moves relative to their own center.

If they move together:

```text id="gkq8cn"
X: ↑ ↑ ↑
Y: ↑ ↑ ↑
```

positive correlation.

If one goes up while the other goes down:

```text id="r1o8jo"
X: ↑ ↑ ↑
Y: ↓ ↓ ↓
```

negative correlation.

If their movements don't follow a consistent pattern:

```text id="7w6q0d"
X: ↑ ↓ ↑ ↑ ↓
Y: ↓ ↑ ↓ ↑ ↑
```

little linear correlation.

Correlation is essentially asking:

> **"Are these two dancers moving together?"**

---

# 22. Correlation Does NOT Mean Causation

This is one of the most important rules in statistics.

Suppose:

$$
X=\text{ice cream sales}
$$

and:

$$
Y=\text{number of people swimming}
$$

You might find:

$$
r>0
$$

Both increase together.

Does ice cream cause people to swim?

No.

A third variable is involved:

$$
\text{Temperature}
$$

When temperature rises:

- ice cream sales increase
- swimming increases.

So:

```text id="3zmb5e"
          Temperature
           ↙       ↘
          ↓         ↓
Ice Cream Sales   Swimming
```

This is an example of a **confounding variable**.

Therefore:

$$
\boxed{\text{Correlation}\neq\text{Causation}}
$$

---

# 23. ML Example: Feature Relationships

Suppose your dataset has:

$$
X_1=\text{house size}
$$

and:

$$
Y=\text{house price}
$$

If:

$$
r=0.85
$$

there is a strong positive linear relationship.

This can tell us:

> House size and price tend to increase together in this dataset.

That can be useful during EDA.

But correlation alone doesn't prove:

> Increasing house size necessarily causes the observed price increase.

There may be other factors:

- location
- number of bedrooms
- neighborhood
- age
- land size.

---

# 24. Correlation in Feature Selection

Suppose we have 100 features.

We might calculate correlations between numerical features.

For example:

```text id="k5zq8g"
Feature A ↔ Target     r = 0.82
Feature B ↔ Target     r = 0.05
Feature C ↔ Target     r = -0.71
```

This gives us useful information about **linear association**.

But be careful:

> A low correlation with the target does not necessarily mean a feature is useless.

Why?

Because the relationship could be **nonlinear**.

---

# 25. A Famous Example of Nonlinear Relationship

Consider:

$$
Y=X^2
$$

For:

$$
X=[-3,-2,-1,0,1,2,3]
$$

we get:

$$
Y=[9,4,1,0,1,4,9]
$$

There is clearly a relationship.

Knowing \(X\) tells us a lot about \(Y\).

But the Pearson correlation can be:

$$
\boxed{r=0}
$$

Why?

Because the relationship is **U-shaped**, not linear.

```text id="x1j57j"
Y
↑
9| ●             ●
 |
4|    ●       ●
 |
1|       ● ●
 |
0|          ●
 +----------------→ X
   -3 -2 -1 0 1 2 3
```

This is one of the most important limitations of correlation.

> **Pearson correlation measures linear association.**

Not all association.

---

# 26. This Matters Greatly in ML

Suppose:

$$
r\approx0
$$

between a feature and target.

A beginner might say:

> "This feature has no relationship with the target."

That conclusion is too strong.

The correct statement is:

> **"There is little or no linear association detected by Pearson correlation."**

There could still be:

- quadratic relationships
- exponential relationships
- periodic relationships
- threshold relationships
- interactions with other features.

---

# 27. Physics Example

Suppose:

$$
X=\text{temperature}
$$

and:

$$
Y=\text{resistance}
$$

You might investigate whether resistance changes linearly with temperature.

Correlation can give an initial measure of linear association.

But physical systems often have nonlinear relationships.

For example:

$$
Y=X^2
$$

could have:

$$
r\approx0
$$

despite a perfectly deterministic relationship.

So:

> **Correlation should be treated as a diagnostic tool, not a complete description of physical relationships.**

---

# 28. Quantum / Scientific Example

Suppose you record two experimental quantities:

$$
X=\text{photon arrival count}
$$

and:

$$
Y=\text{detector signal}
$$

You could investigate their correlation.

If:

$$
r>0
$$

the measurements tend to increase together linearly.

If:

$$
r<0
$$

they tend to move oppositely.

If:

$$
r\approx0
$$

there may be little linear association.

But again:

$$
r\approx0
$$

doesn't rule out nonlinear or more complicated dependence.

This distinction becomes particularly important when analyzing experimental and quantum data.

---

# 29. Correlation vs Covariance

You will encounter both.

### Covariance

Asks:

> Do two variables move together?

But its magnitude depends on the units/scales.

### Correlation

Asks:

> How strongly and in which direction do two variables have a linear relationship, after normalizing for scale?

Therefore:

$$
\boxed{\text{Correlation = normalized covariance}}
$$

We'll derive this properly next.

---

# 30. NumPy Preview

Later, NumPy can calculate a correlation matrix:

```python
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

np.corrcoef(x, y)
```

You would obtain a matrix conceptually like:

$$
\begin{bmatrix}
1 & 1\\
1 & 1
\end{bmatrix}
$$

The diagonal is always:

$$
1
$$

because every variable is perfectly correlated with itself.

The off-diagonal entries represent the correlations between different variables.

We'll properly learn matrices of correlations later.

---

# 31. Correlation Matrix

Suppose you have:

```text id="n9s4ot"
Age
Income
House Size
House Price
```

You can calculate correlations between every pair.

Conceptually:

$$
R=
\begin{bmatrix}
1 & r_{12} & r_{13} & r_{14}\\
r_{21} & 1 & r_{23} & r_{24}\\
r_{31} & r_{32} & 1 & r_{34}\\
r_{41} & r_{42} & r_{43} & 1
\end{bmatrix}
$$

This is called a:

$$
\boxed{\text{Correlation Matrix}}
$$

It is extremely common in EDA.

---

# 32. Why Correlation Matrices Matter in ML

Suppose:

$$
r(\text{House Size},\text{Price})=0.85
$$

and:

$$
r(\text{Bedrooms},\text{Price})=0.80
$$

This tells us both features have strong linear associations with price.

But suppose:

$$
r(\text{House Size},\text{Bedrooms})=0.92
$$

Now we might suspect the two features carry highly overlapping information.

This leads toward an important ML concept:

$$
\boxed{\text{Multicollinearity}}
$$

which we'll eventually study.

---

# 33. Important Warning About Correlation

Don't use correlation blindly.

A high correlation can be caused by:

- confounding variables
- trends
- outliers
- nonlinear-looking data that happens to produce association
- data leakage in ML
- sampling effects.

And a low Pearson correlation can hide nonlinear relationships.

Therefore:

> **Always visualize the data when possible.**

A scatter plot + correlation coefficient is often much more informative than either alone.

---

# 34. The Complete Mental Model

Think of correlation as a **relationship compass**:

```text id="m5tb0w"
                         CORRELATION
                              │
                 ┌────────────┼────────────┐
                 ↓            ↓            ↓
             Positive       Zero       Negative
                 │            │            │
               X↑ Y↑       no clear      X↑ Y↓
                           linear trend
                 │
                 └────── strength ────────┘
                              │
                         -1 ≤ r ≤ +1
```

And:

$$
\boxed{|r|=\text{strength}}
$$

$$
\boxed{\operatorname{sign}(r)=\text{direction}}
$$

---

# 35. Your Statistics Mental Map Is Growing

You now have:

```text id="ojj3zz"
DATA
 │
 ├── CENTER
 │    ├── Mean
 │    └── Median
 │
 ├── SPREAD
 │    ├── Range
 │    ├── Variance
 │    ├── Standard Deviation
 │    └── IQR
 │
 ├── POSITION
 │    ├── Percentiles
 │    └── Quartiles
 │
 ├── SHAPE
 │    ├── Symmetric
 │    ├── Right-skewed
 │    ├── Left-skewed
 │    └── Multimodal
 │
 └── RELATIONSHIPS
      └── Correlation
```

The next branch is:

$$
\boxed{\text{Covariance}}
$$

because covariance is the mathematical foundation underneath the intuition of correlation.

---

# 🧪 Practice

Try these before checking the answers.

### Q1

What does correlation measure?

---

### Q2

What is the range of Pearson correlation?

---

### Q3

What does:

$$
r=+0.9
$$

generally indicate?

---

### Q4

What does:

$$
r=-0.9
$$

generally indicate?

---

### Q5

What does:

$$
r\approx0
$$

tell us?

Be precise.

---

### Q6

If:

$$
X\uparrow
$$

and:

$$
Y\downarrow
$$

what sign would you expect for \(r\)?

---

### Q7

What is the difference between correlation strength and direction?

---

### Q8

True or false:

> If two variables have high correlation, one must cause the other.

---

### Q9

Suppose:

$$
Y=X^2
$$

Can Pearson correlation be close to zero even though \(X\) and \(Y\) clearly have a relationship?

---

### Q10

Why is correlation generally more comparable across units than covariance?

---

# Answers

### Q1

Correlation measures the **direction and strength of a linear relationship** between two variables.

### Q2

$$
\boxed{-1\le r\le1}
$$

### Q3

A strong positive linear association.

### Q4

A strong negative linear association.

### Q5

There is little or no **linear** association detected by Pearson correlation. It does **not** prove there is no relationship at all.

### Q6

Negative:

$$
\boxed{r<0}
$$

### Q7

The **sign** indicates direction; the **absolute value** indicates strength.

### Q8

False.

$$
\boxed{\text{Correlation}\neq\text{Causation}}
$$

### Q9

Yes.

A nonlinear relationship can have:

$$
r\approx0.
$$

### Q10

Correlation normalizes covariance by the spread of both variables, making it unitless and bounded between \(-1\) and \(1\).

---

# 🔑 Remember This Forever

If you remember only five things from this lesson, remember:

$$
\boxed{-1\le r\le1}
$$

$$
\boxed{r>0\Rightarrow\text{positive linear association}}
$$

$$
\boxed{r<0\Rightarrow\text{negative linear association}}
$$

$$
\boxed{|r|\text{ tells strength}}
$$

and most importantly:

$$
\boxed{\text{Correlation}\neq\text{Causation}}
$$

Also:

> **Pearson correlation sees straight-line relationships.**

That last point will save you from many statistical mistakes.

**Next lesson: Covariance** — we'll derive it from the deviations you just learned, understand exactly why its sign tells us whether two variables move together, and then mathematically show how **covariance becomes correlation after normalization**.
