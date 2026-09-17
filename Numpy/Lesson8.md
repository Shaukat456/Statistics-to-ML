# Lesson 8 — Vectors ➡️

This is one of the **most important lessons in the entire mathematical foundation for Machine Learning**.

If you understand vectors properly, later topics like:

- NumPy arrays
- feature vectors
- matrices
- linear regression
- neural networks
- gradients
- embeddings
- quantum states
- scientific computing

will become much easier.

We will go slowly.

---

# 1. First: What Problem Does a Vector Solve?

Suppose I tell you:

> A car is traveling at 80 km/h.

That's one number.

But suppose I tell you:

> A car is traveling 80 km/h **toward the east**.

Now we need two pieces of information:

1. **Magnitude** → 80 km/h
2. **Direction** → east

This is the basic idea behind a **vector**.

A vector carries information about **magnitude and direction**.

---

# 2. Scalar vs Vector

Before vectors, we need one important distinction.

## Scalar

A scalar is simply a quantity with magnitude.

Examples:

- temperature = 30°C
- mass = 5 kg
- time = 10 s
- speed = 80 km/h
- energy = 100 J

For example:

$$
T=30^\circ C
$$

There is no direction attached.

---

## Vector

A vector has magnitude **and direction**.

Examples:

- velocity
- force
- displacement
- acceleration
- electric field

For example:

$$
\vec v = 80\text{ km/h east}
$$

The arrow over \(v\):

$$
\vec v
$$

means we're treating \(v\) as a vector.

---

# 3. The Simplest Mental Model

Imagine you're playing a video game.

Your character is standing here:

```text
●
```

Now you say:

> Move 5 steps right.

That's a vector.

It tells the character:

> **How far + which direction**

Represent it as:

$$
\vec v=
\begin{bmatrix}
5\\
0
\end{bmatrix}
$$

The 5 means:

> Move 5 units horizontally.

The 0 means:

> Don't move vertically.

---

# 4. A Vector Can Be Represented by Components

Consider:

$$
\vec v=
\begin{bmatrix}
3\\
4
\end{bmatrix}
$$

This means:

- 3 units in the x-direction
- 4 units in the y-direction

You can imagine:

```text
y
↑
|             ●
|           /
|         /
|       /
|     /
|   /
| /
●────────────────→ x
      3
```

The vector moves:

$$
3
$$

horizontally and:

$$
4
$$

vertically.

---

# 5. Vector vs Point

This distinction is subtle but important.

A point:

$$
(3,4)
$$

describes a **location**.

A vector:

$$
\begin{bmatrix}
3\\
4
\end{bmatrix}
$$

describes a **displacement/direction and magnitude**.

They can look mathematically similar, but conceptually they are different.

### Point

> "Where am I?"

### Vector

> "How do I move?"

This distinction becomes increasingly important in physics and ML.

---

# 6. Why Are Vectors So Important in Machine Learning?

Now we reach the major connection.

Suppose we have a student:

| Feature     | Value |
| ----------- | ----: |
| Study Hours |     5 |
| Sleep Hours |     7 |
| Attendance  |    90 |

Instead of thinking of these as three separate numbers, we can package them together:

$$
\boxed{
\mathbf{x}=
\begin{bmatrix}
5\\
7\\
90
\end{bmatrix}
}
$$

This is a **feature vector**.

One student is represented by one vector.

---

# 7. A Dataset Is Many Vectors

Suppose we have:

| Student | Study | Sleep | Attendance |
| ------- | ----: | ----: | ---------: |
| A       |     5 |     7 |         90 |
| B       |     2 |     8 |         75 |
| C       |     8 |     6 |         95 |

We can represent them as:

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

So:

> **One observation = one vector**

This is a fundamental ML concept.

---

# 8. The Dimension of a Vector

Look at:

$$
\mathbf{x}=
\begin{bmatrix}
5\\
7\\
90
\end{bmatrix}
$$

There are three components.

Therefore this is a:

$$
\boxed{3\text{-dimensional vector}}
$$

If:

$$
\mathbf{x}=
\begin{bmatrix}
5\\7
\end{bmatrix}
$$

then it's 2-dimensional.

If:

$$
\mathbf{x}=
\begin{bmatrix}
5\\7\\90\\20\\3
\end{bmatrix}
$$

it's 5-dimensional.

---

# 9. Features = Dimensions

This is an extremely useful ML mental model.

Suppose your dataset has:

```text
age
income
height
weight
experience
education
...
```

If there are 10 features, each observation can be represented as:

$$
\mathbf{x}\in\mathbb R^{10}
$$

The symbol:

$$
\mathbb R
$$

means the **real numbers**.

So:

$$
\mathbb R^{10}
$$

means:

> a 10-dimensional space of real-valued vectors.

Don't worry if that notation looks intimidating.

For now, simply remember:

$$
\boxed{\text{Number of features = number of vector components}}
$$

---

# 10. Vector Addition

Suppose:

$$
\mathbf a=
\begin{bmatrix}
2\\
3
\end{bmatrix}
$$

and:

$$
\mathbf b=
\begin{bmatrix}
4\\
1
\end{bmatrix}
$$

We add corresponding components:

$$
\mathbf a+\mathbf b
=
\begin{bmatrix}
2+4\\
3+1
\end{bmatrix}
$$

Therefore:

$$
\boxed{
\mathbf a+\mathbf b=
\begin{bmatrix}
6\\
4
\end{bmatrix}
}
$$

Very simple:

> **Add component by component.**

---

# 11. Why Does Vector Addition Make Sense?

Imagine:

$$
\mathbf a=(2,3)
$$

means:

> Walk 2 right, 3 up.

Then:

$$
\mathbf b=(4,1)
$$

means:

> Walk 4 right, 1 up.

Doing both movements gives:

$$
(2+4,\;3+1)
$$

$$
=(6,4)
$$

So vector addition is literally:

> **Combine movements.**

---

# 12. Vector Subtraction

Suppose:

$$
\mathbf a=
\begin{bmatrix}
7\\
5
\end{bmatrix}
$$

and:

$$
\mathbf b=
\begin{bmatrix}
2\\
3
\end{bmatrix}
$$

Then:

$$
\mathbf a-\mathbf b
=
\begin{bmatrix}
7-2\\
5-3
\end{bmatrix}
$$

$$
=
\boxed{
\begin{bmatrix}
5\\
2
\end{bmatrix}}
$$

Again:

> Component by component.

---

# 13. Multiplying a Vector by a Number

Suppose:

$$
\mathbf v=
\begin{bmatrix}
2\\
3
\end{bmatrix}
$$

Multiply by 4:

$$
4\mathbf v
=
4
\begin{bmatrix}
2\\
3
\end{bmatrix}
$$

Multiply every component:

$$
=
\begin{bmatrix}
8\\
12
\end{bmatrix}
$$

This is called **scalar multiplication**.

The vector's direction stays the same, but its magnitude changes.

---

# 14. Think of a Vector as an Arrow

This is probably the most useful visualization.

Imagine:

```text
●────────────→
```

The arrow has:

- direction
- length

If we multiply it by 2:

```text
●────────────────────────→
```

Same direction.

Twice the length.

If we multiply by \(-1\):

```text
←────────────●
```

The direction reverses.

---

# 15. Vector Magnitude

Now an important question:

> How long is a vector?

For:

$$
\mathbf v=
\begin{bmatrix}
3\\
4
\end{bmatrix}
$$

we already have a right triangle.

Using Pythagoras:

$$
|\mathbf v|
=
\sqrt{3^2+4^2}
$$

$$
=\sqrt{9+16}
$$

$$
=\sqrt{25}
$$

Therefore:

$$
\boxed{|\mathbf v|=5}
$$

The magnitude is the **length of the vector**.

---

# 16. General Formula for 2D

For:

