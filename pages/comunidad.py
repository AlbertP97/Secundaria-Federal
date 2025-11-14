# pages/comunidad.py
import streamlit as st
from datetime import datetime
from components import navbar

# 🔥 Navbar
current_page = navbar()

st.title("👥 Generaciones")
st.markdown("---")

# CSS personalizado para la galería
st.markdown("""
<style>
    .gallery-title {
        color: #1a5276;
        text-align: center;
        margin-bottom: 2rem;
        font-size: 2.5rem;
    }
    .generation-card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border-left: 5px solid #1a5276;
    }
    .photo-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin: 1rem 0;
    }
    .photo-item {
        border-radius: 10px;
        overflow: hidden;
        transition: transform 0.3s ease;
    }
    .photo-item:hover {
        transform: scale(1.05);
    }
    .year-badge {
        background: linear-gradient(135deg, #1a5276, #2e86c1);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 1rem;
    }
    .stats-card {
        background: #e8f4f8;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem;
    }
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
            
            # Galería de fotos
            st.subheader("📷 Galería de Recuerdos")
            
            # Mostrar fotos en grid
            cols = st.columns(3)
            for i, foto in enumerate(generacion['fotos']):
                with cols[i % 3]:
                    # En una app real, usarías st.image(foto['ruta'])
                    st.markdown(f"""
                    <div class='photo-item'>
                        <div style='background: #f0f2f6; padding: 2rem; border-radius: 10px; text-align: center;'>
                            <span style='font-size: 3rem;'>🖼️</span>
                            <p style='margin: 0.5rem 0; font-weight: bold;'>{foto['titulo']}</p>
                            <small>Generación {generacion['año']}</small>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            
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