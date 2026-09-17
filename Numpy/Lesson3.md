# Foundation 3 — Fractions, Ratios, Percentages & Proportions

This is an **important foundation for ML**.

At first glance, fractions and percentages look like school mathematics. But later you'll see the same ideas inside:

- normalization
- standardization
- probability
- classification metrics
- feature engineering
- error calculations
- loss functions
- dataset analysis

So let's build the intuition first.

---

# 1. The basic idea: comparing quantities

Imagine you have **10 apples** 🍎.

You give **3 apples** to your friend.

How many apples did you give **relative to the total**?

You gave:

$$
\frac{3}{10}
$$

This is a **fraction**.

We can also write:

$$
0.3
$$

or:

$$
30\%
$$

These three representations describe the same quantity:

$$
\boxed{\frac{3}{10}=0.3=30\%}
$$

---

# 2. What does a fraction actually mean?

Consider:

$$
\frac{3}{10}
$$

Think of the 10 as the **whole**.

```text
Whole = 10 apples

🍎 🍎 🍎 🍎 🍎 🍎 🍎 🍎 🍎 🍎
│──────────────│
      3
```

The numerator tells us:

> **How many parts we have**

The denominator tells us:

> **How many equal parts make up the whole**

So:

$$
\frac{\text{part}}{\text{whole}}
$$

is one of the most useful mental models in statistics.

---

# 3. Fraction → decimal

To convert:

$$
\frac{3}{10}
$$

to a decimal, divide:

$$
3\div10=0.3
$$

Another example:

$$
\frac{1}{4}=1\div4=0.25
$$

And:

$$
\frac{3}{4}=0.75
$$

---

# 4. Decimal → percentage

Multiply the decimal by 100:

$$
0.3\times100=30\%
$$

Therefore:

$$
0.3=30\%
$$

Another example:

$$
0.75\times100=75\%
$$

So:

$$
\boxed{0.75=75\%}
$$

---

# 5. Real-world ML example: accuracy

Suppose an ML model makes predictions for 100 images.

It correctly identifies 90.

Then:

$$
\text{Accuracy}
=
\frac{\text{correct predictions}}
{\text{total predictions}}
$$

Therefore:

$$
\text{Accuracy}
=
\frac{90}{100}
$$

$$
=0.90
$$

or:

$$
\boxed{90\%}
$$

So when you later see:

> **Model accuracy = 90%**

you should mentally understand:

> "The model got 90 out of every 100 examples correct."

Not just:

> "90% is a number."

---

# 6. Ratio

A **ratio** compares quantities.

Suppose a dataset contains:

- 80 cats
- 20 dogs

The ratio of cats to dogs is:

$$
80:20
$$

We can simplify it by dividing both by 20:

$$
4:1
$$

So there are:

> **4 cats for every 1 dog.**

---

# 7. Ratio vs fraction

This distinction is important.

Suppose:

```text
Cats = 80
Dogs = 20
Total = 100
```

### Ratio of cats to dogs

$$
80:20=4:1
$$

### Fraction of cats in the dataset

$$
\frac{80}{100}=0.8
$$

### Percentage of cats

$$
80\%
$$

They're related, but they're answering different questions.

| Question                  | Calculation |
| ------------------------- | ----------- |
| Cats compared with dogs?  | \(80:20\)   |
| What fraction are cats?   | \(80/100\)  |
| What percentage are cats? | \(80\%\)    |

---

# 8. Why this matters in ML: class imbalance

Suppose you're building an ML model to detect a disease from medical images.

Your dataset contains:

```text
Healthy = 9,500
Disease = 500
```

Total:

$$
10,000
$$

Disease percentage:

$$
\frac{500}{10000}=0.05
$$

Therefore:

$$
5\%
$$

So:

```text
Healthy → 95%
Disease → 5%
```

This is called **class imbalance**.

Why is it important?

Imagine a terrible model that always says:

> "Healthy."

It gets:

$$
9500/10000=95\%
$$

accuracy.

