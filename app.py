import streamlit as st

st.title("🧾 Rough Aussie Tax + Take-Home Estimator 2025–26")
st.caption("For Australian residents — NOT official tax advice! Just for learning & playing.")

st.markdown("---")

# Main inputs
col1, col2 = st.columns(2)

with col1:
    gross_income = st.number_input(
        "Your gross yearly income ($)",
        min_value=0.0,
        value=85000.0,
        step=1000.0,
        format="%.0f"
    )

with col2:
    include_medicare = st.checkbox("Include rough 2% Medicare levy?", value=True)

# Very simplified — no offsets, no HELP/HECS, no low-income tax offset, etc.
def calculate_tax(income):
    if income <= 18200:
        return 0
    elif income <= 45000:
        return (income - 18200) * 0.16
    elif income <= 135000:
        return 4288 + (income - 45000) * 0.30
    elif income <= 190000:
        return 31288 + (income - 135000) * 0.37
    else:
        return 51638 + (income - 190000) * 0.45

tax = calculate_tax(gross_income)

medicare = gross_income * 0.02 if include_medicare else 0
# (in reality many people get exemptions/reductions — this is very rough)

total_tax = tax + medicare
take_home = gross_income - total_tax

st.markdown("### Results")

col_a, col_b, col_c = st.columns(3)

col_a.metric("Gross Income", f"${gross_income:,.0f}")
col_b.metric("Estimated Income Tax", f"${tax:,.0f}", delta_color="inverse")
col_c.metric("Medicare Levy (rough)", f"${medicare:,.0f}", delta_color="inverse")

st.metric("**Total Tax + Levy**", f"${total_tax:,.0f}", delta=f"-${total_tax:,.0f}", delta_color="inverse")
st.metric("**Approximate Take-Home Pay**", f"${take_home:,.0f}", delta_color="normal")

st.info("ℹ️ This uses **2025–26 resident rates** (post-Stage 3 tax cuts). From July 2026 the 16% bracket drops to 15%, etc. Real tax depends on deductions, offsets, HELP debt, etc.")

st.markdown("---")
st.caption("Next versions: super contributions • monthly budget • expense categories • charts • CSV upload")