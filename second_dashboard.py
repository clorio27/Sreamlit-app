import streamlit as st
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt


#seet the page tittle 
st.set_page_config(page_title="Multi_Page Dashboard", layout="wide")

#define the page options for the sidebar
page  = st.sidebar.selectbox("Select an option", ["Home", "Seaborn Charts", "Plotly Charts"])

st.title(f"Welcome to the {page} page!")

#Display content based on the selected page
if page == "Home":
    st.write("This is the home page. Select a page from the sidebar to view the charts.")
if page == "Seaborn Charts":
    st.header("Seaborn Charts")
if page == "Plotly Charts":
    st.header("Plotly Charts")

if page == "Seaborn Charts":
    st.header("Seaborn Charts")

#load dataset
iris = sns.load_dataset("iris")

#create a scatter plot
st.subheader("Scatterplt")
fig, ax = plt.subplot()
sns.scatterplot(data=iris, x="sepal_length", y="sepal_width", hue="species", ax=ax)
st.pyplot(fig)

#create a histogram
st.subheader("Histogram")
fig, ax = plt.subplot()
sns.histplot(data=iris, x="sepal_length", bins=10, ax=ax)
st.pyplot(fig)

#create a heatmap
st.subheader("Heatmap")
corr_matrix = iris.select_dtypes(include="number").corr()
fig, ax = plt.subplots()
sns.heatmap(corr_matrix, annot=True, cmap="collwarm", ax=ax)
st.pyplot(fig)

