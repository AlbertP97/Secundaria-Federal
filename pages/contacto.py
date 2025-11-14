# pages/contacto.py
import streamlit as st
import pandas as pd
from components import navbar

# 🔥 Navbar
current_page = navbar()

st.title("📞 Contacto y Ubicación")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Información de Contacto")
    
    st.markdown("""
    **Escuela Secundaria Federal "Benemérito de las Américas"**
    
    📍 **Dirección:**
    Av. Gonzalez Ortega 1200
    San Isidro
    C.P. 33760
    Santa Rosalía de Camargo, Chihuahua
    
    📞 **Teléfonos:**
    - Dirección: (648) 462-0611
    - Control Escolar: (648) 123-4568
    - Prefectura: (648) 123-4569
    - Biblioteca: (648) 123-4570
    
    📧 **Correos Electrónicos:**
    - Dirección: direccion@secundariabenemerito.edu.mx
    - Control Escolar: control@secundariabenemerito.edu.mx
    - Biblioteca: biblioteca@secundariabenemerito.edu.mx
    
    ⏰ **Horario de Atención:**
    - Lunes a Viernes: 7:00 - 20:00 hrs
    """)

with col2:
    st.subheader("🗺️ Ubicación")
    st.map(pd.DataFrame({
        'lat': [27.68152],
        'lon': [-105.17870]
    }), zoom=15)
    
    st.markdown("""
    **Cómo llegar:**
    - 🚍 **Transporte público:** Rutas 5, 12, 23
    - 🚗 **Estacionamiento:** Disponible para visitas
    - ♿ **Acceso para personas con discapacidad:** Sí
    """)

# Personal administrativo
st.markdown("---")
st.subheader("👥 Personal Administrativo")

personal = {
    "Directora": "Mtra. Ana María Rodríguez López",
    "Subdirector Académico": "Prof. Carlos Eduardo Martínez",
    "Subdirector Administrativo": "Lic. Laura Patricia González",
    "Jefe de Control Escolar": "Mtro. Roberto Sánchez Jiménez",
    "Prefecto General": "Prof. Jorge Alberto Ramírez"
}

for puesto, nombre in personal.items():
    st.write(f"**{puesto}:** {nombre}")