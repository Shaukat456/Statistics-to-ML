# Lesson 14 — Bernoulli Distribution

We have just learned **probability distributions**. Now we will build the simplest possible probability distribution: the **Bernoulli distribution**.

The key idea is:

> **Bernoulli = one trial + exactly two possible outcomes.**

---

# 1. Start With a Simple Question

Imagine you toss a coin **once**.

What can happen?

- Heads
- Tails

Only **two possible outcomes**.

Or imagine:

**Will a customer click an advertisement?**

- Yes
- No

Again, exactly two outcomes.

Or:

**Does an image contain a car?**

- Yes
- No

Again, two outcomes.

This type of experiment is called a **Bernoulli trial**.

---

# 2. What Is a Bernoulli Trial?

A **Bernoulli trial** is a random experiment with exactly **two possible outcomes**.

Usually we call them:

- **Success**
- **Failure**

Don't get confused by the word "success."

Success simply means:

> **The outcome we decided to call 1.**

For example:

| Experiment     | Success (1) | Failure (0)  |
| -------------- | ----------- | ------------ |
| Coin           | Heads       | Tails        |
| Spam detection | Spam        | Not spam     |
| Medical test   | Positive    | Negative     |
| Machine        | Failed      | Did not fail |
| Ad             | Clicked     | Not clicked  |
| Image          | Car present | Car absent   |

So we can encode the result numerically:

$$
X=
\begin{cases}
1 & \text{success}\\
0 & \text{failure}
\end{cases}
$$

This is extremely important for Machine Learning.

---

# 3. Why Use 0 and 1?

Suppose we have:

> "Did the customer click?"

Instead of storing:

```text
Yes
No
Yes
Yes
No
```

we can represent it as:

```text
1
0
1
1
0
```

Now mathematics can operate on it easily.

So:

$$
1=\text{event happened}
$$

$$
0=\text{event did not happen}
$$

But remember:

> **0 and 1 are just an encoding.**

They don't inherently mean "bad" and "good."

For example, we could define:

$$
1=\text{cat}
$$

$$
0=\text{not cat}.
$$

---

# 4. Introduce Probability \(p\)

Suppose we have a biased coin.

The probability of Heads is:

$$
P(H)=0.7
$$

and therefore:

$$
P(T)=0.3
$$

because all probabilities must add up to 1:

$$
0.7+0.3=1.
$$

We normally give the probability of **success** a special name:

$$
p
$$

So:

$$
p=P(X=1)
$$

And because there are only two possibilities:

$$
P(X=0)=1-p.
$$

---

# 5. What Does \(0\leq p\leq1\) Mean?

Probability can never be below 0 or above 1:

$$
0\leq p\leq1
$$

Examples:

$$
p=0
$$

means success is impossible.

$$
p=1
$$

means success is certain.

$$
p=0.5
$$

means success and failure are equally likely.

$$
p=0.9
$$

means success has a 90% probability.

---

# 6. Bernoulli Distribution

Now we can formally define it:

$$
\boxed{X\sim\mathrm{Bernoulli}(p)}
$$

Let's decode this notation.

### \(X\)

Our random variable.

### \(\sim\)

Means:

> "is distributed according to"

### Bernoulli

The type of probability distribution.

### \(p\)

The probability of success.

So:

$$
X\sim\mathrm{Bernoulli}(0.7)
$$

means:

> Random variable \(X\) follows a Bernoulli distribution where the probability of getting 1 is 0.7.

---

# 7. The Bernoulli PMF

The probability mass function is:

$$
\boxed{
P(X=x)=p^x(1-p)^{1-x}
}
$$

At first glance, this looks scary.

Don't memorize it yet.

Let's understand why it works.

Remember:

$$
x\in\{0,1\}.
$$

There are only two possibilities.

---

## Case 1: \(x=1\)

Substitute \(x=1\):

$$
P(X=1)=p^1(1-p)^{1-1}
$$

$$
=p^1(1-p)^0
$$

We know:

$$
a^0=1
$$

Therefore:

$$
P(X=1)=p.
$$

Exactly what we wanted.

---

## Case 2: \(x=0\)

Now substitute \(x=0\):

$$
P(X=0)=p^0(1-p)^{1-0}
$$

$$
=1(1-p)
$$

Therefore:

$$
\boxed{P(X=0)=1-p}
$$

Again, exactly what we wanted.

---

# 8. Why Is This Formula Clever?

