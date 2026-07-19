import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"  # Dirección del backend FastAPI

st.title("ARGOS - Licitaciones Públicas")

# Botón para actualizar datos
if st.button("Actualizar licitaciones"):
    response = requests.post(f"{API_URL}/actualizar")
    if response.status_code == 200:
        st.success(response.json()["message"])
    else:
        st.error("Error al actualizar datos")

# Obtener licitaciones
response = requests.get(f"{API_URL}/licitaciones")
if response.status_code == 200:
    data = response.json()
    if data:
        df = pd.DataFrame(data)
        st.subheader("Listado de licitaciones")
        st.dataframe(df)

        # Ejemplo de gráfico por entidad
        st.subheader("Monto total por entidad")
        grafico = df.groupby("entidad")["monto"].sum()
        st.bar_chart(grafico)
    else:
        st.warning("No hay licitaciones registradas aún.")
else:
    st.error("Error al conectar con el backend")

