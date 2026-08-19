"""
PyRLab — Reference
Searchable Python reference documentation. All content is hardcoded.
"""
import streamlit as st

st.set_page_config(page_title="Reference — PyRLab", page_icon="📖", layout="wide")

st.header("📖 Python Reference")
st.caption("Searchable documentation for Python fundamentals. Click any example to copy it.")

# --- Reference Data ---
ENTRIES = [
    # --- Variables & Types ---
    {"cat": "Basics", "name": "Variables", "desc": "Store data in named containers. Python is dynamically typed — no need to declare types.",
     "code": '# Variables\nname = "Alice"       # str\nage = 25             # int\nprice = 9.99         # float\nis_active = True     # bool\ndata = None          # NoneType\n\nprint(type(name))    # <class \'str\'>\nprint(type(age))     # <class \'int\'>'},

    {"cat": "Basics", "name": "Data Types", "desc": "Python has several built-in types: str, int, float, bool, list, dict, tuple, set, None.",
     "code": '# Type checking and conversion\nx = "42"\nprint(type(x))         # <class \'str\'>\n\ny = int(x)             # Convert to int\nprint(y + 8)           # 50\n\nz = float(x)           # Convert to float\nprint(z)               # 42.0\n\nprint(str(100))        # "100"\nprint(bool(0))         # False\nprint(bool(1))         # True'},

    {"cat": "Basics", "name": "Operators", "desc": "Arithmetic: +, -, *, /, //, %, **. Comparison: ==, !=, <, >, <=, >=. Logical: and, or, not.",
     "code": '# Arithmetic\nprint(10 + 3)    # 13\nprint(10 - 3)    # 7\nprint(10 * 3)    # 30\nprint(10 / 3)    # 3.333...\nprint(10 // 3)   # 3 (floor division)\nprint(10 % 3)    # 1 (remainder)\nprint(10 ** 3)   # 1000 (power)\n\n# Comparison\nprint(5 == 5)    # True\nprint(5 != 3)    # True\n\n# Logical\nprint(True and False)  # False\nprint(True or False)   # True\nprint(not True)        # False'},

    {"cat": "Basics", "name": "String Methods", "desc": "Strings are immutable sequences of characters. Tons of built-in methods.",
     "code": 's = "Hello, World!"\n\nprint(s.upper())           # "HELLO, WORLD!"\nprint(s.lower())           # "hello, world!"\nprint(s.replace("World", "Python"))  # "Hello, Python!"\nprint(s.split(", "))       # [\'Hello\', \'World!\']\nprint(s.strip())           # Remove whitespace\nprint(s.startswith("Hello"))  # True\nprint(s.find("World"))     # 7\nprint(len(s))              # 13\n\n# f-strings (formatted strings)\nname, age = "Alice", 25\nprint(f"{name} is {age} years old.")'},

    {"cat": "Basics", "name": "Input & Output", "desc": "print() outputs text. input() reads from the user. Use f-strings for formatting.",
     "code": '# Print with formatting\nname = "Alice"\nscore = 95.678\nprint(f"Name: {name}")          # f-string\nprint(f"Score: {score:.1f}")     # 1 decimal\nprint(f"Score: {score:>10.2f}")  # right-aligned\n\n# Multiple print options\nprint("A", "B", "C", sep="-")   # A-B-C\nprint("No newline", end=" ")    # suppress newline\nprint("continues here")'},

    # --- Control Flow ---
    {"cat": "Control Flow", "name": "if / elif / else", "desc": "Conditional logic. Python uses indentation (not braces) to define code blocks.",
     "code": 'score = 85\n\nif score >= 90:\n    grade = "A"\nelif score >= 80:\n    grade = "B"\nelif score >= 70:\n    grade = "C"\nelse:\n    grade = "F"\n\nprint(f"Score {score} = Grade {grade}")\n\n# Ternary (one-line if)\nstatus = "pass" if score >= 60 else "fail"\nprint(f"Status: {status}")'},

    {"cat": "Control Flow", "name": "for Loop", "desc": "Iterate over sequences (lists, strings, ranges, etc.).",
     "code": '# Loop over a list\nfruits = ["apple", "banana", "cherry"]\nfor fruit in fruits:\n    print(fruit)\n\n# Loop with range\nfor i in range(5):        # 0, 1, 2, 3, 4\n    print(i, end=" ")\nprint()\n\n# Loop with index using enumerate\nfor i, fruit in enumerate(fruits):\n    print(f"{i}: {fruit}")\n\n# Loop over dictionary\nperson = {"name": "Alice", "age": 25}\nfor key, value in person.items():\n    print(f"{key} = {value}")'},

    {"cat": "Control Flow", "name": "while Loop", "desc": "Repeat while a condition is True. Use break and continue to control flow.",
     "code": '# Basic while loop\ncount = 0\nwhile count < 5:\n    print(f"Count: {count}")\n    count += 1\n\n# break and continue\nfor i in range(10):\n    if i == 3:\n        continue    # skip 3\n    if i == 7:\n        break       # stop at 7\n    print(i, end=" ")\nprint()  # 0 1 2 4 5 6'},

    {"cat": "Control Flow", "name": "List Comprehensions", "desc": "Create lists in a single, readable line. Very Pythonic!",
     "code": '# Basic comprehension\nsquares = [x**2 for x in range(10)]\nprint(squares)  # [0, 1, 4, 9, 16, ...]\n\n# With condition\nevens = [x for x in range(20) if x % 2 == 0]\nprint(evens)  # [0, 2, 4, 6, ...]\n\n# Transform strings\nnames = ["alice", "bob", "carol"]\nupper = [n.capitalize() for n in names]\nprint(upper)  # [\'Alice\', \'Bob\', \'Carol\']\n\n# Dict comprehension\nword_lengths = {w: len(w) for w in names}\nprint(word_lengths)  # {\'alice\': 5, ...}'},

    # --- Functions ---
    {"cat": "Functions", "name": "Defining Functions", "desc": "Reusable blocks of code. Use def keyword. Can have default parameters.",
     "code": 'def greet(name, greeting="Hello"):\n    """Return a greeting string."""\n    return f"{greeting}, {name}!"\n\nprint(greet("Alice"))           # Hello, Alice!\nprint(greet("Bob", "Hi"))       # Hi, Bob!\n\n# Multiple return values\ndef min_max(numbers):\n    return min(numbers), max(numbers)\n\nlo, hi = min_max([5, 2, 8, 1, 9])\nprint(f"Min: {lo}, Max: {hi}")'},

    {"cat": "Functions", "name": "*args & **kwargs", "desc": "Accept variable numbers of positional and keyword arguments.",
     "code": '# *args — variable positional arguments\ndef total(*numbers):\n    return sum(numbers)\n\nprint(total(1, 2, 3))      # 6\nprint(total(10, 20, 30, 40))  # 100\n\n# **kwargs — variable keyword arguments\ndef describe(**info):\n    for key, value in info.items():\n        print(f"  {key}: {value}")\n\ndescribe(name="Alice", age=25, city="NYC")'},

    {"cat": "Functions", "name": "Lambda Functions", "desc": "Small anonymous functions defined inline. Useful with map(), filter(), sorted().",
     "code": '# Lambda — anonymous function\nsquare = lambda x: x ** 2\nprint(square(5))  # 25\n\n# With sorted\nstudents = [("Alice", 90), ("Bob", 75), ("Carol", 88)]\nby_score = sorted(students, key=lambda s: s[1], reverse=True)\nprint(by_score)\n\n# With map and filter\nnums = [1, 2, 3, 4, 5, 6]\nevens = list(filter(lambda x: x % 2 == 0, nums))\ndoubled = list(map(lambda x: x * 2, nums))\nprint(f"Evens: {evens}")    # [2, 4, 6]\nprint(f"Doubled: {doubled}")  # [2, 4, 6, 8, 10, 12]'},

    # --- Data Structures ---
    {"cat": "Data Structures", "name": "Lists", "desc": "Ordered, mutable sequences. The most commonly used Python data structure.",
     "code": 'nums = [3, 1, 4, 1, 5, 9, 2, 6]\n\nnums.append(7)         # add to end\nnums.insert(0, 0)      # insert at index\nnums.remove(1)         # remove first occurrence\npopped = nums.pop()   # remove and return last\n\nprint(f"List: {nums}")\nprint(f"Popped: {popped}")\nprint(f"Sorted: {sorted(nums)}")\nprint(f"Reversed: {nums[::-1]}")\nprint(f"Slice [2:5]: {nums[2:5]}")\nprint(f"Length: {len(nums)}")\nprint(f"3 in list: {3 in nums}")'},

    {"cat": "Data Structures", "name": "Dictionaries", "desc": "Key-value pairs. Fast lookups. Keys must be immutable (strings, numbers, tuples).",
     "code": 'student = {\n    "name": "Alice",\n    "age": 25,\n    "grades": [90, 85, 92]\n}\n\n# Access\nprint(student["name"])           # Alice\nprint(student.get("gpa", "N/A")) # N/A (default)\n\n# Modify\nstudent["gpa"] = 3.8\nstudent.update({"city": "NYC", "age": 26})\n\n# Iterate\nfor key, val in student.items():\n    print(f"  {key}: {val}")\n\nprint(f"Keys: {list(student.keys())}")'},

    {"cat": "Data Structures", "name": "Tuples", "desc": "Immutable ordered sequences. Faster than lists. Good for fixed data.",
     "code": '# Tuples are immutable\npoint = (3, 4)\nx, y = point         # unpacking\nprint(f"x={x}, y={y}")\n\n# Named tuples for clarity\nfrom collections import namedtuple\nPoint = namedtuple("Point", ["x", "y"])\np = Point(3, 4)\nprint(f"Point: {p.x}, {p.y}")\n\n# Tuple as dict key (lists can\'t be keys)\nlocations = {(40.7, -74.0): "NYC", (34.0, -118.2): "LA"}\nprint(locations[(40.7, -74.0)])'},

    {"cat": "Data Structures", "name": "Sets", "desc": "Unordered collections of unique elements. Great for removing duplicates and set operations.",
     "code": 'a = {1, 2, 3, 4, 5}\nb = {4, 5, 6, 7, 8}\n\nprint(f"Union: {a | b}")            # {1,2,3,4,5,6,7,8}\nprint(f"Intersection: {a & b}")     # {4, 5}\nprint(f"Difference: {a - b}")       # {1, 2, 3}\n\n# Remove duplicates from a list\ndupes = [1, 2, 2, 3, 3, 3, 4]\nunique = list(set(dupes))\nprint(f"Unique: {unique}")'},

    # --- File I/O ---
    {"cat": "File I/O", "name": "Reading Files", "desc": "Open and read text files. Always use 'with' for automatic closing.",
     "code": '# Reading a file (concept — run locally)\n# with open("data.txt", "r") as f:\n#     content = f.read()          # entire file as string\n#     print(content)\n\n# Read line by line\n# with open("data.txt", "r") as f:\n#     for line in f:\n#         print(line.strip())\n\n# Read as list of lines\n# with open("data.txt", "r") as f:\n#     lines = f.readlines()\n#     print(f"Total lines: {len(lines)}")\n\nprint("File I/O examples — run these locally!")\nprint("Always use: with open(filename) as f:")'},

    {"cat": "File I/O", "name": "Writing Files", "desc": "Write text to files. Use 'w' to overwrite, 'a' to append.",
     "code": '# Writing a file (concept — run locally)\n# with open("output.txt", "w") as f:\n#     f.write("Hello, World!\\n")\n#     f.write("Second line\\n")\n\n# Append to existing file\n# with open("output.txt", "a") as f:\n#     f.write("Appended line\\n")\n\n# Write a list of lines\n# lines = ["Line 1\\n", "Line 2\\n", "Line 3\\n"]\n# with open("output.txt", "w") as f:\n#     f.writelines(lines)\n\nprint("File writing examples — run these locally!")\nprint("\'w\' = overwrite, \'a\' = append")'},

    {"cat": "File I/O", "name": "CSV Files", "desc": "Read and write CSV files using the built-in csv module.",
     "code": 'import csv\nimport io\n\n# Create sample CSV data in memory\ncsv_text = """Name,Age,Score\nAlice,25,92\nBob,30,85\nCarol,28,90"""\n\n# Read CSV\nreader = csv.DictReader(io.StringIO(csv_text))\nfor row in reader:\n    print(f"{row[\'Name\']}: age {row[\'Age\']}, score {row[\'Score\']}")\n\n# To write CSV (concept):\n# with open("output.csv", "w", newline="") as f:\n#     writer = csv.writer(f)\n#     writer.writerow(["Name", "Age"])\n#     writer.writerow(["Alice", 25])'},

    {"cat": "File I/O", "name": "JSON", "desc": "Read and write JSON data with the built-in json module.",
     "code": 'import json\n\n# Python dict to JSON string\ndata = {"name": "Alice", "age": 25, "scores": [90, 85, 92]}\njson_str = json.dumps(data, indent=2)\nprint("JSON string:")\nprint(json_str)\n\n# JSON string back to Python dict\nparsed = json.loads(json_str)\nprint(f"\\nParsed name: {parsed[\'name\']}")\nprint(f"Parsed scores: {parsed[\'scores\']}")\n\n# File operations (concept):\n# json.dump(data, open("data.json", "w"))\n# data = json.load(open("data.json"))'},

    # --- Error Handling ---
    {"cat": "Error Handling", "name": "try / except", "desc": "Handle errors gracefully. Prevent crashes with try/except blocks.",
     "code": 'try:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print("Cannot divide by zero!")\n\ntry:\n    num = int("not_a_number")\nexcept ValueError as e:\n    print(f"ValueError: {e}")\n\n# Multiple exceptions\ntry:\n    data = [1, 2, 3]\n    print(data[10])\nexcept (IndexError, KeyError) as e:\n    print(f"Error: {e}")\nfinally:\n    print("This always runs")'},

    # --- Classes ---
    {"cat": "Classes", "name": "Basic Class", "desc": "Define custom types with class. Use __init__ for initialization, self for instance reference.",
     "code": 'class Dog:\n    def __init__(self, name, breed):\n        self.name = name\n        self.breed = breed\n        self.tricks = []\n\n    def learn_trick(self, trick):\n        self.tricks.append(trick)\n\n    def show_tricks(self):\n        if self.tricks:\n            print(f"{self.name} knows: {self.tricks}")\n        else:\n            print(f"{self.name} has no tricks yet.")\n\ndog = Dog("Rex", "Labrador")\ndog.learn_trick("sit")\ndog.learn_trick("shake")\ndog.show_tricks()\nprint(f"{dog.name} is a {dog.breed}")'},

    # --- Modules ---
    {"cat": "Modules", "name": "math Module", "desc": "Mathematical functions and constants: sqrt, ceil, floor, pi, e, log, sin, cos.",
     "code": 'import math\n\nprint(f"pi = {math.pi:.4f}")\nprint(f"e = {math.e:.4f}")\nprint(f"sqrt(144) = {math.sqrt(144)}")\nprint(f"ceil(4.2) = {math.ceil(4.2)}")\nprint(f"floor(4.8) = {math.floor(4.8)}")\nprint(f"log(100, 10) = {math.log(100, 10)}")\nprint(f"sin(pi/2) = {math.sin(math.pi/2)}")\nprint(f"factorial(6) = {math.factorial(6)}")\nprint(f"gcd(48, 18) = {math.gcd(48, 18)}")'},

    {"cat": "Modules", "name": "random Module", "desc": "Generate random numbers, make random choices, shuffle sequences.",
     "code": 'import random\n\n# Random float 0-1\nprint(f"Random float: {random.random():.4f}")\n\n# Random integer\nprint(f"Random int 1-10: {random.randint(1, 10)}")\n\n# Random choice\ncolors = ["red", "green", "blue", "yellow"]\nprint(f"Random color: {random.choice(colors)}")\n\n# Random sample (no repeats)\nprint(f"Sample of 2: {random.sample(colors, 2)}")\n\n# Shuffle\nnums = [1, 2, 3, 4, 5]\nrandom.shuffle(nums)\nprint(f"Shuffled: {nums}")'},

    {"cat": "Modules", "name": "datetime Module", "desc": "Work with dates and times. Parse, format, and calculate durations.",
     "code": 'from datetime import datetime, timedelta\n\nnow = datetime.now()\nprint(f"Now: {now}")\nprint(f"Date: {now.strftime(\'%Y-%m-%d\')}")\nprint(f"Time: {now.strftime(\'%H:%M:%S\')}")\nprint(f"Formatted: {now.strftime(\'%B %d, %Y\')}")\n\n# Date arithmetic\ntomorrow = now + timedelta(days=1)\nnext_week = now + timedelta(weeks=1)\nprint(f"Tomorrow: {tomorrow.strftime(\'%Y-%m-%d\')}")\nprint(f"Next week: {next_week.strftime(\'%Y-%m-%d\')}")\n\n# Parse a date string\nbday = datetime.strptime("1999-06-15", "%Y-%m-%d")\nage_days = (now - bday).days\nprint(f"Days since 1999-06-15: {age_days}")'},

    {"cat": "Modules", "name": "statistics Module", "desc": "Statistical functions: mean, median, mode, stdev, variance.",
     "code": 'import statistics\n\ndata = [85, 92, 78, 95, 88, 72, 90, 84, 96, 80]\n\nprint(f"Data: {data}")\nprint(f"Mean:     {statistics.mean(data):.1f}")\nprint(f"Median:   {statistics.median(data):.1f}")\nprint(f"Mode:     {statistics.mode(data)}")\nprint(f"Std Dev:  {statistics.stdev(data):.2f}")\nprint(f"Variance: {statistics.variance(data):.2f}")\nprint(f"Min:      {min(data)}")\nprint(f"Max:      {max(data)}")\nprint(f"Range:    {max(data) - min(data)}")\n\n# Quantiles\nq = statistics.quantiles(data, n=4)\nprint(f"Quartiles: {q}")'},

    {"cat": "Modules", "name": "collections Module", "desc": "Specialized container types: Counter, defaultdict, namedtuple, deque.",
     "code": 'from collections import Counter, defaultdict\n\n# Counter — count occurrences\nwords = "the cat sat on the mat the cat".split()\ncount = Counter(words)\nprint(f"Word counts: {dict(count)}")\nprint(f"Most common: {count.most_common(2)}")\n\n# defaultdict — dict with default values\nby_length = defaultdict(list)\nfor word in ["apple", "hi", "cat", "an", "banana"]:\n    by_length[len(word)].append(word)\nprint(f"\\nGrouped by length:")\nfor length, words in sorted(by_length.items()):\n    print(f"  {length} letters: {words}")'},

    # --- Pandas ---
    {"cat": "Pandas", "name": "Creating DataFrames", "desc": "Pandas DataFrame is a 2D table. Create from dicts, lists, or CSV files.",
     "code": 'import pandas as pd\n\n# From dictionary\ndf = pd.DataFrame({\n    "Name": ["Alice", "Bob", "Carol", "Dave"],\n    "Age": [25, 30, 28, 35],\n    "Score": [92, 85, 90, 78]\n})\nprint(df)\nprint(f"\\nShape: {df.shape}")\nprint(f"Columns: {list(df.columns)}")\nprint(f"Types:\\n{df.dtypes}")'},

    {"cat": "Pandas", "name": "DataFrame Operations", "desc": "Select, filter, sort, and transform DataFrames.",
     "code": 'import pandas as pd\n\ndf = pd.DataFrame({\n    "Name": ["Alice","Bob","Carol","Dave","Eve"],\n    "Dept": ["Sales","IT","Sales","IT","Sales"],\n    "Salary": [70000, 85000, 72000, 90000, 68000]\n})\n\n# Select columns\nprint(df[["Name", "Salary"]])\n\n# Filter rows\nhigh = df[df["Salary"] > 75000]\nprint(f"\\nHigh earners:\\n{high}")\n\n# Sort\nsorted_df = df.sort_values("Salary", ascending=False)\nprint(f"\\nSorted by salary:\\n{sorted_df}")\n\n# Add column\ndf["Bonus"] = df["Salary"] * 0.1\nprint(f"\\nWith bonus:\\n{df}")'},

    {"cat": "Pandas", "name": "GroupBy & Aggregation", "desc": "Group rows by a column and compute aggregated statistics.",
     "code": 'import pandas as pd\n\ndf = pd.DataFrame({\n    "Product": ["A","B","A","B","A","B"],\n    "Quarter": ["Q1","Q1","Q2","Q2","Q3","Q3"],\n    "Revenue": [100, 150, 120, 180, 130, 200]\n})\n\n# Group by Product\ngrouped = df.groupby("Product")["Revenue"]\nprint("Sum by product:")\nprint(grouped.sum())\n\nprint("\\nMean by product:")\nprint(grouped.mean())\n\n# Multiple aggregations\nstats = grouped.agg(["sum", "mean", "min", "max"])\nprint(f"\\nFull stats:\\n{stats}")'},

    {"cat": "Pandas", "name": "Reading CSV with Pandas", "desc": "Read CSV files into DataFrames for analysis. The most common way to load data.",
     "code": 'import pandas as pd\nimport io\n\n# Simulate reading CSV\ncsv_data = """Name,Age,City,Score\nAlice,25,NYC,92\nBob,30,LA,85\nCarol,28,NYC,90\nDave,35,Chicago,78\nEve,22,LA,95"""\n\ndf = pd.read_csv(io.StringIO(csv_data))\nprint(df)\nprint(f"\\nInfo:")\nprint(f"  Shape: {df.shape}")\nprint(f"  Columns: {list(df.columns)}")\nprint(f"\\nDescribe:\\n{df.describe()}")\n\n# To read a real file:\n# df = pd.read_csv("data.csv")'},

    # --- Matplotlib ---
    {"cat": "Visualization", "name": "Bar Chart", "desc": "Create bar charts with matplotlib. Run locally or in the Analysis Lab.",
     "code": '# Run this in the Analysis Lab or locally\nimport matplotlib.pyplot as plt\n\ncategories = ["Math", "Science", "English", "History"]\nscores = [92, 88, 95, 78]\n\nfig, ax = plt.subplots()\nax.bar(categories, scores, color=["#2563eb","#7c3aed","#db2777","#16a34a"])\nax.set_ylabel("Score")\nax.set_title("Scores by Subject")\nplt.tight_layout()\n# plt.show()  # when running locally\nprint("Chart code ready — run in Analysis Lab!")'},

    {"cat": "Visualization", "name": "Line Chart", "desc": "Create line charts for time series and trends.",
     "code": '# Run locally or in Analysis Lab\nimport matplotlib.pyplot as plt\n\nmonths = ["Jan","Feb","Mar","Apr","May","Jun"]\nsales = [120, 135, 150, 165, 180, 210]\n\nfig, ax = plt.subplots()\nax.plot(months, sales, marker="o", color="#2563eb", linewidth=2)\nax.fill_between(range(len(months)), sales, alpha=0.1, color="#2563eb")\nax.set_ylabel("Sales ($)")\nax.set_title("Monthly Sales")\nax.grid(True, alpha=0.3)\nplt.tight_layout()\nprint("Chart code ready!")'},
]

# --- Search & Filter ---
search = st.text_input("Search", placeholder="Type to search (e.g. list, function, pandas)...")
categories = sorted(set(e["cat"] for e in ENTRIES))
selected_cat = st.pills("Category", ["All"] + categories, default="All")

# Filter entries
filtered = ENTRIES
if selected_cat and selected_cat != "All":
    filtered = [e for e in filtered if e["cat"] == selected_cat]
if search:
    query = search.lower()
    filtered = [e for e in filtered if query in e["name"].lower() or query in e["desc"].lower() or query in e["code"].lower()]

# --- Render ---
if not filtered:
    st.info("No results found. Try a different search term.")
else:
    st.caption(f"Showing {len(filtered)} entries")
    for entry in filtered:
        with st.expander(f"**{entry['name']}** — {entry['desc']}", expanded=False):
            st.markdown(f"**Category:** `{entry['cat']}`")
            st.code(entry["code"], language="python")
