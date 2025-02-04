import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def rent_vs_buy(rent, rent_increase, home_price, deposit, interest_rate, loan_term, 
                property_appreciation, stamp_duty, annual_rates, 
                insurance, maintenance, investment_return, years):
    # Renting Costs
    total_rent_paid = 0
    current_rent = rent
    rent_costs = []
    for _ in range(years):
        total_rent_paid += current_rent * 12
        rent_costs.append(total_rent_paid)
        current_rent *= (1 + rent_increase / 100)
    
    # Buying Costs
    loan_amount = home_price - deposit
    monthly_interest = (interest_rate / 100) / 12
    num_payments = loan_term * 12
    mortgage_payment = (loan_amount * monthly_interest * (1 + monthly_interest) ** num_payments) / \
                       ((1 + monthly_interest) ** num_payments - 1)
    total_mortgage_paid = mortgage_payment * 12 * min(years, loan_term)
    
    # Additional Costs of Homeownership
    property_value = home_price * (1 + property_appreciation / 100) ** years
    total_maintenance = maintenance * years
    total_insurance = insurance * years
    total_rates = annual_rates * years
    
    # Investment Opportunity Cost (If Renting)
    invested_deposit = deposit
    total_investment_value = invested_deposit * (1 + investment_return / 100) ** years
    
    # Total Cost Comparison
    total_buying_cost = total_mortgage_paid + stamp_duty + total_maintenance + total_insurance + total_rates
    total_renting_cost = total_rent_paid - total_investment_value
    
    return total_renting_cost, total_buying_cost, property_value, rent_costs

st.set_page_config(page_title="Rent vs. Buy Calculator", page_icon="🏡", layout="wide")
st.title("🏡 Rent vs. Buy Calculator - Australia")

# Layout: Columns for better spacing
col1, col2 = st.columns(2)
with col1:
    rent = st.number_input("Monthly Rent ($)", value=2000)
    rent_increase = st.number_input("Annual Rent Increase (%)", value=3)
    home_price = st.number_input("Home Price ($)", value=600000)
    deposit = st.number_input("Deposit ($)", value=60000)
    interest_rate = st.number_input("Mortgage Interest Rate (%)", value=5.0)
    loan_term = st.number_input("Loan Term (Years)", value=30)
    
with col2:
    property_appreciation = st.number_input("Annual Property Appreciation (%)", value=3.0)
    stamp_duty = st.number_input("Stamp Duty ($)", value=20000)
    annual_rates = st.number_input("Annual Council Rates ($)", value=2000)
    insurance = st.number_input("Annual Home Insurance ($)", value=1500)
    maintenance = st.number_input("Annual Maintenance Costs ($)", value=1000)
    investment_return = st.number_input("Investment Return (%)", value=5.0)
    years = st.number_input("Years to Compare", value=10)

if st.button("📊 Calculate Comparison"):
    total_renting_cost, total_buying_cost, property_value, rent_costs = rent_vs_buy(
        rent, rent_increase, home_price, deposit, interest_rate, loan_term, 
        property_appreciation, stamp_duty, annual_rates, 
        insurance, maintenance, investment_return, years)
    
    # Display results with colored metrics
    st.metric(label="🏠 Buying Cost", value=f"${total_buying_cost:,.2f}")
    st.metric(label="🏡 Renting Cost", value=f"${total_renting_cost:,.2f}")
    st.metric(label="📈 Estimated Property Value", value=f"${property_value:,.2f}")
    
    # Create a comparison chart
    fig, ax = plt.subplots()
    ax.bar(["Renting", "Buying"], [total_renting_cost, total_buying_cost], color=["red", "green"])
    ax.set_ylabel("Total Cost ($)")
    ax.set_title("Rent vs. Buy Cost Comparison")
    st.pyplot(fig)
    
    # Rent cost trend over time
    fig2, ax2 = plt.subplots()
    ax2.plot(range(1, years + 1), rent_costs, marker="o", linestyle="-", color="blue")
    ax2.set_xlabel("Years")
    ax2.set_ylabel("Total Rent Paid ($)")
    ax2.set_title("Rent Paid Over Time")
    st.pyplot(fig2)
