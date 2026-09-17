# Lesson 10 — Summation Notation (Σ)

We are now learning one of the **most important pieces of mathematical notation in ML**.

You will see `Σ` everywhere:

- Mean
- Variance
- Standard deviation
- Probability
- Linear regression
- MSE / RMSE
- Loss functions
- Gradient descent
- Physics equations
- Quantum mechanics

The good news is that the idea is extremely simple:

> **Σ simply means: “Keep adding.”**

---

## 1. Why Do We Need Σ?

Suppose we have five students' study hours:

$$
2,\ 4,\ 3,\ 5,\ 1
$$

If we want to add them, we can write:

$$
2+4+3+5+1
$$

Easy.

But imagine we have **1 million observations**.

Writing:

$$
x_1+x_2+x_3+x_4+\cdots+x_{999999}+x_{1000000}
$$

would be ridiculous.

So mathematicians created a shorthand:

$$
\boxed{\sum_{i=1}^{n}x_i}
$$

Read this as:

> **“Sum all \(x_i\), starting from \(i=1\) and ending at \(i=n\).”**

---

# 2. Understanding Every Part of Σ

Look at:

$$
\boxed{\sum_{i=1}^{5}x_i}
$$

Don't treat this as a scary symbol.

Break it apart:

### `Σ`

$$
\sum
$$

means:

> **Add everything.**

---

### \(i\)

\(i\) is simply a **counter/index**.

Think of it like a Python `for` loop:

```text
for i = 1, 2, 3, 4, 5
```

---

### \(i=1\)

This tells us:

> Start counting from 1.

---

### \(5\)

This tells us:

> Stop at 5.

---

### \(x_i\)

This means:

> Take the value corresponding to the current index.

So:

$$
\sum_{i=1}^{5}x_i
$$

really means:

$$
x_1+x_2+x_3+x_4+x_5
$$

That's all!

---

# 3. The Most Important Mental Model

Think of Sigma as a **mathematical for-loop**.

$$
\boxed{\sum_{i=1}^{5}x_i}
$$

means:

```text
total = 0

i = 1 → add x₁
i = 2 → add x₂
i = 3 → add x₃
i = 4 → add x₄
i = 5 → add x₅
```

So remember:

> **Σ = mathematical "for loop + accumulation".**

This mental model will become extremely useful when we start using NumPy.

---

# 4. Simple Example

Suppose:

$$
x_1=2
$$

$$
x_2=4
$$

$$
x_3=3
$$

$$
x_4=5
$$

$$
x_5=1
$$

Then:

$$
\sum_{i=1}^{5}x_i
$$

means:

$$
x_1+x_2+x_3+x_4+x_5
$$

Substitute the values:

$$
=2+4+3+5+1
$$

$$
\boxed{=15}
$$

---

# 5. Σ Doesn't Always Start at 1

For example:

$$
\sum_{i=3}^{6}x_i
$$

means:

$$
x_3+x_4+x_5+x_6
$$

Notice that we start at 3.

Another example:

$$
\sum_{i=5}^{8}x_i
$$

means:

$$
x_5+x_6+x_7+x_8
$$

---

# 6. Σ Can Sum Numbers Directly

Consider:

$$
\sum_{i=1}^{5}i
$$

Here we're not summing \(x_i\).

We're summing \(i\) itself.

Expand it:

$$
1+2+3+4+5
$$

Therefore:

$$
\boxed{\sum_{i=1}^{5}i=15}
$$

---

# 7. Σ With an Expression

This is where things become more interesting.

Consider:

$$
\sum_{i=1}^{4}2x_i
$$

This means:

$$
2x_1+2x_2+2x_3+2x_4
$$

Suppose:

$$
x=[1,2,3,4]
$$

Then:

$$
2(1)+2(2)+2(3)+2(4)
$$

$$
=2+4+6+8
$$

$$
\boxed{=20}
$$

The important idea:

> Whatever is inside the summation gets evaluated for every value of \(i\).

---

# 8. Σ With Addition

Consider:

$$
\sum_{i=1}^{3}(x_i+5)
$$

This means:

$$
(x_1+5)+(x_2+5)+(x_3+5)
$$

Suppose:

$$
x_1=2,\quad x_2=4,\quad x_3=6
$$

Then:

$$
(2+5)+(4+5)+(6+5)
$$

$$
=7+9+11
$$

$$
\boxed{=27}
$$

---

# 9. Σ With Squares

Consider:

$$
\sum_{i=1}^{3}x_i^2
$$

This means:

$$
x_1^2+x_2^2+x_3^2
$$

Suppose:

$$
x=[2,3,4]
$$

Then:

$$
2^2+3^2+4^2
$$

$$
=4+9+16
$$

$$
\boxed{=29}
$$

---

# 10. VERY IMPORTANT: Two Similar-Looking Expressions

You must understand this distinction.

### Expression A

$$
\boxed{\sum_{i=1}^{3}x_i^2}
$$

means:

$$
x_1^2+x_2^2+x_3^2
$$

---

### Expression B

$$
\boxed{\left(\sum_{i=1}^{3}x_i\right)^2}
$$

means:

First sum:

$$
x_1+x_2+x_3
$$

Then square the **whole result**.

For:

$$
x=[2,3,4]
$$

Expression A:

$$
2^2+3^2+4^2=29
$$

Expression B:

$$
(2+3+4)^2
$$

$$
=9^2=81
$$

Therefore:

$$
\boxed{\sum x_i^2\neq\left(\sum x_i\right)^2}
$$

in general.

This distinction becomes extremely important in statistics and ML.

---

# 11. Σ and the Mean

Now we reach our first major ML/statistics connection.

Suppose our data is:

$$
2,\ 4,\ 3,\ 5,\ 1
$$

We already know the mean is:

$$
\frac{2+4+3+5+1}{5}
$$

Using summation notation:

$$
\boxed{
\bar{x}=
\frac{1}{n}\sum_{i=1}^{n}x_i
}
$$

This equation is extremely important.

Let's decode it.

### Step 1 — Sum everything

$$
\sum_{i=1}^{n}x_i
$$

means:

$$
x_1+x_2+\cdots+x_n
$$

### Step 2 — Divide by the number of observations

$$
\frac{1}{n}
$$

So:

$$
\boxed{\text{Mean}=\frac{\text{sum of all values}}{\text{number of values}}}
$$

That's the entire meaning.

---

# 12. Concrete Mean Example

Data:

$$
x=[2,4,3,5,1]
$$

There are:

$$
n=5
$$

Therefore:

$$
\bar{x}
=
\frac{1}{5}
\sum_{i=1}^{5}x_i
$$

Calculate the sum:

$$
\sum_{i=1}^{5}x_i=15
$$

Therefore:

$$
\bar{x}=\frac{15}{5}
$$

$$
\boxed{\bar{x}=3}
$$

So now you can read:

$$
\boxed{\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i}
$$

without being intimidated by it.

---

# 13. Σ and Variance

This is where Sigma becomes **really important**.

Later, when we properly study statistics, we'll learn variance in detail.

For now, just understand the structure.

Variance is:

$$
\boxed{
\sigma^2=
\frac{1}{n}
\sum_{i=1}^{n}(x_i-\mu)^2
}
$$

Don't worry about memorizing it yet.

Understand the story.

For every observation:

### 1. Take the value

$$
x_i
$$

### 2. Compare it with the mean

$$
x_i-\mu
$$

### 3. Square the difference

$$
(x_i-\mu)^2
$$

### 4. Do this for every observation

That's the:

$$
\sum
$$

### 5. Average the results

That's:

$$
\frac{1}{n}
$$

So Sigma is simply saying:

> **"Do this calculation for every data point and add all the results."**

---

# 14. Σ and Machine Learning: MSE

Now we arrive at one of the most important equations in ML.

You have already encountered **MSE — Mean Squared Error**.

Its mathematical definition is:

$$
\boxed{
MSE=
\frac{1}{n}
\sum_{i=1}^{n}(y_i-\hat y_i)^2
}
$$

At first glance, this looks complicated.

But now we can decode it.

---

## Step 1 — Actual value

$$
y_i
$$

This is what actually happened.

---

## Step 2 — Prediction

$$
\hat y_i
$$

This is what the model predicted.

The hat:

$$
\hat{}
$$

usually means:

> **estimated/predicted value**

---

## Step 3 — Error

$$
y_i-\hat y_i
$$

