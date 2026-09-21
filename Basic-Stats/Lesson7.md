# Lesson 7 — Coordinates & Graphs 📍📈

We now move from **functions** to **visualizing functions**.

So far:

> **Data → Variables → Algebra → Functions**

Now:

> **Functions → Coordinates → Graphs → Visual understanding**

This is extremely important for ML because a lot of machine learning begins with **looking at data on a graph**.

---

# 1. Why Do We Need Coordinates?

Imagine I tell you:

> “The student is somewhere in the classroom.”

Not very useful.

Instead:

> “The student is 3 meters from the left wall and 2 meters from the front wall.”

Now you can locate them precisely.

**Coordinates are a mathematical system for describing location.**

The same idea works for data.

For example:

| Study Hours | Exam Score |
| ----------: | ---------: |
|           1 |         50 |
|           2 |         58 |
|           3 |         65 |
|           4 |         73 |
|           5 |         82 |

We could describe each student using two coordinates:

$$
(1,50)
$$

$$
(2,58)
$$

$$
(3,65)
$$

etc.

And then **plot those points on a graph**.

That's where mathematics becomes visual.

---

# 2. The Number Line

Let's start with one dimension.

```text
← negative                    positive →
───────|───────|───────|───────|───────|───────
      -2      -1       0       1       2       3
```

The center is:

$$
0
$$

Numbers to the right are positive.

Numbers to the left are negative.

For example:

$$
3
$$

is three units to the right of zero.

And:

$$
-3
$$

is three units to the left.

### Mental model 🧠

Think of a number line as a **road**.

Zero is your starting point.

- Walk right → positive
- Walk left → negative

---

# 3. From One Dimension to Two Dimensions

A number line only tells us one thing:

> How far left or right?

But what if we also need:

> How far up or down?

We add another number line perpendicular to the first.

This creates the **Cartesian coordinate system**.

```text
                 y
                 ↑
                 |
                 |
                 |
←────────────────┼────────────────→ x
                 |
                 |
                 |
                 ↓
```

There are two axes.

### x-axis

The horizontal axis.

```text
←────────────── x ──────────────→
```

### y-axis

The vertical axis.

```text
       ↑ y
       |
       |
       |
       |
```

And where they meet:

$$
(0,0)
$$

is called the **origin**.

---

# 4. What Is \((x,y)\)?

A point is usually written as:

$$
(x,y)
$$

The first number tells us:

> Move left/right.

The second tells us:

> Move up/down.

For example:

$$
(3,2)
$$

means:

1. Move 3 units right.
2. Move 2 units up.

---

# 5. Order Matters!

This is VERY important.

$$
(3,2)
$$

is not the same as:

$$
(2,3)
$$

Think:

> **First x, then y.**

A useful memory trick:

### "Walk first, climb second."

- \(x\) → walk horizontally
- \(y\) → climb vertically

So:

$$
(x,y)
$$

means:

> **horizontal → vertical**

---

# 6. Positive and Negative Coordinates

Consider:

$$
(3,2)
$$

Both are positive.

So we go:

- right
- up

Now:

$$
(-3,2)
$$

means:

- left
- up

And:

$$
(-3,-2)
$$

means:

- left
- down

And:

$$
(3,-2)
$$

means:

- right
- down

---

# 7. The Four Quadrants

The coordinate plane is divided into four regions.

```text
                    y
                    ↑
             II     |      I
                    |
                    |
      ──────────────┼──────────────→ x
                    |
             III    |      IV
                    |
```

### Quadrant I

$$
(+,+)
$$

Both positive.

Example:

$$
(3,4)
$$

### Quadrant II

$$
(-,+)
$$

Example:

$$
(-3,4)
$$

### Quadrant III

$$
(-,-)
$$

Example:

$$
(-3,-4)
$$

### Quadrant IV

$$
(+,-)
$$

Example:

$$
(3,-4)
$$

### Memory trick 🧠

Starting from the top-right and moving counterclockwise:

> **I → II → III → IV**

---

# 8. Let's Plot Some Points

Suppose we have:

$$
A=(2,3)
$$

Start at the origin.

Move:

$$
2
$$

to the right.

Then:

$$
3
$$

up.

You reach point \(A\).

---

Another:

$$
B=(-4,2)
$$

Move:

- 4 left
- 2 up

---

Another:

$$
C=(3,-2)
$$

Move:

- 3 right
- 2 down

---

# 9. Coordinates Can Represent Data

This is where things become interesting for ML.

Suppose:

| Student | Study Hours | Exam Score |
| ------- | ----------: | ---------: |
| A       |           1 |         50 |
| B       |           2 |         58 |
| C       |           3 |         65 |
| D       |           4 |         73 |
| E       |           5 |         82 |

