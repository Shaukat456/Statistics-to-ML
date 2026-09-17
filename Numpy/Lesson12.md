# Lesson 12 — Random Variables

Today we learn a concept that looks confusing at first:

$$
\boxed{\text{Random Variable}}
$$

But once you understand the idea, a lot of **statistics, probability, and machine learning** becomes much easier.

The key question is:

> **What exactly is a random variable, and how is it different from an ordinary variable?**

---

# 1. First: What Is a Normal Variable?

From our earlier lessons, we learned that a variable is a quantity that can have a value.

For example:

$$
x=\text{study hours}
$$

A student might have:

$$
x=5
$$

Another student:

$$
x=8
$$

Another:

$$
x=3
$$

So \(x\) represents a quantity whose value can change.

---

# 2. So What Is a Random Variable?

A **random variable** is a variable whose value is determined by the outcome of a random process.

That sounds complicated.

Let's make it simple.

Imagine tossing a coin.

The experiment produces:

$$
H \quad \text{or} \quad T
$$

Now we create a variable \(X\):

$$
X=
\begin{cases}
1 & \text{if Heads}\\
0 & \text{if Tails}
\end{cases}
$$

Now \(X\) is a **random variable**.

Why?

Because before tossing the coin, we don't know whether:

$$
X=0
$$

or:

$$
X=1
$$

The outcome of the random experiment determines its value.

---

# 3. The Most Important Mental Model

Think of a random variable as a **translator**.

It takes:

$$
\boxed{\text{Random outcome}}
$$

and converts it into:

$$
\boxed{\text{Numerical value}}
$$

For example:

```text
Coin experiment
      ↓
   Heads ─────→ X = 1
      │
   Tails ─────→ X = 0
```

So:

> **A random variable assigns a numerical value to an outcome of a random experiment.**

This is the definition you should remember.

---

# 4. Why Do We Need Random Variables?

You might ask:

> "Why not just say Heads or Tails?"

Because mathematics works extremely well with numbers.

Once we convert:

$$
H\rightarrow1
$$

$$
T\rightarrow0
$$

we can calculate things like:

- average
- variance
- probability
- expectation
- distributions

This gives us a bridge:

$$
\boxed{\text{Randomness}\rightarrow\text{Numbers}\rightarrow\text{Mathematics}}
$$

And that bridge is incredibly important in ML.

---

# 5. Example: Dice

Roll a die.

Possible outcomes:

$$
\{1,2,3,4,5,6\}
$$

We could define a random variable:

$$
X=\text{number appearing on the die}
$$

Then:

$$
X\in\{1,2,3,4,5,6\}
$$

Before rolling:

$$
X=?
$$

After rolling, perhaps:

$$
X=4
$$

The experiment determines the value.

Therefore \(X\) is a random variable.

---

# 6. Random Variable Does NOT Mean "The Number Is Random"

This is a subtle but important point.

A random variable isn't necessarily some mysterious number changing randomly.

Rather:

> **The value is uncertain before the random experiment is observed.**

For example, when rolling a die, the die will produce some definite result.

But **before observing it**, we don't know which result it will be.

That's the uncertainty probability mathematics describes.

---

# 7. Two Major Types of Random Variables

There are two major categories:

$$
\boxed{\text{Discrete}}
$$

and

$$
\boxed{\text{Continuous}}
$$

This distinction is extremely important.

---

# 8. Discrete Random Variable

A discrete random variable takes **countable, separate values**.

Examples:

- number of heads
- number of students
- number of cars
- number of defects
- number shown on a die
- number of emails
- number of photons detected

For a die:

$$
X\in\{1,2,3,4,5,6\}
$$

There are only six possible values.

---

# 9. Think "Counting"

A great mental shortcut:

> **Discrete → usually counting.**

For example:

### Number of students

$$
0,1,2,3,\ldots
$$

### Number of defective components

$$
0,1,2,3,\ldots
$$

### Number of heads in 10 coin tosses

$$
0,1,2,\ldots,10
$$

You cannot have:

$$
2.37\text{ students}
$$

So number of students is discrete.

---

# 10. Continuous Random Variable

A continuous random variable can take values over a continuous range.

Examples:

- height
- weight
- temperature
- time
- distance
- velocity
- position
- voltage
- energy

Suppose:

$$
X=\text{height of a person}
$$

Someone might have:

$$
X=170\text{ cm}
$$

Another:

$$
X=170.2\text{ cm}
$$

Another:

$$
X=170.237\text{ cm}
$$

