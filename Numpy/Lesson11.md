# Lesson 11 — Basic Probability

Now we enter one of the **most important foundations of Machine Learning and Statistics**:

$$
\boxed{\text{Probability}}
$$

Probability appears everywhere in ML:

- classification
- logistic regression
- Bayesian methods
- Naive Bayes
- uncertainty
- likelihood
- loss functions
- generative models
- probabilistic ML
- neural networks
- quantum mechanics

And because you told me you want to build the foundation properly, we're going **from zero**.

---

# 1. What Is Probability?

At its simplest:

> **Probability is a mathematical way of describing uncertainty.**

Suppose I ask:

> "Will it rain tomorrow?"

You don't know with certainty.

You might say:

$$
P(\text{rain})=0.7
$$

This means there is a **70% probability** of rain according to whatever information/model produced that estimate.

Probability gives us a way to quantify uncertainty.

---

# 2. The Probability Scale

Probability always lies between:

$$
\boxed{0\leq P\leq1}
$$

Think of a probability scale:

```text
0                    0.5                    1
│---------------------│----------------------│
Impossible          Uncertain              Certain
```

### Probability = 0

The event is impossible.

Example:

> Rolling a normal six-sided die and getting 9.

$$
P(9)=0
$$

---

### Probability = 1

The event is certain.

Example:

> Rolling a normal die and getting a number from 1 to 6.

$$
P(1\text{ to }6)=1
$$

---

### Probability = 0.5

50% probability.

For example, a perfectly fair coin:

$$
P(\text{Heads})=0.5
$$

---

# 3. The Coin Analogy 🪙

Imagine a fair coin.

It has two possible results:

$$
\text{Heads}
$$

or

$$
\text{Tails}
$$

If the coin is perfectly fair:

$$
P(\text{Heads})=\frac12
$$

and:

$$
P(\text{Tails})=\frac12
$$

Convert to decimal:

$$
\frac12=0.5
$$

Convert to percentage:

$$
0.5=50\%
$$

Therefore:

$$
\boxed{P(H)=0.5}
$$

$$
\boxed{P(T)=0.5}
$$

And notice:

$$
P(H)+P(T)=1
$$

---

# 4. Experiment

In probability, an **experiment** is an action/process whose outcome is uncertain.

Examples:

- toss a coin
- roll a die
- draw a card
- measure temperature
- measure particle position
- observe whether an email is spam
- ask whether a patient has a disease

For example:

> Toss a coin.

That is our experiment.

---

# 5. Outcome

An **outcome** is one possible result of an experiment.

For the coin:

$$
\{\text{Heads},\text{Tails}\}
$$

There are two outcomes.

For a die:

$$
\{1,2,3,4,5,6\}
$$

There are six outcomes.

---

# 6. Sample Space

The **sample space** is the set of **all possible outcomes**.

We usually write it as:

$$
\boxed{S}
$$

For a coin:

$$
S=\{H,T\}
$$

For a die:

$$
S=\{1,2,3,4,5,6\}
$$

Think:

> **Sample space = the complete menu of possibilities.**

---

# 7. Event

An **event** is a particular outcome or collection of outcomes that we care about.

We usually represent an event using a capital letter:

$$
A,B,C,\ldots
$$

Suppose we roll a die.

Sample space:

$$
S=\{1,2,3,4,5,6\}
$$

Suppose event \(A\) means:

> "Roll an even number."

Then:

$$
A=\{2,4,6\}
$$

So:

```text
Sample space
{1, 2, 3, 4, 5, 6}
        │
        └── Event A
            {2, 4, 6}
```

---

# 8. Basic Probability Formula

For equally likely outcomes:

$$
\boxed{
P(A)=
\frac{\text{number of favorable outcomes}}
{\text{number of possible outcomes}}
}
$$

This is one of the first probability formulas you should understand.

---

## Example: Die

We roll a fair die.

What is the probability of getting an even number?

Possible outcomes:

$$
\{1,2,3,4,5,6\}
$$

Total:

$$
6
$$

Favorable:

$$
\{2,4,6\}
$$

Total favorable:

$$
3
$$

Therefore:

$$
P(A)=\frac36
$$

$$
\boxed{P(A)=\frac12=0.5=50\%}
$$

---

# 9. "Favorable" Doesn't Mean Good

This word can be confusing.

In probability:

> **Favorable outcome = an outcome that satisfies the event we're asking about.**

It doesn't mean morally good or desirable.

For example:

> Probability of rolling a 5.

The favorable outcomes are:

$$
\{5\}
$$

So:

$$
P(5)=\frac16
$$

---

# 10. Probability and Data

Now let's leave coins and dice.

Suppose we have:

100 emails.

Among them:

- 80 are normal
- 20 are spam

If we randomly select one email:

$$
P(\text{spam})=
\frac{20}{100}
$$

