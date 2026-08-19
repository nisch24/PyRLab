"""
PyRLab — Tutorials
Step-by-step Python lessons from beginner to data analysis.
"""
import streamlit as st

st.set_page_config(page_title="Tutorials — PyRLab", page_icon="🎓", layout="wide")

st.header("Python Tutorials")
st.caption("Progressive lessons from absolute basics to data analysis. Each includes explanations, code, and exercises.")

# --- Tutorial Data ---
TUTORIALS = [
    {
        "title": "1. Hello Python",
        "content": """
### Welcome to Python!

Python is a powerful yet beginner-friendly language. Let's start with the basics.

**Printing output:**
```python
print("Hello, World!")
print("My name is Alice")
print(2 + 3)       # prints 5
print("Age:", 25)   # prints Age: 25
```

**Comments** explain your code. Python ignores them:
```python
# This is a single-line comment
print("This runs")  # inline comment
```

**Variables** store data:
```python
name = "Alice"     # string
age = 25           # integer
height = 5.6       # float
is_student = True  # boolean
```

> **Exercise:** Create variables for your name, age, and favorite color. Print them all using `print()`.

<details>
<summary>Show Solution</summary>

```python
name = "Alice"
age = 25
color = "blue"
print("Name:", name)
print("Age:", age)
print("Favorite color:", color)
```
</details>
"""
    },
    {
        "title": "2. Numbers & Math",
        "content": """
### Working with Numbers

Python supports integers, floats, and all common math operations:

```python
# Arithmetic
print(10 + 3)     # 13   (addition)
print(10 - 3)     # 7    (subtraction)
print(10 * 3)     # 30   (multiplication)
print(10 / 3)     # 3.33 (division — always float)
print(10 // 3)    # 3    (floor division — integer)
print(10 % 3)     # 1    (modulo — remainder)
print(10 ** 3)    # 1000 (power)
```

**The `math` module** has advanced functions:
```python
import math

print(math.sqrt(144))    # 12.0
print(math.pi)           # 3.14159...
print(math.ceil(4.2))    # 5
print(math.floor(4.8))   # 4
```

**Type conversion:**
```python
x = int("42")      # string → int
y = float("3.14")  # string → float
z = str(100)       # int → string
```

> **Exercise:** Calculate the area of a circle with radius 7. (Formula: π × r²)

<details>
<summary>Show Solution</summary>

```python
import math
radius = 7
area = math.pi * radius ** 2
print(f"Area of circle with radius {radius}: {area:.2f}")
```
</details>
"""
    },
    {
        "title": "3. Strings",
        "content": """
### String Operations

Strings are sequences of characters:

```python
name = "Alice"
greeting = 'Hello'          # single or double quotes
multi = \"\"\"This is a
multi-line string.\"\"\"

# String operations
print(name.upper())         # ALICE
print(name.lower())         # alice
print(len(name))            # 5
print(name[0])              # A (first character)
print(name[-1])             # e (last character)
print(name[1:4])            # lic (slice)
```

**f-strings** (formatted strings) — the best way to embed values:
```python
name = "Alice"
age = 25
print(f"{name} is {age} years old.")
print(f"Next year: {age + 1}")
print(f"Pi: {3.14159:.2f}")        # 3.14
```

**Common methods:**
```python
text = "hello world"
print(text.capitalize())    # Hello world
print(text.title())         # Hello World
print(text.count("l"))      # 3
print(text.replace("world", "Python"))
print(text.split())         # ['hello', 'world']
print("-".join(["a","b","c"]))  # a-b-c
```

> **Exercise:** Given name="John Doe", extract the first name and last name separately.

<details>
<summary>Show Solution</summary>

```python
name = "John Doe"
parts = name.split()
first = parts[0]
last = parts[1]
print(f"First: {first}, Last: {last}")
```
</details>
"""
    },
    {
        "title": "4. Lists",
        "content": """
### Lists — Ordered Collections

Lists store multiple items in order:

```python
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40, 50]
mixed = [1, "two", 3.0, True]

# Accessing items (0-indexed)
print(fruits[0])     # apple
print(fruits[-1])    # cherry
print(fruits[1:3])   # ['banana', 'cherry']
```

**Modifying lists:**
```python
fruits.append("date")       # add to end
fruits.insert(1, "avocado") # insert at index
fruits.remove("banana")     # remove by value
last = fruits.pop()         # remove and return last
fruits.sort()               # sort in place
```

**List comprehensions** — create lists in one line:
```python
squares = [x**2 for x in range(1, 6)]
# [1, 4, 9, 16, 25]

evens = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

**Useful functions:**
```python
nums = [5, 2, 8, 1, 9]
print(len(nums))       # 5
print(sum(nums))       # 25
print(min(nums))       # 1
print(max(nums))       # 9
print(sorted(nums))    # [1, 2, 5, 8, 9]
```

> **Exercise:** Create a list of 5 test scores. Calculate and print the average.

<details>
<summary>Show Solution</summary>

```python
scores = [85, 92, 78, 90, 88]
average = sum(scores) / len(scores)
print(f"Scores: {scores}")
print(f"Average: {average:.1f}")
```
</details>
"""
    },
    {
        "title": "5. Dictionaries",
        "content": """
### Dictionaries — Key-Value Pairs

Dictionaries map keys to values:

```python
student = {
    "name": "Alice",
    "age": 25,
    "grades": [90, 85, 92]
}

# Access
print(student["name"])             # Alice
print(student.get("gpa", "N/A"))   # N/A (default if missing)

# Modify
student["gpa"] = 3.8               # add new key
student["age"] = 26                 # update existing

# Delete
del student["gpa"]
```

**Iterating:**
```python
for key in student:
    print(key)

for key, value in student.items():
    print(f"{key}: {value}")

print(list(student.keys()))
print(list(student.values()))
```

**Dictionary comprehension:**
```python
squares = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

> **Exercise:** Create a dictionary of 3 countries and their capitals. Loop through and print each.

<details>
<summary>Show Solution</summary>

```python
capitals = {
    "France": "Paris",
    "Japan": "Tokyo",
    "Brazil": "Brasilia"
}
for country, capital in capitals.items():
    print(f"The capital of {country} is {capital}.")
```
</details>
"""
    },
    {
        "title": "6. if/else & Logic",
        "content": """
### Conditional Logic

Make decisions in your code:

```python
age = 20

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
```

**Comparison operators:** `==`, `!=`, `<`, `>`, `<=`, `>=`

**Logical operators:** `and`, `or`, `not`

```python
x = 15
if x > 10 and x < 20:
    print("Between 10 and 20")

if x == 10 or x == 15:
    print("x is 10 or 15")

if not x == 10:
    print("x is not 10")
```

**Ternary (one-line if):**
```python
status = "adult" if age >= 18 else "minor"
```

**Checking membership:**
```python
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("We have bananas!")
```

> **Exercise:** Write code that checks a number and prints whether it's positive, negative, or zero.

<details>
<summary>Show Solution</summary>

```python
num = -5
if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print(f"{num} is zero")
```
</details>
"""
    },
    {
        "title": "7. Loops",
        "content": """
### for Loops and while Loops

**for loop** — iterate over sequences:
```python
for i in range(5):           # 0, 1, 2, 3, 4
    print(i)

for fruit in ["apple", "banana", "cherry"]:
    print(fruit)

for i, item in enumerate(["a", "b", "c"]):
    print(f"{i}: {item}")
```

**while loop** — repeat while a condition is true:
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

**break and continue:**
```python
for i in range(10):
    if i == 3:
        continue    # skip 3
    if i == 7:
        break       # stop at 7
    print(i)        # 0 1 2 4 5 6
```

**Nested loops:**
```python
for i in range(3):
    for j in range(3):
        print(f"({i},{j})", end=" ")
    print()     # new line
```

> **Exercise:** Print all numbers from 1 to 20 that are divisible by 3.

<details>
<summary>Show Solution</summary>

```python
for n in range(1, 21):
    if n % 3 == 0:
        print(n, end=" ")
# Output: 3 6 9 12 15 18
```
</details>
"""
    },
    {
        "title": "8. Functions",
        "content": """
### Defining and Using Functions

Functions are reusable blocks of code:

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))   # Hello, Alice!
```

**Default parameters:**
```python
def power(base, exp=2):
    return base ** exp

print(power(5))      # 25  (uses default exp=2)
print(power(2, 10))  # 1024
```

**Multiple return values:**
```python
def analyze(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

lo, hi, avg = analyze([10, 20, 30, 40, 50])
print(f"Min: {lo}, Max: {hi}, Avg: {avg}")
```

**Lambda functions** (small, inline):
```python
square = lambda x: x ** 2
add = lambda a, b: a + b
print(square(5))     # 25
print(add(3, 4))     # 7
```

> **Exercise:** Write a function `is_even(n)` that returns True if n is even.

<details>
<summary>Show Solution</summary>

```python
def is_even(n):
    return n % 2 == 0

print(is_even(4))   # True
print(is_even(7))   # False
```
</details>
"""
    },
    {
        "title": "9. File I/O & JSON",
        "content": """
### Reading and Writing Files

Always use `with` to open files — it closes them automatically:

```python
# Writing
with open("notes.txt", "w") as f:
    f.write("Line 1\\n")
    f.write("Line 2\\n")

# Reading
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)

# Reading line by line
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())
```

**JSON — structured data:**
```python
import json

# Python → JSON string
data = {"name": "Alice", "scores": [90, 85, 92]}
json_str = json.dumps(data, indent=2)
print(json_str)

# JSON string → Python
parsed = json.loads(json_str)
print(parsed["name"])
```

**CSV files:**
```python
import csv

# Writing CSV
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Score"])
    writer.writerow(["Alice", 92])

# Reading CSV
with open("data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
```

> **Exercise:** Create a dictionary, save it as JSON, then read it back.

<details>
<summary>Show Solution</summary>

```python
import json

data = {"name": "Bob", "age": 30, "hobbies": ["coding", "gaming"]}

# Save
with open("person.json", "w") as f:
    json.dump(data, f, indent=2)

# Read
with open("person.json") as f:
    loaded = json.load(f)

print(loaded["name"])     # Bob
print(loaded["hobbies"])  # ['coding', 'gaming']
```
</details>
"""
    },
    {
        "title": "10. Error Handling",
        "content": """
### Handling Errors Gracefully

Use `try/except` to handle errors:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

**Catching the error message:**
```python
try:
    num = int("not a number")
except ValueError as e:
    print(f"Error: {e}")
```

**Multiple exceptions:**
```python
try:
    data = [1, 2, 3]
    print(data[10])
except IndexError:
    print("Index out of range!")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    print("This always runs.")
```

**Raising your own errors:**
```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(e)
```

> **Exercise:** Write a function that safely converts a string to an integer, returning `None` on failure.

<details>
<summary>Show Solution</summary>

```python
def safe_int(s):
    try:
        return int(s)
    except (ValueError, TypeError):
        return None

print(safe_int("42"))     # 42
print(safe_int("hello"))  # None
print(safe_int(None))     # None
```
</details>
"""
    },
    {
        "title": "11. Pandas Basics",
        "content": """
### Data Analysis with Pandas

Pandas is the core library for data analysis:

```python
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Carol"],
    "Age": [25, 30, 28],
    "Score": [92, 85, 90]
})
print(df)
```

**Key operations:**
```python
# Basic info
print(df.shape)          # (3, 3)
print(df.columns)        # column names
print(df.describe())     # statistics
print(df.head(2))        # first 2 rows

# Select columns
print(df["Name"])           # single column
print(df[["Name","Score"]]) # multiple columns

# Filter rows
high = df[df["Score"] > 85]

# Sort
sorted_df = df.sort_values("Score", ascending=False)

# New column
df["Pass"] = df["Score"] >= 60
```

**Reading CSV:**
```python
# df = pd.read_csv("data.csv")
# df = pd.read_csv("data.csv", encoding="utf-8")
```

> **Exercise:** Create a DataFrame of 4 products with Name, Price, Quantity. Calculate total value (Price × Quantity).

<details>
<summary>Show Solution</summary>

```python
import pandas as pd

df = pd.DataFrame({
    "Product": ["Widget", "Gadget", "Doohickey", "Thingamajig"],
    "Price": [9.99, 24.99, 14.99, 4.99],
    "Quantity": [100, 50, 75, 200]
})
df["Total"] = df["Price"] * df["Quantity"]
print(df)
print(f"\\nGrand total: ${df['Total'].sum():.2f}")
```
</details>
"""
    },
    {
        "title": "12. Data Visualization",
        "content": """
### Charts with Matplotlib

Create visualizations from your data:

```python
import matplotlib.pyplot as plt

# Bar chart
categories = ["A", "B", "C", "D"]
values = [25, 40, 30, 55]

fig, ax = plt.subplots()
ax.bar(categories, values, color="#2563eb")
ax.set_title("Bar Chart Example")
ax.set_ylabel("Values")
plt.show()
```

```python
# Line chart
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 120, 115, 140, 160]

fig, ax = plt.subplots()
ax.plot(months, sales, marker="o", color="#16a34a")
ax.set_title("Monthly Sales")
ax.grid(True, alpha=0.3)
plt.show()
```

```python
# Pie chart
labels = ["Python", "R", "SQL", "Other"]
sizes = [45, 25, 20, 10]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct="%1.0f%%")
ax.set_title("Language Usage")
plt.show()
```

**With Pandas:**
```python
import pandas as pd

df = pd.DataFrame({
    "Month": ["Jan","Feb","Mar","Apr"],
    "Revenue": [1200, 1500, 1350, 1800]
})
df.plot(x="Month", y="Revenue", kind="bar")
plt.show()
```

> **Exercise:** Head to the **Analysis Lab** to upload real data and make charts!
"""
    },
]

