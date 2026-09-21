# Lesson 22 — Covariance

In the previous lesson, we learned **correlation**.

We saw that correlation answers:

> **“Do two variables tend to move together, and in which direction?”**

Now we're going one level deeper.

The mathematical idea underneath correlation is **covariance**.

---

# 1. Start With the Basic Question

Suppose we measure:

- \(X\) = study hours
- \(Y\) = exam score

Consider:

$$
X=[1,2,3,4,5]
$$

$$
Y=[50,55,65,70,80]
$$

Generally:

$$
X\uparrow \Rightarrow Y\uparrow
$$

So we expect **positive covariance**.

Now imagine:

$$
X=\text{temperature}
$$

$$
Y=\text{heating energy usage}
$$

As temperature increases, heating energy may decrease:

$$
X\uparrow \Rightarrow Y\downarrow
$$

We expect **negative covariance**.

So covariance asks:

> **When one variable moves away from its average, does the other variable tend to move in the same direction or the opposite direction?**

---

# 2. Remember Deviation From the Mean

This is something you've already learned.

Suppose:

$$
X=[1,2,3,4,5]
$$

Mean:

$$
\bar{x}=3
$$

For each value, calculate its deviation from the mean:

$$
x_i-\bar{x}
$$

We get:

| \(x_i\) | \(x_i-\bar{x}\) |
| ------: | --------------: |
|       1 |              -2 |
|       2 |              -1 |
|       3 |               0 |
|       4 |              +1 |
|       5 |              +2 |

This tells us whether each value is:

- below the mean → negative
- equal to mean → zero
- above the mean → positive.

---

# 3. Now Do the Same for \(Y\)

Suppose:

$$
Y=[2,4,6,8,10]
$$

Mean:

$$
\bar{y}=6
$$

Deviations:

| \(y_i\) | \(y_i-\bar{y}\) |
| ------: | --------------: |
|       2 |              -4 |
|       4 |              -2 |
|       6 |               0 |
|       8 |              +2 |
|      10 |              +4 |

Now put both variables together.

| \(X\) | \(Y\) | \(X-\bar X\) | \(Y-\bar Y\) |
| ----: | ----: | -----------: | -----------: |
|     1 |     2 |           -2 |           -4 |
|     2 |     4 |           -1 |           -2 |
|     3 |     6 |            0 |            0 |
|     4 |     8 |           +1 |           +2 |
|     5 |    10 |           +2 |           +4 |

Look at the signs.

---

# 4. The Magic: Multiply the Deviations

Calculate:

$$
(x_i-\bar{x})(y_i-\bar{y})
$$

For the first observation:

$$
(-2)(-4)=8
$$

Second:

$$
(-1)(-2)=2
$$

Third:

$$
(0)(0)=0
$$

Fourth:

$$
(1)(2)=2
$$

Fifth:

$$
(2)(4)=8
$$

So:

$$
[8,2,0,2,8]
$$

All are non-negative.

Why?

Because \(X\) and \(Y\) tend to move in the **same direction relative to their means**.

---

# 5. This Is the Heart of Covariance

This is the most important idea in today's lesson:

> **Covariance looks at the product of the deviations of two variables from their means.**

If both move above their means:

$$
(+)(+)=+
$$

If both move below their means:

$$
(-)(-)=+
$$

So:

$$
\boxed{\text{same direction}\Rightarrow\text{positive covariance}}
$$

But if one is above its mean and the other below:

$$
(+)(-) = -
$$

Therefore:

$$
\boxed{\text{opposite directions}\Rightarrow\text{negative covariance}}
$$

---

# 6. Covariance Formula

For a **population**, covariance is:

$$
\boxed{
\operatorname{Cov}(X,Y)
=
\frac{1}{N}
\sum_{i=1}^{N}
(x_i-\mu_X)(y_i-\mu_Y)
}
$$

Let's decode every symbol.

### \(\operatorname{Cov}(X,Y)\)

Covariance between \(X\) and \(Y\).

### \(N\)

Number of observations in the population.

### \(x_i\)

The \(i\)-th value of \(X\).

### \(y_i\)

The \(i\)-th value of \(Y\).

### \(\mu_X\)

Mean of \(X\).

### \(\mu_Y\)

Mean of \(Y\).

### \(\sum\)

Add all the products.

So in plain English:

> **Subtract each variable's mean, multiply the two deviations, add all those products, then divide by the number of observations.**

---

# 7. Calculate It Completely

Using:

$$
X=[1,2,3,4,5]
$$

$$
Y=[2,4,6,8,10]
$$

We already calculated:

$$
\text{products}=[8,2,0,2,8]
$$

Sum:

$$
8+2+0+2+8=20
$$

There are:

$$
N=5
$$

observations.

Therefore:

$$
\operatorname{Cov}(X,Y)=\frac{20}{5}
$$

$$
\boxed{\operatorname{Cov}(X,Y)=4}
$$

Positive covariance.

---

# 8. Negative Covariance

Let's reverse \(Y\):

$$
X=[1,2,3,4,5]
$$

$$
Y=[10,8,6,4,2]
$$

Means:

$$
\bar{x}=3
$$

$$
\bar{y}=6
$$

Deviations:

| \(X-\bar X\) | \(Y-\bar Y\) |
| -----------: | -----------: |
|           -2 |           +4 |
|           -1 |           +2 |
|            0 |            0 |
|           +1 |           -2 |
|           +2 |           -4 |

Now multiply:

$$
(-2)(4)=-8
$$

$$
(-1)(2)=-2
$$

$$
0(0)=0
$$

$$
(1)(-2)=-2
$$

$$
(2)(-4)=-8
$$

Sum:

$$
-8-2+0-2-8=-20
$$

Divide by 5:

$$
\boxed{\operatorname{Cov}(X,Y)=-4}
$$

Negative covariance.

---

# 9. Zero Covariance

If positive and negative products cancel out:

$$
\sum(x_i-\bar{x})(y_i-\bar{y})\approx0
$$

then:

$$
\operatorname{Cov}(X,Y)\approx0
$$

This means there is little **linear co-movement** detected by covariance.

But remember our correlation lesson:

> Zero covariance does not necessarily mean "no relationship whatsoever."

A nonlinear relationship can still exist.

---

# 10. The Dance Analogy 💃🕺

Imagine two dancers.

### Positive covariance

They move together:

```text id="yrzv0t"
X: ↑  ↑  ↑  ↓  ↓
Y: ↑  ↑  ↑  ↓  ↓
```

Their movements generally match.

$$
\boxed{\text{Positive covariance}}
$$

---

### Negative covariance

One moves up while the other moves down:

```text id="v7kqvi"
X: ↑  ↑  ↑  ↓  ↓
Y: ↓  ↓  ↓  ↑  ↑
```

$$
\boxed{\text{Negative covariance}}
$$

---

### Zero covariance

No consistent directional relationship:

```text id="r3zjxi"
X: ↑ ↓ ↑ ↑ ↓
Y: ↓ ↑ ↓ ↑ ↑
```

$$
\boxed{\text{Covariance}\approx0}
$$

This is the core intuition.

---

# 11. Why Not Just Multiply \(X\) and \(Y\)?

You might ask:

> Why do we subtract the means first?

Because we're interested in **how the variables move relative to their centers**.

Suppose:

$$
X=[100,101,102]
$$

and:

$$
Y=[200,202,204]
$$

The raw values are large.

But what matters for covariance is:

$$
X-\bar X
$$

and:

$$
Y-\bar Y.
$$

We want to understand their **co-movement**, not simply whether large numbers multiply into large numbers.

---

# 12. Covariance Is About "Co-Movement"

Break the word apart:

**Co + variance**

Variance asks:

> How much does one variable vary?

Covariance asks:

> How do two variables vary **together**?

That's why:

$$
\boxed{\text{Covariance = joint variation}}
$$

or more intuitively:

$$
\boxed{\text{Covariance = how two variables move together}}
$$

---

# 13. Connection to Variance

This is beautiful mathematically.

Remember variance:

$$
\operatorname{Var}(X)
=
\frac1N\sum(x_i-\mu_X)^2
$$

Look at covariance:

$$
\operatorname{Cov}(X,Y)
=
\frac1N
\sum
(x_i-\mu_X)(y_i-\mu_Y)
$$

What happens if:

$$
Y=X?
$$

Then:

$$
\operatorname{Cov}(X,X)
=
\frac1N
\sum
(x_i-\mu_X)^2
$$

That's exactly variance.

Therefore:

$$
\boxed{\operatorname{Cov}(X,X)=\operatorname{Var}(X)}
$$

This is a very important relationship.

---

# 14. Covariance Matrix

Now we're going to connect covariance to something you already learned:

> **Matrices.**

Suppose we have three variables:

$$
X_1,X_2,X_3
$$

We can calculate covariance between every pair.

We get:

$$
\boxed{
\Sigma=
\begin{bmatrix}
\operatorname{Var}(X_1)&\operatorname{Cov}(X_1,X_2)&\operatorname{Cov}(X_1,X_3)\\
\operatorname{Cov}(X_2,X_1)&\operatorname{Var}(X_2)&\operatorname{Cov}(X_2,X_3)\\
\operatorname{Cov}(X_3,X_1)&\operatorname{Cov}(X_3,X_2)&\operatorname{Var}(X_3)
\end{bmatrix}
}
$$

This is the:

$$
\boxed{\text{Covariance Matrix}}
$$

---

# 15. Why Are the Diagonal Elements Variances?

Look at the first diagonal element:

$$
\operatorname{Cov}(X_1,X_1)
$$

But we just proved:

$$
\operatorname{Cov}(X,X)=\operatorname{Var}(X)
$$

Therefore:

$$
\Sigma_{11}=\operatorname{Var}(X_1)
$$

Similarly:

$$
\Sigma_{22}=\operatorname{Var}(X_2)
$$

and:

$$
\Sigma_{33}=\operatorname{Var}(X_3)
$$

So:

```text id="9tw0pc"
             X1       X2       X3
        ┌────────┬────────┬────────┐
X1      │ Var X1 │ Cov12  │ Cov13  │
        ├────────┼────────┼────────┤
X2      │ Cov21  │ Var X2 │ Cov23  │
        ├────────┼────────┼────────┤
X3      │ Cov31  │ Cov32  │ Var X3 │
        └────────┴────────┴────────┘
```

---

# 16. Covariance Is Symmetric

Usually:

$$
\operatorname{Cov}(X,Y)=\operatorname{Cov}(Y,X)
$$

Why?

Because multiplication is commutative:

$$
ab=ba
$$

Therefore:

$$
(x_i-\mu_X)(y_i-\mu_Y)
=
(y_i-\mu_Y)(x_i-\mu_X)
$$

So the covariance matrix is symmetric:

$$
\boxed{\Sigma=\Sigma^T}
$$

This connects directly to the transpose concept you learned earlier.

---

# 17. The Big Problem With Covariance

Covariance is useful, but there's a problem.

### Units matter.

Suppose:

$$
X=\text{height in meters}
$$

and:

$$
Y=\text{weight in kilograms}.
$$

Then covariance has units:

$$
\text{meters}\times\text{kilograms}
$$

Now change height from meters to centimeters.

The numerical covariance changes.

So covariance's magnitude isn't easy to interpret universally.

For example:

$$
\operatorname{Cov}(X,Y)=50
$$

Is that large?

Small?

We can't answer without knowing the scales and units.

---

# 18. Enter Correlation

This is exactly why correlation is so useful.

We normalize covariance using the standard deviations:

$$
\boxed{
r=
\frac{\operatorname{Cov}(X,Y)}
{\sigma_X\sigma_Y}
}
$$

where:

- \(r\) = correlation
- \(\operatorname{Cov}(X,Y)\) = covariance
- \(\sigma_X\) = standard deviation of \(X\)
- \(\sigma_Y\) = standard deviation of \(Y\).

And now:

$$
\boxed{-1\le r\le1}
$$

---

# 19. The Beautiful Relationship

Now you can see the whole chain:

$$
\boxed{
\text{Variance}
\rightarrow
\text{Covariance}
\rightarrow
\text{Correlation}
}
$$

More explicitly:

### Variance

One variable's spread:

$$
\operatorname{Var}(X)
$$

### Covariance

Two variables' joint movement:

$$
\operatorname{Cov}(X,Y)
$$

### Correlation

Normalized joint movement:

$$
r=
\frac{\operatorname{Cov}(X,Y)}
{\sigma_X\sigma_Y}
$$

This is one of the most important statistical connections you've learned so far.

---

# 20. Why Correlation Has No Units

Suppose covariance has units:

$$
\text{meters}\cdot\text{kilograms}
$$

Standard deviations have units:

$$
\sigma_X=\text{meters}
$$

$$
\sigma_Y=\text{kilograms}
$$

Therefore:

$$
\frac{
\text{meters}\cdot\text{kilograms}
}{
\text{meters}\cdot\text{kilograms}
}
$$

The units cancel.

So correlation is:

$$
\boxed{\text{unitless}}
$$

That's one reason it is much easier to compare across datasets and variables.

---

# 21. ML Example

Suppose your dataset contains:

$$
X_1=\text{study hours}
$$

$$
X_2=\text{sleep hours}
$$

$$
Y=\text{exam score}
$$

You might calculate:

$$
\operatorname{Cov}(X_1,Y)>0
$$

meaning study hours and score tend to move together.

You might also find:

$$
\operatorname{Cov}(X_2,Y)>0
$$

meaning sleep and score tend to move together.

But covariance magnitude depends on units.