$$
=0.2
$$

$$
\boxed{P(\text{spam})=20\%}
$$

This is already starting to look like Machine Learning.

---

# 11. Probability in Machine Learning

Suppose an ML model looks at an email and says:

$$
P(\text{spam})=0.92
$$

What does that mean?

The model is saying:

> Based on the information it has learned, this email has an estimated probability of 92% of belonging to the spam class.

Then we might classify it as:

$$
\text{Spam}
$$

if the probability exceeds some threshold such as 0.5.

For example:

$$
P(\text{spam})=0.92
$$

→ Spam

while:

$$
P(\text{spam})=0.13
$$

→ Not spam.

We'll later learn that **probability outputs and classification decisions are related but not identical concepts**.

---

# 12. Probability vs Percentage

These are the same information in different forms.

$$
\frac14=0.25=25\%
$$

$$
\frac12=0.5=50\%
$$

$$
\frac34=0.75=75\%
$$

So:

| Fraction | Decimal | Percentage |
| -------- | ------: | ---------: |
| \(1/4\)  |    0.25 |        25% |
| \(1/2\)  |    0.50 |        50% |
| \(3/4\)  |    0.75 |        75% |
| \(1\)    |    1.00 |       100% |

---

# 13. Complement

Now we learn a very important concept.

Suppose:

$$
P(A)=0.7
$$

What is the probability that \(A\) **doesn't happen**?

Obviously:

$$
1-0.7=0.3
$$

So:

$$
\boxed{P(A^c)=1-P(A)}
$$

where \(A^c\) means:

> "not A"

---

## Example

Suppose:

$$
P(\text{Rain})=0.7
$$

Then:

$$
P(\text{No Rain})=1-0.7
$$

$$
\boxed{=0.3}
$$

or:

$$
30\%
$$

---

# 14. Why Does the Complement Formula Work?

Something either happens or it doesn't.

Therefore:

$$
P(A)+P(\text{not A})=1
$$

because the entire probability space equals 100%.

So:

$$
P(A)+P(A^c)=1
$$

Rearrange:

$$
\boxed{P(A^c)=1-P(A)}
$$

---

# 15. Multiple Events

Suppose we roll a die.

Let:

$$
A=\text{getting an even number}
$$

So:

$$
A=\{2,4,6\}
$$

Now let:

$$
B=\text{getting a number greater than 3}
$$

So:

$$
B=\{4,5,6\}
$$

Now we can ask more interesting questions.

For example:

> What's the probability of A **OR** B?

or:

> What's the probability of A **AND** B?

These ideas are extremely important.

---

# 16. "OR" in Probability

"OR" means:

> A happens, or B happens, or both happen.

The mathematical symbol is:

$$
\boxed{A\cup B}
$$

called the **union**.

For our die:

$$
A=\{2,4,6\}
$$

$$
B=\{4,5,6\}
$$

Therefore:

$$
A\cup B=\{2,4,5,6\}
$$

Notice that 4 and 6 aren't counted twice.

---

# 17. "AND" in Probability

"AND" means:

> Both A and B happen.

The mathematical symbol is:

$$
\boxed{A\cap B}
$$

called the **intersection**.

Our sets:

$$
A=\{2,4,6\}
$$

$$
B=\{4,5,6\}
$$

Both contain:

$$
4,6
$$

Therefore:

$$
\boxed{A\cap B=\{4,6\}}
$$

---

# 18. Visual Mental Model

Imagine two circles:

```text
          A                 B
       _______           _______
      /       \         /       \
     /         \_______/         \
     \          4  6            /
      \________/   \____________/
```

The overlapping region is:

$$
A\cap B
$$

So remember:

> **AND = overlap**

and:

> **OR = everything belonging to either group.**

---

# 19. Independent Events

Now comes an important concept.

Two events are **independent** if knowing that one happened does not change the probability of the other.

### Example: Two coin tosses

First toss:

$$
H/T
$$

Second toss:

$$
H/T
$$

Whether the first toss is Heads doesn't change the physical probability of the second toss.

So:

$$
P(\text{second Heads})=\frac12
$$

regardless of the first toss.

---

# 20. Multiplication Rule for Independent Events

If \(A\) and \(B\) are independent:

$$
\boxed{
P(A\cap B)=P(A)P(B)
}
$$

Example:

Probability of getting Heads twice:

$$
P(H_1)=\frac12
$$

$$
P(H_2)=\frac12
$$

Therefore:

$$
P(H_1\cap H_2)
=
\frac12\times\frac12
$$

$$
\boxed{\frac14}
$$

or:

$$
25\%
$$

---

# 21. Conditional Probability

This is one of the **most important probability concepts for ML**.

Suppose I tell you:

> "The person is a student."

Now I ask:

> "What is the probability that they study more than 5 hours?"

