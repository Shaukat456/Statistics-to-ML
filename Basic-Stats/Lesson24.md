# Lesson 24 — Sampling Methods

We now know:

$$
\text{Population}\rightarrow\text{Sample}\rightarrow\text{Statistic}\rightarrow\text{Estimate}
$$

But there is a huge question:

> **How should we choose the sample?**

If we choose the wrong people, measurements, images, or experiments, even a very large dataset can give misleading results.

So today we learn **how samples are selected**.

---

# 1. Why Sampling Method Matters

Imagine a university has:

$$
10,000
$$

students.

You want to estimate their average daily study time.

You need a sample of:

$$
500
$$

students.

You could simply choose the first 500 students on a list.

But what if the list is ordered by department?

```text
Students 1–500 → Physics
Students 501–1000 → Computer Science
Students 1001–1500 → Mathematics
...
```

Then your "random-looking" sample might actually contain only Physics students.

Your sample is not representative of the entire university.

So:

$$
\boxed{\text{How you sample can affect what you conclude.}}
$$

---

# 2. The Four Important Sampling Methods

For our foundation, learn these four:

1. **Simple Random Sampling**
2. **Systematic Sampling**
3. **Stratified Sampling**
4. **Cluster Sampling**

We'll build each one from intuition.

---

# 3. Simple Random Sampling 🎲

This is the simplest idea.

Suppose we have:

```text
Population = 10,000 students
```

Assign every student a number:

```text
1, 2, 3, 4, ..., 10000
```

Then randomly select 500.

For example:

```text
137
829
1045
3912
...
```

Every student has a known chance of being selected.

That's **simple random sampling**.

### Mental model

Imagine putting everyone's name into a giant box:

📦

Shake it.

Randomly pick 500 names.

---

# 4. Why Randomness Helps

Suppose the university contains:

```text
Physics        20%
Computer Sci   30%
Engineering    25%
Mathematics    15%
Other          10%
```

A genuinely random sample will tend, on average, to contain roughly similar proportions.

Not exactly.

But approximately.

For example, a sample of 500 might contain:

```text
Physics        103
Computer Sci   147
Engineering    128
Mathematics     71
Other           51
```

That's reasonably representative.

---

# 5. Important: Random ≠ Perfect

This is a common misunderstanding.

Random sampling does **not** guarantee:

$$
\text{Sample}=\text{Population}
$$

Instead, it gives us a principled way of avoiding systematic selection.

A random sample can still, by chance, contain unusual proportions.

For example, suppose we randomly select 10 people.

We could accidentally select:

```text
8 Physics
1 Mathematics
1 Engineering
```

even if the population has very different proportions.

This is called **sampling variability**.

We'll study this deeply when we learn sampling distributions.

---

# 6. Systematic Sampling

Now imagine you have:

$$
10,000
$$

students listed in some order.

You want:

$$
1,000
$$

students.

Instead of randomly choosing every individual, you select every \(k\)-th person after choosing a random starting point.

For example:

$$
k=10
$$

Choose a random starting position:

$$
7
$$

Then select:

$$
7,17,27,37,47,\ldots
$$

This is **systematic sampling**.

---

# 7. Mental Model for Systematic Sampling

Imagine a long line of people:

```text
1  2  3  4  5  6  7  8  9  10  11  12  13...
                     ↑
                random start

                     ↓
7 → 17 → 27 → 37 → 47 → ...
```

You are essentially saying:

> "Start somewhere randomly, then take every 10th person."

---

# 8. When Can Systematic Sampling Go Wrong?

This is important.

Suppose your list has a hidden repeating pattern:

```text
A B A B A B A B A B ...
```

And your sampling interval is:

$$
k=2
$$

If you start at A:

```text
A → A → A → A → A
```

You might select only A.

You completely miss B.

So systematic sampling can be problematic when the ordering contains **periodicity** that interacts with the sampling interval.

---

# 9. Stratified Sampling

Now we encounter a very useful technique.

Suppose a population contains different groups.

For example:

```text
University
│
├── Physics
├── Chemistry
├── Computer Science
├── Mathematics
└── Engineering
```

These groups are called **strata**.

Instead of selecting from the whole population without considering groups, we divide the population into strata and sample from **each stratum**.

That's **stratified sampling**.

---

# 10. Example

Suppose our university has:

| Department  |   Students |
| ----------- | ---------: |
| Physics     |      2,000 |
| CS          |      3,000 |
| Engineering |      2,500 |
| Mathematics |      1,500 |
| Chemistry   |      1,000 |
| **Total**   | **10,000** |

Suppose we need a sample of:

$$
1,000
$$

We can sample proportionally.

Physics represents:

$$
\frac{2000}{10000}=20\%
$$

Therefore:

$$
2000\times10\%=200
$$

We select approximately 200 Physics students.

Similarly:

```text
Physics       → 200
CS            → 300
Engineering   → 250
Mathematics   → 150
Chemistry     → 100
```

Total:

$$
1000
$$

---

# 11. Why Stratification Is Useful

Suppose Physics students are only 2% of a huge population.

Pure random sampling might accidentally select very few Physics students.

If Physics is scientifically important, we may want to ensure that this group is represented.

Stratified sampling gives us explicit control over representation.

### Mental model:

> **Stratified sampling = divide into important groups, then sample within each group.**

---

# 12. Stratified vs Simple Random

This distinction is important.

### Simple random

```text
Population
████████████████████
        ↓
      random
        ↓
      Sample
```

### Stratified

```text
Population
│
├── Group A ──→ sample
├── Group B ──→ sample
├── Group C ──→ sample
└── Group D ──→ sample
```

The key difference:

> **Stratified sampling deliberately ensures representation from defined subgroups.**

---

# 13. Cluster Sampling

Now imagine something different.

Suppose Pakistan has thousands of schools.

You want to survey students.

It may be expensive to travel to hundreds of schools.

Instead, you randomly select:

```text
School A
School B
School C
School D
```

Then survey students within those selected schools.

This is **cluster sampling**.

The schools are the clusters.

---

# 14. Mental Model

Think of a city:

```text
🏫 School A
🏫 School B
🏫 School C
🏫 School D
🏫 School E
🏫 School F
...
```

Instead of randomly selecting individual students throughout the entire city, you randomly select some schools and collect data within those schools.

So:

> **Cluster sampling = select groups/clusters, then study units within selected clusters.**

---

# 15. Stratified vs Cluster — VERY IMPORTANT

These two are commonly confused.

### Stratified

You divide the population into groups and sample from **every group**.

```text
A → sample
B → sample
C → sample
D → sample
```

### Cluster

You divide the population into groups and select **some groups**.

```text
A → selected
B → not selected
C → selected
D → not selected
```

Then study observations within selected clusters.

### Memory trick

**Stratified:**

> "I want everyone represented."

**Cluster:**

> "I'll select some groups and work within them."

---

# 16. Real-World ML Example 🤖

Suppose you're building an autonomous-driving dataset.

Your population is conceptually:

> All driving situations the vehicle could encounter.

But you collect data from:

```text
Karachi
Lahore
Islamabad
Peshawar
Quetta
```

Suppose 90% of your data comes from sunny daytime driving.

Then your model might learn:

> "The world is mostly sunny."

But real driving includes:

- daytime
- nighttime
- rain
- fog
- traffic
- highways
- rural roads
- urban roads

Your dataset may be **biased toward certain conditions**.

---

# 17. Stratified Sampling for ML

Suppose your collected data has:

| Condition | Percentage |
| --------- | ---------: |
| Sunny     |        60% |
| Cloudy    |        20% |
| Rain      |        10% |
| Night     |        10% |

You could define strata based on conditions.

Then ensure that each important condition is represented in your sample.

This can be especially useful when rare conditions matter.

---

# 18. Physics Example 🔬

Suppose you're collecting experimental measurements.

Your population of possible measurements includes:

```text
Low temperature
Medium temperature
High temperature
```

If you only collect measurements at room temperature, your dataset doesn't represent the entire experimental regime.

You could stratify measurements by temperature range.

For example:

```text
0–10°C      → sample
10–20°C     → sample
20–30°C     → sample
30–40°C     → sample
```

This helps ensure coverage across the experimental domain.

---

# 19. Quantum Experiment Example ⚛️

Suppose you study photon waiting times.

You might collect:

$$
\tau_1,\tau_2,\tau_3,\ldots,\tau_n
$$

But perhaps the experiment is performed under different conditions:

```text
Condition A → low driving
Condition B → medium driving
Condition C → high driving
```

If you want to compare waiting-time behavior across these regimes, you need to ensure you actually collect enough measurements under each condition.

Otherwise, your sample may be dominated by one experimental regime.

---

# 20. Sampling Bias vs Sampling Variability

These are **not the same thing**.

### Sampling variability

Different random samples naturally produce different results.

For example:

```text
Sample 1 → mean = 49.8
Sample 2 → mean = 50.3
Sample 3 → mean = 49.6
Sample 4 → mean = 50.1
```

That's normal.

### Sampling bias

Your sampling procedure systematically favors certain observations.

For example:

> Surveying only people who visit a luxury shopping mall to estimate the income of the entire city.

That's a systematic problem.

---

# 21. A Powerful Distinction

Think:

### Variability

> "I got a different sample."

### Bias

> "My sampling process consistently pushes me in a particular direction."

This distinction becomes extremely important later when we study **estimators**.

---

# 22. Convenience Sampling

There's another method you should know.

Suppose you need 100 people and simply ask:

> "Whoever is available, please participate."

That's **convenience sampling**.

It's easy.

But it can introduce serious selection bias.

Example:

You want to study sleep patterns of university students.