So you might instead examine:

$$
r(X_1,Y)
$$

and:

$$
r(X_2,Y)
$$

to get standardized measures of linear association.

---

# 22. Feature Relationships

Suppose:

$$
r(X_1,X_2)=0.95
$$

This means the two features have a very strong positive linear association.

In some ML models, highly correlated features can create issues related to:

$$
\boxed{\text{multicollinearity}}
$$

For example:

```text id="9msv8d"
House Size ──────────┐
                     ├── strongly related
Number of Rooms ─────┘
```

They may contain overlapping information.

We'll study this later.

---

# 23. Scientific Computing Example

Suppose you have two sensors:

$$
X=\text{temperature sensor}
$$

$$
Y=\text{pressure sensor}
$$

You collect many measurements.

Covariance can tell you whether deviations from their respective means tend to occur together.

For example:

$$
\operatorname{Cov}(X,Y)>0
$$

means:

> When temperature tends to be above its average, pressure also tends to be above its average, and vice versa.

This can help identify relationships between experimental variables.

---

# 24. Quantum / Physics Connection

Covariance has an especially interesting role in physics.

Suppose you have two measured quantities:

$$
A
$$

and:

$$
B.
$$

You can ask whether their fluctuations around their means are related.

The basic classical covariance idea is:

$$
\operatorname{Cov}(A,B)
=
E[(A-E[A])(B-E[B])]
$$

In quantum mechanics, closely related ideas appear in **quantum covariance**, fluctuations, and correlations between observables.

For a quantum observable \(A\):

$$
\operatorname{Var}(A)
=
\langle A^2\rangle-\langle A\rangle^2.
$$

So the statistics you've been learning are directly connected to the mathematical language of physics.

---

# 25. Covariance and Correlation: Don't Confuse Them

| Concept     | Question                                                                  |
| ----------- | ------------------------------------------------------------------------- |
| Variance    | How much does one variable vary?                                          |
| Covariance  | How do two variables vary together?                                       |
| Correlation | How strongly do two variables linearly vary together after normalization? |

And:

$$
\boxed{\operatorname{Cov}(X,X)=\operatorname{Var}(X)}
$$

$$
\boxed{
r=\frac{\operatorname{Cov}(X,Y)}
{\sigma_X\sigma_Y}
}
$$

---

# 26. A Critical Limitation

Just like correlation:

> **Covariance mainly captures linear co-movement.**

For example:

$$
Y=X^2
$$

can have:

$$
\operatorname{Cov}(X,Y)=0
$$

for a symmetric distribution of \(X\), even though \(Y\) is completely determined by \(X\).

So:

$$
\boxed{\text{Zero covariance does not mean independence}}
$$

This distinction becomes very important in probability and ML.

---

# 27. Covariance vs Independence

If two variables are independent, then under appropriate conditions:

$$
\boxed{\operatorname{Cov}(X,Y)=0}
$$

But the reverse is **not generally true**.

That means:

$$
\boxed{
\text{Independence}
\Rightarrow
\text{zero covariance}
}
$$

but generally:

$$
\boxed{
\text{zero covariance}
\not\Rightarrow
\text{independence}
}
$$

This is a very important statistical fact.

For jointly Gaussian variables, there is a special stronger relationship, which we'll encounter later.

---

# 28. NumPy Preview

Later, NumPy can calculate covariance using:

```python
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

np.cov(x, y)
```

You'll get a covariance matrix conceptually like:

$$
\begin{bmatrix}
\operatorname{Var}(X)&\operatorname{Cov}(X,Y)\\
\operatorname{Cov}(Y,X)&\operatorname{Var}(Y)
\end{bmatrix}
$$

And:

```python
np.corrcoef(x, y)
```

gives the corresponding correlation matrix.

We'll later learn the NumPy details carefully, including the important distinction between **population and sample covariance**.

---

# 29. The Deepest Mental Model

Think of every observation as a pair:

$$
(x_i,y_i)
$$

Now draw a vertical and horizontal line through the means:

```text id="f3s6jm"
                  Y
                  ↑
        II        │        I
                  │
     negative     │     positive
       product    │       product
──────────────────┼──────────────────→ X
                  │
        III       │        IV
                  │
```

The means divide the plane into four regions.

### Upper-right

Both above mean:

$$
(+)(+)=+
$$

### Lower-left

Both below mean:

$$
(-)(-)=+
$$

→ positive covariance contribution.

### Upper-left

X below mean, Y above mean:

$$
(-)(+) = -
$$

### Lower-right

X above mean, Y below mean:

$$
(+)(-) = -
$$

