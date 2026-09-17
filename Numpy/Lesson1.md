---
---

Since your goal is ML, I want to build NumPy alongside the **mathematics + statistics that NumPy is actually implementing**. If you understand the mathematical idea first, NumPy becomes much easier to remember.

## Our learning method

For **every NumPy concept**, we will follow this cycle:

> **Real-world problem → Mathematical idea → Statistical idea → NumPy concept → NumPy implementation → ML application → When/where/why ML uses it → Practice**

For example:

**Problem:** We have students' exam scores and want to know their typical performance.

→ Mathematics: addition and division
→ Statistics: mean
→ NumPy: `np.mean()`
→ ML: mean is used in normalization, loss calculations, imputation, evaluation, etc.

And we'll always ask:

> **"What problem does this solve?"**

rather than just memorizing functions.

---

# 🗺️ Our NumPy + Math + Statistics Roadmap

We will go **one step at a time**.

### Phase 0 — Mathematical Foundation

Before NumPy:

1. Numbers and variables
2. Arithmetic
3. Fractions and percentages
4. Ratios
5. Powers and roots
6. Algebra
7. Functions
8. Coordinates
9. Vectors
10. Matrices
11. Summation notation
12. Basic probability

---

### Phase 1 — Statistics Foundation

Then:

1. What is data?
2. Population vs sample
3. Mean
4. Median
5. Mode
6. Range
7. Variance
8. Standard deviation
9. Percentiles
10. Quartiles
11. IQR
12. Distribution
13. Probability distributions
14. Correlation
15. Covariance
16. Outliers
17. Sampling
18. Basic statistical intuition

---

### Phase 2 — NumPy Foundation

Then NumPy:

1. What NumPy is
2. Why NumPy exists
3. `ndarray`
4. Creating arrays
5. Shape
6. Dimensions
7. Data types
8. Indexing
9. Slicing
10. Reshaping
11. Flattening
12. Concatenation
13. Stacking
14. Broadcasting
15. Vectorization

---

### Phase 3 — NumPy Through Statistics

Now we'll connect them:

```text
Statistics             NumPy
--------------------------------
Mean                →  np.mean()
Median              →  np.median()
Variance             →  np.var()
Standard deviation  →  np.std()
Minimum             →  np.min()
Maximum             →  np.max()
Percentile          →  np.percentile()
Correlation         →  np.corrcoef()
```

But importantly, you will understand **what each calculation means before learning the function**.

---

### Phase 4 — NumPy for ML

Then:

```text
Dataset
   ↓
NumPy arrays
   ↓
Features / targets
   ↓
Mathematical operations
   ↓
Statistics
   ↓
Scaling / normalization
   ↓
Distance calculations
   ↓
Linear algebra
   ↓
ML algorithms
```

We'll eventually cover things like:

- feature matrices
- target vectors
- train/test data
- normalization
- standardization
- dot products
- matrix multiplication
- distances
- predictions
- errors
- MSE
- RMSE
- gradients
- vectorization
- batch operations

---

# 🚀 Lesson 1 — What Is Data?

**We will stop here today.**

Before learning even `np.array()`, you need to understand what we're actually putting inside an array.

---

## 1. Imagine you're running a small experiment

Suppose you ask 5 students:

> "How many hours did you study yesterday?"

You get:

```text
Student A → 2 hours
Student B → 4 hours
Student C → 3 hours
Student D → 5 hours
Student E → 1 hour
```

We can write this as:

$$
2,\ 4,\ 3,\ 5,\ 1
$$

This collection of measurements is called **data**.

That's all data is at its simplest:

> **Information collected about something we care about.**

---

# 2. What is a data point?

Each individual observation is a **data point**.

For example:

```text
2
```

is one data point.

And:

```text
2, 4, 3, 5, 1
```

contains five data points.

Think of a **basket of apples**.

```text
🍎 🍎 🍎 🍎 🍎
```

Each apple is an individual object.

Similarly:

```text
2  4  3  5  1
↑  ↑  ↑  ↑  ↑
```

Each number is an individual observation.

---

# 3. What is a variable?

Now imagine we repeat the experiment.

Instead of only asking:

> "How many hours did you study?"

we ask:

- study hours
- sleep hours
- attendance
- exam score

For one student:

| Student | Study Hours | Sleep Hours | Attendance | Score |
| ------- | ----------: | ----------: | ---------: | ----: |
| A       |           2 |           7 |         80 |    65 |
| B       |           4 |           6 |         90 |    78 |
| C       |           3 |           8 |         85 |    72 |
| D       |           5 |           6 |         95 |    88 |
| E       |           1 |           8 |         70 |    55 |

Here:

**Study Hours** is a variable.

**Sleep Hours** is a variable.

**Attendance** is a variable.

**Score** is a variable.

A variable is simply:

