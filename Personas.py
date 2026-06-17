import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Customer Personas",
    page_icon="👥",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv(
        "../reports/customer_personas.csv"
    )

personas = load_data()

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("👥 Customer Personas")

st.markdown(
    """
    Customer personas help marketing teams understand
    customer behavior and create targeted campaigns.
    """
)

st.divider()

# --------------------------------------------------
# PERSONA CARDS
# --------------------------------------------------

for _, row in personas.iterrows():

    st.markdown(
        f"""
        <div style="
            background-color:#111827;
            padding:20px;
            border-radius:15px;
            margin-bottom:20px;
            border:1px solid #374151;
        ">
            <h2 style="color:#60A5FA;">
                {row['Persona_Name']}
            </h2>

            <h4>
                Cluster: {row['Cluster']}
            </h4>

            <p>
                <b>Business Value:</b>
                {row['Business_Value']}
            </p>

            <p>
                <b>Marketing Focus:</b>
                {row['Marketing_Focus']}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# PERSONA DETAILS
# --------------------------------------------------

st.subheader("Persona Summary Table")

st.dataframe(
    personas,
    use_container_width=True
)

# --------------------------------------------------
# PERSONA DESCRIPTIONS
# --------------------------------------------------

st.subheader("Detailed Persona Profiles")

persona_details = {

    "Premium Protection Customers":
    {
        "Age":"35-55",
        "Income":"High",
        "Behavior":"High premium and high coverage",
        "Strategy":"VIP loyalty programs and premium offers"
    },

    "Value Seeking Customers":
    {
        "Age":"25-40",
        "Income":"Medium",
        "Behavior":"Price sensitive",
        "Strategy":"Discount campaigns and bundle offers"
    },

    "Wealthy Low-Risk Customers":
    {
        "Age":"40-60",
        "Income":"Very High",
        "Behavior":"Stable and profitable",
        "Strategy":"Investment-linked insurance products"
    },

    "Affluent Growth Customers":
    {
        "Age":"30-50",
        "Income":"High",
        "Behavior":"Growth potential",
        "Strategy":"Upselling and personalized products"
    },

    "Senior Loyal Customers":
    {
        "Age":"55+",
        "Income":"Medium to High",
        "Behavior":"Long-term customers",
        "Strategy":"Retention and relationship management"
    }

}

for persona, details in persona_details.items():

    with st.expander(persona):

        st.write(
            f"**Age Group:** {details['Age']}"
        )

        st.write(
            f"**Income Level:** {details['Income']}"
        )

        st.write(
            f"**Behavior:** {details['Behavior']}"
        )

        st.write(
            f"**Marketing Strategy:** {details['Strategy']}"
        )

# --------------------------------------------------
# BUSINESS INSIGHTS
# --------------------------------------------------

st.subheader("Business Insights")

st.info(
    """
    • Premium customers generate the highest revenue.

    • Value-seeking customers respond well to discounts.

    • Wealthy customers are ideal for cross-selling.

    • Growth customers offer strong upselling opportunities.

    • Senior customers require retention-focused campaigns.
    """
)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Customer Personas | Marketing Intelligence Dashboard"
)