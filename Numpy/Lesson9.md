# Lesson 9 — Matrices 🔢

Now we're moving from **one data point** to an **entire dataset**.

You already understand vectors:

$$
\mathbf{x}=
\begin{bmatrix}
5\\
7\\
90
\end{bmatrix}
$$

That could represent **one student**:

- 5 study hours
- 7 sleep hours
- 90% attendance

But what if we have **10,000 students**?

We need a structure that can hold many vectors together.

That structure is a **matrix**.

---

# 1. What Is a Matrix?

A matrix is essentially a rectangular arrangement of numbers.

For example:

$$
A=
\begin{bmatrix}
5&7&90\\
2&8&75\\
8&6&95\\
4&7&85
\end{bmatrix}
$$

Think of it as a table of numbers.

```text
             Features
          ↓      ↓       ↓
        Study   Sleep   Attendance
          │      │       │
Student A  5      7       90
Student B  2      8       75
Student C  8      6       95
Student D  4      7       85
```

This is a matrix.

---

# 2. The Most Important Mental Model

Remember:

### Vector

> **One data point**

### Matrix

> **Many data points arranged together**

For example:

$$
\mathbf{x}_1=
\begin{bmatrix}
5\\7\\90
\end{bmatrix}
$$

$$
\mathbf{x}_2=
\begin{bmatrix}
2\\8\\75
\end{bmatrix}
$$

$$
\mathbf{x}_3=
\begin{bmatrix}
8\\6\\95
\end{bmatrix}
$$

Put them together:

$$
X=
\begin{bmatrix}
5&7&90\\
2&8&75\\
8&6&95
\end{bmatrix}
$$

So:

$$
\boxed{
\text{Matrix}=\text{collection of vectors}
}
$$

---

# 3. Rows and Columns

This is absolutely fundamental.

Consider:

$$
A=
\begin{bmatrix}
5&7&90\\
2&8&75\\
8&6&95
\end{bmatrix}
$$

There are **3 rows**.

There are **3 columns**.

---

## Rows

A row goes horizontally.

First row:

$$
\begin{bmatrix}
5&7&90
\end{bmatrix}
$$

Second row:

$$
\begin{bmatrix}
2&8&75
\end{bmatrix}
$$

Third row:

$$
\begin{bmatrix}
8&6&95
\end{bmatrix}
$$

In our ML example:

> **One row = one observation/student.**

---

## Columns

A column goes vertically.

First column:

$$
\begin{bmatrix}
5\\
2\\
8
\end{bmatrix}
$$

Second column:

$$
\begin{bmatrix}
7\\
8\\
6
\end{bmatrix}
$$

Third column:

$$
\begin{bmatrix}
90\\
75\\
95
\end{bmatrix}
$$

In our ML example:

> **One column = one feature.**

---

# 4. This Is How ML Data Naturally Looks

Suppose our dataset is:

| Student | Study | Sleep | Attendance |
| ------- | ----: | ----: | ---------: |
| A       |     5 |     7 |         90 |
| B       |     2 |     8 |         75 |
| C       |     8 |     6 |         95 |
| D       |     4 |     7 |         85 |

Our feature matrix is:

$$
X=
\begin{bmatrix}
5&7&90\\
2&8&75\\
8&6&95\\
4&7&85
\end{bmatrix}
$$

Notice:

$$
\boxed{\text{Rows = observations}}
$$

$$
\boxed{\text{Columns = features}}
$$

This is one of the most important conventions in traditional ML.

---

# 5. Matrix Dimensions

Suppose:

$$
A=
\begin{bmatrix}
5&7&90\\
2&8&75\\
8&6&95\\
4&7&85
\end{bmatrix}
$$

It has:

$$
4
$$

rows and:

$$
3
$$

columns.

Therefore its dimensions are:

$$
\boxed{4\times3}
$$

Read this as:

> **4 by 3**

or:

> 4 rows × 3 columns.

---

# 6. Don't Reverse It!

This mistake is extremely common.

For:

$$
A=
\begin{bmatrix}
1&2&3\\
4&5&6
\end{bmatrix}
$$

there are:

- 2 rows
- 3 columns

Therefore:

$$
\boxed{2\times3}
$$

Not \(3\times2\).

### Memory trick 🧠

> **Rows come first.**

$$
\boxed{\text{rows}\times\text{columns}}
$$

---

# 7. Matrix Elements

Every individual number inside a matrix is called an **element** or **entry**.

For:

$$
A=
\begin{bmatrix}
5&7&90\\
2&8&75
\end{bmatrix}
$$