In mathematical modeling, there can be infinitely many possible values within a range.

---

# 11. Counting vs Measuring

A very useful mental model:

```text
                RANDOM VARIABLE
                       │
              ┌────────┴────────┐
              │                 │
          DISCRETE          CONTINUOUS
              │                 │
           COUNTING          MEASURING
              │                 │
         # of students       height
         # of cars           weight
         # of defects        temperature
         die result           time
```

Remember:

$$
\boxed{\text{Discrete = count}}
$$

$$
\boxed{\text{Continuous = measure}}
$$

There are edge cases in real-world data, but this distinction is an excellent foundation.

---

# 12. Example: Coin Tosses

Suppose we toss a coin 3 times.

Let:

$$
X=\text{number of Heads}
$$

What values can \(X\) take?

Possibilities:

### TTT

$$
X=0
$$

### HTT

$$
X=1
$$

### HHT

$$
X=2
$$

### HHH

$$
X=3
$$

Therefore:

$$
\boxed{X\in\{0,1,2,3\}}
$$

This is discrete.

---

# 13. Random Variable vs Outcome

This distinction is worth making very clear.

Suppose we toss a coin.

### Outcome

$$
H
$$

is an outcome.

### Random variable

$$
X
$$

is the mathematical variable we define to represent the outcome numerically.

For example:

$$
X(H)=1
$$

$$
X(T)=0
$$

So:

> **Outcome = what happened.**

> **Random variable = numerical representation of the outcome.**

---

# 14. Random Variable vs Ordinary Variable

This is another common confusion.

### Ordinary variable

Could be:

$$
x=\text{age}
$$

We may simply be storing an observed value.

### Random variable

Could be:

$$
X=\text{age of a randomly selected person}
$$

Before selecting the person, we don't know what age we'll observe.

Therefore:

$$
X=?
$$

After selecting someone:

$$
X=23
$$

The randomness comes from the **selection/experiment**.

---

# 15. Probability Attached to a Random Variable

Now something very important happens.

Suppose:

$$
X=\text{die result}
$$

Then:

$$
P(X=1)=\frac16
$$

$$
P(X=2)=\frac16
$$

$$
P(X=3)=\frac16
$$

and so on.

We're no longer just talking about outcomes.

We're describing the **probabilities associated with the possible values of \(X\)**.

---

# 16. Probability Mass Function — First Introduction

For a discrete random variable, we can define:

$$
\boxed{P(X=x)}
$$

This means:

> Probability that random variable \(X\) takes the value \(x\).

For a fair die:

$$
P(X=4)=\frac16
$$

For a biased die, perhaps:

$$
P(X=4)=0.25
$$

The probabilities can be different.

---

# 17. Probabilities Must Add to 1

For a discrete random variable:

$$
\boxed{
\sum_x P(X=x)=1
}
$$

Look at the connection with our previous lesson on Sigma!

For a fair die:

$$
P(X=1)+P(X=2)+\cdots+P(X=6)=1
$$

Therefore:

$$
\boxed{
\sum_{x=1}^{6}P(X=x)=1
}
$$

Why?

Because the die **must** produce one of those six outcomes.

---

# 18. A Probability Table

For a fair die:

| \(X\) | \(P(X=x)\) |
| ----: | ---------: |
|     1 |    \(1/6\) |
|     2 |    \(1/6\) |
|     3 |    \(1/6\) |
|     4 |    \(1/6\) |
|     5 |    \(1/6\) |
|     6 |    \(1/6\) |

Add them:

$$
\frac16+\frac16+\frac16+\frac16+\frac16+\frac16
$$

$$
=\frac66
$$

$$
=1
$$

---

# 19. A Machine Learning Example

Suppose an ML model classifies an image.

Let:

$$
X=\text{class of image}
$$

Possible values:

$$
\{\text{cat},\text{dog},\text{horse}\}
$$

The model might assign:

$$
P(X=\text{cat})=0.70
$$

$$
P(X=\text{dog})=0.20
$$

$$
P(X=\text{horse})=0.10
$$

Notice:

$$
0.70+0.20+0.10=1
$$

The model is essentially describing a probability distribution over possible values of \(X\).

---

# 20. Why This Matters in Classification

Traditional programming might say:

```text
Image → CAT
```

Probabilistic ML can say:

```text
Image
  ↓
Cat:   0.70
Dog:   0.20
Horse: 0.10
```

This gives us information about **uncertainty**.

For example, compare:

### Model A

$$
[0.99,\ 0.01,\ 0.00]
$$