This single formula:

$$
p^x(1-p)^{1-x}
$$

automatically handles both cases.

If:

$$
x=1
$$

we get:

$$
p.
$$

If:

$$
x=0
$$

we get:

$$
1-p.
$$

That's why this formula appears repeatedly in **Machine Learning**, especially in **binary classification** and **logistic regression**.

---

# 9. Example — Disease Detection

Suppose an ML model is analyzing whether a patient has a disease.

Define:

$$
X=
\begin{cases}
1 & \text{disease present}\\
0 & \text{disease absent}
\end{cases}
$$

Suppose:

$$
p=0.8.
$$

Then:

$$
P(X=1)=0.8
$$

and:

$$
P(X=0)=1-0.8=0.2.
$$

So:

| Outcome    | Probability |
| ---------- | ----------: |
| Disease    |         0.8 |
| No disease |         0.2 |

The random variable is:

$$
X\sim\mathrm{Bernoulli}(0.8).
$$

---

# 10. Coin Example

For a fair coin:

$$
P(H)=0.5
$$

and:

$$
P(T)=0.5.
$$

Define:

$$
X=
\begin{cases}
1 & H\\
0 & T
\end{cases}
$$

Then:

$$
X\sim\mathrm{Bernoulli}(0.5).
$$

Its distribution is:

$$
P(X=0)=0.5
$$

$$
P(X=1)=0.5.
$$

---

# 11. VERY Important: One Trial

This is one of the most important things to remember.

### One coin toss:

$$
\boxed{\text{Bernoulli}}
$$

because there is one trial with two outcomes.

But suppose we toss the coin **10 times**.

Now we have:

```text
H T H H T T H H H T
```

That's **10 Bernoulli trials**, not one Bernoulli trial.

Later, we can ask:

> "How many Heads did I get in those 10 trials?"

That leads us to the **Binomial distribution**.

So:

$$
\boxed{\text{Bernoulli = one binary trial}}
$$

$$
\boxed{\text{Binomial = number of successes in multiple Bernoulli trials}}
$$

We'll study Binomial in the **next lesson**, not yet.

---

# 12. Expected Value of a Bernoulli Random Variable

Now we introduce another important statistical idea:

## Expected value

Think of expected value as a **probability-weighted average**.

For a discrete random variable:

$$
E[X]=\sum_x xP(X=x).
$$

For Bernoulli, there are only two values:

$$
X=0
$$

or

$$
X=1.
$$

Therefore:

$$
E[X]
=
0\cdot P(X=0)
+
1\cdot P(X=1)
$$

Substitute the probabilities:

$$
E[X]
=
0(1-p)+1(p)
$$

$$
\boxed{E[X]=p}
$$

This is a beautiful result.

---

# 13. What Does \(E[X]=p\) Actually Mean?

Suppose:

$$
p=0.7.
$$

Then:

$$
E[X]=0.7.
$$

But wait!

Our random variable can only be:

$$
0\quad\text{or}\quad1.
$$

How can its expected value be 0.7?

Because expected value doesn't necessarily have to be an outcome that actually occurs.

Imagine repeating the experiment thousands of times.

If:

$$
P(X=1)=0.7,
$$

then approximately 70% of the trials produce 1.

For example:

```text
1  0  1  1  0  1  1  0  1  1
```

The average of many such 0/1 outcomes approaches:

$$
0.7.
$$

So:

> **The expected value of a Bernoulli variable is its probability of success.**

$$
\boxed{E[X]=p}
$$

---

# 14. Variance of Bernoulli

Variance tells us how much a random variable tends to vary around its expected value.

For Bernoulli:

$$
\boxed{\mathrm{Var}(X)=p(1-p)}
$$

Let's actually derive it rather than blindly memorizing it.

We know:

$$
E[X]=p.
$$

For Bernoulli:

$$
X^2=X
$$

because:

$$
0^2=0
$$

and:

$$
1^2=1.
$$

Therefore:

$$
E[X^2]=p.
$$

The variance formula is:

$$
\mathrm{Var}(X)=E[X^2]-(E[X])^2.
$$

Substitute:

$$
\mathrm{Var}(X)=p-p^2
$$

Factor \(p\):

$$
\boxed{\mathrm{Var}(X)=p(1-p)}
$$

---

# 15. Why Is Variance Largest at \(p=0.5\)?

Let's compare.

### \(p=0\)

$$
\mathrm{Var}(X)=0(1-0)=0
$$

