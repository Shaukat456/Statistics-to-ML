# Lesson 35 — NumPy `ndarray`: Dimensions, Shape, Axes & Size

Now we're going to understand the **most important object in NumPy**:

$$
\boxed{\texttt{ndarray}}
$$

Before learning indexing, slicing, reshaping, broadcasting, or ML data manipulation, you need to develop a strong mental model of arrays.

The key idea of today's lesson is:

> **A NumPy array is a mathematical structure with a specific number of dimensions, a shape, a size, and a data type.**

---

# 1. What Is an `ndarray`?

Recall:

```python
import numpy as np

x = np.array([10, 20, 30, 40])
```

`x` is a NumPy:

```text
ndarray
```

The `n` means:

> any number of dimensions.

So NumPy can represent:

- 1D arrays
- 2D arrays
- 3D arrays
- 4D arrays
- ...
- N-dimensional arrays

---

# 2. Start With Something You Already Know: A Vector

You learned vectors:

$$
\mathbf{x}
=
\begin{bmatrix}
10\\
20\\
30\\
40
\end{bmatrix}
$$

In NumPy:

```python
x = np.array([10, 20, 30, 40])
```

This is a:

$$
\boxed{\text{1-dimensional array}}
$$

or:

$$
\boxed{\text{1D array}}
$$

---

# 3. What Does "Dimension" Actually Mean?

This is one of the most confusing things for beginners.

Don't think:

> dimension = number of elements

That's wrong.

Instead, think:

> **Dimension tells you how many directions/axes are needed to locate an element.**

Let's build this carefully.

---

# 4. 0D Array — A Single Number

Consider:

$$
5
$$

There is only one value.

NumPy can represent it as:

```python
x = np.array(5)
```

This is a:

$$
\boxed{\text{0-dimensional array}}
$$

You can imagine:

```text
5
```

There is no row direction or column direction.

---

# 5. 1D Array — One Direction

Now:

```python
x = np.array([10, 20, 30, 40])
```

Visually:

```text
10   20   30   40
```

There is one direction:

```text
───────────────→
```

Therefore:

$$
\boxed{\text{1 dimension}}
$$

Mathematically, this is similar to the vector:

$$
\mathbf{x}
=
\begin{bmatrix}
10\\20\\30\\40
\end{bmatrix}
$$

---

# 6. 2D Array — Rows and Columns

Now consider:

```python
X = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
```

Visualize it:

```text
          columns →
        1    2    3

row 1  10   20   30
row 2  40   50   60
  ↓
 rows
```

There are two directions:

1. rows
2. columns

Therefore:

$$
\boxed{\text{2D array}}
$$

Mathematically:

$$
X=
\begin{bmatrix}
10&20&30\\
40&50&60
\end{bmatrix}
$$

---

# 7. 3D Array

Now things become interesting.

Suppose you have multiple 2D matrices:

```text
Matrix 1

10 20 30
40 50 60


Matrix 2

70 80 90
100 110 120
```

You can think of them as stacked:

```text
       Matrix
          ↓

     ┌─────────────┐
     │ 10 20 30    │
     │ 40 50 60    │
     ├─────────────┤
     │ 70 80 90    │
     │100 110 120  │
     └─────────────┘
```

Now we need:

1. matrix/layer
2. row
3. column

So:

$$
\boxed{\text{3 dimensions}}
$$

---

# 8. Real-World Analogy: Building 🏢

Imagine a building.

You need:

### Dimension 1

Which floor?

### Dimension 2

Which row?

### Dimension 3

Which room/column?

So an element might be identified by:

$$
(\text{floor},\text{row},\text{column})
$$

This is the basic idea of higher-dimensional arrays.

---

# 9. Another Analogy: Images 🖼️

This is extremely important for ML.

A grayscale image might be represented as:

$$
\text{height}\times\text{width}
$$

For example:

$$
28\times28
$$

So:

$$
X.shape=(28,28)
$$