with:

### Model B

$$
[0.40,\ 0.35,\ 0.25]
$$

Both might predict "Cat" as the largest class probability, but the second output represents much greater uncertainty.

---

# 21. Continuous Random Variables

Now let's consider temperature.

Let:

$$
X=\text{temperature at noon}
$$

Perhaps:

$$
X=30.2^\circ C
$$

Tomorrow:

$$
X=28.7^\circ C
$$

Another day:

$$
X=31.123^\circ C
$$

Here \(X\) can take values across a continuous range.

For continuous random variables, we generally don't assign probability in the same way as a discrete variable.

This is a very important point.

For a continuous variable:

$$
P(X=30)=0
$$

in the ideal mathematical continuous model.

That does **not** mean 30°C is impossible.

It means that probability is assigned to **ranges/intervals**, such as:

$$
P(29<X<31)
$$

rather than to an exact infinitely precise point.

We'll study this carefully when we reach probability distributions.

---

# 22. Why Is \(P(X=30)=0\)?

This initially sounds strange.

Imagine all real numbers between:

$$
29\text{ and }31
$$

There are infinitely many.

For example:

$$
29.1
$$

$$
29.01
$$

$$
29.001
$$

$$
29.0001
$$

and so on.

A single exact point has no width.

Probability for a continuous variable comes from **area over an interval**, not from the height of the distribution at one exact point.

We'll build this from scratch later, so don't worry if this feels unfamiliar right now.

---

# 23. Random Variables in Scientific Measurements

This is particularly relevant to you as a physics student.

Suppose you're measuring:

$$
X=\text{position of a particle}
$$

Every measurement can differ because of:

- experimental uncertainty
- measurement noise
- environmental effects
- quantum effects
- imperfect instruments

We can model \(X\) as a random variable.

Then instead of simply saying:

$$
X=2.31\text{ m}
$$

we can describe the possible values and their probabilities.

This is one of the fundamental ideas behind statistical physics and quantum measurement.

---

# 24. Random Variables in Quantum Mechanics

This connection is especially important for your future quantum work.

Suppose a measurement observable has possible outcomes:

$$
x_1,x_2,x_3,\ldots
$$

The measurement result is uncertain before measurement.

We can mathematically model the result using a random variable:

$$
X
$$

with probabilities:

$$
P(X=x_i)
$$

In quantum mechanics, these probabilities are determined from the quantum state and measurement operator.

For example, if a qubit is:

$$
|\psi\rangle
=
\alpha|0\rangle+\beta|1\rangle
$$

then measurement in the computational basis gives:

$$
P(X=0)=|\alpha|^2
$$

and:

$$
P(X=1)=|\beta|^2
$$

with:

$$
|\alpha|^2+|\beta|^2=1.
$$

So there is a beautiful connection:

$$
\boxed{
\text{Quantum state}
\rightarrow
\text{Measurement}
\rightarrow
\text{Random outcome}
\rightarrow
\text{Probability}
}
$$

---

# 25. Random Variable → Dataset

Now let's connect everything to ML data.

Suppose we're studying student exam scores.

We define:

$$
X=\text{exam score of a randomly selected student}
$$

Before selecting a student:

$$
X=?
$$

After selecting one:

$$
X=78
$$

Select another:

$$
X=65
$$

Another:

$$
X=91
$$

So a dataset could give us observations:

$$
78,\ 65,\ 91,\ 72,\ 84,\ldots
$$

These are **realized/observed values** of the underlying random variable.

This is a very important statistical idea.

---

# 26. Random Variable vs Observed Data

Think of it like this:

```text
             RANDOM VARIABLE
                    X
                    │
          "What value might occur?"
                    │
          ┌─────────┼─────────┐
          ↓         ↓         ↓
         78        65        91
          │         │         │
       Observation Observation Observation
```

The random variable is the **underlying uncertain quantity**.

The observations are the **actual values we collected**.

---

# 27. This Is Where Statistics Starts Becoming Powerful

Suppose:

$$
X=\text{height of a randomly selected person}
$$

We collect:

$$
170,\ 175,\ 168,\ 182,\ 171,\ldots
$$

Now we can use these observations to estimate things about \(X\):

- mean
- variance
- distribution
- probability
- correlations
- uncertainty

This is essentially the foundation of statistical learning.

---

# 28. Random Variables and Features

Suppose our dataset has:

| Study Hours | Sleep | Score |
| ----------: | ----: | ----: |
|           2 |     7 |    65 |
|           4 |     6 |    78 |
|           3 |     8 |    72 |
|           5 |     6 |    88 |

