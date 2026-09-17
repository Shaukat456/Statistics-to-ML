# Lesson 15 — Binomial Distribution

We now know **Bernoulli distribution**:

> One trial → two possible outcomes → 0 or 1.

Now let's ask the natural next question:

> **What happens when we repeat a Bernoulli trial many times?**

That brings us to the **Binomial Distribution**.

---

# 1. Start With Bernoulli

Suppose we have a coin.

One toss:

$$
X=
\begin{cases}
1 & \text{Heads}\\
0 & \text{Tails}
\end{cases}
$$

If:

$$
P(H)=0.5
$$

then:

$$
X\sim\text{Bernoulli}(0.5)
$$

That's **one trial**.

But suppose we toss the coin **10 times**.

Now we might get:

```text
H T H H T H T T H H
```

There are 10 trials.

Instead of caring about every individual result, suppose we ask:

> **How many Heads did we get?**

Here the answer could be:

$$
0,1,2,3,\ldots,10
$$

This new random variable is modeled by a **Binomial distribution**.

---

# 2. The Core Idea

Remember:

$$
\boxed{\text{Bernoulli = one binary trial}}
$$

while:

$$
\boxed{\text{Binomial = number of successes in }n\text{ Bernoulli trials}}
$$

This is the most important thing to remember.

---

# 3. Real-World Example

Imagine an autonomous vehicle system that detects pedestrians.

Suppose we test the detector on **20 independent frames**.

For every frame:

$$
X_i=
\begin{cases}
1 & \text{pedestrian detected correctly}\\
0 & \text{otherwise}
\end{cases}
$$

Suppose the probability of success on each frame is:

$$
p=0.9.
$$

Now ask:

> What is the probability that the detector correctly detects pedestrians in exactly 18 out of 20 frames?

This is a **Binomial** problem.

---

# 4. What Does "Binomial" Mean?

A binomial experiment has:

1. A fixed number of trials \(n\)
2. Each trial has exactly two outcomes
3. Each trial has the same probability of success \(p\)
4. The trials are independent

Let's understand each one.

---

# 5. Condition 1 — Fixed Number of Trials

Suppose we say:

> Toss the coin 10 times.

Then:

$$
n=10.
$$

The number of trials is fixed before we start.

Not:

> "Keep tossing until you get 5 Heads."

That's a different type of probability problem.

For Binomial:

$$
\boxed{n=\text{fixed number of trials}}
$$

---

# 6. Condition 2 — Two Outcomes

Every trial must have two possible outcomes.

For example:

```text
Success / Failure
Yes / No
1 / 0
True / False
Detected / Not detected
```

Exactly like Bernoulli.

---

# 7. Condition 3 — Same Probability \(p\)

Suppose a coin has:

$$
P(H)=0.6.
$$

If we toss it repeatedly, we assume:

$$
P(H)=0.6
$$

for each trial.

So:

$$
p=0.6.
$$

The probability doesn't change from one trial to another.

---

# 8. Condition 4 — Independence

This is extremely important.

Two events are **independent** if the outcome of one doesn't change the probability of the other.

For example, with an ideal coin:

```text
First toss → Heads
Second toss → ?
```

Knowing the first toss was Heads doesn't change the probability of the second toss.

The second toss is still:

$$
P(H)=0.5.
$$

So the tosses are independent.

---

# 9. The Four Conditions 🧠

Whenever you see a Binomial problem, ask:

### **F-I-S-T**

**F** → Fixed number of trials

**I** → Independent trials

**S** → Same probability of success

**T** → Two outcomes

A little mnemonic:

> **Binomial needs FIST.** 👊

---

# 10. Define the Random Variable

Suppose we toss a coin 10 times.

Let:

$$
X=\text{number of Heads}.
$$

Then:

$$
X
$$

can be:

$$
0,1,2,\ldots,10.
$$

Notice something interesting.

A **Bernoulli random variable** could only be:

$$
0\text{ or }1.
$$

But a **Binomial random variable** can be:

$$
0,1,2,\ldots,n.
$$

That's because we're counting successes across multiple trials.

---

# 11. Binomial Notation

We write:

$$
\boxed{X\sim\mathrm{Binomial}(n,p)}
$$

For example:

$$
X\sim\mathrm{Binomial}(10,0.5).
$$

This means:

- \(n=10\) trials
- \(p=0.5\) probability of success on each trial
- \(X\) = number of successes.

---