the element 8 is located at:

- row 2
- column 2

Mathematically we can write:

$$
A_{2,2}=8
$$

Similarly:

$$
A_{1,3}=90
$$

Meaning:

> Row 1, column 3.

---

# 8. Matrix Indexing

This is going to become extremely important when we reach NumPy.

For example:

$$
A=
\begin{bmatrix}
10&20&30\\
40&50&60\\
70&80&90
\end{bmatrix}
$$

Conceptually:

```text
         col
         1   2   3
       ┌───────────
row 1  │10  20  30
row 2  │40  50  60
row 3  │70  80  90
```

So:

$$
A_{2,3}=60
$$

because:

> row 2, column 3.

Later in NumPy you'll encounter zero-based indexing:

```text
row 0
row 1
row 2
```

We'll deal with that carefully when we reach NumPy.

---

# 9. Matrix Addition

Matrices can be added.

But there is an important condition:

> They must have the **same dimensions**.

Suppose:

$$
A=
\begin{bmatrix}
1&2\\
3&4
\end{bmatrix}
$$

and:

$$
B=
\begin{bmatrix}
5&6\\
7&8
\end{bmatrix}
$$

Then:

$$
A+B=
\begin{bmatrix}
1+5&2+6\\
3+7&4+8
\end{bmatrix}
$$

Therefore:

$$
\boxed{
A+B=
\begin{bmatrix}
6&8\\
10&12
\end{bmatrix}
}
$$

It's simply:

> **Add corresponding elements.**

---

# 10. Scalar Multiplication

Just like with vectors, we can multiply a matrix by a number.

Suppose:

$$
A=
\begin{bmatrix}
1&2\\
3&4
\end{bmatrix}
$$

Multiply by 3:

$$
3A=
\begin{bmatrix}
3(1)&3(2)\\
3(3)&3(4)
\end{bmatrix}
$$

Therefore:

$$
\boxed{
3A=
\begin{bmatrix}
3&6\\
9&12
\end{bmatrix}
}
$$

Every element gets multiplied.

---

# 11. Matrix Transpose

This operation is extremely important in ML.

The **transpose** switches rows and columns.

Suppose:

$$
A=
\begin{bmatrix}
1&2&3\\
4&5&6
\end{bmatrix}
$$

This is:

$$
2\times3
$$

Its transpose is:

$$
A^T=
\begin{bmatrix}
1&4\\
2&5\\
3&6
\end{bmatrix}
$$

Now it's:

$$
3\times2
$$

So:

$$
\boxed{\text{Transpose = rows become columns}}
$$

and:

$$
\boxed{\text{columns become rows}}
$$

---

# 12. Visualize Transpose

Think of the original:

```text
1  2  3
4  5  6
```

After transpose:

```text
1  4
2  5
3  6
```

The matrix is essentially reflected across its main diagonal.

---

# 13. Why Is Transpose Important in ML?

You'll frequently see expressions such as:

$$
X^T
$$

and:

$$
\mathbf{x}^T
$$

especially in:

- linear regression
- least squares
- covariance matrices
- optimization
- neural networks
- linear algebra
- scientific computing

For example, a common linear regression equation is:

$$
\boxed{
\mathbf w=(X^TX)^{-1}X^Ty
}
$$

Don't worry about understanding this equation yet.

We haven't learned enough mathematics for it.

But eventually you'll understand every symbol in it.

---

# 14. Now the Big One: Matrix × Vector

This operation is **extremely important for ML**.

Suppose:

$$
A=
\begin{bmatrix}
1&2\\
3&4
\end{bmatrix}
$$

and:

$$
\mathbf{x}=
\begin{bmatrix}
5\\
6
\end{bmatrix}
$$

We want:

$$
A\mathbf{x}
$$

Here's the rule:

> Multiply each row of the matrix with the vector using a dot product.

---

## First row

$$
[1,2]
$$

with:

$$
\begin{bmatrix}
5\\
6
\end{bmatrix}
$$

gives:

$$
1(5)+2(6)
$$

$$
=5+12=17
$$

---

## Second row

$$
[3,4]
$$

gives:

$$
3(5)+4(6)
$$

$$
=15+24=39
$$

Therefore:

$$
\boxed{
A\mathbf{x}
=
\begin{bmatrix}
17\\
39
\end{bmatrix}
}
$$

---

# 15. The Pattern

Suppose:

$$
A=
\begin{bmatrix}
a&b\\
c&d
\end{bmatrix}
$$

and:

$$
\mathbf{x}=
\begin{bmatrix}
x\\
y
\end{bmatrix}
$$

