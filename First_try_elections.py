import streamlit as st
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Cargar los datos
data_enero_ig = pd.read_csv("infotracer-instagram-enero-24.csv")
cleaned_data = data_enero_ig.dropna()

# Limpiar y preparar los datos
all_data_combined = cleaned_data.dropna()
all_data_combined['datetime'] = pd.to_datetime(all_data_combined['datetime'], errors='coerce')
all_data_combined['month_year'] = all_data_combined['datetime'].dt.to_period('M').astype(str)

# Agrupar por candidato y sumar interacciones
interactions_for_candidate = cleaned_data.groupby('candidate_name')['num_interaction'].sum()

# Calcular el porcentaje de interacciones por candidato
percentage_for_interactions = (interactions_for_candidate / interactions_for_candidate.sum()) * 100
df_plotly = percentage_for_interactions.reset_index()

# Gráfico de pastel
pie_chart_fig = px.pie(df_plotly, values='num_interaction', names='candidate_name', 
                       title='Interacciones Totales (en porcentaje) por Candidato - Enero - Instagram',
                       hover_data=['num_interaction'], labels={'num_interaction':'% de Interacciones'})

# Agrupar interacciones diarias por candidato
daily_interactions = all_data_combined.groupby(['candidate_name', 'datetime'])['num_interaction'].sum().reset_index()

# Gráfico de líneas por interacciones diarias
line_chart_fig = px.line(daily_interactions, 
                         x='datetime', y='num_interaction', color='candidate_name',
                         title='Interacciones Diarias por Candidato - Enero - Instagram',
                         labels={'num_interaction': 'Cantidad de Interacciones', 'datetime': 'Fecha'},
                         markers=True)

line_chart_fig.update_layout(
    xaxis=dict(
        tickformat="%Y-%m",
        tickvals=pd.date_range(start=daily_interactions['datetime'].min(), end=daily_interactions['datetime'].max(), freq='M')
    ),
    margin=dict(l=0, r=0, t=30, b=0),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

# Dashboard de múltiples páginas
st.set_page_config(page_title='Multi-Page Dashboard', layout='wide')
page = st.sidebar.selectbox('Select an option', ['Home', 'Enero', 'Febrero', "Marzo", "Abril", "Combined"])
st.title('Welcome to the {} Page'.format(page))

# Página de Enero
if page == 'Enero':
    st.header('Análisis de Enero')

    st.subheader('Gráfico de Pastel - Porcentaje de Interacciones por Candidato')
    st.plotly_chart(pie_chart_fig)

    st.subheader('Gráfico de Líneas - Interacciones Diarias por Candidato')
    st.plotly_chart(line_chart_fig)

# Página de inicio
elif page == 'Home':
    st.write('This is the home page. Select a page from the sidebar to view the charts.')