There is no uncertainty.

You know the result will always be 0.

---

### \(p=1\)

$$
\mathrm{Var}(X)=1(1-1)=0.
$$

Again, no uncertainty.

You know the result will always be 1.

---

### \(p=0.5\)

$$
\mathrm{Var}(X)=0.5(0.5)=0.25.
$$

This is the maximum.

Why?

Because when:

$$
P(0)=P(1)=0.5
$$

you are maximally uncertain about what will happen.

### Mental model

Think of a light switch.

If someone tells you:

> "It is 99.9% certain to be ON."

Very little uncertainty.

If they tell you:

> "It is 50% ON and 50% OFF."

You have maximum uncertainty.

So:

$$
\boxed{\text{Maximum Bernoulli uncertainty occurs at }p=0.5}
$$

---

# 16. Bernoulli Distribution in Machine Learning

Now we reach the important ML connection.

Suppose we are building a spam classifier.

For every email:

$$
Y=
\begin{cases}
1 & \text{spam}\\
0 & \text{not spam}
\end{cases}
$$

The model receives features:

$$
X=
\begin{bmatrix}
\text{number of links}\\
\text{number of suspicious words}\\
\text{sender information}\\
\vdots
\end{bmatrix}
$$

The model might say:

$$
P(Y=1\mid X=x)=0.92.
$$

This means:

> Given these features, the model assigns a 92% probability to the email being spam.

Therefore:

$$
P(Y=0\mid X=x)=0.08.
$$

We can write:

$$
\boxed{
Y\mid X=x\sim\mathrm{Bernoulli}(0.92)
}
$$

This is a fundamental idea in probabilistic binary classification.

---

# 17. The Big ML Picture

A binary classifier isn't necessarily saying:

> "This is definitely class 1."

Instead, it can produce:

$$
p=P(Y=1\mid X).
$$

For example:

```text
Input image
     ↓
    ML Model
     ↓
Probability
     ↓
P(car | image) = 0.87
```

So the model says:

> "Given what I observed, my estimated probability of class 1 is 87%."

Then you might choose a decision rule such as:

$$
p\ge0.5\Rightarrow1
$$

$$
p<0.5\Rightarrow0.
$$

The **probability** and the eventual **class decision** are separate concepts.

That's an important distinction.

---

# 18. Logistic Regression Connection

This is where Bernoulli becomes extremely important.

Logistic regression produces a probability:

$$
p=\sigma(z)
$$

where:

$$
\sigma(z)=\frac{1}{1+e^{-z}}.
$$

The sigmoid guarantees:

$$
0<p<1.
$$

That probability can then be interpreted as:

$$
\boxed{
p=P(Y=1\mid X)
}
$$

and therefore:

$$
Y\mid X\sim\mathrm{Bernoulli}(p).
$$

So conceptually:

$$
\boxed{
X
\rightarrow
\text{logistic regression}
\rightarrow
p
\rightarrow
\text{Bernoulli probability model}
\rightarrow
Y\in\{0,1\}
}
$$

We'll later study **why logistic regression uses the sigmoid** and how the Bernoulli likelihood leads to **log loss/cross-entropy**.

For now, just remember the connection.

---

# 19. Real-World Bernoulli Examples

Almost everywhere you have a binary outcome, Bernoulli can appear.

### Manufacturing

Did the machine fail?

$$
X\in\{0,1\}
$$

### Computer vision

Does this image contain a pedestrian?

$$
X\in\{0,1\}
$$

### Cybersecurity

Is this network connection malicious?

$$
X\in\{0,1\}
$$

### Marketing

Did the customer click?

$$
X\in\{0,1\}
$$

### Medical diagnosis

Is the test positive?

$$
X\in\{0,1\}
$$

### Physics

Was a photon detected during a particular measurement window?

$$
X\in\{0,1\}
$$

---

# 20. Quantum Physics Connection

This one is particularly useful for you.

Consider a qubit:

$$
|\psi\rangle
=
\alpha|0\rangle+\beta|1\rangle
$$

When measured in the computational basis:

$$
P(0)=|\alpha|^2
$$

and:

$$
P(1)=|\beta|^2.
$$

Since:

$$
|\alpha|^2+|\beta|^2=1,
$$

we can encode the measurement result as:

$$
X=
\begin{cases}
0 & \text{measurement gives }0\\
1 & \text{measurement gives }1
\end{cases}
$$