Then:

$$
A\mathbf{x}
=
\begin{bmatrix}
ax+by\\
cx+dy
\end{bmatrix}
$$

Notice what happened.

A matrix transformed one vector into another vector.

This is one reason matrices are so powerful.

---

# 16. Matrix Multiplication Is NOT Element-by-Element Multiplication

This is a very common beginner mistake.

Given:

$$
A=
\begin{bmatrix}
1&2\\
3&4
\end{bmatrix}
$$

and:

$$
B=
\begin{bmatrix}
5&6\\
7&8
\end{bmatrix}
$$

ordinary matrix multiplication is **not**:

$$
\begin{bmatrix}
1(5)&2(6)\\
3(7)&4(8)
\end{bmatrix}
$$

Instead, we use:

> **row × column**

This distinction will become very important when you start NumPy.

---

# 17. Matrix × Matrix

Suppose:

$$
A=
\begin{bmatrix}
1&2\\
3&4
\end{bmatrix}
$$

and:

$$
B=
\begin{bmatrix}
5&6\\
7&8
\end{bmatrix}
$$

To calculate:

$$
AB
$$

we take rows from \(A\) and columns from \(B\).

### Top-left

$$
1(5)+2(7)=19
$$

### Top-right

$$
1(6)+2(8)=22
$$

### Bottom-left

$$
3(5)+4(7)=43
$$

### Bottom-right

$$
3(6)+4(8)=50
$$

Therefore:

$$
\boxed{
AB=
\begin{bmatrix}
19&22\\
43&50
\end{bmatrix}
}
$$

---

# 18. The Matrix Multiplication Rule

This is one rule you MUST remember:

Suppose:

$$
A
$$

has dimensions:

$$
m\times n
$$

and:

$$
B
$$

has dimensions:

$$
n\times p
$$

Then:

$$
AB
$$

is possible and produces:

$$
m\times p
$$

In other words:

$$
\boxed{
(m\times n)(n\times p)
=
(m\times p)
}
$$

The **inside dimensions must match**.

---

# 19. Example

Suppose:

$$
A: 3\times4
$$

and:

$$
B: 4\times2
$$

Can we multiply?

Yes.

Because:

$$
(3\times\boxed4)(\boxed4\times2)
$$

The inner 4s match.

Result:

$$
\boxed{3\times2}
$$

---

But:

$$
A:3\times4
$$

and:

$$
B:3\times2
$$

cannot be multiplied as:

$$
AB
$$

because:

$$
(3\times4)(3\times2)
$$

The inner dimensions:

$$
4\neq3
$$

So multiplication is not defined.

---

# 20. Why Does This Matter for ML?

Let's return to:

$$
\hat y=\mathbf w\cdot\mathbf x+b
$$

For one observation.

But suppose we have **1000 observations**.

Our dataset is:

$$
X=
\begin{bmatrix}
x_{11}&x_{12}&x_{13}\\
x_{21}&x_{22}&x_{23}\\
\vdots&\vdots&\vdots\\
x_{1000,1}&x_{1000,2}&x_{1000,3}
\end{bmatrix}
$$

This has:

$$
1000\times3
$$

dimensions.

Our weight vector:

$$
\mathbf w=
\begin{bmatrix}
w_1\\
w_2\\
w_3
\end{bmatrix}
$$

has:

$$
3\times1
$$

dimensions.

Now:

$$
X\mathbf w
$$

has dimensions:

$$
(1000\times3)(3\times1)
$$

The inner dimensions match:

$$
3=3
$$

So the result is:

$$
\boxed{1000\times1}
$$

That's **1000 predictions**.

This is one of the fundamental reasons matrices are so important in ML.

---

# 21. Let's See It Conceptually

Instead of calculating:

```text
Student 1 → prediction
Student 2 → prediction
Student 3 → prediction
...
Student 1000 → prediction
```

we can express all predictions compactly:

$$
\boxed{
\hat{\mathbf y}=X\mathbf w+b
}
$$

This is the mathematical foundation of **vectorized ML computation**.

---

# 22. A Complete Small Example

Suppose:

$$
X=
\begin{bmatrix}
2&7\\
4&6\\
3&8
\end{bmatrix}
$$

Maybe:

- column 1 = study hours
- column 2 = sleep hours

And:

$$
\mathbf w=
\begin{bmatrix}
5\\
2
\end{bmatrix}
$$

Then:

$$
X\mathbf w
$$

becomes:

