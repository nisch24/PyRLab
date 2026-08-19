"""
PyRLab — Playground
Write and execute Python code live in the browser.
"""
import streamlit as st
import io
import contextlib
import traceback

st.set_page_config(page_title="Playground — PyRLab", page_icon="📝", layout="wide")

st.header("📝 Python Playground")
st.caption("Write Python code and run it instantly. Output appears below.")

# Default code
DEFAULT_CODE = '''# Welcome to the Python Playground!
# Write any Python code here and click "Run".

name = "World"
print(f"Hello, {name}!")

# Lists
numbers = [10, 20, 30, 40, 50]
print(f"Numbers: {numbers}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers)}")

# Dictionary
student = {"name": "Alice", "grade": "A", "score": 95}
for key, value in student.items():
    print(f"  {key}: {value}")
'''

# Code editor
code = st.text_area(
    "Python Code",
    value=DEFAULT_CODE,
    height=350,
    key="playground_code",
    help="Type your Python code here. Click Run to execute.",
)

col1, col2, col3 = st.columns([1, 1, 6])
with col1:
    run_clicked = st.button("▶ Run", type="primary", use_container_width=True)
with col2:
    if st.button("🗑 Clear", use_container_width=True):
        st.session_state["playground_code"] = ""
        st.rerun()

st.divider()

# Execute code safely
if run_clicked:
    st.subheader("📤 Output")

    # Capture stdout and stderr
    stdout_capture = io.StringIO()
    stderr_capture = io.StringIO()

    # Safe globals — allow common safe builtins, block dangerous ones
    safe_builtins = {
        k: v for k, v in __builtins__.__dict__.items()
        if k not in (
            "exec", "eval", "compile", "__import__", "open",
            "exit", "quit", "breakpoint", "globals", "locals",
        )
    }

    # Allow importing safe modules
    allowed_modules = {
        "math", "statistics", "random", "datetime", "collections",
        "itertools", "functools", "string", "re", "json", "csv",
        "fractions", "decimal", "copy", "textwrap", "operator",
    }

    def safe_import(name, *args, **kwargs):
        if name in allowed_modules:
            return __builtins__.__dict__["__import__"](name, *args, **kwargs)
        raise ImportError(
            f"Module '{name}' is not available in the Playground. "
            f"Allowed: {', '.join(sorted(allowed_modules))}"
        )

    safe_globals = {"__builtins__": {**safe_builtins, "__import__": safe_import}}

    try:
        with contextlib.redirect_stdout(stdout_capture), \
             contextlib.redirect_stderr(stderr_capture):
            exec(code, safe_globals)

        output = stdout_capture.getvalue()
        errors = stderr_capture.getvalue()

        if output:
            st.code(output, language="text")
        if errors:
            st.warning(errors)
        if not output and not errors:
            st.info("Code ran successfully with no output. Use `print()` to see results.")

    except Exception:
        error_msg = traceback.format_exc()
        # Clean up the traceback to show only relevant parts
        lines = error_msg.split("\n")
        clean_lines = []
        skip = True
        for line in lines:
            if 'File "<string>"' in line:
                skip = False
            if not skip:
                clean_lines.append(line)
        if clean_lines:
            st.error("\n".join(clean_lines))
        else:
            st.error(error_msg)

else:
    st.info("Write some code above and click **Run** to see the output.")

# Quick examples sidebar
st.divider()
st.subheader("Quick Examples")
st.caption("Click to load an example into the editor.")

examples = {
    "Hello World": 'print("Hello, World!")',
    "Math Operations": """a, b = 10, 3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} ** {b} = {a ** b}")
print(f"{a} % {b} = {a % b}")""",
    "List Operations": """fruits = ["apple", "banana", "cherry", "date"]
print("Original:", fruits)

fruits.append("elderberry")
print("After append:", fruits)

fruits.sort()
print("Sorted:", fruits)

print("Sliced [1:3]:", fruits[1:3])
print("Length:", len(fruits))

# List comprehension
upper = [f.upper() for f in fruits]
print("Uppercase:", upper)""",
    "Dictionary": """person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "coding", "hiking"]
}

for key, value in person.items():
    print(f"{key}: {value}")

print(f"\\n{person['name']} is {person['age']} years old.")
print(f"First hobby: {person['hobbies'][0]}")""",
    "Functions": """def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Hi"))

# Lambda
square = lambda x: x ** 2
numbers = [1, 2, 3, 4, 5]
squares = list(map(square, numbers))
print(f"Squares of {numbers}: {squares}")

# Function with *args
def average(*nums):
    return sum(nums) / len(nums) if nums else 0

print(f"Average of 10,20,30: {average(10, 20, 30)}")""",
    "Statistics": """import statistics

data = [85, 92, 78, 95, 88, 72, 90, 84, 96, 80]
print(f"Data: {data}")
print(f"Mean: {statistics.mean(data):.1f}")
print(f"Median: {statistics.median(data):.1f}")
print(f"Std Dev: {statistics.stdev(data):.1f}")
print(f"Min: {min(data)}")
print(f"Max: {max(data)}")
print(f"Range: {max(data) - min(data)}")

# Frequency
from collections import Counter
grades = ["A","B","A","C","B","A","B","B","A","C"]
freq = Counter(grades)
print(f"\\nGrade frequency: {dict(freq)}")""",
    "String Methods": """text = "  Hello, World! Welcome to Python.  "
print(f"Original: '{text}'")
print(f"Stripped: '{text.strip()}'")
print(f"Upper: '{text.strip().upper()}'")
print(f"Lower: '{text.strip().lower()}'")
print(f"Replace: '{text.strip().replace('World', 'PyRLab')}'")
print(f"Split: {text.strip().split()}")
print(f"Starts with 'Hello': {text.strip().startswith('Hello')}")
print(f"Count 'l': {text.count('l')}")

# f-strings
name, age = "Alice", 25
print(f"\\n{name} is {age} years old.")
print(f"{name} will be {age + 10} in 10 years.")""",
}

cols = st.columns(4)
for i, (name, code_example) in enumerate(examples.items()):
    with cols[i % 4]:
        if st.button(name, key=f"ex_{i}", use_container_width=True):
            st.session_state["playground_code"] = code_example
            st.rerun()