$$
\mathbf v=
\begin{bmatrix}
x\\
y
\end{bmatrix}
$$

the magnitude is:

$$
\boxed{
|\mathbf v|=\sqrt{x^2+y^2}
}
$$

For a 3D vector:

$$
\mathbf v=
\begin{bmatrix}
x\\
y\\
z
\end{bmatrix}
$$

the magnitude is:

$$
\boxed{
|\mathbf v|
=
\sqrt{x^2+y^2+z^2}
}
$$

And for \(n\) dimensions:

$$
\boxed{
|\mathbf v|
=
\sqrt{\sum_{i=1}^{n}x_i^2}
}
$$

Don't worry about the summation notation yet. We'll study it later.

---

# 17. Vector Magnitude in ML

This becomes extremely useful.

Suppose:

$$
\mathbf x=
\begin{bmatrix}
3\\
4
\end{bmatrix}
$$

Its magnitude is:

$$
5
$$

You can think of magnitude as:

> **How large is this vector overall?**

This concept appears in:

- distance calculations
- normalization
- optimization
- gradients
- similarity
- regularization
- neural networks

---

# 18. Distance Between Two Data Points

Here's a beautiful connection.

Suppose:

$$
A=
\begin{bmatrix}
1\\
2
\end{bmatrix}
$$

and:

$$
B=
\begin{bmatrix}
4\\
6
\end{bmatrix}
$$

To find the displacement from \(A\) to \(B\):

$$
\mathbf d=B-A
$$

Therefore:

$$
\mathbf d=
\begin{bmatrix}
4\\6
\end{bmatrix}
-
\begin{bmatrix}
1\\2
\end{bmatrix}
$$

$$
=
\begin{bmatrix}
3\\4
\end{bmatrix}
$$

Magnitude:

$$
|\mathbf d|
=
\sqrt{3^2+4^2}
$$

$$
=5
$$

Therefore:

$$
\boxed{\text{Distance}(A,B)=5}
$$

So:

> **Distance = magnitude of the difference vector.**

This is a VERY important ML idea.

---

# 19. Why This Matters for KNN

Imagine we have:

```text
Student A → [5, 7]
Student B → [5.2, 7.1]
Student C → [20, 2]
```

If we want to know which students are similar to Student A, we can calculate distances.

Small distance:

> probably similar.

Large distance:

> probably different.

This is the basic intuition behind **K-Nearest Neighbors (KNN)**.

We'll study KNN much later.

For now remember:

$$
\boxed{
\text{Similarity can often be based on distance between vectors}
}
$$

---

# 20. Unit Vector

Suppose:

$$
\mathbf v=
\begin{bmatrix}
3\\
4
\end{bmatrix}
$$

Its magnitude is:

$$
5
$$

A **unit vector** has magnitude:

$$
1
$$

To create one, divide the vector by its magnitude:

$$
\hat{\mathbf v}
=
\frac{\mathbf v}{|\mathbf v|}
$$

Therefore:

$$
\hat{\mathbf v}
=
\frac{1}{5}
\begin{bmatrix}
3\\
4
\end{bmatrix}
$$

$$
=
\begin{bmatrix}
3/5\\
4/5
\end{bmatrix}
$$

So:

$$
\boxed{
\hat{\mathbf v}
=
\begin{bmatrix}
0.6\\
0.8
\end{bmatrix}
}
$$

It preserves the direction but gives it length 1.

---

# 21. Why Do We Need Unit Vectors?

Because sometimes we want:

> **direction only**

without caring about magnitude.

This idea appears throughout:

- physics
- computer graphics
- robotics
- optimization
- machine learning
- quantum mechanics

---

# 22. The Dot Product ⭐

Now we're reaching one of the most important vector operations.

Suppose:

$$
\mathbf a=
\begin{bmatrix}
a_1\\
a_2
\end{bmatrix}
$$

and:

$$
\mathbf b=
\begin{bmatrix}
b_1\\
b_2
\end{bmatrix}
$$

