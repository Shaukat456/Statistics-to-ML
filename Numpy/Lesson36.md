---

---

From now on, we’ll treat **NumPy, Pandas, Matplotlib, SciPy, scikit-learn, etc. as tools introduced when the underlying concept makes them useful**, rather than forcing ourselves through one library completely before touching another.

For example:

$$
\text{NumPy}
\rightarrow
\text{numerical arrays}
$$

$$
\text{Pandas}
\rightarrow
\text{tabular/labelled data}
$$

$$
\text{Matplotlib}
\rightarrow
\text{visualization}
$$

$$
\text{SciPy}
\rightarrow
\text{scientific/numerical methods}
$$

$$
\text{scikit-learn}
\rightarrow
\text{classical ML}
$$

We'll bring each one in **when it solves a problem we have just learned about**.

---

# Lesson 36 — Creating NumPy Arrays

Last lesson we learned what an array **is**.

Today we learn how to **create arrays properly**.

This may sound simple, but array creation is foundational because almost everything in NumPy starts with:

$$
\boxed{\text{Create the numerical structure first}}
$$

Then we manipulate it.

---

# 1. The Most Basic Method — `np.array()`

You already saw:

```python
import numpy as np

x = np.array([1, 2, 3, 4])
```

This converts a Python sequence into a NumPy array.

Think:

```text
Python data
     ↓
np.array()
     ↓
NumPy ndarray
```

---

# 2. Creating a 1D Array

```python
x = np.array([10, 20, 30, 40, 50])
```

We get:

$$
x=
\begin{bmatrix}
10&20&30&40&50
\end{bmatrix}
$$

Its properties:

```python
x.ndim
```

→

```text
1
```

and:

```python
x.shape
```

→

```text
(5,)
```

and:

```python
x.size
```

→

```text
5
```

---

# 3. Creating a 2D Array

Remember our ML dataset:

```python
X = np.array([
    [2, 7, 80],
    [4, 6, 90],
    [3, 8, 85],
    [5, 6, 95],
    [1, 8, 70]
])
```

This gives:

$$
X=
\begin{bmatrix}
2&7&80\\
4&6&90\\
3&8&85\\
5&6&95\\
1&8&70
\end{bmatrix}
$$

and:

```python
X.shape
```

→

```text
(5, 3)
```

So:

$$
5\text{ observations}\times3\text{ features}
$$

---

# 4. The Important Rule for 2D Arrays

Notice this:

```python
X = np.array([
    [2, 7, 80],
    [4, 6, 90],
    [3, 8, 85]
])
```

Each inner list represents a **row**.

So:

```text
[2, 7, 80]  → row 1
[4, 6, 90]  → row 2
[3, 8, 85]  → row 3
```

Therefore:

$$
X.shape=(3,3)
$$

---

# 5. Rectangular Arrays

A NumPy array doesn't need to be square.

This is perfectly valid:

```python
X = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
```

Shape:

$$
(2,4)
$$

meaning:

$$
2\text{ rows}\times4\text{ columns}
$$

This is extremely common in ML.

For example:

$$
X.shape=(10000,50)
$$

means:

$$
10,000\text{ observations}
\times50\text{ features}
$$

---

# 6. Why Rows Must Have Compatible Structure

Consider:

```python
X = np.array([
    [1, 2, 3],
    [4, 5]
])
```

This doesn't represent a proper rectangular numerical matrix.

A mathematical matrix requires:

$$
\boxed{\text{same number of columns in every row}}
$$

This is an important mental model.

---

# 7. `np.zeros()`

Often we need an array containing zeros.

Use:

```python
np.zeros(5)
```

Result:

```text
[0. 0. 0. 0. 0.]
```

Shape:

$$
(5,)
$$

---

# 8. Why Would We Want Zeros?

Suppose you're preparing storage for:

$$
100
$$

measurements.

You can create:

```python
data = np.zeros(100)
```

Then later fill it.

In numerical algorithms, zero arrays are also frequently used as initial values.

---

# 9. 2D Zeros

You can specify the shape:

```python
np.zeros((3, 4))
```

