"""
PyRLab — Snippets
Categorized, copy-ready Python code examples.
"""
import streamlit as st

st.set_page_config(page_title="Snippets — PyRLab", page_icon="✂️", layout="wide")

st.header("✂️ Python Snippets")
st.caption("Copy-ready code examples organized by category. Click to expand, then copy.")

# --- Snippet Data ---
SNIPPETS = [
    # --- Basics ---
    {"cat": "Basics", "title": "Hello World", "desc": "The simplest Python program.",
     "code": 'print("Hello, World!")'},

    {"cat": "Basics", "title": "User Input", "desc": "Read input from the user.",
     "code": 'name = input("What is your name? ")\nprint(f"Hello, {name}!")'},

    {"cat": "Basics", "title": "Type Checking & Conversion", "desc": "Check and convert data types.",
     "code": 'x = "42"\nprint(type(x))        # <class \'str\'>\n\ny = int(x)            # str → int\nz = float(x)          # str → float\nw = str(100)          # int → str\nb = bool(1)           # int → bool\n\nprint(f"int: {y}, float: {z}, str: \'{w}\', bool: {b}")'},

    {"cat": "Basics", "title": "Multiple Assignment", "desc": "Assign multiple variables at once.",
     "code": '# Multiple assignment\nx, y, z = 1, 2, 3\nprint(x, y, z)  # 1 2 3\n\n# Swap variables\na, b = 10, 20\na, b = b, a\nprint(a, b)  # 20 10\n\n# Same value\nx = y = z = 0\nprint(x, y, z)  # 0 0 0'},

    # --- Strings ---
    {"cat": "Strings", "title": "f-String Formatting", "desc": "Embed expressions in strings with f-strings.",
     "code": 'name = "Alice"\nage = 25\npi = 3.14159\n\nprint(f"{name} is {age} years old.")\nprint(f"Pi rounded: {pi:.2f}")\nprint(f"Age in 10 years: {age + 10}")\nprint(f"{\'HELLO\':>15}")   # right-aligned\nprint(f"{1000000:,}")       # 1,000,000'},

    {"cat": "Strings", "title": "String Manipulation", "desc": "Common string operations and methods.",
     "code": 'text = "Hello, World!"\n\nprint(text.upper())          # HELLO, WORLD!\nprint(text.lower())          # hello, world!\nprint(text.split(", "))      # [\'Hello\', \'World!\']\nprint(text.replace("World", "Python"))\nprint(text.count("l"))       # 3\nprint(text.find("World"))    # 7\nprint("-".join(["a","b","c"]))  # a-b-c\nprint("  spaces  ".strip())  # spaces'},

    # --- Lists ---
    {"cat": "Lists", "title": "List Comprehension", "desc": "Create lists in one elegant line.",
     "code": '# Squares\nsquares = [x**2 for x in range(1, 11)]\nprint(squares)\n\n# Filter even numbers\nevens = [x for x in range(20) if x % 2 == 0]\nprint(evens)\n\n# Transform\nnames = ["alice", "bob", "carol"]\ntitled = [n.title() for n in names]\nprint(titled)\n\n# Nested\nmatrix = [[i*3+j for j in range(3)] for i in range(3)]\nprint(matrix)  # [[0,1,2],[3,4,5],[6,7,8]]'},

    {"cat": "Lists", "title": "Sorting", "desc": "Sort lists with sorted() and .sort().",
     "code": 'nums = [5, 2, 8, 1, 9, 3]\nprint(sorted(nums))              # ascending\nprint(sorted(nums, reverse=True)) # descending\n\n# Sort objects by key\nstudents = [("Alice", 90), ("Bob", 75), ("Carol", 88)]\nby_score = sorted(students, key=lambda s: s[1], reverse=True)\nprint(by_score)\n\n# Sort dicts\npeople = [{"name": "A", "age": 30}, {"name": "B", "age": 25}]\nby_age = sorted(people, key=lambda p: p["age"])\nprint(by_age)'},

    {"cat": "Lists", "title": "Flatten Nested Lists", "desc": "Flatten a list of lists into a single list.",
     "code": 'nested = [[1, 2], [3, 4], [5, 6]]\n\n# List comprehension\nflat = [item for sublist in nested for item in sublist]\nprint(flat)  # [1, 2, 3, 4, 5, 6]\n\n# Using itertools\nfrom itertools import chain\nflat2 = list(chain.from_iterable(nested))\nprint(flat2)'},

    # --- Dictionaries ---
    {"cat": "Dictionaries", "title": "Dict Comprehension", "desc": "Create dictionaries in one line.",
     "code": '# Square lookup\nsquares = {x: x**2 for x in range(1, 6)}\nprint(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}\n\n# Filter\nscores = {"Alice": 92, "Bob": 78, "Carol": 85}\nhigh = {k: v for k, v in scores.items() if v >= 80}\nprint(high)  # {\'Alice\': 92, \'Carol\': 85}\n\n# Invert\ninverted = {v: k for k, v in scores.items()}\nprint(inverted)'},

    {"cat": "Dictionaries", "title": "Group Items", "desc": "Group list items by a property into a dictionary.",
     "code": 'from collections import defaultdict\n\nwords = ["apple", "ant", "banana", "bat", "cherry", "cat"]\n\nby_letter = defaultdict(list)\nfor word in words:\n    by_letter[word[0]].append(word)\n\nfor letter, group in sorted(by_letter.items()):\n    print(f"{letter}: {group}")\n# a: [\'apple\', \'ant\']\n# b: [\'banana\', \'bat\']\n# c: [\'cherry\', \'cat\']'},

    # --- Functions ---
    {"cat": "Functions", "title": "Decorator Pattern", "desc": "Wrap functions to add behavior.",
     "code": 'import time\n\ndef timer(func):\n    """Measure how long a function takes."""\n    def wrapper(*args, **kwargs):\n        start = time.time()\n        result = func(*args, **kwargs)\n        elapsed = time.time() - start\n        print(f"{func.__name__} took {elapsed:.4f}s")\n        return result\n    return wrapper\n\n@timer\ndef slow_function():\n    total = sum(range(1_000_000))\n    return total\n\nresult = slow_function()'},

    # --- Data Analysis ---
    {"cat": "Data Analysis", "title": "Read & Explore CSV", "desc": "Load and inspect a CSV file with pandas.",
     "code": 'import pandas as pd\n\n# df = pd.read_csv("data.csv")\n\n# Quick exploration\n# print(df.head())         # first 5 rows\n# print(df.shape)          # (rows, cols)\n# print(df.columns.tolist())  # column names\n# print(df.dtypes)         # column types\n# print(df.describe())     # statistics\n# print(df.info())         # summary\n# print(df.isnull().sum()) # missing values\nprint("Pandas exploration cheatsheet ready!")'},

    {"cat": "Data Analysis", "title": "Filter & Transform", "desc": "Select, filter, and create new columns.",
     "code": 'import pandas as pd\n\ndf = pd.DataFrame({\n    "Name": ["Alice","Bob","Carol","Dave","Eve"],\n    "Dept": ["Sales","IT","Sales","IT","HR"],\n    "Salary": [70000,85000,72000,90000,65000]\n})\n\n# Filter\nsales = df[df["Dept"] == "Sales"]\nprint("Sales dept:\\n", sales)\n\n# Multiple conditions\nhigh_pay = df[(df["Salary"] > 70000) & (df["Dept"] == "IT")]\nprint("\\nHigh-paid IT:\\n", high_pay)\n\n# New column\ndf["Bonus"] = df["Salary"] * 0.1\nprint("\\nWith bonus:\\n", df)'},

    {"cat": "Data Analysis", "title": "GroupBy Summary", "desc": "Aggregate data by groups.",
     "code": 'import pandas as pd\n\ndf = pd.DataFrame({\n    "Product": ["A","B","A","B","A","B"],\n    "Region": ["East","East","West","West","East","West"],\n    "Sales": [100, 150, 120, 180, 130, 200]\n})\n\n# Group and sum\nprint(df.groupby("Product")["Sales"].sum())\n\n# Multiple aggregations\nstats = df.groupby("Product")["Sales"].agg(\n    ["sum", "mean", "min", "max", "count"]\n)\nprint("\\n", stats)\n\n# Group by multiple columns\nmulti = df.groupby(["Product", "Region"])["Sales"].sum()\nprint("\\n", multi)'},

    {"cat": "Data Analysis", "title": "Pivot Table", "desc": "Create Excel-like pivot tables.",
     "code": 'import pandas as pd\n\ndf = pd.DataFrame({\n    "Name": ["Alice","Bob","Alice","Bob","Alice","Bob"],\n    "Subject": ["Math","Math","Science","Science","English","English"],\n    "Score": [92, 85, 88, 90, 95, 82]\n})\n\npivot = df.pivot_table(\n    values="Score",\n    index="Name",\n    columns="Subject",\n    aggfunc="mean"\n)\nprint(pivot)'},

    # --- Statistics ---
    {"cat": "Statistics", "title": "Descriptive Statistics", "desc": "Calculate common statistics from data.",
     "code": 'import statistics\n\ndata = [85, 92, 78, 95, 88, 72, 90, 84, 96, 80]\n\nprint(f"Count:    {len(data)}")\nprint(f"Sum:      {sum(data)}")\nprint(f"Mean:     {statistics.mean(data):.2f}")\nprint(f"Median:   {statistics.median(data):.2f}")\nprint(f"Mode:     {statistics.mode(data)}")\nprint(f"Std Dev:  {statistics.stdev(data):.2f}")\nprint(f"Variance: {statistics.variance(data):.2f}")\nprint(f"Min:      {min(data)}")\nprint(f"Max:      {max(data)}")\nprint(f"Range:    {max(data) - min(data)}")'},

    {"cat": "Statistics", "title": "Frequency Counter", "desc": "Count occurrences and find most common.",
     "code": 'from collections import Counter\n\ngrades = ["A","B","A","C","B","A","B","B","A","C","A","B"]\ncount = Counter(grades)\n\nprint(f"Counts: {dict(count)}")\nprint(f"Most common: {count.most_common(1)[0]}")\nprint(f"Total elements: {sum(count.values())}")\n\n# Percentage\ntotal = sum(count.values())\nfor grade, n in count.most_common():\n    pct = n / total * 100\n    print(f"  {grade}: {n} ({pct:.1f}%)")'},

    # --- Visualization ---
    {"cat": "Visualization", "title": "Matplotlib Bar Chart", "desc": "Create a bar chart with matplotlib.",
     "code": 'import matplotlib.pyplot as plt\n\ncategories = ["Python", "R", "SQL", "Julia"]\nscores = [85, 72, 90, 65]\ncolors = ["#0d9488", "#2563eb", "#7c3aed", "#db2777"]\n\nfig, ax = plt.subplots(figsize=(8, 5))\nax.bar(categories, scores, color=colors)\nax.set_ylabel("Popularity Score")\nax.set_title("Language Popularity")\nplt.tight_layout()\nplt.show()'},

    {"cat": "Visualization", "title": "Matplotlib Line Chart", "desc": "Create a line chart for time series.",
     "code": 'import matplotlib.pyplot as plt\n\nmonths = ["Jan","Feb","Mar","Apr","May","Jun"]\nrevenue = [1200, 1500, 1350, 1800, 2100, 1950]\n\nfig, ax = plt.subplots(figsize=(8, 5))\nax.plot(months, revenue, marker="o", linewidth=2, color="#0d9488")\nax.fill_between(range(len(months)), revenue, alpha=0.1, color="#0d9488")\nax.set_ylabel("Revenue ($)")\nax.set_title("Monthly Revenue")\nax.grid(True, alpha=0.3)\nplt.tight_layout()\nplt.show()'},
]

# --- Filters ---
search = st.text_input("🔍 Search snippets", placeholder="e.g. sort, pandas, chart...")
categories = sorted(set(s["cat"] for s in SNIPPETS))
selected_cat = st.pills("Category", ["All"] + categories, default="All")

# Filter
filtered = SNIPPETS
if selected_cat and selected_cat != "All":
    filtered = [s for s in filtered if s["cat"] == selected_cat]
if search:
    q = search.lower()
    filtered = [s for s in filtered if q in s["title"].lower() or q in s["desc"].lower() or q in s["code"].lower()]

# --- Render ---
if not filtered:
    st.info("No snippets found.")
else:
    st.caption(f"Showing {len(filtered)} snippets")
    for s in filtered:
        with st.expander(f"**{s['title']}** — {s['desc']}"):
            st.markdown(f"`{s['cat']}`")
            st.code(s["code"], language="python")
