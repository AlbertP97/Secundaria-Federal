# pages/calendario.py
import streamlit as st
import pandas as pd
from datetime import datetime
from components import navbar

# 🔥 Navbar
current_page = navbar()

st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("<h2 class='section-title'>📅 Calendario Escolar</h2>", unsafe_allow_html=True)
st.markdown("---")

# Datos de ejemplo: calendario de eventos
eventos = [
    {"fecha": "2026-01-15", "evento": "Inicio de Inscripciones", "hora": "08:00", "lugar": "Control Escolar"},
    {"fecha": "2026-02-05", "evento": "Ceremonia Cívica", "hora": "09:00", "lugar": "Auditorio"},
    {"fecha": "2026-03-10", "evento": "Feria de Ciencias", "hora": "09:00-13:00", "lugar": "Cancha Principal"},
    {"fecha": "2026-04-20", "evento": "Reunión de Padres de Familia", "hora": "17:00", "lugar": "Salón de Actos"},
    {"fecha": "2026-05-25", "evento": "Entrega de Boletas", "hora": "Todo el día", "lugar": "Salones"}
]

df = pd.DataFrame(eventos)
df['fecha'] = pd.to_datetime(df['fecha']).dt.date

# Selector de mes o rango
col1, col2 = st.columns([2,1])
with col1:
    fecha_seleccion = st.date_input("Selecciona una fecha para ver eventos", value=datetime.now().date())
with col2:
    filtro_mes = st.checkbox("Mostrar sólo eventos del mes seleccionado", value=False)

if filtro_mes:
    df_filtrado = df[df['fecha'].apply(lambda d: d.month == fecha_seleccion.month and d.year == fecha_seleccion.year)]
else:
    df_filtrado = df[df['fecha'] >= fecha_seleccion]

st.markdown("### Próximos eventos")
if df_filtrado.empty:
    st.info("No hay eventos para la selección actual.")
else:
    st.table(df_filtrado)

# Descargar calendario como CSV
csv_bytes = df.to_csv(index=False).encode('utf-8')
st.download_button("📥 Descargar calendario (CSV)", data=csv_bytes, file_name="calendario_escolar.csv", mime="text/csv")

st.markdown("---")

st.markdown("### 📝 Notas importantes")
st.markdown("- Las fechas pueden estar sujetas a cambios.\n- Para confirmar asistencia a eventos, contacta a la oficina de Control Escolar.")

st.info("Contacto Control Escolar: control@secundariabenemerito.edu.mx | Tel: (614) 123-4568")