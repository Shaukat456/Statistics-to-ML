# Foundation 2 — Variables & Arithmetic

We are still **building the mathematical foundation**. No NumPy yet.

Today’s goal is to understand something that will appear everywhere in ML:

> **How do we represent changing quantities mathematically?**

---

# 1. Start with a real-world situation

Imagine we are studying students.

We record how many hours each student studies:

| Student | Study Hours |
| ------- | ----------: |
| A       |           2 |
| B       |           4 |
| C       |           3 |
| D       |           5 |
| E       |           1 |

We could simply write:

$$
2,\ 4,\ 3,\ 5,\ 1
$$

But suppose I ask:

> "What if I want to talk about the study hours of _any_ student?"

We need a symbol.

We use a **variable**.

For example:

$$
x = \text{study hours}
$$

Now:

- Student A → \(x=2\)
- Student B → \(x=4\)
- Student C → \(x=3\)

So a variable is essentially a **label for a quantity whose value can change**.

---

# 2. Think of a variable as a box 📦

Imagine:

```text
       x
   ┌─────────┐
   │    4    │
   └─────────┘
```

`x` is the name of the box.

`4` is what's currently inside it.

If tomorrow:

```text
       x
   ┌─────────┐
   │    6    │
   └─────────┘
```

the box still has the same name, but its value changed.

That's why it's called a **variable**.

---

# 3. Variables in ML

This idea becomes extremely important.

Suppose we're predicting someone's salary.

We might have:

$$
x = \text{years of experience}
$$

and

$$
y = \text{salary}
$$

For example:

| Experience \(x\) | Salary \(y\) |
| ---------------: | -----------: |
|                1 |       40,000 |
|                2 |       48,000 |
|                3 |       55,000 |
|                5 |       75,000 |
|                8 |      110,000 |

Now we're beginning to see the ML problem.

We want to discover:

$$
x \longrightarrow y
$$

In words:

> How does experience relate to salary?

---

# 4. Arithmetic: the language of calculations

Before statistics, we need basic arithmetic.

There are four fundamental operations.

### Addition

$$
5+3=8
$$

### Subtraction

$$
5-3=2
$$

### Multiplication

$$
5\times3=15
$$

### Division

$$
\frac{5}{3}=1.67
$$

These seem trivial.

But ML is essentially **massive amounts of mathematical operations applied to data**.

For example:

$$
\text{prediction} = 3x+10
$$

If:

$$
x=5
$$

then:

$$
3(5)+10=25
$$

---

# 5. Why variables make mathematics powerful

Consider:

$$
2+4+3+5+1
$$

That's fine for five numbers.

But imagine:

```text
10,000 numbers
```

Writing them all is inconvenient.

Instead, mathematics gives us notation.

We can say:

$$
x_1,x_2,x_3,\ldots,x_n
$$

This means:

```text
x₁ = first observation
x₂ = second observation
x₃ = third observation
...
xₙ = nth observation
```

For our students:

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

---

# 6. What does the little number mean?

This is important.

In:

$$
x_1
$$

the `1` is **not multiplication**.

It means:

> "the first value of x."

Similarly:

$$
x_2
$$

means the second value.

Think of it like numbered boxes:

```text
x₁   x₂   x₃   x₄   x₅
 ↓    ↓    ↓    ↓    ↓
 2    4    3    5    1
```

This notation will become incredibly useful once we start working with NumPy arrays.

---

# 7. A very important distinction: variable vs value

Suppose:

$$
x=5
$$

Here:

**\(x\)** = variable

**5** = value

If:

$$
x=10
$$

the variable hasn't changed.

Its **value** changed.

Think:

> Variable = name
> Value = what's currently stored under that name

---

# 8. Expressions

Now we can combine variables and arithmetic.

Suppose:

$$
x=5
$$

Then:

$$
x+2
$$

means:

$$
5+2=7
$$

Similarly:

$$
2x
$$

means:

$$
2\times x
$$

so:

$$
2(5)=10
$$

And:

$$
x^2
$$

means:

$$
x\times x
$$

so:

$$
5^2=25
$$

---

# 9. Why this matters for ML

Imagine a simple ML model:

$$
y=2x+5
$$

This is a mathematical function.

Suppose:

$$
x=3
$$

Then:

$$
y=2(3)+5
$$

$$
y=11
$$

If:

$$
x=10
$$

then:

$$
y=2(10)+5
$$

$$
y=25
$$

So:

```text
x changes
   ↓
calculation changes
   ↓
y changes
```

That's the basic idea behind a huge amount of machine learning.

---

# 10. Real-world analogy: a vending machine 🥤

Imagine a vending machine.

You put in money:

$$
x
$$

The machine performs some operation.

Suppose the machine gives you:

$$
y=2x+1
$$

Think of it as:

```text
         Mathematical machine

x ─────────→ [ ×2 ] ──→ [ +1 ] ─────────→ y
```

Put:

$$
x=3
$$

inside:

```text
3 → ×2 → 6 → +1 → 7
```

Therefore:

$$
y=7
$$

A mathematical **function** is basically this idea formalized.

---

# 11. Function — the next important concept

A function describes a relationship:

$$
y=f(x)
$$

Read this as:

> "y is a function of x."