The **observed binary measurement outcome** can therefore be modeled as a Bernoulli random variable with:

$$
p=|\beta|^2.
$$

So:

$$
X\sim\mathrm{Bernoulli}(|\beta|^2).
$$

Important nuance:

> The quantum state itself is not simply "a Bernoulli distribution." Rather, the **binary measurement outcome** can be represented by a Bernoulli random variable.

This distinction becomes very useful later when you study quantum measurements, quantum trajectories, and photon-counting.

---

# 21. Bernoulli vs Random Variable vs Distribution

Let's connect everything we've learned.

### Random variable

A numerical representation of a random outcome.

Example:

$$
X\in\{0,1\}.
$$

### Bernoulli random variable

A random variable with exactly two possible values:

$$
0,1.
$$

### Bernoulli distribution

The probability distribution describing those two values:

$$
P(X=1)=p
$$

$$
P(X=0)=1-p.
$$

So:

$$
\boxed{
\text{Random Variable}
\rightarrow
\text{Bernoulli RV}
\rightarrow
\text{Bernoulli Distribution}
}
$$

---

# 22. The Complete Bernoulli Cheat Sheet

| Concept             | Formula                        |
| ------------------- | ------------------------------ |
| Possible values     | \(X\in\{0,1\}\)                |
| Success probability | \(P(X=1)=p\)                   |
| Failure probability | \(P(X=0)=1-p\)                 |
| Distribution        | \(X\sim\mathrm{Bernoulli}(p)\) |
| PMF                 | \(P(X=x)=p^x(1-p)^{1-x}\)      |
| Expected value      | \(E[X]=p\)                     |
| Variance            | \(\mathrm{Var}(X)=p(1-p)\)     |
| Standard deviation  | \(\sqrt{p(1-p)}\)              |

---

# 23. Your Mental Model 🧠

Imagine a **tiny two-sided machine**:

```text
              RANDOM TRIAL
                   │
             ┌─────┴─────┐
             │           │
            0            1
         Failure       Success
             │           │
          1 - p           p
```

That's Bernoulli.

### One sentence to remember forever:

> **Bernoulli describes one random experiment whose result is either 0 or 1.**

And the most important ML connection:

$$
\boxed{
P(Y=1\mid X)=p
\quad\Rightarrow\quad
Y\mid X\sim\mathrm{Bernoulli}(p)
}
$$

---

# 24. Practice — Don't Look at the Answers Yet

### Q1

Which of these can be modeled as a Bernoulli trial?

A. Number of students in a classroom
B. Whether a student passes an exam
C. Height of a student
D. Temperature

---

### Q2

A machine has a 20% probability of failing during a particular test.

Define failure as \(X=1\).

What is:

$$
P(X=1)?
$$

And:

$$
P(X=0)?
$$

---

### Q3

If:

$$
X\sim\mathrm{Bernoulli}(0.8)
$$

find:

$$
E[X]
$$

and:

$$
\mathrm{Var}(X).
$$

---

### Q4

A binary classifier produces:

$$
P(Y=1\mid X)=0.73.
$$

What is:

$$
P(Y=0\mid X)?
$$

---

### Q5

Is tossing a coin **10 times** one Bernoulli trial?

Why or why not?

---

## Answers

**Q1:** B

**Q2:**

$$
P(X=1)=0.2
$$

$$
P(X=0)=0.8
$$

**Q3:**

$$
E[X]=0.8
$$

$$
\mathrm{Var}(X)=0.8(0.2)=0.16
$$

**Q4:**

$$
P(Y=0\mid X)=1-0.73=0.27
$$

**Q5:** No. It consists of **10 Bernoulli trials**. If we count how many successes occur among those 10 trials, we enter the territory of the **Binomial distribution**.

---

## Where We Are Now

```text
Probability
    ↓
Random Variables
    ↓
Probability Distributions
    ↓
Bernoulli Distribution  ← YOU ARE HERE
    ↓
Binomial Distribution
    ↓
Expectation / Variance
    ↓
More important distributions
    ↓
Statistics
    ↓
NumPy
    ↓
Machine Learning
```

**Next lesson: Binomial Distribution** — we'll take Bernoulli and ask the natural next question:

> **"If I perform the Bernoulli experiment \(n\) times, what is the probability of getting exactly \(k\) successes?"**

That is where the **binomial coefficient \(\binom nk\)**, counting, and repeated binary outcomes come together.