That's a 2D array.

Each number represents a pixel intensity.

---

# 10. Color Images

A color image usually has:

$$
\text{height}\times\text{width}\times\text{channels}
$$

For example:

$$
224\times224\times3
$$

where:

- 224 = height
- 224 = width
- 3 = color channels

So:

$$
\boxed{224\times224\times3}
$$

is a 3D array for a single image.

---

# 11. A Batch of Images

Suppose you have:

$$
32
$$

images, each:

$$
224\times224\times3
$$

Now you have:

$$
32\times224\times224\times3
$$

That's a:

$$
\boxed{\text{4D array}}
$$

This is something you'll encounter later in deep learning.

For example:

```text
batch
 ↓
images
 ↓
height
 ↓
width
 ↓
channels
```

The exact ordering can differ between libraries/models, but the dimensional concept remains the same.

---

# 12. `ndim`

NumPy gives us a way to ask:

> How many dimensions does this array have?

Use:

```python
x.ndim
```

Example:

```python
x = np.array([10, 20, 30])
```

Then:

```python
x.ndim
```

returns:

```text
1
```

---

For a matrix:

```python
X = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

Then:

```python
X.ndim
```

returns:

```text
2
```

---

# 13. Shape

Now we reach one of the **most important concepts in NumPy and ML**:

$$
\boxed{\text{shape}}
$$

Shape tells you:

> **How many elements exist along each dimension.**

For:

```python
x = np.array([10, 20, 30, 40])
```

we have:

```python
x.shape
```

which gives:

```text
(4,)
```

Meaning:

> 4 elements along the only axis.

---

# 14. Shape of a Matrix

Consider:

```python
X = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
```

There are:

- 2 rows
- 3 columns

Therefore:

```python
X.shape
```

gives:

```text
(2, 3)
```

So:

$$
\boxed{
X.shape=(2,3)
}
$$

means:

$$
\boxed{
2\text{ rows}\times3\text{ columns}
}
$$

---

# 15. Shape Is Extremely Important in ML

Suppose:

$$
X.shape=(1000,20)
$$

This means:

$$
\boxed{
1000\text{ observations}
\times
20\text{ features}
}
$$

So:

```text
Rows    = observations
Columns = features
```

This is the standard convention we'll use throughout this course for a tabular ML dataset.

---

# 16. Example

Suppose:

```python
X = np.array([
    [2, 7, 80],
    [4, 6, 90],
    [3, 8, 85],
    [5, 6, 95],
    [1, 8, 70]
])
```

There are:

$$
5
$$

students and:

$$
3
$$

features.

Therefore:

```python
X.shape
```

gives:

```text
(5, 3)
```

Interpretation:

$$
\boxed{
5\text{ observations}\times3\text{ features}
}
$$

---

# 17. Size

Shape tells you the structure.

But sometimes you want:

> How many total elements are there?

Use:

```python
X.size
```

For:

$$
X.shape=(5,3)
$$

we have:

$$
5\times3=15
$$

Therefore:

```python
X.size
```

returns:

```text
15
```

---

# 18. Shape vs Size vs Dimensions

This distinction is crucial.

Suppose:

```python
X.shape
```

returns:

```text
(5, 3)
```

Then:

### Number of dimensions

```python
X.ndim
```

gives:

$$
2
$$

### Shape

```python
X.shape
```

gives:

$$
(5,3)
$$

### Total elements

```python
X.size
```

gives:

$$
15
$$

So:

$$
\boxed{
\texttt{ndim}=2
}
$$

$$
\boxed{
\texttt{shape}=(5,3)
}
$$

$$
\boxed{
\texttt{size}=15
}
$$

---

# 19. A Mental Model

Imagine a classroom.

There are:

$$
5
$$

rows of desks and:

$$
3
$$

desks per row.

Then:

### Shape

$$
(5,3)
$$

### Total desks

$$
5\times3=15
$$

### Dimensions

$$
2
$$

because there are two structural directions:

- rows
- columns

---

# 20. Axes

Now we need to understand:

$$
\boxed{\text{axis}}
$$

This is extremely important in NumPy.

For a 2D array:

```text
        columns
           →
      0    1    2
   ┌──────────────
