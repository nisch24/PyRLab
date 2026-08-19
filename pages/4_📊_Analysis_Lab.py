"""
PyRLab — Analysis Lab
Upload CSV data, explore it with pandas, compute statistics, and build charts.
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
import statistics as stat_module

st.set_page_config(page_title="Analysis Lab — PyRLab", page_icon="📊", layout="wide")

st.header("📊 Analysis Lab")
st.caption("Upload data, explore it, compute statistics, and build visualizations — all in Python.")

# --- Sample datasets ---
SAMPLES = {
    "Sales Data": """Product,Quarter,Revenue,Units
Widget A,Q1,12000,150
Widget A,Q2,15000,190
Widget A,Q3,14000,175
Widget B,Q1,8000,95
Widget B,Q2,9500,110
Widget B,Q3,10200,125
Widget C,Q1,22000,280
Widget C,Q2,25000,310
Widget C,Q3,27000,340""",
    "Student Grades": """Student,Math,Science,English,History,Art
Alice,92,88,95,78,85
Bob,85,90,82,88,91
Carol,78,72,90,85,80
Dave,95,94,88,92,76
Eve,88,85,76,80,93
Frank,72,68,85,90,87
Grace,91,93,89,84,78""",
    "Monthly Budget": """Category,Jan,Feb,Mar,Apr,May,Jun
Rent,1200,1200,1200,1200,1200,1200
Food,450,380,420,400,440,390
Transport,150,130,160,140,135,155
Entertainment,100,120,80,95,110,130
Utilities,200,210,190,205,195,215
Savings,300,400,350,500,450,380""",
    "Survey Results": """Respondent,Age,Satisfaction,Recommend,Category