Their **dot product** is:

$$
\boxed{
\mathbf a\cdot\mathbf b
=
a_1b_1+a_2b_2
}
$$

Notice something:

The result is a **single number**.

Not another vector.

---

# 23. Example of Dot Product

Suppose:

$$
\mathbf a=
\begin{bmatrix}
2\\
3
\end{bmatrix}
$$

and:

$$
\mathbf b=
\begin{bmatrix}
4\\
5
\end{bmatrix}
$$

Then:

$$
\mathbf a\cdot\mathbf b
=
(2)(4)+(3)(5)
$$

$$
=8+15
$$

$$
\boxed{23}
$$

That's it.

---

# 24. But Why Is Dot Product Important?

Here's the deeper idea.

The dot product can be written:

$$
\boxed{
\mathbf a\cdot\mathbf b
=
|\mathbf a||\mathbf b|\cos\theta
}
$$

where:

- \(|\mathbf a|\) = magnitude of \(a\)
- \(|\mathbf b|\) = magnitude of \(b\)
- \(\theta\) = angle between them

This means the dot product tells us something about **how aligned two vectors are**.

---

# 25. Imagine Two Arrows

### Same direction

```text
────────→
────────→
```

They are strongly aligned.

$$
\cos(0^\circ)=1
$$

So dot product is positive and large.

---

### Perpendicular

```text
──────→

   ↑
   |
   |
```

Angle:

$$
90^\circ
$$

And:

$$
\cos(90^\circ)=0
$$

Therefore:

$$
\boxed{\mathbf a\cdot\mathbf b=0}
$$

for nonzero perpendicular vectors.

---

### Opposite directions

```text
────────→
←────────
```

Angle:

$$
180^\circ
$$

And:

$$
\cos(180^\circ)=-1
$$

So the dot product is negative.

---

# 26. Dot Product in Machine Learning

This is HUGE.

Remember our ML equation:

$$
\hat y=w_1x_1+w_2x_2+w_3x_3+b
$$

We can package the weights into a vector:

$$
\mathbf w=
\begin{bmatrix}
w_1\\
w_2\\
w_3
\end{bmatrix}
$$

And features into:

$$
\mathbf x=
\begin{bmatrix}
x_1\\
x_2\\
x_3
\end{bmatrix}
$$

Then:

$$
\mathbf w\cdot\mathbf x
=
w_1x_1+w_2x_2+w_3x_3
$$

Therefore:

$$
\boxed{
\hat y=\mathbf w\cdot\mathbf x+b
}
$$

This is one of the fundamental equations of machine learning.

---

# 27. Let's See It Numerically

Suppose:

$$
\mathbf x=
\begin{bmatrix}
5\\
7\\
90
\end{bmatrix}
$$

and:

$$
\mathbf w=
\begin{bmatrix}
4\\
2\\
0.3
\end{bmatrix}
$$

Then:

$$
\mathbf w\cdot\mathbf x
=
(4)(5)+(2)(7)+(0.3)(90)
$$

$$
=20+14+27
$$

$$
=61
$$

If:

$$
b=10
$$

then:

$$
\hat y=61+10
$$

$$
\boxed{\hat y=71}
$$

You have just performed the core computation behind a linear model.

---

# 28. This Is Why Vectors Matter So Much

Without vectors:

$$
w_1x_1+w_2x_2+w_3x_3+\cdots
$$

becomes increasingly messy.

With vectors:

$$
\boxed{
\hat y=\mathbf w\cdot\mathbf x+b
}
$$

Everything becomes compact.

And computers can perform these operations extremely efficiently.

---

# 29. NumPy Connection — But Only Conceptually for Now

Eventually we'll represent:

$$
\mathbf x=
\begin{bmatrix}
5\\
7\\
90
\end{bmatrix}
$$

as a NumPy array.

Conceptually:

```text
[5, 7, 90]
```

And:

$$
\mathbf w=
\begin{bmatrix}
4\\
2\\
0.3
\end{bmatrix}
$$

