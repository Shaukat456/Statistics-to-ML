# Lesson 4 — Powers, Roots, Exponents & Logarithms

This is an **extremely important foundation for Machine Learning**.

You will eventually see these everywhere:

- \(x^2\), \(x^3\), \(x^n\)
- \(\sqrt{x}\)
- \(e^x\)
- \(e^{-x}\)
- \(\log(x)\)
- \(\ln(x)\)
- sigmoid
- softmax
- log loss / cross-entropy
- probability and likelihood
- radioactive decay
- exponential growth
- numerical stability

So let's build this **from zero**.

---

# 1. The Big Idea

Imagine you have a bacteria colony.

You start with:

$$
2 \text{ bacteria}
$$

Every hour, the number doubles.

After:

- 1 hour → \(2\times2=4\)
- 2 hours → \(2\times2\times2=8\)
- 3 hours → \(2\times2\times2\times2=16\)

Instead of repeatedly writing multiplication, mathematics gives us:

$$
2^4=16
$$

This is the fundamental idea behind **powers/exponents**.

> **Exponent = tells you how many times to multiply the base by itself.**

---

# 2. Powers / Exponents

Consider:

$$
2^3
$$

There are two parts:

$$
\boxed{2^3}
$$

- \(2\) → **base**
- \(3\) → **exponent**

It means:

$$
2^3=2\times2\times2
$$

Therefore:

$$
2^3=8
$$

Another example:

$$
5^4
$$

means:

$$
5\times5\times5\times5
$$

Therefore:

$$
5^4=625
$$

### Mental model

Think:

> **Base = what is growing**
> **Exponent = how many times the growth happens**

---

# 3. Why Exponents Matter in ML

Suppose a feature is:

$$
x=10
$$

Now square it:

$$
x^2=100
$$

If:

$$
x=100
$$

then:

$$
x^2=10,000
$$

So powers can make numbers grow **very quickly**.

This matters in ML because we frequently encounter:

$$
x^2
$$

For example, **Mean Squared Error**:

$$
MSE=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat y_i)^2
$$

The error is squared.

Why?

Because squaring:

1. makes negative and positive errors both positive;
2. strongly penalizes large errors.

For example:

$$
(-2)^2=4
$$

while

$$
(-10)^2=100
$$

So a large mistake becomes much more important.

We'll study MSE properly later.

---

# 4. Important Exponent Rules

These rules are worth understanding rather than memorizing blindly.

## Rule 1 — Multiplication

Suppose:

$$
2^3\times2^2
$$

Expand:

$$
(2\times2\times2)(2\times2)
$$

There are five 2s:

$$
2^5
$$

Therefore:

$$
\boxed{a^m\times a^n=a^{m+n}}
$$

Example:

$$
x^3x^4=x^7
$$

---

# 5. Division

Consider:

$$
\frac{2^5}{2^2}
$$

Expand:

$$
\frac{2\times2\times2\times2\times2}
{2\times2}
$$

Two pairs cancel:

$$
2\times2\times2=2^3
$$

Therefore:

$$
\boxed{\frac{a^m}{a^n}=a^{m-n}}
$$

Example:

$$
\frac{x^7}{x^3}=x^4
$$

---

# 6. Power of a Power

Suppose:

$$
(2^3)^2
$$

First:

$$
2^3=8
$$

Then:

$$
8^2=64
$$

But:

$$
2^6=64
$$

Therefore:

$$
\boxed{(a^m)^n=a^{mn}}
$$

Notice that we **multiply the exponents**.

Example:

$$
(x^2)^3=x^6
$$

---

# 7. Anything to the Power 0

This seems strange initially:

$$
5^0=1
$$

Why?

Consider:

$$
\frac{5^3}{5^3}=1
$$

Using the exponent division rule:

$$
5^{3-3}=5^0
$$

Therefore:

$$
\boxed{5^0=1}
$$

And generally:

$$
\boxed{a^0=1}
$$

for \(a\neq0\).

Examples:

$$
10^0=1
$$

$$
100^0=1
$$

$$
x^0=1
$$

---

# 8. Negative Exponents

Now something interesting:

$$
2^{-1}
$$

A negative exponent means **take the reciprocal**.

$$
\boxed{a^{-n}=\frac{1}{a^n}}
$$

Therefore:

$$
2^{-1}=\frac12
$$

And:

$$
2^{-2}=\frac{1}{2^2}
=\frac14
$$

Similarly:

$$
10^{-3}=\frac{1}{1000}=0.001
$$

### Mental model

Positive exponent:

> "Multiply upward."

Negative exponent:

> "Flip it and move downward."

---

