# Dashboard de vehículos usados

Aplicación web interactiva para explorar más de 50 000 anuncios de venta de autos usados en Estados Unidos. Permite ver la distribución del kilometraje y la relación entre kilometraje y precio.

🔗 **App en vivo:** https://vehicles-project-h6ku.onrender.com/
(Render pone en pausa las apps gratuitas; la primera carga puede tardar unos segundos).

## Qué incluye

- **EDA** (`notebooks/EDA.ipynb`): exploración inicial con Plotly.
- **App** (`app.py`) en **Streamlit**:
  - Histograma del odómetro, activado con una casilla.
  - Diagrama de dispersión odómetro vs. precio, generado con un botón.
- **Despliegue** en Render.

## Cómo ejecutarlo

```bash
pip install -r requirements.txt
streamlit run app.py
```

**Herramientas:** Python, pandas, Plotly, Streamlit, Render.

## Autor

Diego Parra · [LinkedIn](https://www.linkedin.com/in/diegoparragar)