Actual minus prediction.

---

## Step 4 — Square the error

$$
(y_i-\hat y_i)^2
$$

Why square?

Because otherwise positive and negative errors could cancel each other.

---

## Step 5 — Do this for every observation

That's:

$$
\sum_{i=1}^{n}
$$

---

## Step 6 — Average them

That's:

$$
\frac{1}{n}
$$

Therefore:

$$
\boxed{
MSE=
\frac{1}{n}
\sum_{i=1}^{n}(y_i-\hat y_i)^2
}
$$

means:

> **Calculate the squared prediction error for every observation, add them all together, then divide by the number of observations.**

That's it.

---

# 15. MSE Example

Suppose the actual values are:

$$
y=[10,20,30]
$$

and the model predicts:

$$
\hat y=[12,18,29]
$$

### Observation 1

Actual:

$$
10
$$

Prediction:

$$
12
$$

Error:

$$
10-12=-2
$$

Squared error:

$$
(-2)^2=4
$$

---

### Observation 2

$$
20-18=2
$$

Squared:

$$
2^2=4
$$

---

### Observation 3

$$
30-29=1
$$

Squared:

$$
1^2=1
$$

Therefore:

$$
MSE=
\frac{4+4+1}{3}
$$

$$
=\frac{9}{3}
$$

$$
\boxed{MSE=3}
$$

Sigma allowed us to express all of that compactly:

$$
\boxed{
MSE=\frac{1}{3}
\sum_{i=1}^{3}(y_i-\hat y_i)^2
}
$$

---

# 16. Σ in Linear Regression

Suppose our model predicts:

$$
\hat y_i=w_1x_{i1}+w_2x_{i2}+b
$$

for each observation.

We could calculate the prediction error for every observation:

$$
(y_1-\hat y_1)^2
$$

$$
(y_2-\hat y_2)^2
$$

$$
(y_3-\hat y_3)^2
$$

$$
\vdots
$$

$$
(y_n-\hat y_n)^2
$$

And add them:

$$
(y_1-\hat y_1)^2+
(y_2-\hat y_2)^2+
\cdots+
(y_n-\hat y_n)^2
$$

Or simply:

$$
\boxed{
\sum_{i=1}^{n}(y_i-\hat y_i)^2
}
$$

This is why you will encounter Sigma constantly when studying **linear regression and optimization**.

---

# 17. Σ Rules You Should Know

There are a few very useful rules.

## Rule 1 — Constant can come outside

$$
\boxed{
\sum_{i=1}^{n}cx_i
=
c\sum_{i=1}^{n}x_i
}
$$

Example:

$$
2x_1+2x_2+2x_3
$$

can be written:

$$
2(x_1+x_2+x_3)
$$

Therefore:

$$
\sum 2x_i=2\sum x_i
$$

---

## Rule 2 — Sum distributes over addition

$$
\boxed{
\sum_{i=1}^{n}(a_i+b_i)
=
\sum_{i=1}^{n}a_i+
\sum_{i=1}^{n}b_i
}
$$

For example:

$$
(a_1+b_1)+(a_2+b_2)+(a_3+b_3)
$$

equals:

$$
(a_1+a_2+a_3)+(b_1+b_2+b_3)
$$

---

# 18. Σ in Physics

As a physics student, you'll encounter this everywhere.

Suppose several forces act on an object:

$$
F_1,F_2,F_3,\ldots,F_n
$$

Total force:

$$
\boxed{
F_{\text{total}}=\sum_{i=1}^{n}F_i
}
$$

Meaning:

$$
F_{\text{total}}
=
F_1+F_2+F_3+\cdots+F_n
$$

---

### Discrete probability

Suppose a random variable can take values:

$$
x_1,x_2,\ldots,x_n
$$

The probabilities must add up to 1:

$$
\boxed{
\sum_{i=1}^{n}P(X=x_i)=1
}
$$

Again, Sigma simply means:

> Add all of them.

---

# 19. Σ and Scientific Computing

Imagine an experiment where you measure temperature 10,000 times:

$$
T_1,T_2,T_3,\ldots,T_{10000}
$$

The average temperature is:

$$
\bar T=
\frac{1}{10000}
\sum_{i=1}^{10000}T_i
$$

You don't need to write 10,000 terms.

