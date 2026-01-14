# app.py
import streamlit as st
import pandas as pd
from datetime import datetime
from components import navbar
import streamlit.components.v1 as st_components
import base64
from pathlib import Path


# Configuración de la página
st.set_page_config(
    page_title="Escuela Secundaria Federal Benemérito de las Américas",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Función para convertir imagen a base64
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

# CSS personalizado mejorado
st.markdown("""
<style>
:root{
  --primary: #1a365d;
  --primary-light: #2d5a8c;
  --primary-dark: #0f1f36;
  --accent: #f39c12;
  --accent-dark: #d68910;
  --success: #27ae60;
  --danger: #e74c3c;
  --bg: #f8f9fa;
  --card-bg: #ffffff;
  --text: #1a1a1a;
  --text-light: #555555;
  --border-color: #e0e0e0;
  --nav-height: 100px;
}

.stApp {
  background: var(--bg);
  color: var(--text);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  padding: 1.5rem;
  padding-top: calc(var(--nav-height) + 80px);
}

/* Headers */
.main-header {
  font-size: 2.5rem;
  color: var(--primary);
  text-align: center;
  margin-bottom: 0.5rem;
  font-weight: 700;
  letter-spacing: -0.5px;
}

.sub-header {
  font-size: 1.1rem;
  color: var(--text-light);
  text-align: center;
  margin-bottom: 2rem;
  font-weight: 500;
}

/* Section title */
.section-title {
  color: var(--primary);
  border-bottom: 3px solid var(--accent);
  padding-bottom: 10px;
  margin: 2rem 0 1.5rem 0;
  font-weight: 700;
  font-size: 1.5rem;
  letter-spacing: -0.3px;
}

/* Cards */
.news-card {
  background-color: var(--card-bg);
  padding: 1.5rem;
  border-radius: 8px;
  border-left: 4px solid var(--accent);
  margin-bottom: 1.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
}

.news-card:hover {
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
  transform: translateY(-2px);
}

.news-card h4 {
  color: var(--primary);
  margin-top: 0;
}

.news-card strong {
  color: var(--accent);
}

.important-card {
  background: linear-gradient(135deg, #ffffff 0%, #f0f4f8 100%);
  color: var(--text);
  padding: 1.5rem;
  border-radius: 8px;
  margin: 1.5rem 0;
  border-left: 4px solid var(--accent);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
}

.important-card:hover {
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
  transform: translateY(-2px);
}

.important-card h3 {
  color: var(--primary);
  margin-top: 0;
  font-weight: 700;
}

/* Mission/Vision */
.mission-vision {
  background-color: var(--card-bg);
  padding: 1.5rem;
  border-radius: 8px;
  border-left: 4px solid var(--primary);
  margin: 1.5rem 0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
}

.mission-vision:hover {
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
}

.mission-vision h3 {
  color: var(--primary);
  margin-top: 0;
  font-weight: 700;
}

/* Footer */
.footer {
  background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
  color: white;
  padding: 2.5rem;
  text-align: center;
  margin-top: 3rem;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(26, 54, 93, 0.15);
}

.footer h3 {
  margin-top: 0;
  font-size: 1.3rem;
  font-weight: 700;
}

.footer p {
  margin: 0.5rem 0;
  font-size: 0.9rem;
  opacity: 0.9;
}

/* Buttons (global) */
.stButton>button {
  background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 6px;
  box-shadow: 0 4px 12px rgba(26, 54, 93, 0.15);
  transition: all 0.3s ease;
  font-weight: 600;
  font-size: 0.95rem;
}

.stButton>button:hover {
  background: linear-gradient(135deg, var(--primary-dark) 0%, var(--primary) 100%);
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(26, 54, 93, 0.25);
}

/* Links (page_link) */
a[data-testid="stPageLink"] { 
  color: var(--primary) !important; 
  font-weight: 600;
  text-decoration: none;
  transition: color 0.3s ease;
}

a[data-testid="stPageLink"]:hover {
  color: var(--accent) !important;
}

/* Expander */
.streamlit-expanderHeader {
  background-color: #f0f4f8;
  color: var(--primary);
  font-weight: 600;
}

/* Small helpers */
.subtle-muted { 
  color: var(--text-light); 
  font-size: 0.95rem;
}

/* Horizontal line */
hr {
  border-color: var(--border-color);
  margin: 2rem 0;
}

/* Subheader */
.stMarkdown h2 {
  color: var(--primary);
  font-weight: 700;
}

.stMarkdown h3 {
  color: var(--primary);
  font-weight: 600;
}

/* Data tables */
.stDataFrame {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# 🔥 Navbar
current_page = navbar()

# (Header moved into the sticky navbar to show on every page)
st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

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
     
with col2:
    # Convertir imágenes a base64
    img1_base64 = get_base64_image("imgs/address_background.jpg")
    img2_base64 = get_base64_image("imgs/background1.jpg")
    img3_base64 = get_base64_image("imgs/background2.jpg")
    img4_base64 = get_base64_image("imgs/background3.jpg")
    
    carousel_html = f"""
    <style>
    .carousel {{ position: relative; overflow: hidden; border-radius: 12px; background: #f0f0f0; }}
    .carousel .slides {{ display: flex; transition: transform 0.5s ease; }}
    .carousel .slide {{ min-width: 100%; border-radius: 10px; overflow: hidden; display: flex; align-items: center; justify-content: center; }}
    .carousel img {{ width: 100%; height: 320px; object-fit: contain; display:block; }}
    .carousel .nav {{ position: absolute; top: 50%; transform: translateY(-50%); width: 100%; display:flex; justify-content:space-between; pointer-events:none; padding: 0 0.5rem; }}
    .carousel .nav button {{ pointer-events:auto; background: rgba(255,255,255,0.92); border:none; padding:0.4rem 0.7rem; border-radius:6px; margin:0 0.5rem; box-shadow:0 6px 18px rgba(11,37,70,0.08); cursor:pointer; font-size:18px; }}
    .carousel .dots {{ text-align:center; margin-top:0.5rem; }}
    .carousel .dot {{ display:inline-block; width:10px; height:10px; background:#ddd; border-radius:50%; margin:0 4px; cursor:pointer; }}
    .carousel .dot.active {{ background: #1a365d; width:12px; height:12px; }}
    </style>
    <div class="carousel" id="carousel">
      <div class="slides" id="slides">
        <div class="slide"><img src="data:image/jpeg;base64,{img1_base64}" alt="Imagen 1" /></div>
        <div class="slide"><img src="data:image/jpeg;base64,{img2_base64}" alt="Imagen 2" /></div>
        <div class="slide"><img src="data:image/webp;base64,{img3_base64}" alt="Imagen 3" /></div>
        <div class="slide"><img src="data:image/jpeg;base64,{img4_base64}" alt="Imagen 4" /></div>
      </div>
      <div class="nav">
        <button id="prev">&#10094;</button>
        <button id="next">&#10095;</button>
      </div>
      <div class="dots" id="dots">
        <span class="dot active" data-index="0"></span>
        <span class="dot" data-index="1"></span>
        <span class="dot" data-index="2"></span>
        <span class="dot" data-index="3"></span>
      </div>
    </div>
    <script>
    const slides = document.getElementById('slides');
    const dots = document.querySelectorAll('#dots .dot');
    let index = 0;
    let autoplayInterval;
    
    function update() {{
      slides.style.transform = 'translateX(' + (-index * 100) + '%)';
      dots.forEach(d => d.classList.remove('active'));
      dots[index].classList.add('active');
    }}
    
    function nextSlide() {{
      index = (index + 1) % 4;
      update();
    }}
    
    function startAutoplay() {{
      autoplayInterval = setInterval(nextSlide, 5000); // Cambia cada 5 segundos
    }}
    
    function stopAutoplay() {{
      clearInterval(autoplayInterval);
    }}
    
    // Iniciar autoplay
    startAutoplay();
    
    // Detener autoplay al interactuar
    document.getElementById('prev').addEventListener('click', () => {{ 
      stopAutoplay();
      index = (index - 1 + 4) % 4; 
      update(); 
      startAutoplay(); // Reiniciar autoplay después de 3 segundos
    }});
    
    document.getElementById('next').addEventListener('click', () => {{ 
      stopAutoplay();
      index = (index + 1) % 4; 
      update(); 
      startAutoplay();
    }});
    
    dots.forEach(d => d.addEventListener('click', e => {{ 
      stopAutoplay();
      index = parseInt(e.target.dataset.index); 
      update(); 
      startAutoplay();
    }}));
    
    // Touch support
    let startX = 0;
    slides.addEventListener('touchstart', (e) => {{ 
      stopAutoplay();
      startX = e.touches[0].clientX; 
    }});
    slides.addEventListener('touchend', (e) => {{ 
      const dx = e.changedTouches[0].clientX - startX; 
      if (dx < -50) {{ 
        index = (index + 1) % 4; 
        update(); 
      }} else if (dx > 50) {{ 
        index = (index -1 +4) %4; 
        update(); 
      }}
      startAutoplay();
    }});
    
    // Pausar autoplay cuando el mouse está sobre el carrusel
    document.getElementById('carousel').addEventListener('mouseenter', stopAutoplay);
    document.getElementById('carousel').addEventListener('mouseleave', startAutoplay);
    </script>
    """

    st_components.html(carousel_html, height=380, scrolling=False)

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

# Apoyo con Donaciones
st.markdown("<h2 class='section-title'>💙 Apoya Nuestra Escuela</h2>", unsafe_allow_html=True)

st.markdown("""
<div class='important-card'>
    <h3>🏫 Tu Ayuda Transforma Vidas</h3>
    <p style='font-size: 1.05rem; line-height: 1.6; margin-bottom: 1rem;'>
    Cada estudiante que cruza nuestras puertas lleva consigo un sueño, una esperanza de un futuro mejor. 
    En la Escuela Secundaria Federal "Benemérito de las Américas", trabajamos incansablemente para hacer 
    realidad esos sueños, pero <strong>necesitamos tu ayuda</strong>.
    </p>
    <p style='font-size: 1.05rem; line-height: 1.6; margin-bottom: 1rem;'>
    Tus donaciones nos permiten mejorar nuestras instalaciones, equipar laboratorios, renovar mobiliario, 
    adquirir material didáctico y crear espacios dignos donde nuestros jóvenes puedan desarrollar todo su 
    potencial. <strong>Cada peso cuenta, cada aporte marca la diferencia</strong> en la vida de cientos de 
    estudiantes que confían en nosotros para construir su futuro.
    </p>
    <p style='font-size: 1.05rem; line-height: 1.6; margin-bottom: 1rem;'>
    No solo estarás ayudando a una escuela, estarás <strong>invirtiendo en el futuro de nuestra comunidad</strong>, 
    en la educación de los líderes del mañana, en la esperanza de familias que luchan día a día por dar a sus 
    hijos la mejor preparación posible.
    </p>
    <p style='font-size: 1.1rem; font-weight: 600; color: var(--primary); margin-top: 1.5rem;'>
    🏦 <strong>Cuenta Bancaria para Donaciones:</strong><br>
    <span style='font-size: 1.15rem; color: var(--accent);'>BBVA Bancomer: 0123 4567 8901 2345</span><br>
    <span style='font-size: 0.95rem;'>A nombre de: Escuela Secundaria Federal "Benemérito de las Américas"</span>
    </p>
    <p style='font-size: 1rem; margin-top: 1rem; font-style: italic; color: var(--text-light);'>
    ❤️ Gracias por creer en la educación y en nuestros jóvenes. Tu generosidad ilumina su camino.
    </p>
</div>
""", unsafe_allow_html=True)

# Enlaces Rápidos
st.markdown("<h2 class='section-title'>🔗 Enlaces Rápidos</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📚 Académico")
    st.page_link("pages/ofertas.py", label="Plan de Estudios")

with col2:
    st.subheader("👥 Comunidad")
    st.page_link("pages/comunidad.py", label="Generaciones")

with col3:
    st.subheader("🌐 Recursos")
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
    <h3 style='color: #ffffff;'>Escuela Secundaria Federal "Benemérito de las Américas"</h3>
    <p>© 2026 - Formando jóvenes para un mejor futuro</p>
    <p>Zona Escolar 15, Sector 5 | Todos los derechos reservados</p>
    <p>Pagina diseñada por: M.I. José Alberto Payán Marta</p>
</div>
""", unsafe_allow_html=True)