# --- Render ---
col1, col2 = st.columns([1, 3])

with col1:
    st.markdown("### Lessons")
    selected = None
    for i, tut in enumerate(TUTORIALS):
        if st.button(tut["title"], key=f"tut_{i}", use_container_width=True):
            selected = i

    if "selected_tutorial" not in st.session_state:
        st.session_state["selected_tutorial"] = None
    if selected is not None:
        st.session_state["selected_tutorial"] = selected

with col2:
    idx = st.session_state.get("selected_tutorial")
    if idx is not None and idx < len(TUTORIALS):
        st.markdown(TUTORIALS[idx]["content"])
    else:
        st.markdown("""
        ### 👈 Select a lesson from the sidebar

        **12 lessons from basics to data visualization:**

        | # | Topic | What You'll Learn |
        |---|-------|-------------------|
        | 1 | Hello Python | print, variables, comments |
        | 2 | Numbers & Math | arithmetic, math module |
        | 3 | Strings | methods, f-strings, slicing |
        | 4 | Lists | indexing, methods, comprehensions |
        | 5 | Dictionaries | key-value pairs, iteration |
        | 6 | if/else & Logic | conditionals, operators |
        | 7 | Loops | for, while, break, continue |
        | 8 | Functions | def, lambda, returns |
        | 9 | File I/O & JSON | read, write, csv, json |
        | 10 | Error Handling | try/except, raise |
        | 11 | Pandas Basics | DataFrames, filtering |
        | 12 | Data Visualization | matplotlib charts |
        """)