# 12. The Big Question

Suppose:

$$
X\sim\mathrm{Binomial}(10,0.5)
$$

What is:

$$
P(X=3)?
$$

In words:

> What is the probability of getting exactly 3 Heads in 10 tosses?

We need a formula.

---

# 13. First Understand One Specific Sequence

Suppose the 10 tosses produce:

```text
H H H T T T T T T T
```

That's exactly 3 Heads.

Because the coin is fair:

$$
P(H)=0.5
$$

and:

$$
P(T)=0.5.
$$

The probability of this **specific sequence** is:

$$
0.5\times0.5\times0.5\times0.5\times\cdots
$$

10 times.

Therefore:

$$
(0.5)^{10}.
$$

More generally, suppose:

- \(k\) successes
- \(n-k\) failures.

Then one particular sequence has probability:

$$
\boxed{p^k(1-p)^{n-k}}
$$

---

# 14. But There Is a Problem...

We don't want just:

```text
H H H T T T T T T T
```

We want **any arrangement containing exactly 3 Heads**.

For example:

```text
H H H T T T T T T T
H H T H T T T T T T
H T H H T T T T T T
T H H H T T T T T T
...
```

There are many possible arrangements.

So we need to know:

> **How many ways can we arrange \(k\) successes among \(n\) trials?**

That's where combinations enter.

---

# 15. Combinations

Suppose you have 5 students:

```text
A B C D E
```

and you want to choose 2.

The combinations are:

```text
AB
AC
AD
AE
BC
BD
BE
CD
CE
DE
```

There are:

$$
10
$$

ways.

This is written:

$$
\binom52=10.
$$

Read it as:

> "5 choose 2."

---

# 16. The Combination Formula

The formula is:

$$
\boxed{
\binom nk=
\frac{n!}{k!(n-k)!}
}
$$

Now we have to understand the exclamation mark.

---

# 17. Factorial

Factorial means multiply all positive integers down to 1.

For example:

$$
5!=5\times4\times3\times2\times1
$$

so:

$$
5!=120.
$$

Similarly:

$$
3!=3\times2\times1=6.
$$

And:

$$
0!=1.
$$

Therefore:

$$
\binom52
=
\frac{5!}{2!3!}
$$

$$
=
\frac{120}{2\times6}
$$

$$
=10.
$$

---

# 18. Now Build the Binomial Formula

We established that:

### Probability of one particular arrangement:

$$
p^k(1-p)^{n-k}
$$

### Number of arrangements:

$$
\binom nk
$$

Therefore:

$$
\boxed{
P(X=k)=
\binom nk
p^k(1-p)^{n-k}
}
$$

This is the **Binomial PMF**.

---

# 19. Decode Every Symbol

Don't memorize blindly.

$$
\boxed{
P(X=k)=
\binom nk
p^k(1-p)^{n-k}
}
$$

### \(X\)

Random variable = number of successes.

### \(k\)

The number of successes we're interested in.

### \(n\)

Total number of trials.

### \(p\)

Probability of success on each trial.

### \(1-p\)

Probability of failure.

### \(\binom nk\)

Number of ways to arrange \(k\) successes among \(n\) trials.

### \(p^k\)

Probability contribution from the \(k\) successes.

### \((1-p)^{n-k}\)

Probability contribution from the failures.

---

# 20. Full Example

Let's toss a fair coin:

$$
n=10
$$

and:

$$
p=0.5.
$$

We want:

$$
P(X=3).
$$

Use:

$$
P(X=k)=
\binom nkp^k(1-p)^{n-k}.
$$

Therefore:

$$
P(X=3)=
\binom{10}{3}(0.5)^3(0.5)^7.
$$

Calculate the combination:

$$
\binom{10}{3}
=
\frac{10!}{3!7!}
=120.
$$

Therefore:

$$
P(X=3)=120(0.5)^{10}.
$$

Since:

$$
(0.5)^{10}=\frac1{1024},
$$

we get:

$$
P(X=3)=\frac{120}{1024}
$$

$$
\boxed{P(X=3)\approx0.1172}
$$

So there's about an **11.72% probability** of getting exactly 3 Heads.

---

# 21. "Exactly" Is Important

Suppose:

$$
X=\text{number of Heads}.
$$

### Exactly 3

Means:

$$
P(X=3)
$$

### At most 3

Means:

$$
P(X\le3)
$$

which includes:

$$
0,1,2,3.
$$

### At least 3

