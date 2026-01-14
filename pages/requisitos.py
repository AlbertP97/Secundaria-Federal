# pages/requisitos.py
import streamlit as st
from components import navbar

# 🔥 Navbar
current_page = navbar()

st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("<h2 class='section-title'>📋 Requisitos de Inscripción</h2>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("""
### Documentos necesarios
- Acta de nacimiento original y copia
- CURP (copia)
- Comprobante de domicilio (recibo reciente)
- Boleta o certificado de primaria
- 2 fotografías tamaño infantil (si aplica)
- Identificación del tutor/representante
""")

st.markdown("### Pasos para inscribirse")
st.markdown("""
1. Reúne la documentación requerida.
2. Acude a Control Escolar en horario de atención: Lunes a Viernes 8:00 - 14:00 hrs.
3. Entrega los documentos y llena la hoja de inscripción.
4. Espera confirmación y fecha de validación.
""")

st.markdown("---")
st.info("Para dudas o citas: control@secundariabenemerito.edu.mx | Tel: (614) 123-4568")

# Footer
st.markdown("""
<div class='footer'>
    <h3>Escuela Secundaria Federal "Benemérito de las Américas"</h3>
    <p>© 2026 - Formando jóvenes para un mejor futuro</p>
    <p>Zona Escolar 15, Sector 5 | Todos los derechos reservados</p>
    <p>Pagina diseñada por: M.I. José Alberto Payán Marta</p>
</div>
""", unsafe_allow_html=True)