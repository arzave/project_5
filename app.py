import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('C:\\project_5\\vehicles_us.csv')

# Encabezado
st.header('Aplicación de análisis de vehículos')

# Casillas de verificación
build_histogram = st.checkbox('Construir histograma')
build_scatter = st.checkbox('Construir gráfico de dispersión')

# Mostrar contenido al seleccionar la casilla de verificación del histograma
if build_histogram:
    # Mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear el histograma
    fig = px.histogram(car_data, x="odometer")

    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)

# Mostrar contenido al seleccionar la casilla de verificación del gráfico de dispersión
if build_scatter:
    # Mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear el gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")

    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)