You ask your closest 100 friends.

Your friends may have similar:

- schedules
- departments
- socioeconomic backgrounds
- lifestyles
- sleep patterns

So the sample may not represent the entire population.

---

# 23. The Sampling Hierarchy

Build this mental map:

```text
                    POPULATION
                        │
              How do we select?
                        │
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
     Random         Structured        Convenience
        │
   ┌────┼────┐
   ▼    ▼    ▼
Simple Systematic Stratified
Random
             │
          Cluster
```

The exact taxonomy can vary in statistical texts, but these are the main ideas you should recognize.

---

# 24. Why This Matters for Machine Learning

Imagine you have:

$$
1,000,000
$$

training images.

It sounds impressive.

But suppose:

```text
900,000 → daytime
80,000  → cloudy
15,000  → rain
5,000   → night
```

The dataset is huge.

Yet the model has relatively little exposure to nighttime conditions.

So:

$$
\boxed{\text{Large dataset} \neq \text{representative dataset}}
$$

This is one of the most important lessons in real-world ML.

---

# 25. The Connection to Generalization

Machine learning wants:

$$
\text{Good performance on unseen data}
$$

But your training data are only a sample from the real-world distribution.

Conceptually:

$$
\boxed{
\text{Real World}
\rightarrow
\text{Data Collection}
\rightarrow
\text{Sample}
\rightarrow
\text{Training}
\rightarrow
\text{Generalization}
}
$$

If the sample doesn't represent the situations encountered after deployment, generalization can suffer.

---

# 26. Sampling in Your Own Dataset Work

Suppose you have millions of frames from vehicle recordings.

You could simply take:

```text
first 100,000 frames
```

But imagine those frames come from only:

```text
one route
one time period
one weather condition
```

You could instead consider sampling across:

- different routes
- different times
- different weather
- different traffic densities
- different scenes
- different cameras/sensors
- different driving conditions

The goal is to make your dataset cover the relevant variability of the deployment environment.

---

# 27. The Deep Statistical Idea

Sampling isn't just:

> "Take fewer data."

It is:

> **Construct a smaller collection of observations that allows us to learn about a larger population.**

That distinction is crucial.

---

# 28. Practice 🧠

### Q1

You have 100,000 students and randomly choose 1,000 students.

What sampling method?

---

### Q2

You select every 20th student after randomly choosing the first student.

What method?

---

### Q3

You divide students into:

```text
Physics
CS
Engineering
Mathematics
```

and sample from **each department**.

What method?

---

### Q4

You randomly select 10 schools and survey students within those schools.

What method?

---

### Q5

You ask your 100 closest friends to participate.

What type of sampling is this?

---

### Q6

A dataset contains 1 million images, but 95% are daytime images.

Is the dataset necessarily representative?

---

# Answers

**Q1:** Simple random sampling.

**Q2:** Systematic sampling.

**Q3:** Stratified sampling.

**Q4:** Cluster sampling.

**Q5:** Convenience sampling.

**Q6:** No. Dataset size alone doesn't guarantee representativeness.

---

# 🔥 Lesson Summary

Let's connect everything we've learned:

$$
\boxed{\text{Population}}
$$

is the complete group we're interested in.

Because measuring the whole population is often impractical, we take:

$$
\boxed{\text{Sample}}
$$

We calculate:

$$
\boxed{\text{Statistic}}
$$

from the sample and use it to estimate:

$$
\boxed{\text{Population Parameter}}
$$

But the quality of that estimate depends partly on **how the sample was obtained**.

The major sampling ideas are:

$$
\boxed{
\text{Simple Random}
\rightarrow
\text{Systematic}
\rightarrow
\text{Stratified}
\rightarrow
\text{Cluster}
}
$$

And always distinguish:

$$
\boxed{\text{Sampling variability}\neq\text{Sampling bias}}
$$

Variability means different samples naturally give different answers. Bias means the sampling process systematically favors certain observations.

### 🧠 The complete mental picture so far

> **The real world is the population. We usually cannot observe everything, so we collect a sample. Different samples can produce different statistics, and the way we select the sample can introduce bias. We use sample statistics such as \(\bar{x}\) and \(s^2\) to estimate population parameters such as \(\mu\) and \(\sigma^2\). In ML, the same idea appears when we collect a finite dataset from a much larger real-world distribution. A huge dataset can still be unrepresentative if it misses important conditions. In physics and quantum experiments, repeated measurements are likewise finite samples from an underlying probabilistic process.**

---

## Next: Sampling Distribution

Now we are ready for a **major conceptual jump**:

> If we repeatedly take samples, and every sample gives us a different mean, **what is the probability distribution of those sample means?**

That leads directly to:

$$
\boxed{\text{Sampling Distribution}}
$$

and eventually to one of the most important ideas in statistics:

$$
\boxed{\text{Central Limit Theorem (CLT)}}
$$