We can conceptually think of:

$$
X_1=\text{study hours}
$$

$$
X_2=\text{sleep hours}
$$

$$
Y=\text{exam score}
$$

These can be treated as random variables in a statistical model.

An individual observation might be:

$$
(X_1,X_2,Y)=(4,6,78)
$$

Now we're moving toward the language used in statistical ML.

---

# 29. One Extremely Important Idea

In ML, we often write:

$$
X
$$

for an input variable and:

$$
Y
$$

for the target/output variable.

Then we may say:

$$
Y=f(X)+\epsilon
$$

where:

- \(f(X)\) = underlying relationship
- \(\epsilon\) = noise/random variation

This is one of the fundamental ideas behind regression.

For example:

$$
\text{Score}
=
f(\text{Study Hours})
+
\text{Noise}
$$

Two students who study exactly 5 hours might still receive different scores.

Why?

Because reality contains other factors.

That's where probability and statistics enter ML.

---

# 30. A Powerful Mental Model

Imagine a **mystery machine**.

You don't see the future outcome.

You put the experiment into the world:

```text
Random process
      ↓
   UNKNOWN
      ↓
   Random Variable X
      ↓
   Actual observation
      ↓
     Number
```

Probability tells you:

> **What values can happen and how likely are they?**

Statistics tells you:

> **Given observations, what can we learn about the underlying process?**

Machine Learning then uses these ideas to:

> **Learn patterns and make predictions from data.**

---

# 31. Summary Table

| Concept           | Meaning                                             |
| ----------------- | --------------------------------------------------- |
| Random experiment | Process with uncertain outcome                      |
| Outcome           | Actual result                                       |
| Random variable   | Numerical variable representing the outcome         |
| Discrete RV       | Countable possible values                           |
| Continuous RV     | Values across a continuous range                    |
| \(P(X=x)\)        | Probability that \(X\) equals \(x\)                 |
| Distribution      | How probability is allocated across possible values |
| Observation       | Actual value obtained from an experiment            |

---

# 🧠 Mental Map

```text
                 RANDOM EXPERIMENT
                        │
                        ↓
                    OUTCOME
                        │
                        ↓
                RANDOM VARIABLE X
                        │
             ┌──────────┴──────────┐
             │                     │
         DISCRETE              CONTINUOUS
             │                     │
          COUNTING               MEASURING
             │                     │
       die, students          height, time
       defects, heads         temperature
             │                     │
             └──────────┬──────────┘
                        ↓
                 PROBABILITY
                        ↓
                  DISTRIBUTION
                        ↓
                  STATISTICS
                        ↓
                MACHINE LEARNING
```

---

# 🎯 What You Should Know Before Moving On

Make sure these five statements feel natural:

### 1.

$$
\boxed{\text{Random variable = numerical representation of an uncertain outcome}}
$$

### 2.

$$
\boxed{\text{Discrete = count}}
$$

### 3.

$$
\boxed{\text{Continuous = measure}}
$$

### 4.

$$
\boxed{P(X=x)=\text{probability that }X\text{ takes value }x}
$$

### 5.

$$
\boxed{\sum_xP(X=x)=1}
$$

for a discrete random variable.

---

# 📝 Practice

### Q1

You toss a coin and define:

$$
X=
\begin{cases}
1 & H\\
0 & T
\end{cases}
$$

Is \(X\) a random variable? Why?

### Q2

Is the number of cars passing a road in one hour discrete or continuous?

### Q3

Is the temperature of a room discrete or continuous?

### Q4

A die is rolled and:

$$
X=\text{number shown}
$$

What are the possible values of \(X\)?

### Q5

If a fair die is rolled, what is:

$$
P(X=3)
$$

### Q6

A classifier gives:

$$
P(\text{Cat})=0.6
$$

$$
P(\text{Dog})=0.3
$$

$$
P(\text{Horse})=0.1
$$

Why do these probabilities add up to 1?

### Q7

Explain the difference between:

> **random variable**

and

> **observation**

in your own words.

---

## Next lesson: Probability Distributions

Now that we know what a random variable is, the natural next question is:

> **If a random variable can take many possible values, how do we describe the probability of all those values at once?**

That leads us to:

$$
\boxed{\text{Probability Distributions}}
$$

We'll build **PMF, PDF, CDF, discrete vs continuous distributions, Bernoulli, Binomial, Normal/Gaussian distribution**, and connect them to ML and scientific measurements.