That's one of the major purposes of mathematical notation:

> **Represent a huge amount of computation in a compact, precise way.**

---

# 20. The Deep Connection: Σ → Vectors → Matrices → NumPy

Look at the progression we've been building.

### Individual values

$$
x_1,x_2,x_3,\ldots
$$

↓

### Vector

$$
\mathbf{x}=
\begin{bmatrix}
x_1\\
x_2\\
x_3\\
\vdots\\
x_n
\end{bmatrix}
$$

↓

### Summation

$$
\sum_{i=1}^{n}x_i
$$

↓

### Statistics

$$
\bar{x}=
\frac1n\sum_{i=1}^{n}x_i
$$

↓

### ML loss

$$
MSE=
\frac1n\sum_{i=1}^{n}(y_i-\hat y_i)^2
$$

↓

### Matrix/vector notation

Eventually, we can express many of these operations using vectors and matrices.

↓

### NumPy

NumPy allows a computer to perform these operations efficiently over huge arrays.

So we are building toward something very important:

> **Mathematics describes the operation → NumPy performs the operation efficiently.**

---

# 21. One More Powerful Mental Model

Imagine you have 1,000,000 students.

For each student, you calculate something.

Sigma says:

> **"Do this for student 1, then student 2, then student 3... all the way to student 1,000,000, and accumulate the results."**

That's why I want you to remember:

$$
\boxed{\Sigma=\text{REPEAT + ADD}}
$$

Or even better:

> 🧠 **Sigma = a mathematical accumulation loop.**

---

# 22. Practice — Don't Look at the Answers Yet

### Q1

Expand:

$$
\sum_{i=1}^{4}x_i
$$

---

### Q2

Calculate:

$$
\sum_{i=1}^{5}i
$$

---

### Q3

If:

$$
x=[2,4,6]
$$

calculate:

$$
\sum_{i=1}^{3}x_i
$$

---

### Q4

If:

$$
x=[1,2,3]
$$

calculate:

$$
\sum_{i=1}^{3}x_i^2
$$

---

### Q5

If:

$$
x=[2,4,6]
$$

calculate:

$$
\left(\sum_{i=1}^{3}x_i\right)^2
$$

---

### Q6

What does this mean in plain English?

$$
\frac{1}{n}\sum_{i=1}^{n}x_i
$$

---

### Q7

What does this mean?

$$
\sum_{i=1}^{n}(y_i-\hat y_i)^2
$$

---

# Answers

### Q1

$$
x_1+x_2+x_3+x_4
$$

### Q2

$$
1+2+3+4+5=15
$$

### Q3

$$
2+4+6=12
$$

### Q4

$$
1^2+2^2+3^2
$$

$$
=1+4+9
$$

$$
\boxed{14}
$$

### Q5

First:

$$
2+4+6=12
$$

Then:

$$
12^2=\boxed{144}
$$

### Q6

> Add all the \(x_i\) values and divide by the number of observations.

That's the **mean**.

### Q7

> For every observation, calculate the prediction error, square it, and add all the squared errors.

---

# 🧠 Lesson 10 Mental Map

```text
                    Σ
                    │
              "ADD EVERYTHING"
                    │
             ┌──────┴──────┐
             │             │
          Index          Expression
             │             │
        i = 1 → n      what to calculate
             │             │
             └──────┬──────┘
                    │
              Repeat + Add
                    │
        ┌───────────┼────────────┐
        │           │            │
       Mean      Variance       MSE
        │           │            │
    1/n Σxᵢ    1/n Σ(...)²   1/n Σ(error)²
        │           │            │
        └───────────┼────────────┘
                    │
              Machine Learning
                    │
             NumPy later
```

## The one thing I want you to remember

When you see:

$$
\boxed{\sum_{i=1}^{n}f(x_i)}
$$

don't think **“complicated mathematics.”**

Translate it immediately into:

> **“For every \(i\) from 1 to \(n\), calculate \(f(x_i)\), then add all the results.”**

Once that becomes automatic, a huge amount of ML mathematics becomes much easier.

---

### Next lesson

**Lesson 11 — Basic Probability**

We'll build probability **from absolute zero**: experiments, outcomes, events, probability, conditional probability, independence, random variables, and eventually connect them to ML and quantum physics.