Alice,25,4,Yes,Student
Bob,34,5,Yes,Professional
Carol,22,3,No,Student
Dave,41,5,Yes,Professional
Eve,19,2,No,Student
Frank,38,4,Yes,Professional
Grace,27,5,Yes,Student
Hank,45,3,No,Professional
Iris,23,4,Yes,Student
Jack,36,5,Yes,Professional""",
}

# --- Data Loading ---
st.subheader("1️⃣ Load Data")

tab_upload, tab_sample, tab_paste = st.tabs(["📁 Upload CSV", "📋 Sample Dataset", "📝 Paste Data"])

with tab_upload:
    uploaded = st.file_uploader("Choose a CSV file", type=["csv"])
    if uploaded:
        st.session_state["analysis_df"] = pd.read_csv(uploaded)
        st.success(f"Loaded {uploaded.name}")

with tab_sample:
    sample_name = st.selectbox("Choose a sample dataset:", list(SAMPLES.keys()))
    if st.button("Load Sample", type="primary"):
        st.session_state["analysis_df"] = pd.read_csv(io.StringIO(SAMPLES[sample_name]))
        st.success(f"Loaded '{sample_name}'")

with tab_paste:
    pasted = st.text_area("Paste CSV data:", height=150,
                          placeholder="Name,Age,Score\nAlice,25,92\nBob,30,85")
    if st.button("Parse Pasted Data"):
        if pasted.strip():
            try:
                st.session_state["analysis_df"] = pd.read_csv(io.StringIO(pasted))
                st.success("Data parsed!")
            except Exception as e:
                st.error(f"Parse error: {e}")

# --- If data is loaded ---
if "analysis_df" in st.session_state:
    df = st.session_state["analysis_df"]

    st.divider()
    st.subheader("2️⃣ Explore Data")

    # Overview metrics
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Rows", df.shape[0])
    c2.metric("Columns", df.shape[1])
    c3.metric("Numeric Cols", len(df.select_dtypes(include="number").columns))
    c4.metric("Text Cols", len(df.select_dtypes(exclude="number").columns))

    # Data preview
    view_tab, stats_tab, code_tab = st.tabs(["📋 Data Table", "📈 Statistics", "🐍 Python Code"])

    with view_tab:
        st.dataframe(df, use_container_width=True, height=300)

    with stats_tab:
        numeric_cols = df.select_dtypes(include="number").columns.tolist()
        if numeric_cols:
            st.markdown("**Numeric Column Statistics:**")
            st.dataframe(df[numeric_cols].describe().round(2), use_container_width=True)

            # Per-column stats
            for col in numeric_cols:
                vals = df[col].dropna().tolist()
                if vals:
                    with st.expander(f"📊 {col}"):
                        mc1, mc2, mc3, mc4, mc5 = st.columns(5)
                        mc1.metric("Mean", f"{pd.Series(vals).mean():.2f}")
                        mc2.metric("Median", f"{pd.Series(vals).median():.2f}")
                        mc3.metric("Std Dev", f"{pd.Series(vals).std():.2f}")
                        mc4.metric("Min", f"{min(vals)}")
                        mc5.metric("Max", f"{max(vals)}")
        else:
            st.info("No numeric columns found.")

        # Categorical stats
        cat_cols = df.select_dtypes(exclude="number").columns.tolist()
        if cat_cols:
            st.markdown("**Categorical Column Counts:**")
            for col in cat_cols:
                with st.expander(f"🏷️ {col} — {df[col].nunique()} unique values"):
                    st.dataframe(df[col].value_counts().reset_index(), use_container_width=True)

    with code_tab:
        st.markdown("**Here's the Python code to reproduce this analysis:**")
        code = f'''import pandas as pd

# Load data
df = pd.read_csv("your_data.csv")

# Preview
print(df.head())
print(f"Shape: {{df.shape}}")

# Statistics
print(df.describe())

# Column types
print(df.dtypes)
'''
        if numeric_cols:
            code += f'''
# Specific column stats
for col in {numeric_cols}:
    print(f"{{col}}: mean={{df[col].mean():.2f}}, median={{df[col].median():.2f}}")
'''
        st.code(code, language="python")

    # --- Charts ---
    st.divider()
    st.subheader("3️⃣ Visualize")

    if numeric_cols:
        chart_type = st.selectbox("Chart Type:", ["Bar Chart", "Line Chart", "Histogram", "Scatter Plot", "Pie Chart"])

        col_left, col_right = st.columns(2)

        with col_left:
            if chart_type in ("Bar Chart", "Line Chart", "Pie Chart"):
                label_col = st.selectbox("Label Column (X):", df.columns.tolist())
                value_col = st.selectbox("Value Column (Y):", numeric_cols)
            elif chart_type == "Histogram":
                value_col = st.selectbox("Column:", numeric_cols)
                bins = st.slider("Bins:", 5, 50, 15)
            elif chart_type == "Scatter Plot":
                x_col = st.selectbox("X Column:", numeric_cols, index=0)
                y_col = st.selectbox("Y Column:", numeric_cols, index=min(1, len(numeric_cols) - 1))

            chart_title = st.text_input("Chart Title:", f"My {chart_type}")

        with col_right:
            fig, ax = plt.subplots(figsize=(8, 5))

            try:
                if chart_type == "Bar Chart":
                    colors = ["#0d9488", "#2563eb", "#7c3aed", "#db2777", "#ea580c",
                              "#16a34a", "#0891b2", "#4f46e5", "#d97706", "#059669"]
                    bar_data = df.groupby(label_col)[value_col].sum().reset_index()
                    ax.bar(bar_data[label_col].astype(str), bar_data[value_col],
                           color=[colors[i % len(colors)] for i in range(len(bar_data))])
                    ax.set_xlabel(label_col)
                    ax.set_ylabel(value_col)
                    plt.xticks(rotation=45, ha="right")

                elif chart_type == "Line Chart":
                    ax.plot(df[label_col].astype(str), df[value_col],
                            marker="o", color="#0d9488", linewidth=2)
                    ax.fill_between(range(len(df)), df[value_col], alpha=0.1, color="#0d9488")
                    ax.set_xlabel(label_col)
                    ax.set_ylabel(value_col)
                    plt.xticks(rotation=45, ha="right")

                elif chart_type == "Histogram":
                    ax.hist(df[value_col].dropna(), bins=bins, color="#0d9488",
                            edgecolor="white", alpha=0.8)
                    ax.set_xlabel(value_col)
                    ax.set_ylabel("Frequency")

                elif chart_type == "Scatter Plot":
                    ax.scatter(df[x_col], df[y_col], color="#0d9488", alpha=0.7, s=60)
                    ax.set_xlabel(x_col)
                    ax.set_ylabel(y_col)

                elif chart_type == "Pie Chart":
                    pie_data = df.groupby(label_col)[value_col].sum()
                    ax.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%",
                           colors=["#0d9488", "#2563eb", "#7c3aed", "#db2777",
                                   "#ea580c", "#16a34a", "#0891b2"])

                ax.set_title(chart_title)
                plt.tight_layout()
                st.pyplot(fig)
                plt.close()

            except Exception as e:
                st.error(f"Chart error: {e}")

        # Show code for the chart
        with st.expander("🐍 Show Python code for this chart"):
            if chart_type == "Bar Chart":
                st.code(f'''import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("your_data.csv")
bar_data = df.groupby("{label_col}")["{value_col}"].sum()
bar_data.plot(kind="bar", color="#0d9488")
plt.title("{chart_title}")
plt.ylabel("{value_col}")
plt.tight_layout()
plt.show()''', language="python")
            elif chart_type == "Histogram":
                st.code(f'''import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("your_data.csv")
df["{value_col}"].hist(bins={bins}, color="#0d9488", edgecolor="white")
plt.title("{chart_title}")
plt.xlabel("{value_col}")
plt.ylabel("Frequency")
plt.show()''', language="python")

    else:
        st.info("Load data with numeric columns to create charts.")

    # --- Export ---
    st.divider()
    st.subheader("4️⃣ Export")

    ec1, ec2 = st.columns(2)
    with ec1:
        csv_output = df.to_csv(index=False)
        st.download_button("⬇ Download CSV", csv_output, "analysis_output.csv", "text/csv")
    with ec2:
        summary = f"# Analysis Report\n\n**Shape:** {df.shape[0]} rows × {df.shape[1]} columns\n\n"
        summary += "## Column Types\n\n"
        for col in df.columns:
            summary += f"- **{col}**: {df[col].dtype}\n"
        if numeric_cols:
            summary += "\n## Statistics\n\n"
            summary += df[numeric_cols].describe().round(2).to_markdown()
        st.download_button("⬇ Download Report (Markdown)", summary, "report.md", "text/markdown")

else:
    st.info("👆 Load a dataset above to start analyzing!")
    st.markdown("""
    **What you can do in the Analysis Lab:**
    - Upload your own CSV file or use a sample dataset
    - View data in interactive tables
    - Compute statistics (mean, median, std dev, etc.)
    - Create bar charts, line charts, histograms, scatter plots, and pie charts
    - See the Python code behind every analysis
    - Export your data and reports
    """)
