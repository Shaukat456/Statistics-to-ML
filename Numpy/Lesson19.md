# Lesson 19 — IQR & Outlier Detection

In the previous lesson, we learned:

$$
Q_1=P_{25}
$$

$$
Q_2=P_{50}=\text{Median}
$$

$$
Q_3=P_{75}
$$

Now we're going to answer a very important question:

> **How spread out is the middle part of our data, and which values look unusually far away?**

This leads us to **IQR — Interquartile Range**.

---

# 1. First: Why Do We Need IQR?

Suppose we have:

$$
[10,11,12,13,14,15,16,100]
$$

Clearly, `100` looks very different from the other values.

But let's think about our previous statistics.

### Mean

$$
\bar{x}=\frac{10+11+12+13+14+15+16+100}{8}
$$

$$
\bar{x}=23.875
$$

The mean is pulled upward by 100.

### Range

$$
100-10=90
$$

The range tells us the total spread, but it doesn't tell us much about where the **main body of the data** is.

We need something more robust.

That's where IQR comes in.

---

# 2. What Does "Interquartile" Mean?

Break the word apart:

**Inter + Quartile**

"Inter" = between.

"Quartile" = quarters.

So:

> **Interquartile Range = the range between the first and third quartiles.**

We already know:

$$
Q_1=P_{25}
$$

and:

$$
Q_3=P_{75}
$$

Therefore:

$$
\boxed{IQR=Q_3-Q_1}
$$

That's the entire formula.

But understanding **why** it works is more important than memorizing it.

---

# 3. The Middle 50%

Remember our quartile diagram:

```text
0%          25%          50%          75%          100%
|------------|------------|------------|-------------|
             Q1           Q2           Q3
```

Everything between:

$$
Q_1
$$

and:

$$
Q_3
$$

contains approximately the **middle 50% of observations**.

```text
             MIDDLE 50%
        <------------------->
        Q1                 Q3
        │                   │
--------|-------------------|--------
       25%                 75%
```

Therefore:

$$
\boxed{IQR=\text{spread of the middle 50%}}
$$

This is the key idea.

---

# 4. Example

Consider:

$$
X=[10,20,30,40,50,60,70,80,90]
$$

Suppose:

$$
Q_1=25
$$

and:

$$
Q_3=75
$$

Then:

$$
IQR=Q_3-Q_1
$$

$$
IQR=75-25
$$

$$
\boxed{IQR=50}
$$

So the middle 50% of the data spans **50 units**.

---

# 5. Why Is IQR Useful?

Compare two datasets.

### Dataset A

$$
[10,20,30,40,50,60,70]
$$

### Dataset B

$$
[10,20,30,40,50,60,700]
$$

The last value in B is huge.

The **range** changes dramatically.

But IQR focuses on the middle portion.

That's its major advantage:

> **IQR is much less affected by extreme values than range.**

This makes it useful when data contains outliers.

---

# 6. Mean vs Median vs IQR

We now have several ways to describe data.

### Mean

Tells us:

> Where is the average?

### Median

Tells us:

> Where is the middle?

### Range

Tells us:

> How far apart are the minimum and maximum?

### IQR

Tells us:

> How spread out is the middle 50%?

This gives us a much richer description.

---

# 7. The Box Plot Connection

You've probably seen something like this:

```text
       ┌───────────────┐
───────│               │───────
       │      │        │
       │      │        │
       └───────────────┘
```

This is the basic idea of a **box plot**.

The box represents:

$$
Q_1 \rightarrow Q_3
$$

So:

> **The box represents the middle 50% of the data.**

The line inside the box represents:

$$
Q_2=\text{Median}
$$

Conceptually:

```text
             Q1       Q2       Q3
              │        │        │
              ↓        ↓        ↓
──────────────┌────────┬────────┐──────────────
              │        │        │
              │        │        │
              └────────┴────────┘
              <---------------->
                     IQR
```

We'll later study box plots more visually when we get deeper into EDA.

---

# 8. Now: What Is an Outlier?

An **outlier** is an observation that is unusually far from the main body of the data.

For example:

$$
[10,11,12,13,14,15,16,100]
$$

`100` appears unusual compared with the rest.

But there is an important statistical principle:

> **"Unusual" does not automatically mean "wrong."**

An outlier might be:

- a measurement error
- a data-entry error
- a rare but real event
- an unusual customer
- a genuine scientific observation
- a sensor failure
- a real extreme physical event.

So we should **detect** outliers before deciding what they mean.

---

# 9. The IQR Outlier Rule

A common rule uses:

$$
1.5\times IQR
$$

We calculate two boundaries.

### Lower fence

$$
\boxed{Q_1-1.5(IQR)}
$$

### Upper fence

$$
\boxed{Q_3+1.5(IQR)}
$$

Values below the lower fence or above the upper fence are commonly flagged as **potential outliers**.

Notice the word:

> **potential**

This is important.

The rule is a detection heuristic, not proof that a data point is erroneous.

---

# 10. Let's Do a Complete Example

Consider:

$$
X=[10,20,30,40,50,60,70,80,100]
$$

Suppose our quartiles are:

$$
Q_1=30
$$

$$
Q_3=80
$$

Therefore:

$$
IQR=Q_3-Q_1
$$

$$
IQR=80-30
$$

$$
\boxed{IQR=50}
$$

---

# 11. Calculate the Lower Fence

Formula:

$$
Q_1-1.5(IQR)
$$

Substitute:

$$
30-1.5(50)
$$

$$
30-75
$$

$$
\boxed{-45}
$$

So the lower fence is:

$$
-45
$$

---

# 12. Calculate the Upper Fence

Formula:

$$
Q_3+1.5(IQR)
$$

Substitute:

$$
80+1.5(50)
$$

$$
80+75
$$

$$
\boxed{155}
$$

So:

$$
\text{Upper fence}=155
$$

Our data ranges from:

$$
10\rightarrow100
$$

Everything is between:

$$
-45\rightarrow155
$$

Therefore, according to this rule:

> There are no potential outliers.

---

# 13. Let's Add a Huge Value

Now consider:

$$
X=[10,20,30,40,50,60,70,80,300]
$$

Assume:

$$
Q_1=30
$$

$$
Q_3=80
$$

Then:

$$
IQR=50
$$

Lower fence:

$$
-45
$$

Upper fence:

$$
155
$$

But:

$$
300>155
$$

Therefore:

$$
\boxed{300\text{ is flagged as a potential outlier}}
$$

---

# 14. Visualize It

```text
Lower fence                         Upper fence
    ↓                                    ↓
----|------------------------------------|------------------→
    -45                                  155              300
                                                         ↑
                                                   potential
                                                    outlier
```

The main data is inside the fences.

The extreme value is outside.

---

# 15. Why 1.5?

You might ask:

> Why exactly 1.5?

It is a conventional statistical rule used for identifying potential outliers in box-plot style analysis.

It is **not a universal law of nature**.

Different situations may call for different methods.

For example, in scientific data, an extreme value may be physically meaningful even if it falls outside the 1.5-IQR fences.

So don't think:

$$
\text{outside fence}=\text{bad data}
$$

Instead think:

$$
\boxed{\text{outside fence}=\text{investigate this value}}
$$

That's a much better mental model.

---

# 16. Real-World ML Example

Imagine you're building a model to predict house prices.

Your dataset contains:

```text
House Size (m²)

80
90
100
110
120
130
140
150
5000
```

`5000` might be:

- a mansion
- a typo
- wrong unit
- corrupted data
- a legitimate but rare property.

If you automatically delete it, you might destroy useful information.

Instead:

```text
Detect outlier
      ↓
Investigate
      ↓
Understand why it exists
      ↓
Decide how to handle it
```

This is an important ML workflow.

---

# 17. Outlier Detection Is NOT Outlier Removal

These are different tasks.

### Detection

Ask:

> "Which observations look unusual?"

### Handling

Ask:

> "What should I do with them?"

Possible actions include:

- keep them
- correct them
- remove them
- cap/winsorize them
- transform the feature
- use a robust model
- investigate the data source.

