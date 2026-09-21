# Lesson 37 — NumPy Indexing: How to Access Data Inside Arrays

Last lesson we learned **how to create arrays**.

Now we need to answer a very important question:

> **Once I have an array, how do I get a particular value from it?**

That's the job of **indexing**.

This is fundamental because later, when we work with ML datasets, scientific measurements, images, and quantum states, we constantly need to access specific pieces of data.

---

# 1. The Core Idea

Suppose we have:

```python
import numpy as np

x = np.array([10, 20, 30, 40, 50])
```

Think of the array as boxes:

```text
Index:    0    1    2    3    4
          ↓    ↓    ↓    ↓    ↓
Value:   10   20   30   40   50
```

The **index** tells NumPy which position you want.

So:

```python
x[0]
```

means:

> Give me the value at position 0.

Result:

```text
10
```

---

# 2. Why Does Indexing Start at 0?

This is extremely important.

Python and NumPy use **zero-based indexing**.

So:

```text
Position:  1    2    3    4    5
Index:     0    1    2    3    4
```

Therefore:

```python
x[1]
```

is:

```text
20
```

not 10.

### Mental model

Don't think:

> "I want the first value."

Think:

> "I want the value whose index is 0."

---

# 3. Basic 1D Indexing

Given:

```python
x = np.array([10, 20, 30, 40, 50])
```

we have:

```python
x[0]   # 10
x[1]   # 20
x[2]   # 30
x[3]   # 40
x[4]   # 50
```

So:

$$
x_i
$$

in mathematics corresponds conceptually to accessing an element of an array using its index.

---

# 4. Negative Indexing

NumPy also lets us count from the end.

```text
Index:       0    1    2    3    4
             ↓    ↓    ↓    ↓    ↓
Value:      10   20   30   40   50
Negative:   -5   -4   -3   -2   -1
```

Therefore:

```python
x[-1]
```

gives:

```text
50
```

and:

```python
x[-2]
```

gives:

```text
40
```

This is extremely convenient when you want the last element.

---

# 5. Why Negative Indexing Is Useful

Suppose you have 10,000 experimental measurements.

You don't need to know the length to get the final measurement:

```python
measurements[-1]
```

means:

> Give me the last measurement.

Similarly:

```python
measurements[-2]
```

means:

> Give me the second-last measurement.

---

# 6. Indexing a 2D Array

Now things become more interesting.

Consider our ML dataset:

```python
X = np.array([
    [2, 7, 80],
    [4, 6, 90],
    [3, 8, 85],
    [5, 6, 95],
    [1, 8, 70]
])
```

Visualize it with indices:

```text
             Column
             0    1    2

Row 0       [2    7   80]
Row 1       [4    6   90]
Row 2       [3    8   85]
Row 3       [5    6   95]
Row 4       [1    8   70]
```

We now need **two indices**:

$$
\boxed{\text{row, column}}
$$

---

# 7. Basic 2D Indexing

The syntax is:

```python
X[row, column]
```

For example:

```python
X[0, 0]
```

means:

> Row 0, column 0.

Result:

```text
2
```

---

# 8. More Examples

```python
X[0, 1]
```

→

```text
7
```

because:

```text
       0   1   2
Row 0 [2   7  80]
```

And:

```python
X[0, 2]
```

→

```text
80
```

---

# 9. Another Example

```python
X[3, 1]
```

Look at:

```text
Row 3 → [5, 6, 95]
             ↑
          Column 1
```

Therefore:

$$
X[3,1]=6
$$

---

# 10. The Mental Model

For a 2D array:

$$
\boxed{
X[\text{row},\text{column}]
}
$$

Think:

> **First move vertically to the row, then horizontally to the column.**

For:

```python
X[2, 1]
```

think:

```text
Go to row 2
      ↓
[3, 8, 85]
   ↓
column 1
```

Result:

```text
8
```

---

# 11. Negative Indexing in 2D Arrays

Negative indexing works independently on each axis.

For example:

```python
X[-1, -1]
```

means:

> Last row, last column.

Our matrix:

```text
[2  7  80]
[4  6  90]
[3  8  85]
[5  6  95]
[1  8  70]
```

So:

```python
X[-1, -1]
```

gives:

```text
70
```

---

# 12. Last Row

You can access the last row with:

```python
X[-1]
```

Result:

```text
[1 8 70]
```

This is important.

When you provide only one index for a 2D array:

```python
X[3]
```

NumPy interprets it as:

> Give me row 3.

So:

```python
X[0]
```

→ first row

```python
X[1]
```

→ second row

and:

```python
X[-1]
```

→ last row.

---

# 13. ML Connection

Remember our dataset:

| Study Hours | Sleep | Attendance |
| ----------: | ----: | ---------: |
|           2 |     7 |         80 |
|           4 |     6 |         90 |
|           3 |     8 |         85 |
|           5 |     6 |         95 |
|           1 |     8 |         70 |

Each row represents one student.

Therefore:

```python
X[0]
```

means:

> Give me all features of the first student.

Result:

```text
[2 7 80]
```

And:

```python
X[0, 2]
```

means:

> Give me the third feature of the first student.

Result:

```text
80
```

---

# 14. This Is Why Shape Matters

Last lesson we learned:

```python
X.shape
```

gives:

```text
(5, 3)
```

This tells us:

$$
5\text{ rows},3\text{ columns}
$$

Therefore valid row indices are:

$$
0,1,2,3,4
$$

and valid column indices are:

$$
0,1,2
$$

This is why understanding `shape` before indexing was important.

---

# 15. Out-of-Range Index

Suppose:

```python
x = np.array([10, 20, 30])
```

Its indices are:

```text
0  1  2
```

What happens if we write:

```python
x[3]
```

There is no index 3.

NumPy raises an:

```text
IndexError
```

This is similar to asking:

> "Give me the fourth box"

when only three boxes exist.

---

# 16. Mathematical Connection

Remember vectors:

$$
\mathbf{x}
=
\begin{bmatrix}
5\\
7\\
90
\end{bmatrix}
$$

We can think of the components as:

$$
x_0=5
$$

$$
x_1=7
$$

$$
x_2=90
$$

In NumPy:

```python
x[0]
x[1]
x[2]
```

So indexing is the computational way of accessing mathematical components.

---

# 17. Physics Example

Suppose we measure the position of a particle at different times:

```python
x = np.array([
    0.0,
    0.5,
    1.1,
    1.8,
    2.6
])
```

Then:

```python
x[0]
```

is the first recorded position.

And:

```python
x[-1]
```

is the final recorded position.

We could calculate the displacement between them:

$$
\Delta x=x_{\text{final}}-x_{\text{initial}}
$$

which computationally could be:

```python
x[-1] - x[0]
```

giving:

$$
2.6-0=2.6
$$

Notice how mathematics and NumPy map directly onto one another.

---

# 18. Quantum Example ⚛️

Consider a two-level state:

$$
|\psi\rangle=
\begin{bmatrix}
\alpha\\
\beta
\end{bmatrix}
$$

In NumPy:

```python
psi = np.array([alpha, beta])
```

Then:

```python
psi[0]
```

represents:

$$
\alpha
$$

and:

```python
psi[1]
```

represents:

$$
\beta
$$

So indexing is not some arbitrary programming trick.

It gives us direct access to mathematical components of physical objects.

---

# 19. Complex Numbers

Quantum mechanics often requires complex numbers.

For example:

$$
\alpha=0.6+0.2i
$$

NumPy supports this.

```python
psi = np.array([
    0.6 + 0.2j,
    0.7 - 0.1j
])
```

Then:

```python
psi[0]
```

accesses the first complex amplitude.

This is one reason NumPy is particularly important for scientific and quantum computing.

---

# 20. One More Important Idea — Assignment

Indexing isn't only for **reading** values.

You can also **change** them.

For example:

```python
x = np.array([10, 20, 30, 40])
```

Then:

```python
x[2] = 100
```

Now:

```text
[10 20 100 40]
```

So:

$$
x_2:30\rightarrow100
$$

---

# 21. Why This Matters

Imagine experimental data:

```python
measurements = np.array([10.2, 10.5, 99.9, 10.3])
```

Suppose you discover that the third measurement was entered incorrectly.

You can change it:

```python
measurements[2] = 10.0
```

But be careful:

> **Never blindly modify experimental data just because one value looks unusual.**

It might be a genuine physical event.

That's where our earlier lessons on **outliers, distributions, and statistical reasoning** become important.

This is a great example of why we're learning mathematics before blindly manipulating data.

---

# 22. Boolean Thinking — Preview

Later you'll learn that we can ask NumPy questions such as:

```python
x > 30
```

For example:

```python
x = np.array([10, 20, 40, 50])
```

Then:

```python
x > 30
```

conceptually produces:

```text
[False False True True]
```

This eventually allows us to select data based on conditions.

We won't go deeply into this yet.

That's **Boolean indexing**, which we'll study after basic slicing.

---

# 23. Indexing vs Slicing

This distinction is important.

### Indexing

Gets **one specific element**:

```python
x[2]
```

### Slicing

Gets **a portion of an array**:

```python
x[1:4]
```

We'll study slicing properly in the next lesson.

For now:

$$
\boxed{\text{Indexing = one location}}
$$

$$
\boxed{\text{Slicing = a range of locations}}
$$

---

# 24. The Bigger Picture

We now have:

```text
Create array
     ↓
Understand shape
     ↓
Understand axes
     ↓
Index into array
     ↓
Access specific data
     ↓
Modify specific data
     ↓
Next → Slice pieces of data
```

This is the foundation for manipulating real datasets.

---

# 🧪 Practice

Given:

```python
A = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
```

### Q1

What is:

```python
A[0, 0]
```

### Q2

What is:

```python
A[1, 2]
```

### Q3

What is:

```python
A[-1, -1]
```

### Q4

What does:

```python
A[1]
```

return?

### Q5

How would you access `80`?

### Q6

How would you change `60` to `600`?

### Q7

Given:

```python
x = np.array([5, 10, 15, 20])
```

what does:

```python
x[-1]
```

return?

---

## Answers

### Q1

```text
10
```

### Q2

```text
60
```

### Q3

```text
90
```

### Q4

```text
[40 50 60]
```

### Q5

```python
A[2, 1]
```

### Q6

```python
A[1, 2] = 600
```

### Q7

```text
20
```

---

# 🗺️ Complete Roadmap — Lesson 37

