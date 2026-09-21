# Lesson 5 — Algebra: The Language Behind Machine Learning

Now we're moving from **basic arithmetic** into the mathematics that lets us describe relationships.

Don't worry if you've seen algebra before. We're going to build it from the ground up.

The goal is that when you later see something like:

$$
\hat y=w_1x_1+w_2x_2+b
$$

in Machine Learning, it won't look like a mysterious formula. You'll be able to **read it like a sentence**.

---

# 1. What Is Algebra?

Arithmetic asks:

> What is \(5+3\)?

We know:

$$
5+3=8
$$

Algebra asks a more powerful question:

> What if I don't know the number?

For example:

$$
x+3=8
$$

Now we don't know \(x\).

We need to discover it.

Clearly:

$$
x=5
$$

That's algebra.

### The big idea

> **Algebra is arithmetic where some numbers are unknown or represented by symbols.**

---

# 2. Variables Are Unknown Boxes

Imagine a box:

📦

You don't know what's inside.

We call it:

$$
x
$$

Suppose someone tells you:

> "There is some number in the box. Add 3 to it and you get 8."

Mathematically:

$$
x+3=8
$$

You need to figure out what's inside.

Obviously:

$$
x=5
$$

So algebra is essentially:

> **Using known information to discover unknown quantities.**

---

# 3. Expressions

Consider:

$$
3x+5
$$

This is an **algebraic expression**.

It contains:

- \(x\) → variable
- \(3\) → coefficient
- \(5\) → constant
- \(+\) → operation

If:

$$
x=10
$$

then:

$$
3x+5
$$

becomes:

$$
3(10)+5
$$

$$
=30+5
$$

$$
=35
$$

So an expression becomes a number when we know the variable's value.

---

# 4. Coefficients

Consider:

$$
7x
$$

The \(7\) is called the **coefficient**.

It means:

$$
7x=7\times x
$$

For example, if:

$$
x=4
$$

then:

$$
7x=7(4)=28
$$

In ML, you'll see this constantly.

For example:

$$
5x_1+2x_2
$$

Here:

- \(5\) is the coefficient/weight of \(x_1\)
- \(2\) is the coefficient/weight of \(x_2\)

Those coefficients eventually become **model parameters**.

---

# 5. Constants

A constant is simply a value that doesn't depend on the variable.

In:

$$
3x+7
$$

the \(7\) is a constant.

Why?

Because it doesn't matter what \(x\) is.

If:

$$
x=2
$$

then:

$$
3(2)+7=13
$$

If:

$$
x=100
$$

then:

$$
3(100)+7=307
$$

The \(7\) remains \(7\).

---

# 6. Equations

Now we introduce the **equals sign**:

$$
=
$$

An equation says:

> **The thing on the left has the same value as the thing on the right.**

For example:

$$
x+3=8
$$

means:

```text
LEFT SIDE       RIGHT SIDE
   x + 3    =       8
```

Both sides must have the same value.

---

# 7. The Balance Scale Mental Model ⚖️

This is probably the best way to understand equations.

Imagine a perfectly balanced scale:

```text
        ⚖️
   [ x + 3 ] = [ 8 ]
```

Both sides have equal weight.

If you add something to one side, you must add it to the other.

If you remove something from one side, you must remove it from the other.

This gives us the fundamental algebra rule:

> **Whatever you do to one side of an equation, do to the other side.**

---

# 8. Solving an Equation

Let's solve:

$$
x+3=8
$$

We want \(x\) alone.

Currently:

$$
x+3
$$

We need to remove \(+3\).

The opposite operation is subtraction.

So subtract 3 from both sides:

$$
x+3-3=8-3
$$

Therefore:

$$
x=5
$$

Done.

---

# 9. Why Opposite Operations?

This is an important idea.

Operations have opposites:

| Operation   | Opposite    |
| ----------- | ----------- |
| \(+5\)      | \(-5\)      |
| \(-5\)      | \(+5\)      |
| \(\times5\) | \(\div5\)   |
| \(\div5\)   | \(\times5\) |
| square      | square root |
| exponent    | logarithm   |

The goal of solving an equation is:

> **Undo whatever has been done to the variable.**

---

# 10. Example: Multiplication

Suppose:

$$
3x=15
$$

The \(x\) has been multiplied by 3.

Undo multiplication with division:

$$
\frac{3x}{3}=\frac{15}{3}
$$

Therefore:

$$
x=5
$$

---

# 11. Example: Multiplication + Addition

Consider:

$$
3x+2=14
$$

We want \(x\) alone.

### Step 1: Remove \(+2\)

$$
3x+2-2=14-2
$$

$$
3x=12
$$

### Step 2: Remove \(\times3\)

$$
\frac{3x}{3}=\frac{12}{3}
$$

Therefore:

$$
\boxed{x=4}
$$

---

# 12. The Reverse Order Principle

Notice what happened.

The original expression was:

$$
3x+2
$$

Operations were applied in this order:

1. multiply \(x\) by 3
2. add 2

To undo them, we went backwards:

1. subtract 2
2. divide by 3

This is extremely important.

> **When solving equations, undo operations in reverse order.**

---

# 13. Example With a Negative Number

Solve:

$$
2x-6=10
$$

First remove \(-6\).

Add 6:

$$
2x=16
$$

Then divide by 2:

$$
x=8
$$

Check:

$$
2(8)-6=16-6=10
$$

Correct.

---

# 14. Algebra Is Everywhere in ML

Consider a simple prediction model:

$$
y=3x+5
$$

Suppose:

$$
x=10
$$

Then:

$$
y=3(10)+5
$$

$$
y=35
$$

This is already a tiny ML-like model.

The model takes an input:

$$
x
$$

and transforms it into an output:

$$
y
$$

---

# 15. Linear Relationships

Consider:

$$
y=2x+1
$$

Let's calculate some values:

| \(x\) | \(y\) |
| ----: | ----: |
|     0 |     1 |
|     1 |     3 |
|     2 |     5 |
|     3 |     7 |
|     4 |     9 |

Every time \(x\) increases by 1, \(y\) increases by 2.

This is a **linear relationship**.

You'll encounter linear relationships constantly in ML.

---

# 16. The ML Version

Suppose we're predicting a student's exam score.

Features:

$$
x_1=\text{study hours}
$$

$$
x_2=\text{sleep hours}
$$

$$
x_3=\text{attendance}
$$

We might have:

$$
\hat y
=
w_1x_1+w_2x_2+w_3x_3+b
$$

Let's decode this.

### \(\hat y\)

Predicted value.

The hat means:

> "This is a prediction."

### \(x_1,x_2,x_3\)

Input features.

### \(w_1,w_2,w_3\)

Weights.

### \(b\)

Bias/intercept.

---

# 17. A Concrete Example

Suppose:

$$
x_1=5
$$

$$
x_2=7
$$

$$
x_3=90
$$

And our model has:

$$
w_1=4
$$

$$
w_2=2
$$

$$
w_3=0.3
$$

$$
b=10
$$

Then:

$$
\hat y
=
4(5)+2(7)+0.3(90)+10
$$

Calculate:

$$
=20+14+27+10
$$

$$
\boxed{\hat y=71}
$$

We just used algebra to make an ML prediction.

---

# 18. Why Are Weights Necessary?

Imagine three people are giving advice about a student's performance.

- Study hours → very important
- Sleep → moderately important
- Attendance → somewhat important

We could assign:

$$
w_1=4
$$

$$
w_2=2
$$

$$
w_3=0.3
$$

The weights determine how strongly each feature contributes.

This is the beginning of understanding **model parameters**.

Later, ML algorithms learn these weights automatically from data.

---

# 19. Multiple Variables

Real ML problems usually have many features.

Instead of:

$$
y=3x+5
$$

we might have:

$$
y=w_1x_1+w_2x_2+w_3x_3+\cdots+w_nx_n+b
$$

The dots:

$$
\cdots
$$

mean:

> "and so on."

So if we have 100 features:

$$
y=w_1x_1+w_2x_2+\cdots+w_{100}x_{100}+b
$$

This looks complicated.

But conceptually it's still:

> **multiply each feature by its weight, add everything together, then add the bias.**

Later, **vectors and matrices** will give us a much cleaner way to write this.

---

# 20. Algebraic Simplification

Consider:

$$
3x+2x
$$

Both terms contain \(x\).

So:

$$
3x+2x=5x
$$

This is called **combining like terms**.

Another example:

$$
7x-3x=4x
$$

But:

$$
3x+4
$$

cannot become:

$$
7x
$$

because \(3x\) and \(4\) are different types of terms.

Think of it like:

$$
3\text{ apples}+4\text{ apples}=7\text{ apples}
$$

but:

$$
3\text{ apples}+4\text{ oranges}
$$

cannot become 7 apples.

---

# 21. Distributive Property

You'll see this everywhere.

Consider:

$$
3(x+2)
$$

The 3 multiplies **everything inside the parentheses**:

$$
3(x+2)=3x+6
$$

Similarly:

$$
5(x-2)=5x-10
$$

The general rule:

$$
\boxed{a(b+c)=ab+ac}
$$

This becomes especially useful when manipulating ML equations.

---

# 22. Factoring — The Reverse

If:

$$
3x+6
$$

we can take out the common factor 3:

$$
3x+6=3(x+2)
$$

This is called **factoring**.

So:

### Expanding

$$
3(x+2)\rightarrow3x+6
$$

### Factoring

$$
3x+6\rightarrow3(x+2)
$$

They are reverse operations.

---

# 23. Fractions in Algebra

Suppose:

$$
\frac{x}{3}=5
$$

We want \(x\).

Multiply both sides by 3:

$$
x=15
$$

Another example:

$$
\frac{2x}{5}=8
$$

Multiply by 5:

$$
2x=40
$$

Divide by 2:

$$
\boxed{x=20}
$$

---

# 24. Rearranging Equations

This skill is **very important for physics and ML**.

Suppose:

$$
v=\frac{d}{t}
$$

You know velocity and time but want distance.

Multiply both sides by \(t\):

$$
vt=d
$$

Therefore:

$$
\boxed{d=vt}
$$

This is equation rearrangement.

---

# 25. Physics + ML Connection

Physics students constantly rearrange equations.

For example:

$$
F=ma
$$

Want acceleration?

$$
a=\frac{F}{m}
$$

Want mass?

$$
m=\frac{F}{a}
$$

Same algebraic principle.

ML is not using a different kind of algebra.

It's the **same algebra applied to data and models**.

---

# 26. Equations vs Expressions

This distinction is important.

### Expression

$$
3x+5
$$

There is no equals sign.

### Equation

$$
3x+5=20
$$

There is an equals sign.

Think:

> **Expression = mathematical phrase**

> **Equation = mathematical statement that two things are equal**

---

# 27. Functions — A Preview

Now we're approaching one of the most important mathematical ideas for ML.

Suppose:

$$
y=2x+1
$$

We can write:

$$
f(x)=2x+1
$$

This means:

> "Function \(f\) takes \(x\) as input and produces \(2x+1\) as output."

Think of a machine:

```text
       INPUT
         x
         ↓
   ┌─────────────┐
   │   f(x)      │
   │  2x + 1     │
   └─────────────┘
         ↓
       OUTPUT
       2x + 1
```

For:

$$
x=3
$$

we get:

$$
f(3)=2(3)+1=7
$$

This concept will become **central** in ML.

---

# 28. A Machine Learning Model Is Essentially a Function

This is a very important mental shift.

A model can be thought of as:

$$
\boxed{\text{input}\rightarrow\text{function/model}\rightarrow\text{prediction}}
$$

For example:

$$
x\rightarrow f(x)\rightarrow\hat y
$$

With multiple features:

$$
X\rightarrow f(X)\rightarrow\hat y
$$

So when you hear:

> "The model learned a function"

you should understand what that means.

It means the model learned a mathematical relationship that maps inputs to outputs.

---

# 29. The Deep Connection

Let's connect everything we've learned so far:

```text
Numbers
   ↓
Variables
   ↓
Arithmetic
   ↓
Fractions / Ratios
   ↓
Powers / Roots / Logs
   ↓
Algebra
   ↓
Functions
   ↓
Vectors
   ↓
Matrices
   ↓
Machine Learning Models
```

We're building the mathematical language that ML is written in.

---

# 30. Practice

Try these **without looking at the answers**.

### Q1

Solve:

$$
x+7=15
$$

---

### Q2

Solve:

$$
3x=21
$$

---

### Q3

Solve:

$$
2x+5=17
$$

---

### Q4

Solve:

$$
5x-10=20
$$

---

### Q5

Simplify:

$$
3x+5x
$$

---

### Q6

Expand:

$$
4(x+3)
$$

---

### Q7

If:

$$
y=3x+2
$$

what is \(y\) when:

$$
x=4
$$

---

### Q8

Given:

$$
y=5x_1+2x_2
$$

and:

$$
x_1=3,\qquad x_2=4
$$

calculate \(y\).

---

### Q9

Rearrange:

$$
v=\frac{d}{t}
$$

to find \(t\).

---

### Q10 — ML thinking

A model is:

$$
\hat y=4x+10
$$

What prediction does it make when:

$$
x=7?
$$

---

# Answers

1. \(x=8\)

2. \(x=7\)

3. \(x=6\)

4. \(x=6\)

5. \(8x\)

6. \(4x+12\)

7. \(14\)

8. \(23\)

9. \(\displaystyle t=\frac{d}{v}\)

10. \(38\)

---

# 🧠 The "Never Forget" Version

Remember algebra as:

> **A detective solving for the unknown. 🕵️**

You know some information.

You have an unknown:

$$
x
$$

You manipulate the equation until:

$$
\boxed{x=\text{something}}
$$

And the golden rule is:

> ⚖️ **Whatever you do to one side, do to the other side.**

And for ML:

> **Features go into a mathematical function; the function produces a prediction.**

$$
\boxed{X\rightarrow f(X)\rightarrow\hat y}
$$

---

## One important checkpoint

Before moving on, make sure these feel comfortable:

- variable
- coefficient
- constant
- expression
- equation
- solving for an unknown
- opposite operations
- distributive property
- rearranging equations
- basic functions
- weights in an ML equation

**Next lesson: Functions — from absolute zero.**

We'll go much deeper into **input → function → output**, domain, range, linear/nonlinear functions, graphs, and why essentially **every ML model can be understood as a function**.