Your probability estimate may change because you've received additional information.

Conditional probability means:

> **Probability of A given that we already know B happened.**

Written:

$$
\boxed{P(A\mid B)}
$$

Read:

> **"Probability of A given B."**

The vertical bar:

$$
|
$$

means:

> **given that**

---

# 22. Real-World Example

Suppose a university has:

100 students.

Among them:

- 40 are graduate students
- 60 are undergraduate students.

Suppose 20 graduate students use Python daily.

Then:

$$
P(\text{Python daily}\mid\text{Graduate})
$$

means:

> Among graduate students, what fraction use Python daily?

We should **not** divide by all 100 students.

We only consider the graduate group:

$$
\frac{20}{40}=0.5
$$

Therefore:

$$
\boxed{P(\text{Python daily}\mid\text{Graduate})=50\%}
$$

This is the key idea:

> **The condition changes the reference group.**

---

# 23. Conditional Probability Formula

The mathematical definition is:

$$
\boxed{
P(A\mid B)=
\frac{P(A\cap B)}
{P(B)}
}
$$

Don't memorize this blindly.

Understand the story:

> We want A given B, so we restrict our attention to B.

Then ask:

> Within B, how much is also A?

---

# 24. Why Conditional Probability Is Huge in ML

Consider medical diagnosis.

Suppose:

$$
D=\text{patient has disease}
$$

and:

$$
T=\text{test is positive}
$$

A very important question is:

$$
P(D\mid T)
$$

Read:

> Probability that the patient has the disease **given that the test is positive**.

This is fundamentally different from:

$$
P(T\mid D)
$$

which means:

> Probability that the test is positive **given that the patient has the disease**.

These are **not generally the same**.

This distinction becomes critical in:

- medical diagnosis
- Bayesian inference
- spam detection
- anomaly detection
- probabilistic ML
- scientific inference.

---

# 25. Probability and Your Physics Background

Probability becomes especially interesting in quantum mechanics.

For a quantum state:

$$
|\psi\rangle
$$

the coefficients themselves are generally **amplitudes**, not probabilities.

For example:

$$
|\psi\rangle=
\alpha|0\rangle+\beta|1\rangle
$$

The probabilities of measuring the corresponding states are related to:

$$
|\alpha|^2
$$

and:

$$
|\beta|^2
$$

with normalization:

$$
\boxed{
|\alpha|^2+|\beta|^2=1
}
$$

So probability is not just an ML concept.

It is also fundamental to quantum physics.

Later, when we connect ML mathematics with your quantum-physics work, this distinction between **amplitude, probability, and measurement** will become very important.

---

# 26. Probability as a Model of Uncertainty

Here's a deeper way to think about probability.

Imagine you're trying to predict tomorrow's temperature.

You could say:

$$
T=30^\circ C
$$

That's a single prediction.

But reality contains uncertainty.

You might instead describe:

$$
P(T=28^\circ C)
$$

$$
P(T=29^\circ C)
$$

$$
P(T=30^\circ C)
$$

etc.

Now instead of saying:

> "I know exactly what will happen."

you're saying:

> "Here is how uncertainty is distributed across possible outcomes."

This idea eventually leads us to **probability distributions**.

---

# 27. Probability Distribution — First Introduction

Suppose we roll a fair die.

The possible values are:

$$
1,2,3,4,5,6
$$

Each has probability:

$$
\frac16
$$

So we can make a table:

| Outcome | Probability |
| ------- | ----------: |
| 1       |     \(1/6\) |
| 2       |     \(1/6\) |
| 3       |     \(1/6\) |
| 4       |     \(1/6\) |
| 5       |     \(1/6\) |
| 6       |     \(1/6\) |

And:

$$
\sum_{i=1}^{6}P(X=i)=1
$$

Look familiar?

Yes!

This is where our previous lesson on **Σ** connects directly to probability.

---

# 28. Σ + Probability

Remember:

$$
\sum_{i=1}^{n}x_i
$$

means:

> Add everything.

Now:

$$
\boxed{
\sum_i P(X=x_i)=1
}
$$

means:

> Add the probabilities of all possible outcomes, and you must get 1.

So our lessons are connecting:

```text
Σ
│
├── Add values
│
├── Mean
│
├── Variance
│
└── Probability
       │
       └── probabilities add to 1
```

---

# 29. Probability in Classification

Suppose an ML model receives:

```text
Image → Cat/Dog classifier
```

Instead of simply saying:

> Cat

the model can produce:

$$
P(\text{Cat})=0.85
$$

$$
P(\text{Dog})=0.15
$$

Notice:

$$
0.85+0.15=1
$$

The model is expressing its uncertainty over possible classes.

For three classes:

$$
P(\text{Cat})=0.70
$$

$$
P(\text{Dog})=0.20
$$

$$
P(\text{Horse})=0.10
$$