0  │ 10   20   30
1  │ 40   50   60
   ↓
 rows
```

NumPy calls these directions **axes**.

For a 2D array:

$$
\boxed{\text{axis 0 = rows direction}}
$$

$$
\boxed{\text{axis 1 = columns direction}}
$$

---

# 21. But Why Is Axis 0 the Rows?

This initially feels backwards.

Think of axis 0 as:

> The first dimension.

And axis 1 as:

> The second dimension.

Since:

```python
X.shape
```

is:

```text
(2, 3)
```

the dimensions are:

```text
axis 0 → size 2
axis 1 → size 3
```

So:

$$
\boxed{
\text{axis 0 has 2 elements}
}
$$

and:

$$
\boxed{
\text{axis 1 has 3 elements}
}
$$

---

# 22. Another Way to Think About Axes

For:

$$
X.shape=(2,3)
$$

think:

```text
        axis 1 →
      3 columns

axis 0
  ↓
  2 rows
```

The axis number identifies the **dimension position**.

---

# 23. Why Axes Matter

You'll eventually write:

```python
np.mean(X, axis=0)
```

or:

```python
np.mean(X, axis=1)
```

And these produce different results.

If you don't understand axes, NumPy will feel like magic.

We will study this carefully in the next lessons.

For now:

$$
\boxed{
\text{axis = direction/dimension along which an operation can be performed}
}
$$

---

# 24. Example: Student Dataset

Recall:

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

Columns:

```text
Column 0 → Study Hours
Column 1 → Sleep Hours
Column 2 → Attendance
```

Rows:

```text
Row 0 → Student 1
Row 1 → Student 2
Row 2 → Student 3
Row 3 → Student 4
Row 4 → Student 5
```

Thus:

$$
X.shape=(5,3)
$$

and:

$$
X.ndim=2
$$

and:

$$
X.size=15
$$

---

# 25. Data Type — `dtype`

There is another important property:

$$
\boxed{\texttt{dtype}}
$$

It tells us what kind of numerical data the array stores.

Example:

```python
x = np.array([1, 2, 3])
```

You can inspect:

```python
x.dtype
```

You might see something like:

```text
int64
```

The exact integer type can depend on your platform.

---

# 26. Why Does Data Type Matter?

Consider:

```text
1
2
3
```

These are integers.

But:

```text
1.5
2.7
3.1
```

are floating-point numbers.

And:

```text
1 + 2j
```

is a complex number.

Scientific computing often needs different numerical representations.

For example, quantum mechanics frequently uses:

$$
\alpha,\beta\in\mathbb C
$$

so complex-valued arrays are important.

---

# 27. Common NumPy Data Types

You will encounter:

```text
int
float
bool
complex
```

Conceptually:

### Integer

$$
1,2,3,-5
$$

### Float

$$
1.5,\quad2.718,\quad-0.25
$$

### Boolean

```text
True
False
```

### Complex

$$
3+4i
$$

---

# 28. Why Complex Numbers Matter for You

For ordinary ML, most datasets are often real-valued:

$$
x\in\mathbb R
$$

But in quantum physics:

$$
|\psi\rangle
=
\begin{bmatrix}
\alpha\\
\beta
\end{bmatrix}
$$

where:

$$
\alpha,\beta\in\mathbb C
$$

For example:

$$
\alpha=\frac1{\sqrt2}
$$

and:

$$
\beta=\frac{i}{\sqrt2}
$$

So NumPy's complex-number support will eventually become directly relevant to your quantum work.

---

# 29. A Complete Inspection

Given:

```python
X = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

you can ask:

```python
X.ndim
```

→

```text
2
```