The correct choice depends on the reason for the outlier.

---

# 18. Why Outliers Matter in ML

Outliers can affect some algorithms and statistics strongly.

For example, remember:

$$
\bar{x}
$$

the mean.

Extreme values can pull the mean significantly.

Also consider squared errors:

$$
(y-\hat y)^2
$$

A large error becomes **much larger** after squaring.

For example:

$$
2^2=4
$$

but:

$$
20^2=400
$$

Therefore, extreme observations can have a large effect on some ML objectives such as:

$$
MSE=\frac1n\sum_{i=1}^{n}(y_i-\hat y_i)^2.
$$

We'll study this deeply later.

---

# 19. IQR vs Standard Deviation

You already learned standard deviation.

So now you might ask:

> Why not just use standard deviation to detect unusual values?

Because they behave differently.

### Standard deviation

Measures overall spread around the mean:

$$
\sigma=\sqrt{\frac1N\sum_{i=1}^{N}(x_i-\mu)^2}
$$

Because deviations are squared, extreme values can strongly influence it.

### IQR

Uses:

$$
Q_3-Q_1
$$

and focuses on the middle 50%.

Therefore:

> **IQR is generally more robust to extreme observations.**

This is why median + IQR is often called a **robust** way of summarizing data.

---

# 20. Mean + Standard Deviation vs Median + IQR

Think of two different teams:

### Team A

Uses:

$$
\text{Mean + Standard Deviation}
$$

Good when distributions and assumptions make these summaries appropriate.

### Team B

Uses:

$$
\text{Median + IQR}
$$

Useful when data is skewed or contains extreme values.

Neither pair is universally "better."

The choice depends on the data and the question.

---

# 21. Example: Income Data

Suppose annual incomes are:

$$
[30k,32k,35k,37k,40k,42k,45k,48k,50k,2M]
$$

The $2M income is legitimate but extremely large.

The mean will be strongly affected.

The median is much more stable.

Similarly, IQR describes the spread of the central portion without being dominated by the $2M observation.

This is one reason salary/income data is often analyzed with:

$$
\text{Median + Quartiles + IQR}
$$

rather than relying only on the mean.

---

# 22. Physics / Scientific Computing Example

Suppose you're measuring a sensor:

$$
A=[1.01,1.03,1.02,1.01,1.04,1.02,1.03,10.5]
$$

The `10.5` reading might be:

- a sensor glitch,
- electromagnetic interference,
- a real physical event,
- an experimental anomaly.

IQR can flag it as unusual.

But:

> **You should not automatically delete it.**

In scientific computing, an "outlier" can sometimes be the most interesting observation.

This is a very important scientific mindset.

---

# 23. Quantum Experiment Connection

Suppose you're collecting photon arrival times:

$$
t_1,t_2,\ldots,t_n
$$

Most arrival intervals might cluster around some region, but occasionally you get an unusually large interval.

An IQR-based method could flag it as unusual.

But in a quantum experiment, that unusual observation might contain information about:

- detector behavior
- experimental noise
- physical processes
- correlations
- rare events.

So statistical detection is the beginning of investigation, not the end.

---

# 24. A Powerful Mental Model

Think of IQR as a **fence around the main neighborhood of your data**.

```text
             MAIN DATA
        ┌─────────────────┐
        │                 │
--------│-----------------│--------
       Q1                Q3
        <----- IQR ----->
```

Then extend the fence by:

$$
1.5\times IQR
$$

```text
Fence                                  Fence
 ↓                                       ↓
|----------------[ MAIN DATA ]-----------|
                                       •
                                       ↑
                                  unusual point
```

So:

> **IQR describes the neighborhood.**

> **1.5 × IQR creates an investigation boundary.**

---

# 25. One Complete Mental Map

You have now built a very useful statistical toolkit:

```text
                     DATA
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
        CENTER        SPREAD       POSITION
          │            │            │
       Mean/Median   Range/IQR    Percentiles
          │            │            │
          │            │       Q1 / Q2 / Q3
          │            │            │
          └────────────┼────────────┘
                       ↓
                OUTLIER DETECTION
                       │
                       ↓
                Investigate unusual
                    observations
```