# 9. Roots — The Reverse of Powers

Now let's reverse the question.

We know:

$$
3^2=9
$$

Suppose I ask:

> What number squared gives 9?

Answer:

$$
3
$$

Mathematics writes:

$$
\sqrt9=3
$$

So:

$$
\boxed{\text{Square root = reverse of squaring}}
$$

Another example:

$$
5^2=25
$$

therefore:

$$
\sqrt{25}=5
$$

---

# 10. Cube Roots

Same idea.

We know:

$$
2^3=8
$$

So:

$$
\sqrt[3]{8}=2
$$

The cube root asks:

> "What number multiplied by itself three times gives this?"

Therefore:

$$
\sqrt[3]{27}=3
$$

because:

$$
3^3=27
$$

---

# 11. Fractional Exponents

Here's where powers and roots connect beautifully.

We can write:

$$
\sqrt{x}
$$

as:

$$
x^{1/2}
$$

Therefore:

$$
\boxed{x^{1/2}=\sqrt{x}}
$$

Similarly:

$$
\boxed{x^{1/3}=\sqrt[3]{x}}
$$

And:

$$
x^{1/4}=\sqrt[4]{x}
$$

### General rule

$$
\boxed{x^{1/n}=\sqrt[n]{x}}
$$

So:

$$
16^{1/2}=4
$$

because:

$$
\sqrt{16}=4
$$

---

# 12. What About \(x^{3/2}\)?

This combines a power and a root.

$$
x^{3/2}
$$

You can think of it as:

$$
(\sqrt{x})^3
$$

or:

$$
\sqrt{x^3}
$$

For example:

$$
4^{3/2}
$$

First take the square root:

$$
\sqrt4=2
$$

Then cube it:

$$
2^3=8
$$

Therefore:

$$
\boxed{4^{3/2}=8}
$$

---

# 13. Exponential Growth

Now we reach one of the most important ideas.

Suppose you invest $100.

Imagine it grows by 10% every year.

After one year:

$$
100(1.10)=110
$$

After two years:

$$
110(1.10)=121
$$

After three years:

$$
121(1.10)=133.1
$$

Notice what is happening.

We're repeatedly multiplying by \(1.10\).

So after \(t\) years:

$$
A=100(1.10)^t
$$

This is **exponential growth**.

---

# 14. Linear Growth vs Exponential Growth

This distinction is extremely important.

### Linear growth

Suppose you add 10 every year:

$$
10,\ 20,\ 30,\ 40,\ 50,\ldots
$$

The increase is constant.

### Exponential growth

Suppose you multiply by 2:

$$
2,\ 4,\ 8,\ 16,\ 32,\ 64,\ldots
$$

The increase itself keeps becoming larger.

### Visual mental model

Linear:

> 🚶 → 🚶 → 🚶 → 🚶

Exponential:

> 🚶 → 🏃 → 🏃🏃 → 🚀 → 🚀🚀🚀

---

# 15. Physics Connection — Radioactive Decay

Since you're learning physics, this is a beautiful example.

Radioactive substances often follow exponential decay:

$$
N(t)=N_0e^{-\lambda t}
$$

where:

- \(N(t)\) = amount remaining at time \(t\)
- \(N_0\) = initial amount
- \(e\) = special mathematical constant
- \(\lambda\) = decay constant
- \(t\) = time

Notice:

$$
e^{-\lambda t}
$$

The negative exponent represents **decay**.

As \(t\) increases:

$$
e^{-\lambda t}
$$

gets smaller.

So exponential functions aren't just abstract mathematics.

They describe real physical processes.

---

# 16. The Special Number \(e\)

You will see \(e\) **everywhere** in ML and physics.

Its approximate value is:

$$
\boxed{e\approx2.71828}
$$

Don't worry about memorizing many decimal places.

The important thing is understanding what makes \(e\) special.

It naturally appears when something changes continuously.

Examples include:

- continuous growth
- radioactive decay
- probability
- differential equations
- statistical distributions
- neural networks
- optimization
- information theory

---

# 17. Why \(e\) Appears in Machine Learning

Consider the **sigmoid function**:

$$
\sigma(z)=\frac{1}{1+e^{-z}}
$$

Don't worry about learning sigmoid yet.

Just notice:

$$
e^{-z}
$$

The exponential function allows us to transform any real-valued number into something that behaves like a probability between 0 and 1.

For example, conceptually:

$$
z\rightarrow \text{sigmoid}\rightarrow P(\text{class})
$$

We'll study this properly when we reach classification.

---

# 18. Now: Logarithms

This is where many beginners get confused.

But there's a very simple way to remember them.

We know:

$$
10^3=1000
$$