> **A characteristic whose value can differ from one observation to another.**

---

# 4. Why do we care about variables in ML?

Because **machine learning learns relationships between variables**.

Suppose we want to predict exam score.

We might have:

```text
Study Hours ─────┐
                 │
Sleep Hours ─────┤
                 ├──→ ML Model ──→ Predicted Score
Attendance ──────┘
```

The input variables are called **features**.

So:

$$
X = \text{features}
$$

And the thing we're trying to predict is usually called the **target**.

$$
y = \text{target}
$$

For example:

```text
Features (X)                Target (y)

Study   Sleep   Attendance  Score
  2       7        80        65
  4       6        90        78
  3       8        85        72
  5       6        95        88
  1       8        70        55
```

This distinction will become **extremely important** when we start using NumPy.

---

# 5. From a table to mathematics

Look at our table:

$$
\begin{array}{ccc}
2 & 7 & 80\\
4 & 6 & 90\\
3 & 8 & 85\\
5 & 6 & 95\\
1 & 8 & 70
\end{array}
$$

This is more than just a table.

Mathematically, it is a **matrix**.

We can call it \(X\):

$$
X =
\begin{bmatrix}
2 & 7 & 80\\
4 & 6 & 90\\
3 & 8 & 85\\
5 & 6 & 95\\
1 & 8 & 70
\end{bmatrix}
$$

And the scores become a vector:

$$
y =
\begin{bmatrix}
65\\
78\\
72\\
88\\
55
\end{bmatrix}
$$

This is where mathematics, statistics, NumPy, and ML start connecting.

---

# 6. The important mental model

Remember this picture:

```text
                    DATA
                      │
             ┌────────┴────────┐
             │                 │
          FEATURES           TARGET
             │                 │
             X                 y
             │                 │
             └────────┬────────┘
                      ↓
                MACHINE LEARNING
```

And eventually:

```text
Real World
    ↓
Collect Data
    ↓
Represent Data Mathematically
    ↓
NumPy Arrays
    ↓
Statistics + Mathematics
    ↓
ML Algorithm
    ↓
Prediction
```

---

# 7. Why NumPy enters the story

Imagine having:

**5 students**.

Easy.

But real ML datasets might contain:

```text
1,000,000 students
×
100 features
```

That's:

$$
100,000,000
$$

numbers.

You obviously don't want to manually perform calculations on them.

You want the computer to efficiently perform operations such as:

$$
\text{mean}
$$

$$
\text{variance}
$$

$$
X - \mu
$$

$$
\frac{X-\mu}{\sigma}
$$

$$
X^TX
$$

etc.

**NumPy is one of the fundamental tools that lets Python work efficiently with numerical data.**

But notice something important:

> NumPy isn't the mathematics itself.

NumPy is a **tool for performing the mathematics efficiently**.

---

# 🧠 The analogy we'll use throughout this course

Imagine you're learning physics.

You know:

$$
F = ma
$$

The equation is the **concept**.

A calculator is the **tool** used to calculate it.

Similarly:

### Statistics

$$
\mu = \frac{x_1+x_2+\cdots+x_n}{n}
$$

is the mathematical concept.

### NumPy

```python
np.mean(x)
```

is the tool that performs the calculation.

So our learning order will always be:

```text
UNDERSTAND
    ↓
MATHEMATICS
    ↓
STATISTICS
    ↓
NUMPY
    ↓
ML APPLICATION
```

**Never the other way around.**

---

# 🎯 Your first ML connection

Suppose:

```text
Study Hours
2
4
3
5
1
```

We might eventually ask:

> "What is the average study time?"

Mathematically:

$$
\text{Average}
=
\frac{2+4+3+5+1}{5}
$$

$$
=\frac{15}{5}
$$

$$
=3
$$

So the average student studied:

$$
\boxed{3\text{ hours}}
$$

Later NumPy will allow us to do this with a single operation.

And later still, you'll discover that the **same idea of averages appears inside ML algorithms**.

That's why we're building the foundation first.

---

# 🧩 One distinction you should understand now

Don't confuse these three things:

### Observation

One particular measurement.

```text
4 hours
```

### Variable

The thing we're measuring.

```text
Study Hours
```

### Dataset

The collection of observations.

```text
2, 4, 3, 5, 1
```

Think:

> **Variable = question**
> **Observation = one answer**
> **Dataset = all answers**

---

# 🛑 Stop here

Don't learn `np.array()` yet.

Before we touch NumPy, the **next foundation concept** should be:

## **Numbers → Variables → Arithmetic → Functions**

especially:

### **What does a variable actually mean mathematically?**

We'll then build toward **vectors and matrices**, because those are the bridge between statistics, NumPy, and ML.

When you're ready, say **"next"** and we'll do **Foundation 2: Variables & Arithmetic**, from absolute zero, with ML examples.