---

# 26. The Formulas You Should Know

### First quartile

$$
\boxed{Q_1=P_{25}}
$$

### Second quartile

$$
\boxed{Q_2=P_{50}=\text{Median}}
$$

### Third quartile

$$
\boxed{Q_3=P_{75}}
$$

### Interquartile range

$$
\boxed{IQR=Q_3-Q_1}
$$

### Lower fence

$$
\boxed{Q_1-1.5(IQR)}
$$

### Upper fence

$$
\boxed{Q_3+1.5(IQR)}
$$

Potential outlier if:

$$
x<Q_1-1.5(IQR)
$$

or:

$$
x>Q_3+1.5(IQR)
$$

---

# 27. NumPy Preview

Eventually, NumPy will make this extremely easy:

```python
import numpy as np

x = np.array([10, 20, 30, 40, 50, 60, 70, 80, 300])

Q1 = np.percentile(x, 25)
Q2 = np.percentile(x, 50)
Q3 = np.percentile(x, 75)

IQR = Q3 - Q1
```

Then:

```python
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
```

And we can find potential outliers.

But again:

> **The NumPy code is simply implementing the statistics you now understand.**

---

# 28. Practice

Try these before looking at the answers.

### Q1

What does IQR measure?

---

### Q2

Write the formula for IQR.

---

### Q3

If:

$$
Q_1=20,\quad Q_3=80
$$

what is the IQR?

---

### Q4

If:

$$
Q_1=20,\quad IQR=60
$$

what is the lower fence?

---

### Q5

If:

$$
Q_3=80,\quad IQR=60
$$

what is the upper fence?

---

### Q6

If the upper fence is 170 and an observation is 200, what does the IQR rule tell you?

---

### Q7

True or false:

> Every observation outside the IQR fences is definitely an error.

---

### Q8

Why is IQR generally less affected by extreme values than range?

---

### Q9

Which describes the middle 50% of observations?

A. Range
B. IQR
C. Mean
D. Mode

---

### Q10

Suppose a sensor produces:

$$
[10,11,10,12,11,10,1000]
$$

Should you automatically delete 1000 just because it may be an outlier?

---

# Answers

### Q1

The spread of the middle 50% of the data.

### Q2

$$
\boxed{IQR=Q_3-Q_1}
$$

### Q3

$$
IQR=80-20=60
$$

### Q4

$$
20-1.5(60)
$$

$$
20-90=-70
$$

### Q5

$$
80+1.5(60)
$$

$$
80+90=170
$$

### Q6

It is flagged as a **potential outlier** because:

$$
200>170
$$

### Q7

**False.**

It should be investigated, not automatically declared erroneous.

### Q8

Because IQR focuses on the central 50% rather than using the minimum and maximum.

### Q9

$$
\boxed{B.\ IQR}
$$

### Q10

**No.**

First investigate why the value is 1000.

---

# 🧠 The One-Minute Memory Trick

Remember this story:

> **Quartiles divide the data into four parts.**

$$
Q_1\quad Q_2\quad Q_3
$$

Then:

> **IQR measures the middle half.**

$$
IQR=Q_3-Q_1
$$

Then:

> **1.5 × IQR builds fences.**

$$
Q_1-1.5IQR
$$

and

$$
Q_3+1.5IQR
$$

Then:

> **Outside the fence = investigate, not automatically delete.**

---

## Where We Are Now

Your statistics foundation has progressed from:

$$
\boxed{\text{Data}}
$$

→

$$
\boxed{\text{Random Variables}}
$$

→

$$
\boxed{\text{Probability Distributions}}
$$

→

$$
\boxed{\text{Mean / Median / Mode}}
$$

→

$$
\boxed{\text{Percentiles / Quartiles}}
$$

→

$$
\boxed{\text{IQR / Outlier Detection}}
$$

The next important concept is **Distribution Shape**: understanding **symmetric, skewed, left-skewed, right-skewed, and multimodal distributions**. This will connect everything we've learned so far and prepare you for **correlation, covariance, and real EDA**.
