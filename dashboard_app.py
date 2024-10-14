import pandas as pd
import numpy as np
import streamlit as st

st.title("Multi-page Data Dashboard")


#Sidebar for page navigation
page = st.sidebar.radio("Select a Page",["Overview", "Sales", "Expenses", "Profit"])

#function to display overview page
def show_overview():
    st.header("Overview")
    return
def show_sales():
    st.header("Sales Dashboard")
    return
def show_expenses():
    st.header("Expenses Dashboard")
    return
def show_profit():
    st.header("Profit Dashboard")
    return

#navigation logic
if page == "Overview":
    show_overview()
elif page == "Sales":
    show_sales()
elif page == "Expenses":
    show_expenses()
elif page == "Profit":
    show_profit()

#sample data function
@st.cache_data

def load_data():
    data = pd.DataFrame({
        "Date": pd.date_range(start="2023-01-01", periods=100),
        "Sales": np.random.randint(100, 500, size=100),
        "Expenses": np.random.randint(50, 300, size=100)
    })
    data["Profit"] = data["Sales"]-data["Expenses"]
    return data

#funtion to display overview