Means:

$$
P(X\ge3)
$$

which includes:

$$
3,4,5,\ldots,n.
$$

These words are extremely important in probability questions.

---

# 22. Expected Value of Binomial

We learned that Bernoulli has:

$$
E[X]=p.
$$

Now imagine \(n\) Bernoulli trials.

If each trial has expected success rate \(p\), then across \(n\) trials the expected number of successes is:

$$
\boxed{E[X]=np}
$$

For example:

$$
n=100
$$

and:

$$
p=0.7.
$$

Then:

$$
E[X]=100(0.7)=70.
$$

Meaning:

> Over many repetitions of this 100-trial experiment, the average number of successes approaches 70.

It doesn't mean you'll necessarily get exactly 70 every time.

---

# 23. Variance of Binomial

For a Binomial random variable:

$$
\boxed{\mathrm{Var}(X)=np(1-p)}
$$

Compare this with Bernoulli:

$$
\mathrm{Var}(X)=p(1-p).
$$

Binomial simply has \(n\) trials:

$$
\boxed{
\text{Binomial variance}
=
n\times\text{Bernoulli variance}
}
$$

So:

$$
\mathrm{Var}(X)=np(1-p).
$$

And standard deviation is:

$$
\boxed{
\sigma=\sqrt{np(1-p)}
}
$$

---

# 24. Bernoulli → Binomial

This is the connection you should remember.

Imagine each trial is a tiny Bernoulli machine:

```text
Trial 1 → 0/1
Trial 2 → 0/1
Trial 3 → 0/1
Trial 4 → 0/1
...
Trial n → 0/1
```

Now add all the successes:

$$
X=X_1+X_2+\cdots+X_n.
$$

Then:

$$
\boxed{
X\sim\mathrm{Binomial}(n,p)
}
$$

This is a very deep connection.

A Binomial random variable can be viewed as the **sum of \(n\) independent Bernoulli random variables**.

---

# 25. ML Connection — Classification

Suppose we have 100 images.

Our binary classifier predicts whether each image contains a pedestrian.

For each image:

$$
Y_i=
\begin{cases}
1 & \text{correct detection}\\
0 & \text{incorrect detection}
\end{cases}
$$

Suppose the probability of correct detection is:

$$
p=0.9.
$$

For one image:

$$
Y_i\sim\mathrm{Bernoulli}(0.9).
$$

For 100 independent images, let:

$$
X=\text{number of correct detections}.
$$

Then:

$$
X\sim\mathrm{Binomial}(100,0.9).
$$

Now we can ask:

> What is the probability that the model gets exactly 90 images correct?

That's:

$$
P(X=90)
$$

and we can calculate it using the Binomial PMF.

---

# 26. Important ML Distinction

This is subtle.

Suppose your classifier predicts probabilities:

```text
Image 1 → 0.91
Image 2 → 0.72
Image 3 → 0.63
Image 4 → 0.15
...
```

Those probabilities are not automatically a Binomial distribution.

Binomial requires assumptions such as:

- binary outcome
- fixed number of trials
- common success probability \(p\)
- independence.

Real ML datasets may violate these assumptions.

So:

> **Binomial is a mathematical model we may use when its assumptions are appropriate.**

Don't automatically label every collection of 0/1 data as Binomial.

---

# 27. Quantum / Physics Connection

Suppose you're performing repeated binary quantum measurements.

For example, each measurement gives:

$$
0\quad\text{or}\quad1.
$$

Suppose:

$$
P(1)=p.
$$

If you perform \(n\) independent measurements under the same conditions, and you count the number of times you obtain 1:

$$
K=\text{number of 1 outcomes},
$$

then under those assumptions:

$$
\boxed{K\sim\mathrm{Binomial}(n,p)}
$$

For a qubit:

$$
|\psi\rangle=\alpha|0\rangle+\beta|1\rangle
$$

we have:

$$
P(1)=|\beta|^2.
$$

If the same state is independently prepared and measured \(n\) times, then the number of measurements yielding 1 can be Binomial with:

$$
p=|\beta|^2.
$$

This is a useful bridge from quantum measurement to probability theory.

---

# 28. A Beautiful Connection to Your Future FYP

Suppose you're studying **photon detection**.

Imagine dividing time into measurement windows.

For each window:

$$
X_i=
\begin{cases}
1 & \text{photon detected}\\
0 & \text{no photon detected}
\end{cases}
$$