as:

```text
[4, 2, 0.3]
```

Then NumPy can perform vector operations efficiently.

We are **not learning the NumPy syntax yet**.

First:

> Understand the mathematics.

Then:

> Learn how NumPy implements it.

That's the approach we're following.

---

# 30. Vectorization

There's another important ML idea hiding here.

Suppose we have 1 million students.

Doing:

```text
student 1 → calculate
student 2 → calculate
student 3 → calculate
...
student 1,000,000 → calculate
```

individually is inefficient.

Instead, computers can operate on large collections of numerical data together.

This idea is called **vectorization**.

Later, NumPy will make this extremely natural.

---

# 31. Physics Connection ⚛️

Vectors are everywhere in physics.

For example:

### Position

$$
\vec r=
\begin{bmatrix}
x\\
y\\
z
\end{bmatrix}
$$

### Velocity

$$
\vec v=
\begin{bmatrix}
v_x\\
v_y\\
v_z
\end{bmatrix}
$$

### Force

$$
\vec F=
\begin{bmatrix}
F_x\\
F_y\\
F_z
\end{bmatrix}
$$

Newton's second law:

$$
\vec F=m\vec a
$$

This is vector mathematics.

---

# 32. And Now the Beautiful ML ↔ Physics Connection

Physics:

$$
\vec F=m\vec a
$$

Machine Learning:

$$
\hat y=\mathbf w\cdot\mathbf x+b
$$

Both use vectors to represent multidimensional quantities.

Physics says:

> "These components describe the physical system."

ML says:

> "These components describe the data."

Same mathematical language.

---

# 33. Quantum Physics Connection

Eventually, when you study quantum mechanics/QML, you'll encounter things such as:

$$
|\psi\rangle
$$

A quantum state can be represented mathematically using vectors in a complex vector space.

For a simple qubit:

$$
|\psi\rangle=
\begin{bmatrix}
\alpha\\
\beta
\end{bmatrix}
$$

where:

$$
\alpha,\beta\in\mathbb C
$$

and normalization requires:

$$
|\alpha|^2+|\beta|^2=1
$$

So the vector concept you're learning now is not just for ML.

It is part of the mathematical language connecting:

$$
\boxed{
\text{Physics}
\leftrightarrow
\text{Linear Algebra}
\leftrightarrow
\text{Machine Learning}
\leftrightarrow
\text{Quantum Computing}
}
$$

We'll eventually build toward this.

---

# 34. One Very Important Warning

Don't make this mistake:

> "A vector is just a list of numbers."

That's incomplete.

In ML programming, you will often **store a vector as an array of numbers**.

But mathematically, a vector is an object with structure and operations.

It can represent:

- displacement
- velocity
- a feature vector
- a gradient
- a direction
- a quantum state

The numbers are its **components**.

---

# 35. The Vector Mental Model 🧠

Whenever you see:

$$
\mathbf x=
\begin{bmatrix}
x_1\\
x_2\\
x_3
\end{bmatrix}
$$

think:

> **One object containing several numerical components.**

In ML:

$$
\mathbf x=
\begin{bmatrix}
\text{feature}_1\\
\text{feature}_2\\
\text{feature}_3
\end{bmatrix}
$$

Think:

> **One data point described by several features.**

---

# 36. Your Vector Cheat Sheet

| Concept               | Meaning                                   |
| --------------------- | ----------------------------------------- |
| Scalar                | Magnitude only                            |
| Vector                | Magnitude + direction                     |
| Component             | Individual value inside vector            |
| Dimension             | Number of components                      |
| Magnitude             | Length of vector                          |
| Unit vector           | Vector with length 1                      |
| Addition              | Add corresponding components              |
| Subtraction           | Subtract corresponding components         |
| Scalar multiplication | Multiply every component                  |
| Dot product           | Multiply corresponding components and add |
| Feature vector        | One observation represented as a vector   |
| Weight vector         | Model parameters represented as a vector  |

