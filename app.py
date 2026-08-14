import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# -------------------------------
# Histograma
# -------------------------------

hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear el histograma
    fig = go.Figure(
        data=[
            go.Histogram(
                x=car_data['odometer']
            )
        ]
    )

    # Añadir título
    fig.update_layout(
        title_text='Distribución del Odómetro',
        xaxis_title='Odómetro',
        yaxis_title='Cantidad de vehículos'
    )

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)


# -------------------------------
# Diagrama de dispersión
# -------------------------------

disp_button = st.button('Construir diagrama de dispersión')

if disp_button:
    st.write('Creación de un diagrama de dispersión')

    # Crear el diagrama de dispersión
    fig = go.Figure(
        data=[
            go.Scatter(
                x=car_data['odometer'],
                y=car_data['price'],
                mode='markers'
            )
        ]
    )

    # Añadir título y nombres de los ejes
    fig.update_layout(
        title_text='Relación entre Odómetro y Precio',
        xaxis_title='Odómetro',
        yaxis_title='Precio'
    )

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)