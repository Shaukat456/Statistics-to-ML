# Lesson 6 — Functions: The Heart of Machine Learning

We have reached a **major milestone**.

So far we've learned:

$$
\text{Numbers}
\rightarrow
\text{Variables}
\rightarrow
\text{Arithmetic}
\rightarrow
\text{Fractions}
\rightarrow
\text{Powers/Logs}
\rightarrow
\text{Algebra}
$$

Now we learn **functions**.

And I want you to remember this sentence:

> 🧠 **A function is a machine that takes an input and produces an output according to a rule.**

That single idea will eventually help you understand:

- Linear Regression
- Logistic Regression
- Neural Networks
- Activation Functions
- Loss Functions
- Probability Models
- Optimization
- NumPy vectorization

---

# 1. Imagine a Machine

Imagine putting something into a mysterious machine.

```text
        INPUT
          ↓
     ┌─────────┐
     │ MACHINE │
     └─────────┘
          ↓
        OUTPUT
```

You put in:

$$
3
$$

The machine follows a rule:

> Multiply by 2 and add 1.

So:

$$
3\rightarrow 7
$$

Mathematically, we can describe the machine as:

$$
f(x)=2x+1
$$

That's a **function**.

---

# 2. What Does \(f(x)\) Mean?

This notation initially looks scary:

$$
f(x)
$$

But it is actually simple.

Read it as:

> **"The output of function \(f\) when the input is \(x\)."**

For example:

$$
f(x)=2x+1
$$

If we put:

$$
x=3
$$

then:

$$
f(3)=2(3)+1
$$

$$
f(3)=7
$$

So:

$$
\boxed{f(3)=7}
$$

---

# 3. Function = Input → Rule → Output

Always think:

$$
\boxed{\text{Input}\rightarrow\text{Function}\rightarrow\text{Output}}
$$

Example:

$$
3\rightarrow [2x+1]\rightarrow7
$$

Another:

$$
10\rightarrow [2x+1]\rightarrow21
$$

Another:

$$
100\rightarrow [2x+1]\rightarrow201
$$

The rule stays the same.

Only the input changes.

---

# 4. A Real-World Example

Imagine a taxi charges:

- $5 starting fee
- $2 per kilometer

If you travel \(x\) kilometers:

$$
\text{cost}=2x+5
$$

We can define:

$$
C(x)=2x+5
$$

This is a function.

If you travel 3 km:

$$
C(3)=2(3)+5
$$

$$
=11
$$

So the journey costs $11.

If you travel 10 km:

$$
C(10)=2(10)+5
$$

$$
=25
$$

Same function.

Different input.

---

# 5. Why This Matters for ML

Machine Learning is fundamentally about discovering useful relationships between inputs and outputs.

Suppose:

```text
Study Hours → Exam Score
```

We might have data:

| Study Hours | Score |
| ----------: | ----: |
|           1 |    52 |
|           2 |    58 |
|           3 |    65 |
|           4 |    72 |
|           5 |    80 |

We want a function:

$$
f(x)
$$

that approximately describes this relationship.

Then:

$$
\text{Study Hours}\rightarrow f(x)\rightarrow\text{Predicted Score}
$$

This is the essence of supervised learning.

---

# 6. The Model Is a Function

Suppose our model learns:

$$
f(x)=5x+50
$$

If a student studies 4 hours:

$$
f(4)=5(4)+50
$$

$$
=70
$$

The model predicts:

$$
\boxed{70}
$$

In ML notation, we often write:

$$
\hat y=f(x)
$$

where:

- \(x\) = input
- \(f\) = model/function
- \(\hat y\) = predicted output

---

# 7. Why the Hat?

You will see:

$$
\hat y
$$

The little hat means:

> **prediction**

Compare:

$$
y
$$

with:

$$
\hat y
$$

### \(y\)

Actual value.

### \(\hat y\)

Predicted value.

For example:

Actual:

$$
y=75
$$

Model prediction:

$$
\hat y=70
$$

Then the model made an error.

We'll eventually use:

$$
y-\hat y
$$

to calculate the error.

---

# 8. One Input vs Multiple Inputs

So far:

