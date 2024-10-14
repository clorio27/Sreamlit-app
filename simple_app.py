import streamlit as st #package for dashboards

st.title("My Dashboard")
option = st.selectbox(
    "Select a number:",
    [1,2,3,4,5,])
st.write("Welcome to my Dashboard")





# FOR RUNNING: streamlit run simple_app.py