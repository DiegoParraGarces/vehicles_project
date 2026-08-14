import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# -------------------------------
# Encabezado
# -------------------------------

st.header('Análisis de vehículos usados')

st.write(
    'Explora los datos de los anuncios de venta de coches '
    'mediante un histograma y un gráfico de dispersión.'
)


# -------------------------------
# Casilla de verificación
# -------------------------------

show_histogram = st.checkbox('Mostrar histograma')

if show_histogram:
    st.write(
        'Histograma de los kilómetros recorridos '
        'por los vehículos.'
    )

    fig = go.Figure(
        data=[
            go.Histogram(
                x=car_data['odometer']
            )
        ]
    )

    fig.update_layout(
        title_text='Distribución del Odómetro',
        xaxis_title='Odómetro',
        yaxis_title='Cantidad de vehículos'
    )

    st.plotly_chart(fig, use_container_width=True)


# -------------------------------
# Botón para diagrama de dispersión
# -------------------------------

disp_button = st.button('Construir diagrama de dispersión')

if disp_button:
    st.write(
        'Diagrama de dispersión que muestra la relación '
        'entre el odómetro y el precio.'
    )

    fig = go.Figure(
        data=[
            go.Scatter(
                x=car_data['odometer'],
                y=car_data['price'],
                mode='markers'
            )
        ]
    )

    fig.update_layout(
        title_text='Relación entre Odómetro y Precio',
        xaxis_title='Odómetro',
        yaxis_title='Precio'
    )

    st.plotly_chart(fig, use_container_width=True)