# app.py
import streamlit as st
import pandas as pd
from datetime import datetime
from components import navbar 

# Configuración de la página
st.set_page_config(
    page_title="Escuela Secundaria Federal Benemérito de las Américas",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1a5276;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #2e86c1;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-title {
        color: #1a5276;
        border-bottom: 3px solid #f39c12;
        padding-bottom: 0.5rem;
        margin: 2rem 0 1rem 0;
    }
    .news-card {
        background-color: #f8f9f9;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #1a5276;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .event-card {
        background-color: #fff8e1;
        padding: 1.2rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        border: 1px solid #f39c12;
    }
    .important-card {
        background: linear-gradient(135deg, #1a5276, #2e86c1);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .footer {
        background-color: #1a5276;
        color: white;
        padding: 2rem;
        text-align: center;
        margin-top: 3rem;
        border-radius: 10px 10px 0 0;
    }
    .mission-vision {
        background-color: #e8f4f8;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #f39c12;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# 🔥 Navbar
current_page = navbar()

# Header
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<h1 class='main-header'>Escuela Secundaria Federal</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>Benemérito de las Américas</h2>", unsafe_allow_html=True)
    st.markdown("<h5 class='sub-header'>Formando jóvenes con valores y excelencia académica</h5>", unsafe_allow_html=True)

# Menú de navegación
#menu = st.selectbox("Navegación", 
#                   ["🏠 Inicio", "📚 Oferta Educativa", "👨‍🏫 Nosotros", "📅 Calendario Escolar", 
#                    "📋 Requisitos", "📞 Contacto"])

# Hero Section
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    ### 🎓 Educación de Calidad
    
    Formamos estudiantes con:
    - **Excelencia académica**
    - **Valores cívicos y éticos**
    - **Desarrollo integral**
    - **Preparación para el futuro**
    
    **Turnos disponibles:**
    - Matutino: 7:00 - 13:00 hrs
    - Vespertino: 14:00 - 20:00 hrs
    """)
    
    if st.button("📋 Solicitar Informes", type="primary"):
        st.success("¡Próximamente podrás solicitar informes en línea!")
     
with col2:
    #st.image("imgs/80-aniversario.jpg", width=300)
    st.image("imgs/baile.webp", width=300)

# Tarjetas importantes
st.markdown("<h2 class='section-title'>📢 Información Importante</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class='important-card'>
        <h3>📅 Inscripciones 2024</h3>
        <p>Periodo: 15 Enero - 15 Febrero</p>
        <p>Informes en Control Escolar</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='important-card'>
        <h3>🎒 Uniformes</h3>
        <p>Venta en cooperativa escolar</p>
        <p>Lunes a Viernes 8:00-14:00 hrs</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='important-card'>
        <h3>📚 Libros de Texto</h3>
        <p>Disponibles en biblioteca</p>
        <p>Préstamo gratuito</p>
    </div>
    """, unsafe_allow_html=True)

# Sección de Noticias
st.markdown("<h2 class='section-title'>📰 Noticias Escolares</h2>", unsafe_allow_html=True)

noticias = [
    {
        "titulo": "Ceremonia Cívica Mensual - Noviembre",
        "fecha": "6 de Noviembre, 2023",
        "categoria": "Evento Cívico",
        "resumen": "Invitamos a toda la comunidad estudiantil a nuestra ceremonia cívica del mes de noviembre..."
    },
    {
        "titulo": "Concurso de Oratoria Interescolar",
        "fecha": "10 de Noviembre, 2023", 
        "categoria": "Competencia",
        "resumen": "Nuestros estudiantes participarán en el concurso municipal de oratoria..."
    },
    {
        "titulo": "Jornada de Salud Estudiantil",
        "fecha": "15-17 Noviembre, 2023",
        "categoria": "Salud", 
        "resumen": "En colaboración con el centro de salud, realizaremos chequeos médicos gratuitos..."
    },
    {
        "titulo": "Festival Deportivo Anual",
        "fecha": "25 Noviembre, 2023",
        "categoria": "Deportes",
        "resumen": "Competencias deportivas entre grupos y grados. ¡Participa y gana premios!"
    }
]

for i, noticia in enumerate(noticias):
    with st.container():
        st.markdown(f"""
        <div class='news-card'>
            <h4>{noticia['titulo']}</h4>
            <p><strong>{noticia['categoria']}</strong> | 📅 {noticia['fecha']}</p>
            <p>{noticia['resumen']}</p>
        </div>
        """, unsafe_allow_html=True)

# Sección de Eventos Próximos
st.markdown("<h2 class='section-title'>📅 Próximos Eventos</h2>", unsafe_allow_html=True)

eventos = [
    {"nombre": "Reunión de Padres - 1er Grado", "fecha": "8 Noviembre", "hora": "16:00 hrs", "lugar": "Auditorio"},
    {"nombre": "Taller de Regularización Matemáticas", "fecha": "10-14 Noviembre", "hora": "14:00-16:00 hrs", "lugar": "Aula 101"},
    {"nombre": "Feria de Ciencias 2023", "fecha": "20 Noviembre", "hora": "9:00-13:00 hrs", "lugar": "Cancha Principal"},
    {"nombre": "Entrega de Boletas 1er Trimestre", "fecha": "24 Noviembre", "hora": "Todo el día", "lugar": "Salones"}
]

for evento in eventos:
    with st.expander(f"🗓️ {evento['nombre']} - {evento['fecha']}"):
        st.write(f"**⏰ Hora:** {evento['hora']}")
        st.write(f"**📍 Lugar:** {evento['lugar']}")
        st.write("**📋 Descripción:** Actividad escolar para estudiantes y padres de familia")

# Misión y Visión
st.markdown("<h2 class='section-title'>🎯 Misión y Visión</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class='mission-vision'>
        <h3>🎯 Misión</h3>
        <p>Formar ciudadanos responsables, críticos y creativos mediante una educación integral 
        que promueva los valores cívicos, el desarrollo de competencias y el amor por el conocimiento, 
        preparándolos para los desafíos del mundo actual.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='mission-vision'>
        <h3>🔭 Visión</h3>
        <p>Ser la institución educativa de referencia en nuestra comunidad, reconocida por la 
        excelencia académica, la formación en valores y el compromiso con el desarrollo integral 
        de nuestros estudiantes, contribuyendo a la construcción de una sociedad más justa y próspera.</p>
    </div>
    """, unsafe_allow_html=True)

# Enlaces Rápidos
st.markdown("<h2 class='section-title'>🔗 Enlaces Rápidos</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📚 Académico")
    st.page_link("pages/ofertas.py", label="Plan de Estudios")
    #st.page_link("pages/2_📋_Calificaciones.py", label="Sistema de Calificaciones")
    #st.page_link("pages/3_🏫_Reglamento.py", label="Reglamento Escolar")
    #st.page_link("pages/4_📅_Calendario.py", label="Calendario Escolar")

with col2:
    st.subheader("👥 Comunidad")
    st.page_link("pages/comunidad.py", label="Generaciones")
    #st.page_link("pages/6_🎓_Egresados.py", label="Egresados")
    #st.page_link("pages/7_🤝_Asociaciones.py", label="Asociaciones")
    #st.page_link("pages/8_💼_Bolsa_Trabajo.py", label="Bolsa de Trabajo")

with col3:
    st.subheader("🌐 Recursos")
    #st.page_link("pages/9_📖_Biblioteca.py", label="Biblioteca Digital")
    #st.page_link("pages/10_💻_Plataforma.py", label="Plataforma Educativa")
    #st.page_link("pages/11_📄_Formatos.py", label="Formatos y Documentos")
    st.page_link("pages/contacto.py", label="Contacto y Ubicación")

# Información de Contacto
st.markdown("---")
st.subheader("📞 Información de Contacto")

col1, col2, col3 = st.columns(3)
with col1:
    st.write("**📍 Dirección:**")
    st.write("Av. de la Juventud #123")
    st.write("Col. Centro, C.P. 31000")
    st.write("Chihuahua, Chih., México")
    
with col2:
    st.write("**📞 Teléfonos:**")
    st.write("Dirección: (614) 123-4567")
    st.write("Control Escolar: (614) 123-4568")
    st.write("Prefectura: (614) 123-4569")
    
with col3:
    st.write("**📧 Email:**")
    st.write("direccion@secundariabenemerito.edu.mx")
    st.write("control@secundariabenemerito.edu.mx")
    st.write("**🌐 Horario:** Lunes a Viernes 7:00-20:00 hrs")

# Mapa de ubicación
st.subheader("🗺️ Ubicación")
st.map(pd.DataFrame({
    'lat': [27.68152],
    'lon': [-105.17870]
}), zoom=15)

# Footer
st.markdown("""
<div class='footer'>
    <h3>Escuela Secundaria Federal "Benemérito de las Américas"</h3>
    <p>© 2023 - Formando jóvenes para un mejor futuro</p>
    <p>Zona Escolar 15, Sector 5 | Todos los derechos reservados</p>
    <p>Pagina diseñada por: M.I. José Alberto Payán Marta</p>
</div>
""", unsafe_allow_html=True)