It appears to be **95% accurate**!

But it detects:

$$
0
$$

of the 500 disease cases.

This is why understanding proportions becomes extremely important when we later study:

- precision
- recall
- F1-score
- confusion matrices
- imbalanced datasets

---

# 9. Percent change

Now suppose a model takes:

$$
10\text{ seconds}
$$

to process an image.

After optimization:

$$
8\text{ seconds}
$$

How much did the processing time decrease?

First find the difference:

$$
10-8=2
$$

Then compare the difference with the **original** value:

$$
\frac{2}{10}=0.2
$$

Convert to percentage:

$$
0.2\times100=20\%
$$

So the processing time decreased by:

$$
\boxed{20\%}
$$

---

# 10. The golden rule of percentage change

When calculating percentage change:

$$
\boxed{
\text{Percentage Change}
=
\frac{\text{New}-\text{Old}}
{\text{Old}}
\times100
}
$$

For an increase:

$$
\frac{\text{New}-\text{Old}}{\text{Old}}\times100
$$

For a decrease:

$$
\frac{\text{Old}-\text{New}}{\text{Old}}\times100
$$

### Example

Accuracy goes from:

$$
80\%\rightarrow88\%
$$

Difference:

$$
88-80=8
$$

Relative improvement:

$$
\frac{8}{80}\times100=10\%
$$

Notice something subtle:

The accuracy increased by **8 percentage points**, but the **relative increase** is **10%**.

These are not the same thing.

---

# 11. Proportion

A **proportion** tells us how much of something belongs to the whole.

Suppose:

```text
1000 training samples
200 validation samples
```

The validation proportion is:

$$
\frac{200}{1000}=0.2
$$

or:

$$
20\%
$$

This is exactly the type of thinking you'll use when splitting datasets.

For example:

```text
Dataset
│
├── Training → 80%
│
└── Validation → 20%
```

Later, you'll learn why we split data this way and why the **test set must remain unseen**.

---

# 12. A very useful concept: "per"

Now let's introduce another idea.

Suppose a car travels:

$$
300\text{ km}
$$

using:

$$
20\text{ liters}
$$

We can calculate:

$$
\frac{300}{20}=15
$$

So:

$$
15\text{ km/liter}
$$

This means:

> For every 1 liter of fuel, the car travels approximately 15 km.

The word **"per"** often means division.

Examples:

$$
\frac{\text{distance}}{\text{time}}
=
\text{speed}
$$

$$
\frac{\text{cost}}{\text{item}}
=
\text{cost per item}
$$

$$
\frac{\text{errors}}{\text{total predictions}}
=
\text{error proportion}
$$

This "part relative to something" idea appears everywhere in statistics.

---

# 13. ML example: error rate

Suppose our model makes:

$$
25
$$

incorrect predictions out of:

$$
500
$$

predictions.

Error rate:

$$
\frac{25}{500}
$$

$$
=0.05
$$

$$
=5\%
$$

Since accuracy and error rate complement each other:

$$
\text{Accuracy}+\text{Error Rate}=100\%
$$

So:

$$
95\%+5\%=100\%
$$

This is a simple example of how proportions help us understand model performance.

---

# 14. Proportions and scaling

Now we're approaching something **very important for ML**.

Suppose two students have:

```text
Student A:
Exam score = 80/100

Student B:
Exam score = 8/10
```

Are these performances different?

No.

Convert both to proportions:

Student A:

$$
\frac{80}{100}=0.8
$$

Student B:

$$
\frac{8}{10}=0.8
$$

Therefore:

$$
\boxed{80/100=8/10}
$$

The representation changed.

The underlying proportion didn't.

This idea of representing values on a comparable scale will eventually lead us to **normalization and standardization**.

---

# 15. A bridge toward normalization

Suppose one ML feature is:

$$
\text{Age}=20\text{ to }60
$$

and another is:

$$
\text{Salary}=20,000\text{ to }2,000,000
$$

The numerical scales are very different.

One common transformation is **min-max normalization**:

$$
x'=
\frac{x-x_{\min}}
{x_{\max}-x_{\min}}
$$

Don't worry about understanding the entire formula yet.

Just look at its structure:

$$
\frac{\text{position relative to minimum}}
{\text{total range}}
$$

It essentially asks:

> **"Where does this value sit between the minimum and maximum?"**

For example, if:

$$
x_{\min}=0
$$

$$
x_{\max}=100
$$

and:

$$
x=70
$$

then:

$$
x'=\frac{70-0}{100-0}
$$

$$
=0.7
$$

So 70 becomes:

$$
\boxed{0.7}
$$

This is a beautiful example of a basic mathematical idea eventually becoming an ML preprocessing technique.

**We will study normalization properly later.**

---

# 16. Another analogy: Pizza 🍕

Imagine a pizza divided into 8 equal slices.

You eat 2.

You ate:

$$
\frac{2}{8}
$$

Simplify:

$$
\frac{1}{4}
$$

Decimal:

$$
0.25
$$

Percentage:

$$
25\%
$$

So:

```text
2 slices out of 8
        ↓
      2/8
        ↓
      1/4
        ↓
      0.25
        ↓
       25%
```

These aren't four different quantities.

They're **four ways of representing the same quantity**.

---

# 17. Why statistics needs this foundation

Statistics constantly asks questions like:

> "How common is this?"

> "How much larger is this?"

> "What fraction of the observations have this property?"

> "What percentage belongs to this category?"

> "How does this value compare with the rest?"

Those questions naturally produce:

$$
\frac{\text{part}}{\text{whole}}
$$

and:

$$
\frac{\text{difference}}{\text{reference}}
$$

This is why fractions and ratios are foundational.

---

# 🧠 Your mental model

Remember:

```text
                COMPARING QUANTITIES
                         │
            ┌────────────┼────────────┐
            ↓            ↓            ↓
         Fraction       Ratio      Percentage
            │            │            │
        part/whole    A compared    fraction ×100
                         with B
            │
            ↓
        PROPORTION
            │
            ↓
   ┌────────┴─────────┐
   ↓                  ↓
Statistics            ML
   │                  │
   ↓                  ↓
distributions      accuracy
sampling           error rate
probability        class imbalance
                    normalization
                    metrics
```

---

# 🧪 Practice — Think before calculating

### Q1

There are 20 students and 5 failed.

What fraction failed?

---

### Q2

Convert your answer from Q1 into a percentage.

---

### Q3

A model correctly classifies 180 images out of 200.

What is its accuracy?

---

### Q4

A dataset has:

$$
900\text{ cats}
$$

and:

$$
100\text{ dogs}
$$

What is the ratio of cats to dogs?

---

### Q5

What percentage of the dataset is dogs?

---

### Q6 — ML thinking

A dataset contains:

$$
9,000
$$

normal samples and:

$$
1,000
$$

anomalous samples.

A model always predicts **normal**.

What accuracy would it achieve?

And why could that accuracy be misleading?

---

### Q7 — Percentage change

A model's inference time decreases from:

$$
50\text{ ms}
$$

to:

$$
40\text{ ms}
$$

What is the percentage decrease?

---

## 🔑 The one idea I want you to remember

Whenever you see:

$$
\frac{A}{B}
$$

ask yourself:

> **"What is A relative to B?"**

That single question will make a lot of statistics much easier.

For example:

$$
\frac{\text{correct}}{\text{total}}
$$

→ accuracy

$$
\frac{\text{failed}}{\text{total}}
$$

→ failure proportion

$$
\frac{\text{difference}}{\text{original}}
$$

→ relative change

$$
\frac{\text{part}}{\text{whole}}
$$

→ proportion

---

### 🛑 Stop here.

We are **not touching NumPy yet**.

Next foundation topic will be **Powers, Roots, Exponents & Logarithms**. This is particularly important for ML because logarithms later appear in **log transformations, probability, likelihood, cross-entropy, information theory, and numerical stability**.
