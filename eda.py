import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="EDA Dashboard",
    page_icon="📈",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("../data/clustered_customers.csv")

df = load_data()

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("📈 Exploratory Data Analysis")

st.markdown(
    "Comprehensive analysis of customer demographics, income, coverage and premium behavior."
)

st.divider()

# --------------------------------------------------
# DATASET OVERVIEW
# --------------------------------------------------

st.subheader("Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Rows",
        f"{df.shape[0]:,}"
    )

with col2:
    st.metric(
        "Columns",
        df.shape[1]
    )

with col3:
    st.metric(
        "Avg Age",
        round(df["Age"].mean(),1)
    )

with col4:
    st.metric(
        "Avg Income",
        f"₹ {df['Income Level'].mean():,.0f}"
    )

st.divider()

# --------------------------------------------------
# AGE DISTRIBUTION
# --------------------------------------------------

st.subheader("Age Distribution")

fig = px.histogram(
    df,
    x="Age",
    nbins=30,
    color_discrete_sequence=["#4F46E5"]
)

fig.update_layout(
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# INCOME DISTRIBUTION
# --------------------------------------------------

st.subheader("Income Level Distribution")

fig = px.histogram(
    df,
    x="Income Level",
    nbins=40,
    color_discrete_sequence=["#10B981"]
)

fig.update_layout(
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# COVERAGE VS PREMIUM
# --------------------------------------------------

st.subheader("Coverage Amount vs Premium Amount")

sample_df = df.sample(
    min(5000, len(df)),
    random_state=42
)

fig = px.scatter(
    sample_df,
    x="Coverage Amount",
    y="Premium Amount",
    color="Cluster",
    hover_data=["Age"]
)

fig.update_layout(
    height=600
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# BOXPLOTS
# --------------------------------------------------

st.subheader("Outlier Analysis")

col1, col2 = st.columns(2)

with col1:

    fig = px.box(
        df,
        y="Income Level",
        title="Income Level Boxplot"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    fig = px.box(
        df,
        y="Premium Amount",
        title="Premium Amount Boxplot"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# --------------------------------------------------
# CORRELATION HEATMAP
# --------------------------------------------------

st.subheader("Correlation Analysis")

numeric_df = df.select_dtypes(
    include=["int64", "float64"]
)

corr = numeric_df.corr()

fig = ff.create_annotated_heatmap(
    z=corr.values,
    x=list(corr.columns),
    y=list(corr.index),
    annotation_text=round(corr,2).values,
    showscale=True
)

fig.update_layout(
    height=700
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# SEGMENT WISE AGE
# --------------------------------------------------

st.subheader("Age by Customer Segment")

fig = px.box(
    df,
    x="Cluster",
    y="Age",
    color="Cluster"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# SEGMENT WISE INCOME
# --------------------------------------------------

st.subheader("Income by Customer Segment")

cluster_income = (
    df.groupby("Cluster")["Income Level"]
    .mean()
    .reset_index()
)

fig = px.bar(
    cluster_income,
    x="Cluster",
    y="Income Level",
    color="Cluster",
    text_auto=True
)

fig.update_layout(
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# BUSINESS INSIGHTS
# --------------------------------------------------

st.subheader("Business Insights")

st.info("""
• Customer income distribution shows multiple spending capacities.

• Coverage amount is positively associated with premium amount.

• Distinct customer segments display different income patterns.

• High-income clusters provide opportunities for premium products.

• Personalized campaigns can improve customer engagement and retention.
""")