$$
y=f(x)
$$

One feature.

But real ML problems have many features.

Suppose we're predicting house prices.

Features:

$$
x_1=\text{house size}
$$

$$
x_2=\text{number of bedrooms}
$$

$$
x_3=\text{age}
$$

Then:

$$
\hat y=f(x_1,x_2,x_3)
$$

The function takes **multiple inputs**.

---

# 9. Example

Suppose:

$$
\hat y=100x_1+20x_2-5x_3+50
$$

Imagine:

$$
x_1=10
$$

$$
x_2=3
$$

$$
x_3=5
$$

Then:

$$
\hat y
=
100(10)+20(3)-5(5)+50
$$

$$
=1000+60-25+50
$$

$$
\boxed{\hat y=1085}
$$

This is a function of three variables.

---

# 10. Function vs Formula

These are closely related but not exactly the same idea.

A **formula** tells you how to calculate something.

A **function** describes a mapping:

$$
\text{input}\rightarrow\text{output}
$$

For ML, the mapping perspective is particularly useful.

Think:

> **A model is a machine that maps data to predictions.**

---

# 11. Domain

Now we introduce an important concept.

Suppose:

$$
f(x)=x^2
$$

Can we put any real number into it?

Yes.

For example:

$$
f(2)=4
$$

$$
f(-2)=4
$$

$$
f(10)=100
$$

So its possible inputs are essentially all real numbers.

The set of allowed inputs is called the:

$$
\boxed{\text{Domain}}
$$

### Mental model

> **Domain = what you're allowed to put into the function.**

---

# 12. Range

Now ask:

> What outputs can the function produce?

For:

$$
f(x)=x^2
$$

we can get:

$$
0,1,4,9,16,\ldots
$$

But we can't get:

$$
-1
$$

because squaring a real number cannot produce a negative result.

The set of possible outputs is called the:

$$
\boxed{\text{Range}}
$$

### Mental model

> **Domain = possible inputs**

> **Range = possible outputs**

---

# 13. Example: Square Root

Consider:

$$
f(x)=\sqrt{x}
$$

Can we put:

$$
x=9
$$

Yes:

$$
f(9)=3
$$

Can we put:

$$
x=4
$$

Yes:

$$
f(4)=2
$$

But:

$$
f(-4)=\sqrt{-4}
$$

is not a real number.

Therefore the real-number domain is:

$$
x\geq0
$$

This shows why understanding mathematics matters before blindly using functions.

---

# 14. Function Composition

Here's a powerful idea.

Suppose we have two functions.

First:

$$
f(x)=2x
$$

Second:

$$
g(x)=x+3
$$

We can feed the output of one function into another.

```text
x
↓
f
↓
g
↓
output
```

Suppose:

$$
x=5
$$

First:

$$
f(5)=10
$$

Then feed 10 into \(g\):

$$
g(10)=13
$$

So:

$$
g(f(5))=13
$$

This is called **function composition**.

---

# 15. Why Function Composition Is HUGE in Neural Networks

This is one of the most important connections we'll eventually make.

A neural network can essentially be viewed as:

$$
f_3(f_2(f_1(x)))
$$

In other words:

```text
Input
  ↓
Function 1
  ↓
Function 2
  ↓
Function 3
  ↓
Prediction
```

That's why neural networks can learn extremely complicated relationships.

They're composing many mathematical transformations.

Later we'll see:

$$
\boxed{
f(x)=f_3(f_2(f_1(x)))
}
$$

and this will no longer seem mysterious.

---

# 16. Linear Functions

One of the most important functions in ML is:

$$
f(x)=mx+b
$$

This is a **linear function** in the common ML sense.

Here:

- \(m\) = slope
- \(b\) = intercept

For example:

$$
f(x)=3x+2
$$

Here:

$$
m=3
$$

and:

$$
b=2
$$

---

# 17. What Does Slope Mean?

Consider:

$$
y=3x+2
$$

Every time \(x\) increases by 1:

$$
y
$$

increases by 3.

For example:

|   x |   y |
| --: | --: |
|   0 |   2 |
|   1 |   5 |
|   2 |   8 |
|   3 |  11 |

