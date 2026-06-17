import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="🎯",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():

    customers = pd.read_csv(
        "../data/clustered_customers.csv"
    )

    pca_data = pd.read_csv(
        "../data/pca_data.csv"
    )

    cluster_profile = pd.read_csv(
        "../reports/cluster_profile.csv"
    )

    return customers, pca_data, cluster_profile


df, pca_df, cluster_profile = load_data()

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🎯 Customer Segmentation Analysis")

st.markdown(
    """
    Analyze customer clusters generated using
    K-Means Machine Learning algorithm.
    """
)

st.divider()

# --------------------------------------------------
# KPI SECTION
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Customers",
        f"{len(df):,}"
    )

with col2:
    st.metric(
        "Clusters",
        df["Cluster"].nunique()
    )

with col3:
    st.metric(
        "Average Income",
        f"₹ {df['Income Level'].mean():,.0f}"
    )

st.divider()

# --------------------------------------------------
# CLUSTER DISTRIBUTION
# --------------------------------------------------

st.subheader("Customer Segment Distribution")

cluster_counts = (
    df["Cluster"]
    .value_counts()
    .reset_index()
)

cluster_counts.columns = [
    "Cluster",
    "Customers"
]

fig = px.bar(
    cluster_counts,
    x="Cluster",
    y="Customers",
    color="Cluster",
    text="Customers",
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
# PIE CHART
# --------------------------------------------------

st.subheader("Segment Share")

fig = px.pie(
    cluster_counts,
    values="Customers",
    names="Cluster",
    hole=0.5
)

fig.update_layout(
    height=600
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# PCA VISUALIZATION
# --------------------------------------------------

st.subheader("PCA Cluster Visualization")

if "Cluster" in pca_df.columns:

    fig = px.scatter(
        pca_df,
        x="PC1",
        y="PC2",
        color="Cluster",
        opacity=0.8,
        template="plotly_dark"
    )

    fig.update_layout(
        height=650
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:

    st.warning(
        "Cluster column missing in pca_data.csv"
    )

# --------------------------------------------------
# CLUSTER PROFILE TABLE
# --------------------------------------------------

st.subheader("Cluster Profile Summary")

st.dataframe(
    cluster_profile,
    use_container_width=True
)

# --------------------------------------------------
# CLUSTER INCOME COMPARISON
# --------------------------------------------------

st.subheader("Average Income by Cluster")

income_data = (
    df.groupby("Cluster")
    ["Income Level"]
    .mean()
    .reset_index()
)

fig = px.bar(
    income_data,
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
# COVERAGE COMPARISON
# --------------------------------------------------

st.subheader("Average Coverage Amount")

coverage_data = (
    df.groupby("Cluster")
    ["Coverage Amount"]
    .mean()
    .reset_index()
)

fig = px.bar(
    coverage_data,
    x="Cluster",
    y="Coverage Amount",
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
# PREMIUM COMPARISON
# --------------------------------------------------

st.subheader("Average Premium Amount")

premium_data = (
    df.groupby("Cluster")
    ["Premium Amount"]
    .mean()
    .reset_index()
)

fig = px.bar(
    premium_data,
    x="Cluster",
    y="Premium Amount",
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
# INTERACTIVE FILTER
# --------------------------------------------------

st.subheader("Explore Cluster Details")

selected_cluster = st.selectbox(
    "Select Cluster",
    sorted(df["Cluster"].unique())
)

filtered_df = df[
    df["Cluster"] == selected_cluster
]

st.dataframe(
    filtered_df.head(100),
    use_container_width=True
)

# --------------------------------------------------
# CLUSTER INSIGHTS
# --------------------------------------------------

st.subheader("Segmentation Insights")

st.success(
    """
    ✔ K-Means successfully identified distinct customer segments.

    ✔ Different clusters demonstrate unique income,
      premium and coverage behaviors.

    ✔ High-income clusters can be targeted with premium products.

    ✔ Medium-value customers offer strong cross-selling opportunities.

    ✔ Segmentation enables personalized marketing campaigns.
    """
)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Customer Segmentation Analysis | K-Means Clustering"
)