→ negative covariance contribution.

This picture explains covariance almost completely.

---

# 30. Your Statistical Structure Is Becoming Powerful

You now understand:

```text id="xihwsv"
                       DATA
                         │
              ┌──────────┴──────────┐
              ↓                     ↓
          One variable          Two variables
              │                     │
              ↓                     ↓
           Variance             Covariance
              │                     │
              │                     ↓
              │              Normalize by SDs
              │                     │
              └──────────────→ Correlation
```

Mathematically:

$$
\boxed{
\operatorname{Var}(X)
=
\operatorname{Cov}(X,X)
}
$$

and:

$$
\boxed{
r=
\frac{\operatorname{Cov}(X,Y)}
{\sigma_X\sigma_Y}
}
$$

---

# 🧠 Lesson 22 Cheat Sheet

### Covariance:

$$
\boxed{
\operatorname{Cov}(X,Y)
=
\frac1N
\sum_{i=1}^{N}
(x_i-\mu_X)(y_i-\mu_Y)
}
$$

### Interpretation

$$
\operatorname{Cov}>0
$$

→ tend to move together.

$$
\operatorname{Cov}<0
$$

→ tend to move oppositely.

$$
\operatorname{Cov}\approx0
$$

→ little linear co-movement.

### Relationship with variance:

$$
\boxed{\operatorname{Cov}(X,X)=\operatorname{Var}(X)}
$$

### Relationship with correlation:

$$
\boxed{
r=
\frac{\operatorname{Cov}(X,Y)}
{\sigma_X\sigma_Y}
}
$$

### Most important warning:

$$
\boxed{
\text{Correlation/Covariance}\neq\text{Causation}
}
$$

and:

$$
\boxed{
\text{Zero covariance}\not\Rightarrow\text{independence}
}
$$

---

# 🧪 Practice

### Q1

In your own words, what does covariance measure?

### Q2

If:

$$
\operatorname{Cov}(X,Y)>0
$$

what does that suggest?

### Q3

If:

$$
\operatorname{Cov}(X,Y)<0
$$

what does that suggest?

### Q4

Why do we subtract the mean before calculating covariance?

### Q5

What happens when:

$$
X=Y?
$$

Specifically, what does covariance become?

### Q6

Why is covariance harder to interpret across variables with different units?

### Q7

How does correlation solve this problem?

### Q8

True or false:

> If covariance is zero, the variables must be independent.

### Q9

Suppose:

$$
X=[1,2,3]
$$

$$
Y=[2,4,6]
$$

What are:

$$
\bar X,\quad\bar Y?
$$

### Q10

Using the population covariance formula, calculate:

$$
\operatorname{Cov}(X,Y)
$$

for the same data.

---

# Answers

### Q1

Covariance measures how two variables tend to vary together relative to their means.

### Q2

They tend to move in the same direction.

### Q3

They tend to move in opposite directions.

### Q4

To determine whether each value is above or below its variable's center and then examine whether the two deviations move together.

### Q5

$$
\boxed{\operatorname{Cov}(X,X)=\operatorname{Var}(X)}
$$

### Q6

Because covariance depends on the units and scale of the variables.

### Q7

It divides covariance by the standard deviations:

$$
r=\frac{\operatorname{Cov}(X,Y)}
{\sigma_X\sigma_Y}
$$

making it unitless and bounded between \(-1\) and \(1\).

### Q8

False.

$$
\boxed{\text{Zero covariance does not generally imply independence.}}
$$

### Q9

$$
\bar X=\frac{1+2+3}{3}=2
$$

$$
\bar Y=\frac{2+4+6}{3}=4
$$

Therefore:

$$
\boxed{\bar X=2,\quad\bar Y=4}
$$

### Q10

Deviations:

$$
X-\bar X=[-1,0,1]
$$

$$
Y-\bar Y=[-2,0,2]
$$

Products:

$$
[2,0,2]
$$

Sum:

$$
4
$$

Divide by \(N=3\):

$$
\boxed{\operatorname{Cov}(X,Y)=\frac43\approx1.33}
$$

---

## Where We Go Next

You've now built the complete foundation for understanding relationships between variables:

$$
\boxed{
\text{Variance}
\rightarrow
\text{Covariance}
\rightarrow
\text{Correlation}
}
$$

The next major topic should be **Sampling & Population vs Sample Statistics**.

We'll answer a fundamental statistical question:

> **If we only have a small sample of data, how can we use it to learn something about a much larger population?**

This is the foundation for **sample mean, sample variance, \(n-1\), estimation, confidence intervals, hypothesis testing, and eventually statistical learning**.