So the slope tells us:

> **How much does the output change when the input changes?**

This idea will become extremely important when we eventually study:

- gradients
- optimization
- gradient descent
- model coefficients

---

# 18. Intercept

In:

$$
y=3x+2
$$

the intercept is:

$$
2
$$

Why?

Set:

$$
x=0
$$

Then:

$$
y=3(0)+2
$$

$$
y=2
$$

So the intercept is the output when the input is zero.

---

# 19. Nonlinear Functions

Not every relationship is a straight line.

Consider:

$$
f(x)=x^2
$$

Values:

|   x | \(x^2\) |
| --: | ------: |
|  -3 |       9 |
|  -2 |       4 |
|  -1 |       1 |
|   0 |       0 |
|   1 |       1 |
|   2 |       4 |
|   3 |       9 |

The relationship curves.

This is a **nonlinear function**.

Machine Learning often needs nonlinear functions because real-world relationships are rarely perfectly linear.

---

# 20. Why Nonlinearity Matters

Imagine trying to recognize a cat from an image.

The relationship between:

- pixel values
- edges
- shapes
- textures
- ears
- eyes

and:

$$
\text{"cat"}
$$

is enormously complicated.

A simple:

$$
y=mx+b
$$

is not enough to represent many such relationships.

Neural networks introduce **nonlinear activation functions** to create much richer mappings.

---

# 21. Three Functions You'll Eventually Meet

Don't study them deeply yet; just recognize them.

### Linear

$$
f(x)=mx+b
$$

### Sigmoid

$$
\sigma(x)=\frac{1}{1+e^{-x}}
$$

### ReLU

$$
f(x)=\max(0,x)
$$

These functions behave very differently.

Later you'll understand **why** each is useful.

---

# 22. Functions in Statistics

Functions aren't only for ML.

Suppose we calculate the average of some data.

We could think of:

$$
\text{Mean}(x_1,x_2,\ldots,x_n)
$$

as a function.

It takes data as input and returns a number.

For example:

$$
f(2,4,6)=4
$$

Similarly:

$$
\text{variance}(\text{data})
$$

is a function.

So statistics is filled with functions too.

---

# 23. Functions in Physics

You already know many functions from physics.

For example:

Position:

$$
x(t)
$$

This means:

> position as a function of time.

Velocity:

$$
v(t)
$$

Acceleration:

$$
a(t)
$$

Wave function:

$$
\psi(x,t)
$$

Temperature:

$$
T(x,t)
$$

So functions are not an "ML thing."

They are a fundamental language for describing how one quantity depends on another.

---

# 24. A Beautiful Connection

Compare these:

### Physics

$$
x(t)
$$

means:

$$
\text{time}\rightarrow\text{position}
$$

### ML

$$
\hat y=f(X)
$$

means:

$$
\text{features}\rightarrow\text{prediction}
$$

The mathematical idea is the same:

> **Inputs determine outputs through a relationship.**

ML simply tries to **learn that relationship from data**.

---

# 25. What Does "Learning a Function" Mean?

This is a very important question.

Suppose the real world has some unknown relationship:

$$
y=f(x)
$$

But we don't know \(f\).

We collect data:

$$
(x_1,y_1),(x_2,y_2),\ldots
$$

Machine Learning tries to find an approximation:

$$
\hat f(x)
$$

such that:

$$
\hat f(x)\approx f(x)
$$

Then for a new input:

$$
x_{\text{new}}
$$

we can predict:

$$
\hat y=\hat f(x_{\text{new}})
$$

### This is supervised learning at its core.

---

# 26. The Complete ML Picture

Now look at this:

```text
                 TRAINING DATA
                       ↓
             ┌──────────────────┐
             │ Machine Learning │
             │    Algorithm     │
             └──────────────────┘
                       ↓
              Learned Function
                    f(X)
                       ↓
              New Input X
                       ↓
                Prediction ŷ
```

The algorithm's job is essentially to find a useful function.

---

# 27. One More Important Concept: Parameters

Consider:

$$
f(x)=mx+b
$$

The function has two parameters:

$$
m
$$

and:

$$
b
$$

Change \(m\), and the function changes.