```text
PHASE 0 — MATHEMATICS
━━━━━━━━━━━━━━━━━━━━━━━━━━
Numbers & Variables              ✅
Arithmetic                       ✅
Fractions / Ratios              ✅
Powers / Roots / Logs            ✅
Algebra                          ✅
Functions                        ✅
Coordinates                      ✅
Vectors                          ✅
Matrices                         ✅
Summation                        ✅
Probability                      ✅


PHASE 1 — STATISTICS
━━━━━━━━━━━━━━━━━━━━━━━━━━
Descriptive Statistics           ✅
Probability Distributions        ✅
Sampling                         ✅
Sampling Distribution            ✅
SE / CLT / LLN                    ✅
Confidence Intervals             ✅
Inference                        ✅
Hypothesis Testing               ✅
p-values                         ✅
Effect Size                      ✅
Power / Type I / Type II        ✅


PHASE 2 — NUMPY FOUNDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━
What is NumPy?                  ✅
ndarray                          ✅
Dimensions                       ✅
Shape                            ✅
Axes                             ✅
Size                             ✅
dtype                            ✅

Array Creation                   ✅
 ├── np.array()                  ✅
 ├── np.zeros()                  ✅
 ├── np.ones()                   ✅
 ├── np.full()                   ✅
 ├── np.arange()                 ✅
 ├── np.linspace()               ✅
 ├── np.eye()                    ✅
 └── Random arrays                ✅

Indexing                         🔵 YOU ARE HERE
 ├── 1D indexing                 ✅
 ├── Negative indexing            ✅
 ├── 2D indexing                 ✅
 ├── Row access                  ✅
 └── Element modification        ✅

Slicing                          ⬜ NEXT
Boolean indexing                 ⬜
Reshaping                        ⬜
Flattening                       ⬜
Concatenation                    ⬜
Stacking                         ⬜
Broadcasting                     ⬜
Vectorization                    ⬜


PHASE 3 — NUMPY + STATISTICS
━━━━━━━━━━━━━━━━━━━━━━━━━━
Mean                             ⬜
Variance                         ⬜
Standard Deviation               ⬜
Percentiles                      ⬜
IQR                              ⬜
Covariance                       ⬜
Correlation                      ⬜
Sampling simulations             ⬜
CLT / LLN simulations            ⬜
Confidence intervals             ⬜
Hypothesis testing               ⬜


PHASE 4 — DATA TOOLS
━━━━━━━━━━━━━━━━━━━━━━━━━━
Pandas                           ⬜ ← introduced when tabular
Matplotlib                       ⬜ ← introduced when visualization
SciPy                            ⬜ ← introduced when scientific methods
scikit-learn                     ⬜ ← introduced with ML


PHASE 5 — MACHINE LEARNING
━━━━━━━━━━━━━━━━━━━━━━━━━━
Regression                       ⬜
Classification                   ⬜
Clustering                       ⬜
Trees                            ⬜
SVM                              ⬜
Evaluation                       ⬜
Feature Engineering              ⬜
Cross Validation                 ⬜
Optimization                     ⬜


PHASE 6 — SCIENTIFIC / QUANTUM
━━━━━━━━━━━━━━━━━━━━━━━━━━
Scientific Computing             ⬜
Numerical Simulation             ⬜
Quantum States                   ⬜
Quantum Measurement              ⬜
Quantum Simulation               ⬜
Quantum ML                       ⬜
```

### 🔗 Where NumPy fits right now

We're still building the **mechanical skills of numerical computing**:

$$
\boxed{
\text{Create}
\rightarrow
\text{Understand}
\rightarrow
\text{Access}
\rightarrow
\text{Manipulate}
}
$$

Then we'll start using those skills to computationally revisit the mathematics and statistics you've already learned:

$$
\boxed{
\text{Math}
\rightarrow
\text{Statistics}
\rightarrow
\text{NumPy implementation}
}
$$

For example, you'll eventually see:

$$
\bar{x}=\frac1n\sum_{i=1}^nx_i
$$

become:

```python
np.mean(x)
```

and

$$
\operatorname{Var}(X)
=
\frac1N\sum_i(x_i-\mu)^2
$$

become:

```python
np.var(x)
```

So we're **not learning NumPy functions for the sake of memorization**. We're learning how the mathematics you've already understood becomes executable computation.

---

# 🧠 Final Lesson Paragraph

> **In this lesson we learned NumPy indexing, which is the mechanism used to access individual pieces of data inside an `ndarray`. We learned that NumPy uses zero-based indexing, so the first element has index 0, and we learned negative indexing, where `-1` refers to the last element. For 1D arrays we use `x[index]`, while for 2D arrays we use `X[row, column]`. We connected this directly to our ML feature matrix, where a row represents an observation and a column represents a feature, allowing us to access either an entire observation such as `X[0]` or a particular feature such as `X[0,2]`. We also learned that indexing can be used not only to read values but to modify them, and we connected this to scientific measurements and quantum state vectors, where individual array elements can represent physical quantities or quantum amplitudes. Most importantly, we saw why the earlier concepts of vectors, matrices, dimensions, shape, and axes were necessary: indexing is simply the computational way of locating components within those mathematical structures. We also previewed the distinction between indexing and slicing; indexing selects a specific location, while slicing will allow us to select a range of data. We are therefore progressing from creating numerical structures to actually navigating and manipulating them, and the next major step is learning **slicing**, which will let us work with portions of datasets rather than only individual elements.**