---

# 37. The Big Picture

We've now built:

```text
                    MATHEMATICS
                         │
             ┌───────────┴───────────┐
             │                       │
         Coordinates              Vectors
             │                       │
          (x, y)             [x₁, x₂, x₃]
             │                       │
           Graphs                 Features
                                     │
                                     ↓
                               ML Data Point
                                     │
                                     ↓
                              Weight Vector
                                     │
                                     ↓
                            Dot Product
                                     │
                                     ↓
                         ŷ = w · x + b
```

This equation:

$$
\boxed{\hat y=\mathbf w\cdot\mathbf x+b}
$$

is worth remembering.

You'll encounter it repeatedly throughout ML.

---

# 🧠 Practice

Try these **without looking back**.

### Q1

Is temperature \(30^\circ C\) a scalar or vector?

### Q2

Is velocity a scalar or vector?

### Q3

How many dimensions does this vector have?

$$
\begin{bmatrix}
2\\
5\\
7\\
9
\end{bmatrix}
$$

### Q4

Calculate:

$$
\begin{bmatrix}
2\\
3
\end{bmatrix}
+
\begin{bmatrix}
5\\
1
\end{bmatrix}
$$

### Q5

Calculate:

$$
3
\begin{bmatrix}
2\\
4
\end{bmatrix}
$$

### Q6

Find the magnitude:

$$
\begin{bmatrix}
6\\
8
\end{bmatrix}
$$

### Q7

Calculate the dot product:

$$
\begin{bmatrix}
2\\
3
\end{bmatrix}
\cdot
\begin{bmatrix}
4\\
5
\end{bmatrix}
$$

### Q8 — ML

Given:

$$
\mathbf w=
\begin{bmatrix}
2\\
3
\end{bmatrix}
$$

$$
\mathbf x=
\begin{bmatrix}
5\\
4
\end{bmatrix}
$$

and:

$$
b=1
$$

calculate:

$$
\hat y=\mathbf w\cdot\mathbf x+b
$$

---

# Answers

### Q1

Scalar.

### Q2

Vector.

### Q3

4 dimensions.

### Q4

$$
\boxed{
\begin{bmatrix}
7\\
4
\end{bmatrix}}
$$

### Q5

$$
\boxed{
\begin{bmatrix}
6\\
12
\end{bmatrix}}
$$

### Q6

$$
\sqrt{6^2+8^2}
=
\sqrt{36+64}
=
\boxed{10}
$$

### Q7

$$
(2)(4)+(3)(5)
$$

$$
=8+15
$$

$$
\boxed{23}
$$

### Q8

First:

$$
\mathbf w\cdot\mathbf x
=
(2)(5)+(3)(4)
$$

$$
=10+12=22
$$

Then:

$$
\hat y=22+1
$$

$$
\boxed{\hat y=23}
$$

---

# 🔑 One Sentence to Never Forget

> **A vector is a mathematical object that lets us represent many related quantities together, and in ML a data point can be represented as a feature vector.**

And the progression we are building is:

$$
\boxed{
\text{Numbers}
\rightarrow
\text{Variables}
\rightarrow
\text{Algebra}
\rightarrow
\text{Functions}
\rightarrow
\text{Coordinates}
\rightarrow
\text{Vectors}
}
$$

The next step is the **matrix**, where instead of representing **one data point with a vector**, we can represent **an entire dataset with a matrix**.

# Next: Lesson 9 — Matrices

We'll build matrices from scratch:

$$
\begin{bmatrix}
5&7&90\\
2&8&75\\
8&6&95
\end{bmatrix}
$$

and understand:

- rows vs columns
- matrix dimensions
- why datasets naturally become matrices
- matrix indexing
- matrix addition
- scalar multiplication
- matrix-vector multiplication
- matrix-matrix multiplication
- transpose
- why ML models rely heavily on matrices
- how a matrix represents thousands/millions of data points
- and eventually how **NumPy arrays map directly onto all of this**.
