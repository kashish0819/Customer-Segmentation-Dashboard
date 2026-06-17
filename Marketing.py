import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Marketing Recommendations",
    page_icon="📢",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv(
        "../reports/marketing_recommendations.csv"
    )

marketing = load_data()

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("📢 Marketing Strategy Dashboard")

st.markdown("""
This section provides cluster-specific marketing recommendations
to improve customer acquisition, retention, loyalty, and revenue growth.
""")

st.divider()

# --------------------------------------------------
# OVERVIEW KPIs
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Customer Segments",
        len(marketing)
    )

with col2:
    st.metric(
        "Retention Plans",
        len(marketing)
    )

with col3:
    st.metric(
        "Upselling Strategies",
        len(marketing)
    )

with col4:
    st.metric(
        "Cross-Selling Plans",
        len(marketing)
    )

st.divider()

# --------------------------------------------------
# STRATEGY TABLE
# --------------------------------------------------

st.subheader("Marketing Strategy Matrix")

st.dataframe(
    marketing,
    use_container_width=True
)

# --------------------------------------------------
# CLUSTER STRATEGIES
# --------------------------------------------------

st.subheader("Cluster Wise Recommendations")

for _, row in marketing.iterrows():

    with st.expander(
        f"Cluster {row['Cluster']} Marketing Plan"
    ):

        st.markdown(
            f"""
### 🎯 Retention Strategy
{row['Retention_Strategy']}

### 📈 Upselling Strategy
{row['Upselling']}

### 🔄 Cross-Selling Strategy
{row['Cross_Selling']}

### ⭐ Loyalty Program
{row['Loyalty_Program']}
"""
        )

# --------------------------------------------------
# RETENTION CHART
# --------------------------------------------------

st.subheader("Retention Strategy Distribution")

retention_counts = (
    marketing["Retention_Strategy"]
    .value_counts()
    .reset_index()
)

retention_counts.columns = [
    "Strategy",
    "Count"
]

fig = px.bar(
    retention_counts,
    x="Strategy",
    y="Count",
    text="Count",
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
# MARKETING FRAMEWORK
# --------------------------------------------------

st.subheader("Recommended Marketing Framework")

col1, col2 = st.columns(2)

with col1:

    st.success("""
### Customer Retention

✔ VIP Programs

✔ Dedicated Support

✔ Personalized Communication

✔ Loyalty Rewards

✔ Renewal Benefits
""")

with col2:

    st.info("""
### Customer Growth

✔ Cross-Selling

✔ Upselling

✔ Referral Programs

✔ Targeted Campaigns

✔ Personalized Recommendations
""")

# --------------------------------------------------
# EMAIL CAMPAIGNS
# --------------------------------------------------

st.subheader("Email Campaign Recommendations")

email_campaigns = pd.DataFrame({

    "Campaign":[
        "Welcome Campaign",
        "Renewal Reminder",
        "Cross-Sell Campaign",
        "Premium Upgrade",
        "Loyalty Rewards"
    ],

    "Objective":[
        "Customer Onboarding",
        "Retention",
        "Cross-Selling",
        "Upselling",
        "Engagement"
    ]
})

st.dataframe(
    email_campaigns,
    use_container_width=True
)

# --------------------------------------------------
# SOCIAL MEDIA CAMPAIGNS
# --------------------------------------------------

st.subheader("Social Media Campaign Strategy")

social_df = pd.DataFrame({

    "Platform":[
        "Facebook",
        "Instagram",
        "LinkedIn",
        "YouTube",
        "WhatsApp"
    ],

    "Strategy":[
        "Brand Awareness",
        "Customer Engagement",
        "Professional Audience",
        "Educational Content",
        "Direct Communication"
    ]
})

st.dataframe(
    social_df,
    use_container_width=True
)

# --------------------------------------------------
# EXECUTIVE INSIGHTS
# --------------------------------------------------

st.subheader("Executive Marketing Insights")

st.warning("""
1. High-income customers should receive premium product recommendations.

2. Medium-value customers are ideal targets for bundled offers.

3. Loyalty programs can significantly improve retention rates.

4. Personalized campaigns increase conversion and engagement.

5. Segment-specific communication improves marketing ROI.
""")

# --------------------------------------------------
# DOWNLOAD SECTION
# --------------------------------------------------

st.subheader("Download Marketing Report")

csv = marketing.to_csv(
    index=False
)

st.download_button(
    label="📥 Download Marketing Recommendations",
    data=csv,
    file_name="marketing_recommendations.csv",
    mime="text/csv"
)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Marketing Strategy Dashboard | Customer Segmentation Project"
)