We can convert these into coordinates:

$$
(1,50)
$$

$$
(2,58)
$$

$$
(3,65)
$$

$$
(4,73)
$$

$$
(5,82)
$$

Now each student becomes a **point**.

This is called a **scatter plot**.

Conceptually:

```text
Score
 90 |
 80 |                    ●
 70 |              ●
 60 |        ●
 50 |  ●
    |
    +-------------------------
       1    2    3    4    5
             Study Hours
```

Now you can visually see something:

> As study hours increase, scores tend to increase.

That's a **relationship between variables**.

And ML is extremely interested in discovering such relationships.

---

# 10. Why Graphs Matter in Machine Learning

Imagine you have 100,000 rows of data.

Looking at:

```text
3.2, 71
4.1, 78
2.8, 65
5.3, 89
...
```

is difficult.

But put them on a graph and suddenly patterns become visible.

Graphs help us see:

### 1. Trends

Does \(X\) increase when \(Y\) increases?

### 2. Relationships

Are two variables related?

### 3. Outliers

Is there a strange observation?

For example:

```text
Score
100 |                  ●
 90 |             ●
 80 |         ●
 70 |      ●
 60 |   ●
 50 | ●
 40 |
 30 |                         ● ← strange?
    +-------------------------
```

That isolated point might be an **outlier**.

We'll study outliers properly in statistics.

### 4. Nonlinear patterns

Sometimes data doesn't form a straight line.

For example:

```text
Y
|
|       ●
|     ●   ●
|    ●     ●
|   ●       ●
|  ●         ●
+---------------- X
```

This tells us that a straight-line model may not be appropriate.

---

# 11. Distance Between Points

Coordinates also let us calculate **distance**.

On a number line:

Suppose:

$$
A=2
$$

and:

$$
B=7
$$

The distance is:

$$
|7-2|=5
$$

The absolute value means we care about distance, not direction.

---

# 12. Distance in 2D

Suppose:

$$
A=(x_1,y_1)
$$

and:

$$
B=(x_2,y_2)
$$

The horizontal difference is:

$$
x_2-x_1
$$

The vertical difference is:

$$
y_2-y_1
$$

These form a right triangle.

And we already know the **Pythagorean theorem**:

$$
a^2+b^2=c^2
$$

Therefore:

$$
\boxed{
d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}
}
$$

This is the **Euclidean distance**.

---

# 13. Example

Suppose:

$$
A=(1,2)
$$

and:

$$
B=(4,6)
$$

Horizontal difference:

$$
4-1=3
$$

Vertical difference:

$$
6-2=4
$$

Therefore:

$$
d=\sqrt{3^2+4^2}
$$

$$
=\sqrt{9+16}
$$

$$
=\sqrt{25}
$$

$$
\boxed{d=5}
$$

### Why should an ML student care?

Because **distance is extremely important in machine learning**.

For example:

- K-Nearest Neighbors
- clustering
- recommendation systems
- anomaly detection
- computer vision
- similarity calculations

Later, when we learn NumPy, we'll calculate these distances using arrays.

---

# 14. Now Comes Something VERY Important: Slope

Remember our previous lesson:

$$
y=mx+b
$$

What does \(m\) mean?

It's the **slope**.

Slope tells us:

> **How much does \(y\) change when \(x\) changes?**

The formula is:

$$
\boxed{
m=\frac{y_2-y_1}{x_2-x_1}
}
$$

Or:

$$
\boxed{
m=\frac{\text{rise}}{\text{run}}
}
$$

---

# 15. Rise Over Run

Imagine walking up a hill.

If you move:

- 2 meters horizontally
- 1 meter vertically

then:

$$
m=\frac{1}{2}=0.5
$$

The hill rises slowly.

Now imagine:

- 2 meters horizontally
- 4 meters vertically

Then:

$$
m=\frac{4}{2}=2
$$

Much steeper.

### Mental model 🧠

> **Slope = steepness**

---

# 16. Positive and Negative Slope

Consider:

$$
y=2x+1
$$

As \(x\) increases, \(y\) increases.

Therefore:

$$
m=2
$$

Positive slope.

Graphically:

```text
Y
↑
|           /
|         /
|       /
|     /
|   /
| /
+----------------→ X
```

---

Now:

$$
y=-2x+1
$$

As \(x\) increases, \(y\) decreases.

So:

$$
m=-2
$$

Graph:

```text
Y
↑
|\
| \
|  \
|   \
|    \
|     \
+----------------→ X
```

So:

- \(m>0\) → rises
- \(m<0\) → falls
- \(m=0\) → horizontal

---

# 17. Slope Connects Directly to ML

Suppose:

$$
\text{Score}=10(\text{Study Hours})+40
$$

This is:

$$
y=10x+40
$$

Therefore:

$$
m=10
$$

What does that mean?

For every additional hour of studying, the predicted score increases by:

$$
10
$$

points.

That's an ML interpretation of a model parameter.

Later you'll see:

$$
\hat y=wx+b
$$

The \(w\) is essentially controlling the slope.

For multiple features:

$$
\hat y=w_1x_1+w_2x_2+\cdots+w_nx_n+b
$$

each weight tells the model how strongly a feature influences the prediction, assuming the other features are held fixed.

---

# 18. Graphing a Function

Let's graph:

$$
y=2x+1
$$

We can make a table.

| \(x\) | \(y=2x+1\) |
| ----: | ---------: |
|     0 |          1 |
|     1 |          3 |
|     2 |          5 |
|     3 |          7 |

So our points are:

$$
(0,1)
$$

$$
(1,3)
$$

$$
(2,5)
$$

$$
(3,7)
$$

Plot them and connect them:

```text
Y
8 |
7 |              ●
6 |
5 |          ●
4 |
3 |      ●
2 |
1 |  ●
0 +----------------------→ X
   0   1   2   3
```

We have transformed:

$$
\boxed{\text{equation}}
$$

into:

$$
\boxed{\text{graph}}
$$

This is powerful.

---

# 19. The Equation and Graph Are Two Views of the Same Thing

This is an important idea.

Consider:

$$
y=2x+1
$$

You can look at it algebraically:

> "There is a slope of 2 and intercept of 1."

Or visually:

> "There is a straight line rising upward."

They're describing the **same relationship**.

### Think of it like this:

**Equation**

$$
y=2x+1
$$

↓

**Mathematical relationship**

↓

**Graph**

```text
   /
  /
 /
/
```

One is symbolic.

One is visual.

---

# 20. Real-World ML Example: House Prices 🏠

Suppose:

| House Size (m²) | Price |
| --------------: | ----: |
|              50 |  100k |
|              80 |  150k |
|             100 |  180k |
|             150 |  250k |
|             200 |  330k |

Plot:

- x-axis → house size
- y-axis → price

You might see:

```text
Price
 ↑
 |                       ●
 |                 ●
 |            ●
 |       ●
 |   ●
 +----------------------------→ Size
```

You might conclude:

> Larger houses tend to cost more.

An ML algorithm can attempt to learn this relationship.

For example:

$$
\hat y=wx+b
$$

The model tries to find a suitable:

$$
w
$$

and:

$$
b
$$

that produce good predictions.

---

# 21. Another Example: Physics ⚛️

This is where your physics background gives you a huge advantage.

Suppose you have a position-time relationship:

$$
x(t)
$$

You can plot:

- x-axis → time
- y-axis → position

For example:

```text
Position
   ↑
   |             ●
   |          ●
   |       ●
   |    ●
   | ●
   +----------------→ Time
```

The slope of the position-time graph represents velocity:

$$
v=\frac{\Delta x}{\Delta t}
$$

And later, with calculus:

$$
v=\frac{dx}{dt}
$$

Then:

$$
a=\frac{dv}{dt}
$$

This is a beautiful connection:

> **Graph → slope → physical meaning**

And ML does something conceptually similar:

> **Data → graph → relationship → model**

---

# 22. Scatter Plot vs Line Plot

These two are easy to confuse.

### Scatter plot

Used primarily to show individual observations.

Example:

```text
Y
|
|        ●
|   ●
|             ●
| ●
|      ●
+----------------→ X
```

Each dot represents a data point.

Very useful for ML exploratory data analysis.

### Line plot

Connects observations with lines.

Often useful for things like:

- time series
- experimental measurements
- physical trajectories

---

# 23. What Should You Look For in a Scatter Plot?

When you see a scatter plot, ask:

### Question 1

Does \(Y\) generally increase as \(X\) increases?

→ Positive relationship.

### Question 2

Does \(Y\) generally decrease as \(X\) increases?

→ Negative relationship.

### Question 3

Is there no obvious pattern?

→ Weak/no obvious relationship.

### Question 4

Are there unusual points?

→ Possible outliers.

### Question 5

Does the pattern curve?

→ Possible nonlinear relationship.

This visual intuition will become very important when we study **correlation** and **EDA**.

---

# 24. A Very Important ML Idea: Features Become Dimensions

Earlier we had:

$$
x_1,x_2,x_3
$$

For example:

- \(x_1\) = study hours
- \(x_2\) = sleep hours
- \(x_3\) = attendance

With one feature:

$$
x_1
$$

we can visualize data on a number line.

With two features:

$$
x_1,x_2
$$

we can visualize it on a 2D graph.

With three features:

$$
x_1,x_2,x_3
$$

we can visualize it in 3D.

But what happens with:

$$
100
$$

features?

We can't easily visualize all 100 dimensions.

This leads to a fundamental ML idea:

> **Mathematics can work in dimensions that humans cannot directly visualize.**

And this is one reason vectors and matrices become so important.

---

# 25. The Big Picture So Far

Let's connect everything we've learned.

```text
DATA
 │
 ├── Variables
 │      │
 │      └── Values
 │
 ├── Arithmetic
 │
 ├── Algebra
 │      │
 │      └── Equations
 │
 └── Functions
        │
        └── y = f(x)
               │
               ↓
          Coordinates
               │
               ↓
             Graphs
               │
        ┌──────┼──────┐
        ↓      ↓      ↓
      Trend  Slope  Outliers
        │
        ↓
       ML
        │
        ↓
  Learn relationships
```

---

# 26. The Most Important Mental Models

Remember these.

### Coordinate

> **"Where am I?"**

$$
(x,y)
$$

---

### x-axis

> **"How far left/right?"**

---

### y-axis

> **"How far up/down?"**

---

### Graph

> **"Show me the relationship visually."**

---

### Slope

> **"How quickly does \(y\) change when \(x\) changes?"**

$$
m=\frac{\Delta y}{\Delta x}
$$

---

### Scatter plot

> **"Show me my individual data points."**

---

### ML

> **"Can I learn the relationship between these variables?"**

---

# 27. Practice — Don't Look at the Answers Yet 🧠

### Q1

What does the point

$$
(4,7)
$$

mean?

---

### Q2

Which quadrant contains:

$$
(-3,5)
$$

---

### Q3

Which quadrant contains:

$$
(-3,-5)
$$

---

### Q4

Calculate the slope between:

$$
(1,2)
$$

and:

$$
(3,8)
$$

---

### Q5

What does a positive slope mean?

---

### Q6

What does this equation's slope represent?

$$
y=5x+10
$$

---

### Q7

Calculate the distance between:

$$
(0,0)
$$

and:

$$
(3,4)
$$

---

### Q8 — ML Thinking

Suppose:

| Study Hours | Score |
| ----------: | ----: |
|           1 |    50 |
|           2 |    55 |
|           3 |    63 |
|           4 |    70 |
|           5 |    80 |

If you plotted this as a scatter plot, what relationship would you expect to see?

---

# Answers

### Q1

$$
(4,7)
$$

means:

- 4 units right
- 7 units up.

### Q2

$$
(-3,5)
$$

→ Quadrant II.

### Q3

$$
(-3,-5)
$$

→ Quadrant III.

### Q4

$$
m=\frac{8-2}{3-1}
$$

$$
=\frac{6}{2}
$$

$$
\boxed{3}
$$

### Q5

A positive slope means:

> As \(x\) increases, \(y\) tends to increase.

### Q6

$$
y=5x+10
$$

has:

$$
m=5
$$

So \(y\) increases by 5 for every 1-unit increase in \(x\).

### Q7

$$
d=\sqrt{(3-0)^2+(4-0)^2}
$$

$$
=\sqrt{9+16}
$$

$$
=\boxed{5}
$$

### Q8

We would expect a **positive relationship**:

> More study hours → generally higher score.

---

# 🧠 Final Mental Map

You should now be able to think:

> **A coordinate tells me where a value is.**
> **A collection of coordinates gives me data points.**
> **A graph lets me see those points.**
> **A slope tells me how one quantity changes with another.**
> **ML uses these relationships to build predictive models.**

And there is one especially important bridge:

$$
\boxed{
\text{Physics: slope of position vs time} \rightarrow \text{velocity}
}
$$

$$
\boxed{
\text{ML: slope/weight} \rightarrow \text{change in prediction per feature change}
}
$$

---

## Next: Lesson 8 — Vectors ➡️

This is where things become **much more ML/physics oriented**.

We'll learn:

- What a vector actually is
- Scalar vs vector
- Vectors visually
- Vector components
- Vector addition/subtraction
- Vector magnitude
- Unit vectors
- Dot product
- Why vectors are the language of ML
- How a row of a dataset becomes a vector
- How physics vectors connect directly to ML feature vectors
- And finally how NumPy will represent vectors

**We will not jump to matrices yet.** We first need to become completely comfortable with vectors.