Meaning:

> The value of \(y\) depends on \(x\).

For example:

$$
f(x)=2x+1
$$

Then:

$$
f(3)=2(3)+1=7
$$

and:

$$
f(10)=2(10)+1=21
$$

---

# 12. Functions are everywhere in ML

Consider:

$$
y=f(x)
$$

This is the basic structure:

```text
INPUT
  ↓
Function
  ↓
OUTPUT
```

Machine learning does essentially this:

```text
Features
   ↓
ML model
   ↓
Prediction
```

Mathematically:

$$
\hat{y}=f(X)
$$

where:

- \(X\) = input features
- \(f\) = learned model
- \(\hat{y}\) = predicted output

For example:

```text
Experience
   ↓
   ML Model
   ↓
Predicted Salary
```

---

# 13. One input vs multiple inputs

Now things become more interesting.

Suppose salary depends only on experience:

$$
y=f(x)
$$

But in reality salary might depend on:

- experience
- education
- skills
- location
- industry

Now we have multiple variables:

$$
x_1=\text{experience}
$$

$$
x_2=\text{education}
$$

$$
x_3=\text{skills}
$$

and so on.

Our model becomes:

$$
y=f(x_1,x_2,x_3)
$$

This is where we eventually arrive at **vectors and matrices**.

---

# 14. A concrete ML example

Suppose:

$$
x_1=\text{study hours}
$$

$$
x_2=\text{sleep hours}
$$

$$
x_3=\text{attendance}
$$

A very simple model might look like:

$$
y=5x_1+2x_2+0.3x_3
$$

Suppose a student has:

$$
x_1=4
$$

$$
x_2=7
$$

$$
x_3=90
$$

Then:

$$
y=5(4)+2(7)+0.3(90)
$$

$$
y=20+14+27
$$

$$
y=61
$$

This is obviously a **toy model**, not a real exam predictor.

But conceptually, you just performed the type of mathematical computation that ML models perform.

---

# 15. A subtle but extremely important ML idea

Look at:

$$
5x_1+2x_2+0.3x_3
$$

The numbers:

$$
5,\ 2,\ 0.3
$$

are multiplying the features.

In ML, these are related to what we call **weights/parameters**.

So we can write:

$$
y=w_1x_1+w_2x_2+w_3x_3
$$

where:

$$
w_1,w_2,w_3
$$

are weights.

Later, you'll learn how ML algorithms **learn these weights from data**.

Don't worry about that yet.

Just remember:

> **Variables represent information; weights determine how strongly that information contributes to a calculation.**

---

# 16. Where statistics enters

Now let's return to our student data:

$$
2,4,3,5,1
$$

Suppose we want to know:

> "What is the typical study time?"

We need a statistical concept.

We calculate:

$$
\frac{2+4+3+5+1}{5}
$$

This is the **mean**.

$$
\boxed{\text{mean}=3}
$$

Notice what happened.

We used:

- variables
- addition
- division
- observations

to create a **statistical summary**.

This is the direction we're heading:

```text
Mathematics
     ↓
Arithmetic
     ↓
Statistics
     ↓
NumPy
     ↓
Machine Learning
```

---

# 17. Your first important mental map 🧠

Memorize this:

```text
                    DATA
                      │
                      ↓
              Individual values
                      │
                      ↓
                  VARIABLES
                      │
                      ↓
              Mathematical operations
                      │
          ┌───────────┴───────────┐
          ↓                       ↓
      Statistics               Functions
          │                       │
          ↓                       ↓
   Understand data          Model relationships
          │                       │
          └───────────┬───────────┘
                      ↓
                MACHINE LEARNING
```

And later:

```text
Mathematics
     ↓
NumPy
     ↓
Efficient computation
     ↓
ML
```

---

# 🧪 Mini Exercise — Don't skip this

Try these without looking at the answers.

### Q1

If:

$$
x=7
$$

what is:

$$
2x+3
$$

---

### Q2

If:

$$
x_1=4,\quad x_2=8,\quad x_3=6
$$

what is:

$$
x_1+x_2+x_3
$$

---

### Q3

Suppose:

$$
y=3x+2
$$

What is \(y\) when:

$$
x=5
$$

---

### Q4 — ML thinking

Suppose:

$$
x_1=\text{study hours}
$$

$$
x_2=\text{sleep hours}
$$

and:

$$
y=4x_1+2x_2
$$

A student studies 5 hours and sleeps 7 hours.

Calculate \(y\).

---

### Q5 — Conceptual

In:

$$
y=7x+10
$$

identify:

- \(x\)
- \(y\)
- \(7\)
- \(10\)

---

## One thing to remember before we stop

Don't think of mathematics as a collection of scary symbols.

Think:

> **Mathematics is a language for describing relationships between quantities.**

And ML is largely:

> **Using mathematics to discover useful relationships in data.**

We have now established:

**data → variables → values → arithmetic → expressions → functions → simple ML relationships.**

### 🛑 We stop here.

**Do not move to vectors yet.**

First make sure these concepts are comfortable. When you say **"next"**, we'll build **Foundation 3: Fractions, Ratios, Percentages & Proportions** — extremely important because they appear later in normalization, probability, feature engineering, evaluation metrics, and many ML calculations.