```python
X.shape
```

→

```text
(2, 3)
```

```python
X.size
```

→

```text
6
```

```python
X.dtype
```

→ some integer dtype such as `int64`.

---

# 30. A Powerful Habit

Whenever you receive a NumPy array in ML or scientific computing, develop the habit of immediately asking:

```python
x.shape
x.ndim
x.size
x.dtype
```

Think of these as the array's **identity card**.

---

# 31. Why Shape Errors Are So Common in ML

Imagine:

$$
X.shape=(100,10)
$$

This means:

```text
100 observations
10 features
```

Now suppose you accidentally create:

$$
X.shape=(10,100)
$$

You've effectively swapped the interpretation.

This can cause:

- matrix multiplication errors
- model input errors
- incorrect feature calculations
- unexpected broadcasting
- incorrect neural-network input shapes

A huge portion of beginner ML errors are actually **shape errors**.

That's why we're spending time on this now.

---

# 32. Physics Example

Suppose you record:

$$
1000
$$

measurements at:

$$
200
$$

time points.

You might have:

$$
X.shape=(1000,200)
$$

Interpretation could be:

```text
1000 experimental runs
200 time points per run
```

Now suppose you have:

$$
50
$$

experimental runs,

each containing:

$$
100
$$

time points,

and:

$$
3
$$

measurement channels.

Then:

$$
X.shape=(50,100,3)
$$

That's a 3D array.

---

# 33. Quantum Example

Suppose you simulate:

$$
1000
$$

quantum trajectories.

Each trajectory contains:

$$
500
$$

time steps.

If each time step stores one real-valued observable:

$$
X.shape=(1000,500)
$$

If you store three observables:

$$
X.shape=(1000,500,3)
$$

Now you are naturally working with multidimensional NumPy arrays.

This is exactly why understanding dimensions and axes is so important for scientific computing.

---

# 34. The Deep Mental Model

Think of an array as a **coordinate system for data**.

### 1D

One coordinate:

$$
(i)
$$

### 2D

Two coordinates:

$$
(i,j)
$$

### 3D

Three coordinates:

$$
(i,j,k)
$$

### 4D

Four coordinates:

$$
(i,j,k,l)
$$

In general:

$$
\boxed{
\text{N-dimensional array element}
\leftrightarrow
(i_1,i_2,\ldots,i_N)
}
$$

This will become very important when we study indexing.

---

# 35. Shape as a Mathematical Signature

Suppose I tell you:

$$
X.shape=(100,20)
$$

You should immediately visualize:

```text
100 rows
   ×
20 columns
```

If I say:

$$
X.shape=(32,224,224,3)
$$

you should think:

```text
32 images
× 224 height
× 224 width
× 3 channels
```

If I say:

$$
X.shape=(1000,500)
$$

you might think:

```text
1000 experiments
× 500 measurements
```

depending on the application.

So shape isn't just a technical detail.

$$
\boxed{\text{Shape tells you how the data is organized.}}
$$

---

# 🧪 Practice

Don't run these yet if you're focusing on understanding. Try to reason first.

### Q1

What is the dimensionality of:

```python
x = np.array([1, 2, 3, 4])
```

### Q2

What is the shape?

### Q3

What is the shape of:

```python
X = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

### Q4

What is `X.size`?

### Q5

What is `X.ndim`?

### Q6

If:

$$
X.shape=(500,20)
$$

and this is an ML dataset, what could 500 and 20 represent?

### Q7

What could:

$$
X.shape=(32,224,224,3)
$$

represent in deep learning?

---

## Answers

### Q1

$$
\boxed{1D}
$$

### Q2

$$
\boxed{(4,)}
$$

### Q3

$$
\boxed{(2,3)}
$$

### Q4

$$
2\times3=6
$$

### Q5

$$
\boxed{2}
$$

### Q6

Potentially:

$$
500=\text{observations}
$$

$$
20=\text{features}
$$

### Q7

Potentially:

$$
32=\text{images}
$$

$$
224=\text{height}
$$

$$
224=\text{width}
$$

$$
3=\text{color channels}
$$

---

# 🗺️ COMPLETE ROADMAP — LESSON 35

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
Confidence Intervals                ✅
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
Dimensions                           🔵 YOU ARE HERE
Shape                                🔵 YOU ARE HERE
Axes                                 🔵 YOU ARE HERE
Size                                 🔵 YOU ARE HERE
dtype                                🔵 YOU ARE HERE
Creating arrays                      ⬜
Indexing                             ⬜
Slicing                              ⬜
Reshaping                            ⬜
Flattening                           ⬜
Concatenation                        ⬜
Stacking                             ⬜
Broadcasting                        ⬜
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


PHASE 5 — NUMPY FOR ML
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Feature Matrix X                     ⬜
Target Vector y                      ⬜
Standardization                      ⬜
Normalization                        ⬜
Predictions                          ⬜
Errors                               ⬜
MSE / RMSE                           ⬜
Gradients                            ⬜
Vectorized ML                        ⬜


PHASE 6 — MACHINE LEARNING
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


PHASE 7 — ADVANCED ML
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Optimization                         ⬜
Gradient Descent                     ⬜
Regularization                     ⬜
PCA                                  ⬜
Neural Networks                      ⬜
Deep Learning                        ⬜
CNNs                                 ⬜
Transformers                         ⬜


PHASE 8 — SCIENTIFIC / QUANTUM ML
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Scientific Computing                 ⬜
Numerical Methods                    ⬜
Scientific Data Analysis             ⬜
Quantum States                       ⬜
Quantum Measurement                  ⬜
Quantum Probability                  ⬜
Quantum ML                           ⬜
```

---

# 🔗 When Will We Actually Start Using NumPy Heavily?

**We have started.** But we're still learning the language of NumPy before using it for serious computation.

Our sequence is:

$$
\boxed{
\text{NumPy object}
}
$$

↓

$$
\boxed{
\text{Shape / Dimensions / Axes}
}
$$

↓

$$
\boxed{
\text{Indexing / Slicing}
}
$$

↓

$$
\boxed{
\text{Reshaping}
}
$$

↓

$$
\boxed{
\text{Broadcasting}
}
$$

↓

$$
\boxed{
\text{Vectorization}
}
$$

↓

$$
\boxed{
\text{Statistics with NumPy}
}
$$

↓

$$
\boxed{
\text{Linear Algebra with NumPy}
}
$$

↓

$$
\boxed{
\text{ML with NumPy}
}
$$

This order is deliberate.

We don't want you memorizing:

```python
axis=0
axis=1
reshape(...)
```

without understanding what these things mean.

---

# 🧠 Final Lesson Paragraph

> **In this lesson we learned the internal structure of NumPy's central object, the `ndarray`. An array can have zero, one, two, three, or many dimensions, where dimensionality describes how many axes are needed to locate an element. A 1D array behaves like a vector, a 2D array behaves like a matrix with rows and columns, and higher-dimensional arrays can represent structures such as images, batches of images, experimental measurements, and quantum simulations. We learned four critical properties: `ndim` tells us the number of dimensions, `shape` tells us the number of elements along each dimension, `size` tells us the total number of elements, and `dtype` tells us the numerical data type stored in the array. We also introduced axes, where a 2D array has axis 0 and axis 1, and established the convention that for a typical ML feature matrix, rows represent observations and columns represent features. These concepts are foundational because shape determines how data can be manipulated and whether mathematical operations such as matrix multiplication are valid. We connected this to ML datasets such as \(X.shape=(1000,20)\), image tensors such as \(32\times224\times224\times3\), scientific measurements, and quantum trajectory data. The next major step is learning how to actually create different types of NumPy arrays and then access individual elements using indexing, which will turn our understanding of array structure into practical manipulation.**