$$
\begin{bmatrix}
2&7\\
4&6\\
3&8
\end{bmatrix}
\begin{bmatrix}
5\\
2
\end{bmatrix}
$$

### Row 1

$$
2(5)+7(2)=24
$$

### Row 2

$$
4(5)+6(2)=32
$$

### Row 3

$$
3(5)+8(2)=31
$$

Therefore:

$$
\boxed{
X\mathbf w=
\begin{bmatrix}
24\\
32\\
31
\end{bmatrix}
}
$$

Three observations → three outputs.

---

# 23. This Is the Heart of Linear Models

We've gradually built this.

First:

$$
y=w_1x_1+w_2x_2+b
$$

Then vector notation:

$$
y=\mathbf w\cdot\mathbf x+b
$$

Then for many observations:

$$
\boxed{
\mathbf{\hat y}=X\mathbf w+b
}
$$

You are now seeing why the mathematics of ML naturally leads us toward matrices.

---

# 24. A Dataset Is Basically a Matrix

This idea deserves to be burned into your memory.

Suppose you have:

$$
10,000
$$

observations and:

$$
50
$$

features.

Your feature matrix is:

$$
\boxed{
X\in\mathbb R^{10000\times50}
}
$$

Meaning:

- 10,000 rows
- 50 columns

Every row:

> one observation.

Every column:

> one feature.

This is the mathematical representation of your dataset.

---

# 25. Connection to NumPy

Now we're getting very close to NumPy.

A matrix such as:

$$
X=
\begin{bmatrix}
5&7&90\\
2&8&75\\
8&6&95
\end{bmatrix}
$$

will eventually be represented by a NumPy array.

Conceptually:

```text
[ [5, 7, 90],
  [2, 8, 75],
  [8, 6, 95] ]
```

NumPy gives us tools to efficiently perform:

- matrix addition
- multiplication
- transpose
- dot products
- statistics
- reshaping
- slicing
- broadcasting

But notice the learning order we're following:

$$
\boxed{
\text{Mathematics}
\rightarrow
\text{Understand operation}
\rightarrow
\text{NumPy implementation}
}
$$

That's much better than memorizing NumPy commands without understanding what they mean.

---

# 26. Physics Connection ⚛️

Matrices are everywhere in physics too.

For example, a rotation can be represented by a matrix.

A 2D rotation matrix is:

$$
R=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}
$$

Then:

$$
\mathbf{x}'=R\mathbf{x}
$$

The matrix transforms the vector.

This is the same general idea we saw earlier:

$$
A\mathbf{x}=\mathbf{y}
$$

A matrix can act as a **transformation machine**.

---

# 27. Quantum Physics Connection ⚛️

This becomes even more important in quantum mechanics.

A quantum state can be represented as a vector:

$$
|\psi\rangle
$$

and quantum operations are represented using matrices/operators.

For example:

$$
|\psi'\rangle=U|\psi\rangle
$$

where \(U\) is an operator.

So you will eventually encounter the same basic mathematical pattern:

$$
\boxed{
\text{matrix}\times\text{vector}
}
$$

in both:

$$
\text{Machine Learning}
$$

and:

$$
\text{Quantum Mechanics}
$$

That's one reason learning linear algebra properly is so valuable for your goals.

---

# 28. Your Mental Model for Matrices

Don't think:

> "A matrix is just a table."

Instead think:

> **A matrix is a structured mathematical object that can store information and transform vectors.**

For ML:

$$
X
$$

can store the dataset.

For a model:

$$
W
$$

can store parameters.

And matrix multiplication can perform huge numbers of calculations efficiently.

---

# 29. The Complete Mathematical Journey

Look how far we've come:

```text
NUMBER
  ↓
VARIABLE
  ↓
ALGEBRA
  ↓
FUNCTION
  ↓
COORDINATE
  ↓
VECTOR
  ↓
MATRIX
  ↓
MATRIX × VECTOR
  ↓
ML MODEL
```

And eventually:

```text
Matrix
   ↓
NumPy ndarray
   ↓
Vectorized computation
   ↓
Machine Learning
   ↓
Neural Networks
   ↓
Scientific Computing
   ↓
Quantum Computing
```

---

# 🧠 Practice

Try these before looking at the answers.

### Q1

How many rows and columns?

$$
A=
\begin{bmatrix}
1&2&3\\
4&5&6\\
7&8&9\\
10&11&12
\end{bmatrix}
$$

---

### Q2

What are the dimensions of \(A\)?

---

### Q3

What is:

$$
A_{2,3}
$$

for:

$$
A=
\begin{bmatrix}
1&2&3\\
4&5&6\\
7&8&9
\end{bmatrix}
$$

---

### Q4

Calculate:

$$
\begin{bmatrix}
1&2\\
3&4
\end{bmatrix}
+
\begin{bmatrix}
5&6\\
7&8
\end{bmatrix}
$$

---

### Q5

Calculate:

$$
2
\begin{bmatrix}
1&3\\
4&5
\end{bmatrix}
$$

---

### Q6

Find the transpose:

$$
A=
\begin{bmatrix}
1&2&3\\
4&5&6
\end{bmatrix}
$$

---

### Q7

Can these matrices be multiplied?

$$
A:4\times3
$$

$$
B:3\times2
$$

If yes, what is the resulting dimension?

---

### Q8

Can these be multiplied?

$$
A:4\times3
$$

$$
B:4\times2
$$

---

### Q9

Calculate:

$$
\begin{bmatrix}
1&2\\
3&4
\end{bmatrix}
\begin{bmatrix}
5\\
6
\end{bmatrix}
$$

---

### Q10 — ML ⭐

If:

$$
X
$$

has shape:

$$
1000\times20
$$

and:

$$
\mathbf w
$$

has shape:

$$
20\times1
$$

what is the shape of:

$$
X\mathbf w
$$

?

And what could that result represent in an ML model?

---

# Answers

### Q1

4 rows and 3 columns.

### Q2

$$
\boxed{4\times3}
$$

### Q3

$$
A_{2,3}=6
$$

### Q4

$$
\boxed{
\begin{bmatrix}
6&8\\
10&12
\end{bmatrix}}
$$

### Q5

$$
\boxed{
\begin{bmatrix}
2&6\\
8&10
\end{bmatrix}}
$$

### Q6

$$
\boxed{
A^T=
\begin{bmatrix}
1&4\\
2&5\\
3&6
\end{bmatrix}}
$$

### Q7

Yes.

$$
(4\times3)(3\times2)
$$

Therefore:

$$
\boxed{4\times2}
$$

### Q8

No.

$$
(4\times3)(4\times2)
$$

The inner dimensions:

$$
3\neq4
$$

so multiplication is not defined.

### Q9

$$
\begin{bmatrix}
1(5)+2(6)\\
3(5)+4(6)
\end{bmatrix}
$$

$$
=
\boxed{
\begin{bmatrix}
17\\
39
\end{bmatrix}}
$$

### Q10

$$
(1000\times20)(20\times1)
$$

The inner dimensions match.

Therefore:

$$
\boxed{X\mathbf w:1000\times1}
$$

It can represent:

> **1000 model outputs/predictions — one for each observation.**

---

# 🔥 The Five Things You Must Remember

If you remember nothing else from this lesson, remember these:

### 1. Matrix

$$
\boxed{\text{A rectangular collection of numbers}}
$$

### 2. Rows

$$
\boxed{\text{Usually observations in ML}}
$$

### 3. Columns

$$
\boxed{\text{Usually features in ML}}
$$

### 4. Matrix dimensions

$$
\boxed{\text{rows}\times\text{columns}}
$$

### 5. Matrix multiplication

$$
\boxed{\text{row}\times\text{column}}
$$

And especially:

$$
\boxed{
(m\times n)(n\times p)=(m\times p)
}
$$

---

# 🧠 One Final Mental Picture

Imagine a university.

### One student:

$$
\mathbf{x}
$$

→ **vector**

### All students:

$$
X
$$

→ **matrix**

### Model's learned weights:

$$
\mathbf w
$$

→ **weight vector**

### Predictions:

$$
X\mathbf w
$$

→ **one prediction per student**

So:

$$
\boxed{
\text{Students}
\rightarrow
\text{Feature Vectors}
\rightarrow
\text{Feature Matrix}
\rightarrow
\text{Matrix Operations}
\rightarrow
\text{Predictions}
}
$$

That is the bridge from **basic mathematics to real machine learning**.

---

## Next: Lesson 10 — Summation Notation \(\Sigma\)

Before we start NumPy, there's one more mathematical language you need to become comfortable with.

You'll learn what this means:

$$
\sum_{i=1}^{n}x_i
$$

and why ML papers are full of expressions like:

$$
\text{MSE}=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat y_i)^2
$$

We'll break summation notation down **from absolute zero**, then connect it to:

- averages
- vectors
- variance
- MSE
- linear regression
- ML loss functions
- and eventually NumPy operations.

After that, we'll move into **basic probability**, then the **statistics foundation**, and only then start the practical NumPy phase.
