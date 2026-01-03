# pages/comunidad.py
import streamlit as st
import os
from datetime import datetime
from components import navbar
import streamlit.components.v1 as st_components

# 🔥 Navbar
current_page = navbar()

st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
st.markdown("---")

st.title("👥 Generaciones")
st.markdown("---")

# CSS personalizado para la galería (usa variables globales)
st.markdown("""
<style>
    .gallery-title { color: var(--text); text-align:center; margin-bottom:1rem; font-size:2rem; }
    .generation-card { background: var(--card); border-radius:12px; padding:1rem; margin: 1rem 0; border-left:4px solid var(--primary); }
    .year-badge { background: linear-gradient(135deg, var(--primary), var(--accent)); color: white; padding:0.4rem 0.8rem; border-radius: 18px; font-weight:700; display:inline-block; margin-bottom:0.5rem; }
    .stats-card { background: #f8fafc; padding:0.8rem; border-radius:8px; text-align:center; margin:0.5rem; }
    /* Carousel helpers (mobile-friendly) */
    .carousel { position: relative; overflow: hidden; border-radius: 10px; }
    .carousel .slides { display:flex; transition: transform 0.5s ease; }
    .carousel .slide { min-width:100%; }
    .carousel img { width:100%; height:320px; object-fit:cover; display:block; border-radius:8px; }
    .carousel .nav { position:absolute; top:50%; transform:translateY(-50%); width:100%; display:flex; justify-content:space-between; pointer-events:none; padding:0 0.5rem; }
    .carousel .nav button { pointer-events:auto; background: rgba(255,255,255,0.92); border:none; padding:0.3rem 0.6rem; border-radius:6px; box-shadow:0 6px 18px rgba(11,37,70,0.06); cursor:pointer; }
    .carousel .dots { text-align:center; margin-top:0.5rem; }
    .carousel .dot { display:inline-block; width:10px; height:10px; background:#ddd; border-radius:50%; margin:0 4px; cursor:pointer; }
    .carousel .dot.active { background: var(--primary); width:12px; height:12px; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='gallery-title'>👥 Galería de Generaciones</h1>", unsafe_allow_html=True)
st.markdown("---")

# Introducción
st.markdown("""
### 📸 Nuestra Historia en Imágenes

Revive los momentos especiales de cada generación que ha pasado por nuestras aulas. 
Cada foto cuenta una historia de esfuerzo, amistad y crecimiento.
""")

# Filtros y búsqueda
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    search_term = st.text_input("🔍 Buscar generación por año o nombre:", placeholder="Ej: 2023, 2020...")
with col2:
    sort_order = st.selectbox("Ordenar por:", ["Más reciente", "Más antigua"])
with col3:
    items_per_page = st.selectbox("Fotos por página:", [6, 12, 24])

# Datos de ejemplo de generaciones (en una app real, esto vendría de una base de datos)
generaciones = [
    {
        "año": 1945,
        "nombre": "Primer Generación",
        "total_estudiantes": 45,
        "fotos": [
            {"titulo": "Ceremonia de Graduación", "ruta": "generaciones/2023/graduacion.jpg"},
            {"titulo": "Viaje de Estudios", "ruta": "generaciones/2023/viaje_estudios.jpg"},
            {"titulo": "Fiesta de Fin de Curso", "ruta": "generaciones/2023/fiesta_fin_curso.jpg"},
            {"titulo": "Equipo Deportivo", "ruta": "generaciones/2023/deportes.jpg"},
            {"titulo": "Proyecto de Ciencias", "ruta": "generaciones/2023/ciencias.jpg"},
            {"titulo": "Grupo Completo", "ruta": "generaciones/2023/grupo_completo.jpg"}
        ],
        "logros": ["Primer lugar en feria de ciencias", "Campeones deportivos inter escolar"]
    }
]

# Filtrar y ordenar generaciones
generaciones_filtradas = generaciones
if search_term:
    generaciones_filtradas = [g for g in generaciones if search_term in str(g["año"]) or search_term.lower() in g["nombre"].lower()]

if sort_order == "Más reciente":
    generaciones_filtradas.sort(key=lambda x: x["año"], reverse=True)
else:
    generaciones_filtradas.sort(key=lambda x: x["año"])

# Mostrar generaciones
if not generaciones_filtradas:
    st.warning("🚫 No se encontraron generaciones que coincidan con tu búsqueda.")
else:
    for generacion in generaciones_filtradas:
        with st.container():
            st.markdown(f"""
            <div class='generation-card'>
                <div class='year-badge'>{generacion['año']}</div>
                <h2>✨ {generacion['nombre']}</h2>
            </div>
            """, unsafe_allow_html=True)
            
            # Estadísticas de la generación
            col_stats1, col_stats2, col_stats3 = st.columns(3)
            with col_stats1:
                st.markdown(f"""
                <div class='stats-card'>
                    <h3>👥</h3>
                    <p><strong>Estudiantes</strong></p>
                    <h4>{generacion['total_estudiantes']}</h4>
                </div>
                """, unsafe_allow_html=True)
            with col_stats2:
                st.markdown(f"""
                <div class='stats-card'>
                    <h3>📸</h3>
                    <p><strong>Fotos</strong></p>
                    <h4>{len(generacion['fotos'])}</h4>
                </div>
                """, unsafe_allow_html=True)
            with col_stats3:
                st.markdown(f"""
                <div class='stats-card'>
                    <h3>🏆</h3>
                    <p><strong>Logros</strong></p>
                    <h4>{len(generacion['logros'])}</h4>
                </div>
                """, unsafe_allow_html=True)
            
            # Galería de fotos (carrusel)
            st.subheader("📷 Galería de Recuerdos")
            slides = []
            for foto in generacion['fotos']:
                img_path = foto['ruta']
                abs_path = os.path.join(os.getcwd(), img_path)
                if os.path.exists(abs_path):
                    slides.append(f"<div class='slide'><img src='{img_path}' alt='{foto['titulo']}' /></div>")
                else:
                    # Fallback placeholder
                    slides.append(f"<div class='slide'><div style='height:320px;display:flex;align-items:center;justify-content:center;background:#f0f2f6;border-radius:8px;'><div style='text-align:center;'><span style='font-size:3rem;'>🖼️</span><p style='margin:8px 0 0;font-weight:600;'>{foto['titulo']}</p><small>Generación {generacion['año']}</small></div></div></div>")

            slides_html = "\n".join(slides)
            carousel_html = f"""
            <div class='carousel' id='carousel-{generacion['año']}'>
              <div class='slides' id='slides-{generacion['año']}'>
                {slides_html}
              </div>
              <div class='nav'>
                <button id='prev-{generacion['año']}'>&#10094;</button>
                <button id='next-{generacion['año']}'>&#10095;</button>
              </div>
              <div class='dots' id='dots-{generacion['año']}'>
                {''.join([f"<span class='dot {'active' if i==0 else ''}' data-index='{i}'></span>" for i in range(len(slides))])}
              </div>
            </div>
            <script>
            (function(){{
              const slides = document.querySelectorAll('#slides-{generacion['año']} .slide');
              const container = document.getElementById('slides-{generacion['año']}');
              const dots = document.querySelectorAll('#dots-{generacion['año']} .dot');
              let index = 0;
              function update(){{
                container.style.transform = 'translateX(' + (-index * 100) + '%)';
                dots.forEach(d => d.classList.remove('active'));
                if(dots[index]) dots[index].classList.add('active');
              }}
              document.getElementById('prev-{generacion['año']}').addEventListener('click', () => {{ index = (index - 1 + slides.length) % slides.length; update(); }});
              document.getElementById('next-{generacion['año']}').addEventListener('click', () => {{ index = (index + 1) % slides.length; update(); }});
              dots.forEach(d => d.addEventListener('click', e => {{ index = parseInt(e.target.dataset.index); update(); }}));
              // touch
              let startX = 0;
              container.addEventListener('touchstart', (e) => {{ startX = e.touches[0].clientX; }});
              container.addEventListener('touchend', (e) => {{ const dx = e.changedTouches[0].clientX - startX; if (dx < -50) {{ index = (index + 1) % slides.length; update(); }} else if (dx > 50) {{ index = (index -1 + slides.length) % slides.length; update(); }} }});
            }})();
            </script>
            """

            st_components.html(carousel_html, height=380, scrolling=False)
            
            # Logros destacados
            with st.expander("🏆 Logros Destacados de esta Generación"):
                for logro in generacion['logros']:
                    st.write(f"• {logro}")
            
            # Botón para ver más (en una app real, redirigiría a una página específica de la generación)
            if st.button(f"👀 Ver Galería Completa - {generacion['nombre']}", key=f"btn_{generacion['año']}"):
                st.success(f"🔜 Próximamente: Galería completa de la {generacion['nombre']}")
            
            st.markdown("---")

# Sección para ex-alumnos
st.markdown("""
## 🎓 ¿Eres Ex-Alumno?

¡Mantente en contacto con tu generación! 
""")

col_contact1, col_contact2 = st.columns(2)
with col_contact1:
    with st.form("contacto_exalumno"):
        st.subheader("📩 Actualiza tus Datos")
        nombre = st.text_input("Nombre completo:")
        generacion = st.number_input("Año de graduación:", min_value=1980, max_value=2023, value=2020)
        email = st.text_input("Email actual:")
        profesion = st.text_input("¿A qué te dedicas ahora?")
        
        if st.form_submit_button("📤 Enviar Información"):
            st.success("¡Gracias por actualizar tus datos! Te mantendremos informado de eventos y reuniones.")

with col_contact2:
    st.markdown("""
    ### 🤝 Próximos Eventos para Ex-Alumnos
    
    **Reunión Generación 2020**  
    📅 15 de Diciembre, 2023  
    🕒 18:00 hrs  
    📍 Patio Central de la Escuela
    
    **Encuentro Generacional**  
    📅 20 de Enero, 2024  
    🕒 11:00 hrs  
    📍 Auditorio Principal
    
    *¿Quieres organizar una reunión de tu generación?*
    """)
    
    if st.button("📋 Organizar Reunión"):
        st.info("📞 Contacta a la dirección para coordinar tu evento")

# Pie de página
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>🏫 Escuela Secundaria Federal "Benemérito de las Américas"</p>
    <p>📞 Contacto ex-alumnos: exalumnos@secundariabenemerito.edu.mx</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class='footer'>
    <h3>Escuela Secundaria Federal "Benemérito de las Américas"</h3>
    <p>© 2023 - Formando jóvenes para un mejor futuro</p>
    <p>Zona Escolar 15, Sector 5 | Todos los derechos reservados</p>
    <p>Pagina diseñada por: M.I. José Alberto Payán Marta</p>
</div>
""", unsafe_allow_html=True)