Again:

$$
0.70+0.20+0.10=1
$$

This idea eventually leads us toward **softmax**, which we'll encounter later.

---

# 30. Important Vocabulary

Make sure these are clear:

| Term                     | Meaning                                       |
| ------------------------ | --------------------------------------------- |
| Experiment               | Process with uncertain outcome                |
| Outcome                  | One possible result                           |
| Sample space             | All possible outcomes                         |
| Event                    | Outcome/group of outcomes we're interested in |
| Probability              | Numerical measure of uncertainty              |
| Complement               | Event not happening                           |
| Independent              | One event doesn't affect the other            |
| Conditional probability  | Probability given additional information      |
| Union \(A\cup B\)        | A OR B                                        |
| Intersection \(A\cap B\) | A AND B                                       |

---

# 🧠 The Big Mental Model

Imagine a **probability universe**:

```text
                    SAMPLE SPACE
              "Everything that can happen"
                         │
          ┌──────────────┼──────────────┐
          │              │              │
       Outcome A      Outcome B      Outcome C
          │              │              │
          └──────────────┼──────────────┘
                         │
                    PROBABILITY
                         │
              "How likely is it?"
                         │
          ┌──────────────┼──────────────┐
          │              │              │
        AND             OR           NOT
       A ∩ B           A ∪ B          Aᶜ
                         │
                         ↓
                 CONDITIONAL
                    P(A | B)
                         │
                         ↓
               MACHINE LEARNING
                         │
        ┌────────────────┼────────────────┐
        │                │                │
   Classification     Diagnosis       Uncertainty
```

---

# 🔥 The Most Important Distinction Today

You should be able to immediately distinguish:

$$
\boxed{P(A)}
$$

from:

$$
\boxed{P(A\mid B)}
$$

### \(P(A)\)

> Probability of A.

### \(P(A\mid B)\)

> Probability of A **after we know B**.

The information \(B\) changes the situation we're considering.

This idea becomes absolutely central when we later study **Bayes' theorem**.

---

# 📝 Practice

Try these yourself before looking at the answers.

### Q1

A fair coin is tossed once.

What is:

$$
P(H)
$$

---

### Q2

A fair die is rolled.

What is:

$$
P(\text{even})
$$

---

### Q3

If:

$$
P(A)=0.8
$$

what is:

$$
P(A^c)
$$

---

### Q4

A fair coin is tossed twice.

What is the probability of getting Heads both times?

---

### Q5

A die is rolled.

Let:

$$
A=\{2,4,6\}
$$

and:

$$
B=\{4,5,6\}
$$

Find:

$$
A\cap B
$$

---

### Q6

In your own words, what does this mean?

$$
P(A\mid B)
$$

---

### Q7

A classifier produces:

$$
P(\text{Cat})=0.8
$$

$$
P(\text{Dog})=0.2
$$

What does this tell us?

---

# Answers

### Q1

$$
\boxed{\frac12=0.5=50\%}
$$

### Q2

Even outcomes:

$$
\{2,4,6\}
$$

Therefore:

$$
P(\text{even})=\frac36
=\boxed{\frac12}
$$

### Q3

$$
P(A^c)=1-P(A)
$$

$$
=1-0.8
$$

$$
\boxed{0.2}
$$

### Q4

$$
P(HH)=\frac12\times\frac12
$$

$$
\boxed{\frac14=25\%}
$$

### Q5

Common elements:

$$
\boxed{A\cap B=\{4,6\}}
$$

### Q6

> Probability of A **given that we already know B happened**.

### Q7

The classifier assigns:

- 80% probability to Cat
- 20% probability to Dog

So Cat has the larger estimated probability, but the model is also expressing **uncertainty** rather than absolute certainty.

---

# 🎯 Where We Are Going

Notice the path we're constructing:

$$
\boxed{
\text{Arithmetic}
\rightarrow
\text{Algebra}
\rightarrow
\text{Functions}
\rightarrow
\text{Vectors}
\rightarrow
\text{Matrices}
\rightarrow
\Sigma
\rightarrow
\text{Probability}
}
$$

And from probability we'll eventually build:

$$
\boxed{
\text{Probability}
\rightarrow
\text{Random Variables}
\rightarrow
\text{Distributions}
\rightarrow
\text{Expectation}
\rightarrow
\text{Variance}
\rightarrow
\text{Statistics}
\rightarrow
\text{ML}
}
$$

For your ML foundation, **don't rush past probability**. A lot of things that look like mysterious ML formulas later are actually just probability concepts combined with algebra.

### Next lesson

**Lesson 12 — Random Variables**

We'll answer a fundamental question:

> **What exactly is a random variable, and why do we need one if we already have variables?**

We'll build it from coins and dice first, then connect it to **real datasets, ML classification, continuous measurements, and physics**.
