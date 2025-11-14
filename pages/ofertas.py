# pages/ofertas_academicas.py
import streamlit as st
from components import navbar

# 🔥 Navbar
current_page = navbar()

st.title("📚 Plan de Estudios")
st.markdown("---")

st.markdown("""
### Grados que Ofrecemos

Nuestra escuela ofrece educación secundaria en tres grados:
""")

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
        st.download_button(
            label=f"Descargar Plan de Estudios - {grado}",
            data=f"Contenido del plan de estudios {grado}",
            file_name=f"plan_estudios_{grado.lower().replace(' ', '_')}.pdf",
            mime="application/pdf"
        )