Now reverse the question.

Instead of asking:

> What is \(10^3\)?

ask:

> **What exponent do I need to put on 10 to get 1000?**

Answer:

$$
3
$$

Mathematics writes:

$$
\boxed{\log_{10}(1000)=3}
$$

So:

> **A logarithm asks: "What exponent produces this number?"**

That's the most important definition.

---

# 19. Exponent vs Logarithm

Think of them as opposite operations.

### Exponent

$$
10^3=1000
$$

Question:

> What happens when I raise 10 to 3?

Answer:

$$
1000
$$

### Logarithm

$$
\log_{10}(1000)=3
$$

Question:

> What exponent on 10 produces 1000?

Answer:

$$
3
$$

Therefore:

$$
\boxed{\text{logarithm = inverse of exponentiation}}
$$

### Memory trick

**Exponent:** Build the number.

**Log:** Find out how many exponential steps built the number.

---

# 20. More Log Examples

$$
\log_{10}(100)=2
$$

because:

$$
10^2=100
$$

---

$$
\log_{10}(10,000)=4
$$

because:

$$
10^4=10,000
$$

---

$$
\log_2(8)=3
$$

because:

$$
2^3=8
$$

---

$$
\log_2(32)=5
$$

because:

$$
2^5=32
$$

---

# 21. The Three Important Parts of a Log

Consider:

$$
\log_2(8)=3
$$

There are three things:

- \(2\) → **base**
- \(8\) → **input**
- \(3\) → **answer/exponent**

It means:

$$
2^3=8
$$

So whenever you see:

$$
\log_b(x)=y
$$

you can immediately translate it into:

$$
\boxed{b^y=x}
$$

This relationship is incredibly useful.

---

# 22. Natural Logarithm — \(\ln\)

In ML and statistics, you will very frequently see:

$$
\ln(x)
$$

This means logarithm with base \(e\):

$$
\boxed{\ln(x)=\log_e(x)}
$$

So:

$$
\ln(e^3)=3
$$

because:

$$
\log_e(e^3)=3
$$

You don't need to fear the notation.

Just remember:

> **\(\ln\) = log with base \(e\)**

---

# 23. Why ML Loves Logarithms

This is extremely important.

Suppose a model gives probabilities:

$$
0.9,\quad0.8,\quad0.7
$$

If we multiply them:

$$
0.9\times0.8\times0.7=0.504
$$

With many probabilities, the product can become **extremely tiny**.

For example:

$$
0.9^{100}
$$

is very small.

Computers can eventually have numerical problems when dealing with extremely tiny numbers.

Logarithms help.

Because:

$$
\ln(ab)=\ln(a)+\ln(b)
$$

So instead of multiplying:

$$
a\times b\times c\times d
$$

we can work with:

$$
\ln(a)+\ln(b)+\ln(c)+\ln(d)
$$

This is one major reason logarithms appear in probability and ML.

---

# 24. Logarithms Turn Multiplication Into Addition

This is one of the **most powerful properties of logarithms**.

$$
\boxed{\ln(ab)=\ln(a)+\ln(b)}
$$

For example:

$$
\ln(10\times100)
$$

can become:

$$
\ln(10)+\ln(100)
$$

Similarly:

$$
\boxed{\ln\left(\frac{a}{b}\right)=\ln(a)-\ln(b)}
$$

And:

$$
\boxed{\ln(a^b)=b\ln(a)}
$$

This is extremely useful in statistics and ML.

---

# 25. Log Transformations

Suppose we have salaries:

$$
30,000
$$

$$
50,000
$$

$$
100,000
$$

$$
1,000,000
$$

The last value is much larger than the others.

A logarithm compresses large values.

For example, using base 10:

$$
\log_{10}(1000)=3
$$

$$
\log_{10}(1,000,000)=6
$$

Instead of dealing with values differing by thousands or millions, we're dealing with much smaller numbers.

This is called a **log transformation**.

You will use this when data is highly skewed.

For example:

- salary
- income
- population
- wealth
- transaction amounts
- scientific measurements

---

# 26. Why Log Transformations Are Useful

Imagine:

```text
Salary

30k
40k
50k
60k
70k
100k
1,000k
```

The $1 million value is far away from the others.

A log transformation compresses the scale:

```text
30k  → smaller log value
50k  → slightly larger
100k → larger
1M   → much less extreme
```

It doesn't magically remove information.

It changes the **scale**.

This can make some statistical/ML models behave better.

---

# 27. Cross-Entropy and Log Loss

Eventually, you'll encounter:

$$
-\log(p)
$$

in classification.

Suppose the correct class has predicted probability:

$$
p=0.9
$$

Then:

$$
-\ln(0.9)
$$

is relatively small.

But suppose the model confidently predicts the wrong thing:

$$
p=0.01
$$

Then:

$$
-\ln(0.01)
$$

is much larger.

So log loss effectively says:

> "If you are confidently wrong, you should be punished heavily."

This is why logarithms are central to classification.

We'll derive this properly later.

---

# 28. A Very Important Restriction

For ordinary real-valued logarithms:

$$
\log(0)
$$

is **not defined**.

Why?

There is no finite exponent \(x\) such that:

$$
10^x=0
$$

As \(x\) becomes increasingly negative:

$$
10^{-1}=0.1
$$

$$
10^{-2}=0.01
$$

$$
10^{-3}=0.001
$$

It gets closer and closer to zero but never reaches it.

So:

$$
\boxed{\log(0)\text{ is undefined}}
$$

Similarly, ordinary real logarithms of negative numbers are not defined.

For example:

$$
\log(-5)
$$

is not a real number.

---

# 29. Your Mental Map

You should now have this chain:

```text
MULTIPLICATION
      ↓
POWERS
      ↓
ROOTS
      ↓
EXPONENTIAL FUNCTIONS
      ↓
LOGARITHMS
```

And in ML:

```text
Powers
  ↓
x² → squared error → MSE

Exponentials
  ↓
eˣ
  ↓
sigmoid / softmax
  ↓
probabilities

Logarithms
  ↓
log transformations
  ↓
likelihood
  ↓
log-likelihood
  ↓
cross-entropy / log loss
  ↓
numerical stability
```

---

# 30. The One Story You Should Remember

Imagine a scientist studying a radioactive substance.

At first there are:

$$
N_0
$$

atoms.

The amount changes exponentially:

$$
N(t)=N_0e^{-\lambda t}
$$

Now you want to know:

> "How long has it been decaying?"

You need to **undo the exponential**.

What operation undoes exponentiation?

### Logarithm.

So logarithms let you turn:

$$
e^{-\lambda t}
$$

into something involving:

$$
\ln(N)
$$

This is the deep relationship:

> **Exponentials describe growth/decay.**
> **Logarithms help us reverse and analyze exponential behavior.**

That's why both appear constantly in physics, statistics and ML.

---

# 31. Practice — Don't Look at the Answers Immediately

### Q1

Calculate:

$$
2^5
$$

### Q2

Simplify:

$$
x^3x^4
$$

### Q3

Simplify:

$$
\frac{x^8}{x^3}
$$

### Q4

Calculate:

$$
(2^3)^2
$$

### Q5

Calculate:

$$
25^{1/2}
$$

### Q6

Calculate:

$$
27^{1/3}
$$

### Q7

Rewrite using a root:

$$
x^{1/2}
$$

### Q8

Find:

$$
\log_{10}(1000)
$$

### Q9

Find:

$$
\log_2(16)
$$

### Q10

Translate this into exponential form:

$$
\log_3(81)=4
$$

---

## Answers

<details>
<summary>Click to reveal</summary>

1. \(32\)

2. \(x^7\)

3. \(x^5\)

4. \(64\)

5. \(5\)

6. \(3\)

7. \(\sqrt{x}\)

8. \(3\)

9. \(4\)

10. \(3^4=81\)

</details>

---

# 🔑 Final Takeaways

If you remember only these things from today's lesson, remember these:

### Powers

$$
\boxed{a^n=\text{multiply }a\text{ by itself }n\text{ times}}
$$

### Roots

$$
\boxed{\sqrt[n]{x}=x^{1/n}}
$$

### Negative powers

$$
\boxed{x^{-n}=\frac1{x^n}}
$$

### Exponential

$$
\boxed{e^x}
$$

describes many natural growth/decay processes.

### Logarithm

$$
\boxed{\log_b(x)=y\iff b^y=x}
$$

A logarithm asks:

> **"What exponent produced this number?"**

### Natural log

$$
\boxed{\ln(x)=\log_e(x)}
$$

### ML connection

$$
\boxed{x^2\rightarrow\text{MSE}}
$$

$$
\boxed{e^x\rightarrow\text{sigmoid/softmax}}
$$

$$
\boxed{\log(x)\rightarrow\text{log transforms, likelihood, cross-entropy}}
$$

---

## Next lesson

**Lesson 5 — Algebra**

We'll build algebra from the ground up:

**expressions → equations → unknowns → rearranging equations → solving for variables → inequalities → ML formulas.**

And this will prepare you for the next major jump:

$$
\boxed{\text{Functions}}
$$

which is the mathematical language behind ML models.