Change \(b\), and the function changes.

In ML, models often contain parameters that are learned from data.

For linear regression:

$$
\hat y=w_1x_1+w_2x_2+\cdots+w_nx_n+b
$$

The:

$$
w_1,w_2,\ldots,w_n,b
$$

are parameters.

The learning algorithm tries to find good values for them.

---

# 28. The Big Mental Model

You can now think about ML like this:

```text
                 DATA
                  ↓
        ┌─────────────────┐
        │ Find parameters │
        └─────────────────┘
                  ↓
        ┌─────────────────┐
        │ Learned function│
        └─────────────────┘
                  ↓
               NEW DATA
                  ↓
             PREDICTION
```

Or mathematically:

$$
\boxed{
X
\overset{\text{model}}{\longrightarrow}
\hat y
}
$$

---

# 29. Practice

Try these yourself.

### Q1

If:

$$
f(x)=2x+3
$$

calculate:

$$
f(5)
$$

---

### Q2

If:

$$
f(x)=x^2
$$

calculate:

$$
f(-4)
$$

---

### Q3

If:

$$
f(x)=3x-2
$$

calculate:

$$
f(10)
$$

---

### Q4

For:

$$
f(x)=5x+7
$$

identify:

- slope
- intercept

---

### Q5

Given:

$$
f(x)=2x
$$

and:

$$
g(x)=x+5
$$

calculate:

$$
g(f(3))
$$

---

### Q6

Given:

$$
\hat y=4x+10
$$

and:

$$
x=5
$$

calculate the prediction.

---

### Q7 — ML thinking

Suppose:

$$
\hat y=2x_1+3x_2+5
$$

where:

$$
x_1=4,\qquad x_2=2
$$

Calculate:

$$
\hat y
$$

---

### Q8 — Conceptual

In:

$$
\hat y=f(X)
$$

what does:

- \(X\) represent?
- \(f\) represent?
- \(\hat y\) represent?

---

# Answers

### Q1

$$
f(5)=2(5)+3=13
$$

### Q2

$$
f(-4)=(-4)^2=16
$$

### Q3

$$
f(10)=30-2=28
$$

### Q4

$$
m=5
$$

$$
b=7
$$

### Q5

First:

$$
f(3)=6
$$

Then:

$$
g(6)=11
$$

Therefore:

$$
\boxed{11}
$$

### Q6

$$
\hat y=4(5)+10=30
$$

### Q7

$$
\hat y=2(4)+3(2)+5
$$

$$
=8+6+5
$$

$$
\boxed{19}
$$

### Q8

$$
X=\text{input/features}
$$

$$
f=\text{model/function}
$$

$$
\hat y=\text{prediction}
$$

---

# 🧠 Never-Forget Summary

If you remember **one picture**, remember this:

```text
              FUNCTION
          ┌──────────────┐
INPUT ───→│     RULE     │───→ OUTPUT
          └──────────────┘
```

Mathematically:

$$
\boxed{x\rightarrow f(x)\rightarrow y}
$$

In ML:

$$
\boxed{X\rightarrow f(X)\rightarrow\hat y}
$$

And in a neural network:

$$
\boxed{x\rightarrow f_1(x)\rightarrow f_2(\cdots)\rightarrow f_3(\cdots)\rightarrow\hat y}
$$

So when you eventually see a giant neural-network equation, remember:

> **It's still just functions taking inputs and producing outputs—only composed together and with many parameters.**

---

## Where We Are

We've now completed:

$$
\boxed{
\text{Numbers}
\rightarrow
\text{Arithmetic}
\rightarrow
\text{Fractions}
\rightarrow
\text{Powers/Logs}
\rightarrow
\text{Algebra}
\rightarrow
\text{Functions}
}
$$

### Next: **Coordinates & Graphs**

We'll learn:

- number lines
- Cartesian coordinates
- \(x\)-axis and \(y\)-axis
- points
- plotting
- slope visually
- lines
- graphs of functions
- how ML data is visualized
- how a dataset becomes a graph

Then we'll move toward **vectors and matrices**, which will finally bring us much closer to NumPy and the mathematical structure of ML.
