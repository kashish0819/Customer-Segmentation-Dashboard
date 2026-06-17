import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# LOAD CSS
# --------------------------------------------------

with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():

    customers = pd.read_csv(
        "../data/clustered_customers.csv"
    )

    personas = pd.read_csv(
        "../reports/customer_personas.csv"
    )

    marketing = pd.read_csv(
        "../reports/marketing_recommendations.csv"
    )

    return customers, personas, marketing


df, personas, marketing = load_data()

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
<div class='header'>
<h1>📊 Customer Segmentation Analytics Dashboard</h1>
<p>Customer Intelligence • Marketing Analytics • Segmentation Insights</p>
</div>
""",
unsafe_allow_html=True)

st.write("")

# --------------------------------------------------
# KPI SECTION
# --------------------------------------------------

total_customers = len(df)

avg_income = round(
    df["Income Level"].mean(),
    0
)

avg_coverage = round(
    df["Coverage Amount"].mean(),
    0
)

avg_premium = round(
    df["Premium Amount"].mean(),
    0
)

total_segments = df["Cluster"].nunique()

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "Customers",
        f"{total_customers:,}"
    )

with col2:
    st.metric(
        "Avg Income",
        f"₹ {avg_income:,.0f}"
    )

with col3:
    st.metric(
        "Coverage",
        f"₹ {avg_coverage:,.0f}"
    )

with col4:
    st.metric(
        "Premium",
        f"₹ {avg_premium:,.0f}"
    )

with col5:
    st.metric(
        "Segments",
        total_segments
    )

st.divider()

# --------------------------------------------------
# CLUSTER DISTRIBUTION
# --------------------------------------------------

st.subheader("Customer Segment Distribution")

cluster_count = (
    df["Cluster"]
    .value_counts()
    .reset_index()
)

cluster_count.columns = [
    "Cluster",
    "Customers"
]

fig = px.bar(
    cluster_count,
    x="Cluster",
    y="Customers",
    text="Customers",
    color="Cluster",
    template="plotly_dark"
)

fig.update_layout(
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# AGE DISTRIBUTION
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("Age Distribution")

    fig = px.histogram(
        df,
        x="Age",
        nbins=30,
        template="plotly_dark"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    st.subheader("Income Distribution")

    fig = px.histogram(
        df,
        x="Income Level",
        nbins=30,
        template="plotly_dark"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# --------------------------------------------------
# CLUSTER COMPARISON
# --------------------------------------------------

st.subheader(
    "Cluster Income Analysis"
)

cluster_income = (
    df.groupby("Cluster")[
        "Income Level"
    ]
    .mean()
    .reset_index()
)

fig = px.bar(
    cluster_income,
    x="Cluster",
    y="Income Level",
    color="Cluster",
    template="plotly_dark"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# COVERAGE VS PREMIUM
# --------------------------------------------------

st.subheader(
    "Coverage vs Premium"
)

fig = px.scatter(
    df.sample(5000),
    x="Coverage Amount",
    y="Premium Amount",
    color="Cluster",
    template="plotly_dark"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# TOP INSIGHTS
# --------------------------------------------------

st.subheader(
    "Executive Insights"
)

st.success("""
✔ Customer segmentation successfully identified meaningful customer groups.

✔ K-Means clustering produced the most interpretable segments.

✔ High-income customer groups represent the greatest revenue opportunity.

✔ Premium-paying customers should be targeted through loyalty programs.

✔ Personalized marketing can significantly improve retention and upselling.
""")

# --------------------------------------------------
# DOWNLOAD SECTION
# --------------------------------------------------

st.subheader(
    "Download Reports"
)

col1, col2 = st.columns(2)

with col1:

    csv = personas.to_csv(
        index=False
    )

    st.download_button(
        "Download Personas",
        csv,
        file_name="customer_personas.csv"
    )

with col2:

    csv = marketing.to_csv(
        index=False
    )

    st.download_button(
        "Download Marketing Report",
        csv,
        file_name="marketing_recommendations.csv"
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Customer Segmentation Dashboard | Built with Streamlit, Plotly & Machine Learning"
)