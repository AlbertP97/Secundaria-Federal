# pages/ofertas_academicas.py
import streamlit as st
from components import navbar

# 🔥 Navbar
current_page = navbar()

st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("<h2 class='section-title'>📚 Plan de Estudios</h2>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("""
<div class='card'>
Nuestra escuela ofrece educación secundaria en tres grados:
</div>
""", unsafe_allow_html=True)

grados = {
    "Primer Grado": {
        "materias": ["Español", "Matemáticas", "Ciencias (Biología)", "Geografía", "Inglés", 
                     "Formación Cívica y Ética", "Artes", "Educación Física", "Tecnología"],
        "enfoque": "Adaptación a la vida secundaria y desarrollo de hábitos de estudio"
    },
    "Segundo Grado": {
        "materias": ["Español", "Matemáticas", "Ciencias (Física)", "Historia", "Inglés", "Formación Cívica y Ética", 
                     "Artes", "Educación Física", "Tecnología"],
        "enfoque": "Profundización en conocimientos y desarrollo de habilidades"
    },
    "Tercer Grado": {
        "materias": ["Español", "Matemáticas", "Ciencias (Química)", "Historia", "Inglés", "Formación Cívica y Ética", 
                     "Artes", "Educación Física", "Tecnología"],
        "enfoque": "Consolidación de aprendizajes y preparación para educación media superior"
    }
}

for grado, info in grados.items():
    with st.expander(f"🎓 {grado}"):
        st.write(f"**Materias:** {', '.join(info['materias'])}")
        st.write(f"**Enfoque educativo:** {info['enfoque']}")

# Footer
st.markdown("""
<div class='footer'>
    <h3>Escuela Secundaria Federal "Benemérito de las Américas"</h3>
    <p>© 2026 - Formando jóvenes para un mejor futuro</p>
    <p>Zona Escolar 15, Sector 5 | Todos los derechos reservados</p>
    <p>Pagina diseñada por: M.I. José Alberto Payán Marta</p>
</div>
""", unsafe_allow_html=True)