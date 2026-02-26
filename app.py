import pandas as pd
import plotly.express as px
import streamlit as st

# Leer datos
car_data = pd.read_csv('vehicles_us.csv')

# Título
st.header("Panel de análisis de vehículos en EE.UU.")

# Checkbox para histograma
build_histogram = st.checkbox('Mostrar histograma del odómetro')

if build_histogram:
    st.write('Distribución del kilometraje')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para gráfico de dispersión
build_scatter = st.checkbox('Mostrar gráfico precio vs odómetro')

if build_scatter:
    st.write('Relación entre precio y kilometraje')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)