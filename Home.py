"""
PyRLab — Home Page
A comprehensive offline learning tool for Python.
Built with Streamlit.
"""
import streamlit as st

st.set_page_config(
    page_title="PyRLab — Learn Python",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS
st.markdown("""
<style>
    .main-title { font-size: 2.5rem; font-weight: 800; color: #0d9488; margin-bottom: 0; }
    .subtitle { font-size: 1.1rem; color: #64748b; margin-top: 0; }
    .feature-card {
        background: linear-gradient(135deg, #f0fdfa 0%, #e0f2fe 100%);
        border: 1px solid #99f6e4;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        transition: transform 0.2s;
    }
    .feature-card h3 { color: #0d9488; margin-top: 0.5rem; }
    .feature-card p { color: #475569; font-size: 0.9rem; }
    .tip-box {
        background: #f0fdfa;
        border-left: 4px solid #14b8a6;
        padding: 1rem 1.2rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<p class="main-title">🐍 PyRLab</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your offline learning companion for Python — tutorials, reference, code playground, and data analysis tools</p>', unsafe_allow_html=True)
st.divider()

# --- Feature Cards ---
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div style="font-size:2rem;">📝</div>
        <h3>Playground</h3>
        <p>Write and run Python code live</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div style="font-size:2rem;">📖</div>
        <h3>Reference</h3>
        <p>Searchable docs for 50+ topics</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div style="font-size:2rem;">🎓</div>
        <h3>Tutorials</h3>
        <p>12 step-by-step lessons</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card">
        <div style="font-size:2rem;">📊</div>
        <h3>Analysis Lab</h3>
        <p>Real data analysis tasks</p>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="feature-card">
        <div style="font-size:2rem;">✂️</div>
        <h3>Snippets</h3>
        <p>Copy-ready code examples</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- Getting Started ---
st.subheader("🚀 Getting Started")
st.markdown("""
Use the **sidebar** (← left) to navigate between modules:

1. **Playground** — Write Python code and see instant output. Great for experimenting.
2. **Reference** — Look up any Python concept, with syntax and examples.
3. **Tutorials** — Follow 12 progressive lessons from variables to data analysis.
4. **Analysis Lab** — Upload CSV data, compute statistics, and build charts.
5. **Snippets** — Browse and copy ready-to-use code examples.
""")

st.markdown("""
<div class="tip-box">
    <strong>💡 Tip:</strong> You don't need an internet connection to use this tool.
    Everything runs locally on your computer with Python and Streamlit.
</div>
""", unsafe_allow_html=True)

# --- Quick Python Demo ---
st.subheader("⚡ Quick Demo — Python Runs Right Here")
st.code("""
# Python can do math
result = 2 ** 10
print(f"2 to the power of 10 = {result}")

# Work with lists
fruits = ["apple", "banana", "cherry"]
print(f"Fruits: {fruits}")
print(f"First fruit: {fruits[0]}")
""", language="python")

if st.button("▶ Run This Demo", type="primary"):
    st.write("**Output:**")
    result = 2 ** 10
    st.code(f"2 to the power of 10 = {result}")
    fruits = ["apple", "banana", "cherry"]
    st.code(f"Fruits: {fruits}\nFirst fruit: {fruits[0]}")
    st.success("✅ Python is working! Head to the Playground to write your own code.")