If each window behaves independently with the same detection probability \(p\), then:

$$
X_i\sim\mathrm{Bernoulli}(p).
$$

After \(n\) windows:

$$
K=\sum_{i=1}^{n}X_i
$$

can follow:

$$
K\sim\mathrm{Binomial}(n,p).
$$

This becomes particularly interesting when you later study situations where the assumptions of independence or constant \(p\) **do not hold**—for example, correlated photon detection and **antibunching**.

That's where probability distributions become much more than just textbook formulas.

---

# 29. Bernoulli vs Binomial

|                    | Bernoulli  | Binomial            |
| ------------------ | ---------- | ------------------- |
| Number of trials   | 1          | \(n\)               |
| Outcomes per trial | 2          | 2                   |
| Random variable    | Outcome    | Number of successes |
| Values             | 0, 1       | \(0,1,\ldots,n\)    |
| Parameter          | \(p\)      | \(n,p\)             |
| Mean               | \(p\)      | \(np\)              |
| Variance           | \(p(1-p)\) | \(np(1-p)\)         |

### Memory trick:

> **Bernoulli asks: "Did it happen?"**

> **Binomial asks: "How many times did it happen?"**

---

# 30. The Whole Story 🧠

```text
RANDOM EXPERIMENT
       │
       ▼
 ONE BINARY TRIAL
       │
       ▼
   BERNOULLI
       │
       │ repeat n times
       ▼
┌──────────────────┐
│ 0/1  0/1  0/1   │
│ 0/1  0/1  0/1   │
│      ...         │
└──────────────────┘
       │
       ▼
COUNT THE 1s
       │
       ▼
    BINOMIAL
```

And mathematically:

$$
\boxed{
X_i\sim\mathrm{Bernoulli}(p)
}
$$

and:

$$
\boxed{
X=\sum_{i=1}^{n}X_i
}
$$

then:

$$
\boxed{
X\sim\mathrm{Binomial}(n,p)
}
$$

---

# 31. Practice 🧠

Try these yourself before looking at the answers.

### Q1

A fair coin is tossed 20 times.

What are \(n\) and \(p\)?

---

### Q2

A medical test has a 90% probability of correctly identifying a disease when the disease is present.

If the test is performed on 50 independent patients under the same conditions, what distribution could model the number of correct identifications?

---

### Q3

For:

$$
X\sim\mathrm{Binomial}(10,0.5)
$$

what are the possible values of \(X\)?

---

### Q4

For:

$$
X\sim\mathrm{Binomial}(20,0.4)
$$

calculate:

$$
E[X].
$$

---

### Q5

For:

$$
X\sim\mathrm{Binomial}(20,0.4)
$$

calculate:

$$
\mathrm{Var}(X).
$$

---

### Q6

What's the difference between:

$$
P(X=3)
$$

and:

$$
P(X\le3)?
$$

---

### Q7

A single coin toss is what distribution?

What about the number of Heads obtained in 10 independent coin tosses?

---

## Answers

**Q1**

$$
n=20,\qquad p=0.5.
$$

**Q2**

$$
X\sim\mathrm{Binomial}(50,0.9).
$$

**Q3**

$$
X\in\{0,1,2,\ldots,10\}.
$$

**Q4**

$$
E[X]=np
$$

$$
=20(0.4)=8.
$$

**Q5**

$$
\mathrm{Var}(X)=np(1-p)
$$

$$
=20(0.4)(0.6)
$$

$$
=\boxed{4.8}.
$$

**Q6**

$$
P(X=3)
$$

means **exactly 3**.

Whereas:

$$
P(X\le3)
$$

means:

$$
P(X=0)+P(X=1)+P(X=2)+P(X=3).
$$

**Q7**

One coin toss:

$$
\boxed{\mathrm{Bernoulli}}
$$

Number of Heads in 10 tosses:

$$
\boxed{\mathrm{Binomial}}
$$

---

# Your Progress

You have now built:

```text
Probability
    ↓
Random Variable
    ↓
Probability Distribution
    ↓
Bernoulli
    ↓
Binomial  ← YOU ARE HERE
```

The next important step is to understand **Expectation and Variance properly from first principles**—not just memorize \(E[X]=np\) or \(Var(X)=np(1-p)\).

We'll build the intuition of:

$$
\boxed{\text{Expected Value}}
$$

and then:

$$
\boxed{\text{Variance}}
$$

before moving deeper into statistical distributions.
