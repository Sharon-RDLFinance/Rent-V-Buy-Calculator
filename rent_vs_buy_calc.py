import streamlit as st
import numpy as np

def rent_vs_buy(rent, rent_increase, home_price, deposit, interest_rate, loan_term, 
                property_appreciation, stamp_duty, annual_rates, 
                insurance, maintenance, investment_return, years):
    # Renting Costs
    total_rent_paid = 0
    current_rent = rent
    for _ in range(years):
        total_rent_paid += current_rent * 12
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
    
    return total_renting_cost, total_buying_cost, property_value

st.title("Rent vs. Buy Calculator - Australia")

# User Inputs
rent = st.number_input("Monthly Rent ($)", value=2000)
rent_increase = st.number_input("Annual Rent Increase (%)", value=3)
home_price = st.number_input("Home Price ($)", value=600000)
deposit = st.number_input("Deposit ($)", value=60000)
interest_rate = st.number_input("Mortgage Interest Rate (%)", value=5.0)
loan_term = st.number_input("Loan Term (Years)", value=30)
property_appreciation = st.number_input("Annual Property Appreciation (%)", value=3.0)
stamp_duty = st.number_input("Stamp Duty ($)", value=20000)
annual_rates = st.number_input("Annual Council Rates ($)", value=2000)
insurance = st.number_input("Annual Home Insurance ($)", value=1500)
maintenance = st.number_input("Annual Maintenance Costs ($)", value=1000)
investment_return = st.number_input("Investment Return (%)", value=5.0)
years = st.number_input("Years to Compare", value=10)

if st.button("Calculate"):
    total_renting_cost, total_buying_cost, property_value = rent_vs_buy(
        rent, rent_increase, home_price, deposit, interest_rate, loan_term, 
        property_appreciation, stamp_duty, annual_rates, 
        insurance, maintenance, investment_return, years)
    
    st.write(f"Total Renting Cost over {years} years: ${total_renting_cost:,.2f}")
    st.write(f"Total Buying Cost over {years} years: ${total_buying_cost:,.2f}")
    st.write(f"Estimated Property Value after {years} years: ${property_value:,.2f}")