Conceptually:

$$
\begin{bmatrix}
0&0&0&0\\
0&0&0&0\\
0&0&0&0
\end{bmatrix}
$$

Shape:

$$
\boxed{(3,4)}
$$

Notice the syntax:

```python
(3, 4)
```

The tuple describes:

$$
\text{rows},\text{columns}
$$

---

# 10. `np.ones()`

Similarly:

```python
np.ones(5)
```

gives:

```text
[1. 1. 1. 1. 1.]
```

And:

```python
np.ones((2,3))
```

gives:

$$
\begin{bmatrix}
1&1&1\\
1&1&1
\end{bmatrix}
$$

---

# 11. Why `zeros()` and `ones()` Matter in ML

You'll eventually encounter:

- initializing parameters
- creating masks
- creating temporary arrays
- numerical algorithms
- simulations
- neural-network computations

For example, a vector of model parameters could initially be represented as:

$$
\mathbf w=
\begin{bmatrix}
0\\
0\\
0
\end{bmatrix}
$$

using:

```python
w = np.zeros(3)
```

We'll later learn why **initialization strategy** matters for different ML algorithms.

---

# 12. `np.full()`

Sometimes you want every element to have the same value.

For example:

```python
np.full(5, 7)
```

gives:

```text
[7 7 7 7 7]
```

For a matrix:

```python
np.full((2, 3), 7)
```

gives:

$$
\begin{bmatrix}
7&7&7\\
7&7&7
\end{bmatrix}
$$

Mental model:

$$
\boxed{\texttt{full(shape,value)}}
$$

---

# 13. `np.empty()`

NumPy also provides:

```python
np.empty(5)
```

This creates an array of the requested size **without initializing its values to a meaningful constant**.

The contents should not be interpreted as zeros.

You might see arbitrary-looking values.

So:

```python
np.empty(...)
```

means roughly:

> Give me the memory structure; I'll fill it myself.

It can be useful in performance-sensitive numerical code when you know every element will be overwritten.

For beginners:

$$
\boxed{\text{Don't use `empty()` when you need initialized values.}}
$$

Use:

```python
np.zeros()
```

or:

```python
np.ones()
```

instead.

---

# 14. `np.arange()`

Now something extremely useful.

Suppose you want:

$$
0,1,2,3,4,5
$$

Use:

```python
np.arange(6)
```

Result:

```text
[0 1 2 3 4 5]
```

Why does it stop at 6?

Because the endpoint is **excluded**.

This follows the familiar Python range convention:

$$
[0,6)
$$

---

# 15. Starting Somewhere Else

```python
np.arange(2, 8)
```

gives:

```text
[2 3 4 5 6 7]
```

Mathematically:

$$
2,3,4,5,6,7
$$

---

# 16. Adding a Step

```python
np.arange(0, 10, 2)
```

gives:

```text
[0 2 4 6 8]
```

So:

$$
\boxed{
\texttt{arange(start, stop, step)}
}
$$

For example:

```python
np.arange(1, 11, 2)
```

gives:

```text
[1 3 5 7 9]
```

---

# 17. Why `arange()` Is Useful in Physics

Suppose you want discrete time points:

$$
t=0,1,2,\ldots,9
$$

You could use:

```python
t = np.arange(10)
```

Then:

$$
t=[0,1,2,\ldots,9]
$$

This becomes useful for simulations.

For example:

$$
x(t)=t^2
$$

could later be computed over the whole array.

---

# 18. Why `arange()` Is Useful in ML

You might need:

- sample indices
- iteration numbers
- array positions
- synthetic datasets
- simulation coordinates

For example:

```python
indices = np.arange(100)
```

creates:

$$
0,1,2,\ldots,99
$$

---

# 19. `np.linspace()`

Now we encounter a very important scientific-computing function:

$$
\boxed{\texttt{np.linspace()}}
$$

Suppose you want:

$$
0,0.25,0.5,0.75,1
$$

You can write:

```python
np.linspace(0, 1, 5)
```

Result:

```text
[0.   0.25 0.5  0.75 1.  ]
```

Notice something different from `arange()`.

---

# 20. `arange()` vs `linspace()`

### `arange`

You specify:

$$
\boxed{\text{step size}}
$$

Example:

```python
np.arange(0, 1, 0.2)
```

---

### `linspace`

You specify:

$$
\boxed{\text{number of points}}
$$

Example:

```python
np.linspace(0, 1, 6)
```

which gives six evenly spaced points.

---

# 21. Why `linspace()` Is Extremely Important for Physics

Suppose you want to simulate:

$$
t\in[0,10]
$$

using:

$$
1000
$$

equally spaced time points.

You can write:

```python
t = np.linspace(0, 10, 1000)
```

This is incredibly common in scientific computing.

For example:

$$
x(t)=e^{-t}\cos(t)
$$

can then be evaluated over all those points.

---

# 22. Quantum Physics Example

Suppose you want to simulate a decaying population:

$$
P(t)=e^{-\gamma t}
$$

with:

$$
t\in[0,10]
$$

You can create:

```python
t = np.linspace(0, 10, 1000)
```

and later calculate:

```python
P = np.exp(-gamma * t)
```

We haven't formally learned NumPy's mathematical functions yet, so don't worry about `np.exp()` right now.

The important idea is:

$$
\boxed{
\text{Create physical domain}
\rightarrow
\text{evaluate mathematical function}
}
$$

This is the beginning of scientific computing.

---

# 23. `np.eye()` — Identity Matrix

Now let's connect to linear algebra.

The identity matrix is:

$$
I=
\begin{bmatrix}
1&0&0\\
0&1&0\\
0&0&1
\end{bmatrix}
$$

NumPy:

```python
np.eye(3)
```

produces a \(3\times3\) identity matrix.

Why is this important?

Because later we'll use identity matrices in:

- linear algebra
- transformations
- optimization
- regularization
- quantum mechanics
- matrix equations

---

# 24. Quantum Connection ⚛️

For a two-level quantum system:

$$
I=
\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}
$$

In NumPy:

```python
I = np.eye(2)
```

This is directly useful when working with quantum states and operators.

For example:

$$
I|\psi\rangle=|\psi\rangle
$$

The identity operator leaves a state unchanged.

So even a simple NumPy array-creation function already has a direct quantum-physics interpretation.

---

# 25. Random Arrays

We also need random numbers.

NumPy has a random-number system.

For example:

```python
rng = np.random.default_rng()
```

This creates a random-number generator.

Then you can generate random values.

For example:

```python
rng.random(5)
```

produces five random values between 0 and 1.

The exact values will differ each time.

---

# 26. Why Randomness Matters

Random numbers are everywhere in:

### Statistics

Sampling.

### ML

Train/test splitting, initialization, simulation.

### Physics

Monte Carlo methods.

### Quantum experiments

Simulating measurement outcomes.

### Scientific computing

Uncertainty and stochastic processes.

So randomness is not a side feature.

It is fundamental.

---

# 27. Reproducibility

Suppose you run:

```python
rng = np.random.default_rng()
```

and generate random numbers.

You get one sequence.

Run it again and you'll generally get another.

But in scientific computing and ML, we often want experiments to be reproducible.

We can initialize the generator with a seed:

```python
rng = np.random.default_rng(42)
```

Now repeated runs using the same generator setup produce the same pseudo-random sequence.

The number `42` isn't mathematically special.

It's simply a chosen seed.

---

# 28. Why Reproducibility Matters

Imagine training an ML model and getting:

```text
Accuracy = 91.2%
```

Then your colleague runs the same code and gets:

```text
Accuracy = 89.7%
```

If randomness is involved, you need controlled random seeds when appropriate so that you can reproduce experiments.

In scientific computing:

$$
\boxed{
\text{Reproducibility is part of good science.}
}
$$

---

# 29. One Important Warning About Randomness

A random seed doesn't make something "truly random."

NumPy generates **pseudo-random numbers** using deterministic algorithms.

The seed determines the sequence.

For ML and simulations, this is usually exactly what we want.

---

# 30. Array Creation Summary

You now have several ways to create arrays:

| Function        | Main purpose                   |
| --------------- | ------------------------------ |
| `np.array()`    | Convert data into an array     |
| `np.zeros()`    | Array filled with zeros        |
| `np.ones()`     | Array filled with ones         |
| `np.full()`     | Array filled with chosen value |
| `np.empty()`    | Uninitialized array structure  |
| `np.arange()`   | Regular sequence using a step  |
| `np.linspace()` | Evenly spaced points           |
| `np.eye()`      | Identity matrix                |
| `np.random...`  | Random data                    |

Don't memorize them blindly.

Think about the **problem** first.

---

# 31. Choosing the Right Tool

Suppose you need:

### Existing data

```python
np.array(data)
```

### 100 zeros

```python
np.zeros(100)
```

### 10 ones

```python
np.ones(10)
```

### Values 0 through 9

```python
np.arange(10)
```

### 100 points between 0 and 1

```python
np.linspace(0, 1, 100)
```

### Identity matrix

```python
np.eye(5)
```

### Random numbers

```python
rng.random(100)
```

This is much easier to remember because you're thinking in terms of **intent**.

---

# 32. One Important Scientific-Computing Distinction

Suppose you want:

$$
0,0.1,0.2,\ldots,1.0
$$

You might think:

```python
np.arange(0, 1, 0.1)
```

But floating-point arithmetic can introduce endpoint/rounding surprises.

For scientific work where you specifically want a certain number of evenly spaced points over an interval, `linspace` is often clearer:

```python
np.linspace(0, 1, 11)
```

because you explicitly request:

$$
11\text{ points}
$$

including both endpoints.

---

# 33. Let's Connect Everything to Our Previous Mathematics

You learned functions:

$$
f(x)=x^2
$$

Now we can create input points:

```python
x = np.linspace(-5, 5, 100)
```

Then eventually:

```python
y = x**2
```

Conceptually:

$$
x=
\begin{bmatrix}
-5&\cdots&5
\end{bmatrix}
$$

and:

$$
y=f(x)
$$

for every element.

This is the beginning of **vectorized computation**.

We'll study that properly later.

---

# 34. ML Example

Suppose we want synthetic study-hour data:

```python
hours = np.array([1, 2, 3, 4, 5])
```

Scores:

```python
scores = np.array([55, 60, 68, 78, 88])
```

Now we have two numerical variables:

$$
X=\text{hours}
$$

$$
Y=\text{scores}
$$

We can later use:

- NumPy
- Pandas
- Matplotlib
- scikit-learn

to analyze and model them.

This is exactly where we'll eventually introduce **Pandas**.

---

# 35. When Will We Introduce Pandas?

You specifically asked me to introduce libraries when they become useful.

Here's the important distinction.

NumPy is excellent for:

$$
\boxed{\text{numerical arrays}}
$$

But imagine a dataset like:

| Student | Hours | Sleep | Department | Score |
| ------- | ----: | ----: | ---------- | ----: |
| Ali     |     5 |     7 | Physics    |    90 |
| Sara    |     3 |     8 | CS         |    82 |
| Ahmed   |     7 |     6 | Physics    |    94 |

Now we have:

- numbers
- strings
- column names
- rows
- missing values
- categorical variables

This is where **Pandas** becomes much more useful.

So we won't blindly finish every NumPy topic first.

When we reach the point where **real tabular datasets** become important, we'll bring Pandas in.

Likewise, when visualization becomes necessary, we'll introduce:

$$
\boxed{\text{Matplotlib}}
$$

And when numerical scientific methods become necessary:

$$
\boxed{\text{SciPy}}
$$

This curriculum will be **problem-driven**, not library-driven.

---

# 🧪 Practice

### Q1

What does this create?

```python
np.zeros((3,4))
```

### Q2

What is the difference between:

```python
np.arange(0, 10, 2)
```

and:

```python
np.linspace(0, 10, 6)
```

### Q3

Which would you prefer for generating 1000 equally spaced time points between \(0\) and \(20\)?

### Q4

What does:

```python
np.eye(3)
```

represent mathematically?

### Q5

Why might a random seed be useful in ML experiments?

### Q6

Which library is better suited to a table containing columns such as:

```text
Age
Height
Department
Salary
```

once we start doing tabular-data analysis?

---

## Answers

### Q1

A:

$$
3\times4
$$

array filled with zeros.

---

### Q2

`arange` specifies a **step**:

$$
0,2,4,6,8
$$

while `linspace` specifies the **number of points**:

$$
0,2,4,6,8,10
$$

for six points.

---

### Q3

```python
np.linspace(0, 20, 1000)
```

---

### Q4

The \(3\times3\) identity matrix:

$$
I=
\begin{bmatrix}
1&0&0\\
0&1&0\\
0&0&1
\end{bmatrix}
$$

---

### Q5

For reproducibility. If randomness is involved, controlling the seed can allow an experiment to be repeated with the same pseudo-random sequence.

---

### Q6

Eventually:

$$
\boxed{\text{Pandas}}
$$

because this is structured/tabular data with labelled columns and mixed data types.

---

# 🗺️ COMPLETE ROADMAP — LESSON 36

```text
PHASE 0 — MATHEMATICAL FOUNDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Numbers & Variables                  ✅
Arithmetic                           ✅
Fractions / Ratios / %               ✅
Powers / Roots / Logs                ✅
Algebra                              ✅
Functions                            ✅
Coordinates & Graphs                 ✅
Vectors                              ✅
Matrices                             ✅
Summation                            ✅
Basic Probability                    ✅


PHASE 1 — STATISTICS FOUNDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Data                                 ✅
Population vs Sample                 ✅
Mean / Median / Mode                 ✅
Variance / SD / Range                ✅
Percentiles / Quartiles              ✅
IQR / Outliers                       ✅
Distribution Shape                   ✅
Random Variables                     ✅
Probability Distributions            ✅
Bernoulli                            ✅
Binomial                             ✅
Expected Value                       ✅
Correlation                          ✅
Covariance                           ✅
Sampling Methods                     ✅
Sampling Distribution                ✅
Standard Error                       ✅
CLT                                  ✅
LLN                                  ✅
Confidence Intervals                 ✅
Statistical Inference                ✅
Hypothesis Testing                   ✅
p-values                             ✅
Statistical Significance             ✅
Effect Size                          ✅
Type I / Type II Errors              ✅
Statistical Power                    ✅


PHASE 2 — NUMPY FOUNDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
What is NumPy?                      ✅
Why NumPy?                           ✅
ndarray                              ✅
Dimensions / Shape / Axes / Size    ✅
dtype                                ✅
Creating arrays                      🔵 YOU ARE HERE
zeros / ones / full                  🔵
arange / linspace                    🔵
identity matrices                    🔵
random arrays                        🔵
Indexing                             ⬜
Slicing                              ⬜
Reshaping                            ⬜
Flattening                           ⬜
Concatenation                        ⬜
Stacking                             ⬜
Broadcasting                         ⬜
Vectorization                        ⬜


PHASE 3 — STATISTICS WITH NUMPY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mean                                 ⬜
Median                               ⬜
Variance                             ⬜
Standard deviation                   ⬜
Percentiles                          ⬜
IQR                                  ⬜
Covariance                           ⬜
Correlation                          ⬜
Sampling simulations                 ⬜
CLT simulations                      ⬜
LLN simulations                      ⬜
Confidence intervals                 ⬜
Hypothesis tests                     ⬜
p-values                             ⬜


PHASE 4 — LINEAR ALGEBRA WITH NUMPY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Vectors                              ⬜
Dot Product                          ⬜
Norms / Distance                     ⬜
Matrices                             ⬜
Matrix Multiplication                ⬜
Transpose                            ⬜
Inverse                              ⬜
Linear Systems                       ⬜
Eigenvalues                          ⬜
Eigenvectors                         ⬜


PHASE 5 — DATA + VISUALIZATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pandas — tabular data                ⬜ ← introduce when needed
Matplotlib — visualization           ⬜ ← introduce when needed
Data cleaning                        ⬜
Missing values                       ⬜
Categorical data                     ⬜
Grouping / aggregation               ⬜
Real datasets                        ⬜


PHASE 6 — NUMPY / SCIENTIFIC COMPUTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Scientific functions                 ⬜
Numerical operations                 ⬜
Simulation                           ⬜
SciPy                                ⬜ ← introduce when needed
Numerical integration                ⬜
Optimization                         ⬜
Differential equations               ⬜


PHASE 7 — MACHINE LEARNING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Supervised Learning                  ⬜
Unsupervised Learning                ⬜
Regression                           ⬜
Classification                       ⬜
Linear Regression                    ⬜
Logistic Regression                  ⬜
KNN                                  ⬜
Decision Trees                       ⬜
Random Forest                        ⬜
SVM                                  ⬜
Clustering                           ⬜
Model Evaluation                     ⬜
Feature Engineering                  ⬜
Cross Validation                     ⬜
Hyperparameter Tuning                ⬜


PHASE 8 — ADVANCED ML
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Optimization                         ⬜
Gradient Descent                     ⬜
Regularization                       ⬜
PCA                                  ⬜
Neural Networks                      ⬜
Deep Learning                        ⬜
CNNs                                 ⬜
Transformers                         ⬜


PHASE 9 — SCIENTIFIC / QUANTUM ML
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Scientific Computing                 ⬜
Scientific Data Analysis             ⬜
Quantum States                       ⬜
Quantum Measurement                  ⬜
Quantum Probability                  ⬜
Quantum Simulation                   ⬜
Quantum ML                           ⬜
```

---

# 🔗 Our New Learning Philosophy

From now on, the roadmap isn't:

> "Finish NumPy → then Pandas → then Matplotlib → then SciPy."

Instead:

$$
\boxed{
\text{Learn a concept}
\rightarrow
\text{Identify the computational problem}
\rightarrow
\text{Use the appropriate library}
}
$$

For example:

$$
\text{Numerical array}
\rightarrow
\boxed{\text{NumPy}}
$$

$$
\text{Real tabular dataset}
\rightarrow
\boxed{\text{Pandas}}
$$

$$
\text{Need to see relationship/distribution}
\rightarrow
\boxed{\text{Matplotlib}}
$$

$$
\text{Numerical integration / optimization / ODE}
\rightarrow
\boxed{\text{SciPy}}
$$

$$
\text{Classical ML}
\rightarrow
\boxed{\text{scikit-learn}}
$$

$$
\text{Deep learning}
\rightarrow
\boxed{\text{PyTorch}}
$$

And because your longer-term direction includes **scientific computing + quantum physics**, we will also introduce the scientific Python ecosystem where it actually becomes useful rather than treating ML as the only destination.

---

# 🧠 Final Lesson Paragraph

> **In this lesson we learned how to create NumPy arrays for different computational purposes. We started with `np.array()` for converting existing Python data into NumPy arrays, then learned `np.zeros()`, `np.ones()`, and `np.full()` for creating initialized arrays, `np.arange()` for generating sequences using a specified step, `np.linspace()` for generating a specified number of evenly spaced points, `np.eye()` for creating identity matrices, and NumPy's random-number generation tools for simulations and ML experiments. We connected `arange()` and especially `linspace()` to scientific computing, where evenly spaced time or spatial coordinates are frequently needed, and connected identity matrices directly to linear algebra and quantum operators. We also learned why random seeds matter for reproducibility. Most importantly, we established a new principle for the rest of the curriculum: we will not learn libraries as isolated lists of functions; instead, we will introduce NumPy, Pandas, Matplotlib, SciPy, scikit-learn, PyTorch, and other important libraries when a concept creates a genuine need for them. NumPy remains our current numerical foundation, but when we begin working with real labelled tabular datasets, Pandas will be introduced; when visualization becomes necessary, Matplotlib will appear; and when scientific numerical methods become relevant, SciPy will be introduced. This keeps the learning path centered on understanding problems and concepts rather than memorizing libraries.**
