import streamlit as st
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(page_title='Multi-Page Dashboard', layout='wide')

page = st.sidebar.selectbox('Select an option', ['Home', 'Seaborn Charts', 'Plotly Charts'])

st.title('Welcome to the {} Page'.format(page))

if page == 'Home':
    st.write('This is the home page. Select a page from the sidebar to view the charts.')
    
elif page == 'Seaborn Charts':
    st.header('Seaborn Charts')
    iris = sns.load_dataset('iris')

    st.subheader('Scatterplot')
    fig, ax = plt.subplots()
    sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species', ax=ax)
    st.pyplot(fig)

    st.subheader('Histogram')
    fig, ax = plt.subplots()
    sns.histplot(data=iris, x='sepal_length', bins=10, ax=ax)
    st.pyplot(fig)

    st.header('Heatmap')
    corr_matrix = iris.select_dtypes(include='number').corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr_matrix, annot=True, cmap='flare', ax=ax)
    st.pyplot(fig)

elif page == 'Plotly Charts':
    st.header('Plotly Charts')
    iris = px.data.iris()
    st.subheader('Scatterplot')
    scatter_fig = px.scatter(iris, x='sepal_width', y='sepal_length', color='species')
    st.plotly_chart(scatter_fig)

    st.subheader('Bar Chart')
    bar_fig = px.bar(iris, x='species', y='sepal_width', color='species')
    st.plotly_chart(bar_fig)

    st.subheader('Line Plot')
    line_fig = px.line(iris, x='sepal_length', y='sepal_width', color='species')
    st.plotly_chart(line_fig)