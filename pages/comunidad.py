# pages/comunidad.py
import streamlit as st
import os
import base64
from pathlib import Path
from components import navbar
import streamlit.components.v1 as st_components

# 🔥 Navbar
current_page = navbar()

st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
st.markdown("---")

# Función para convertir imagen a base64
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

# CSS personalizado
st.markdown("""
<style>
    .main-title { 
        color: #1a365d; 
        text-align: center; 
        margin-bottom: 1rem; 
        font-size: 2.5rem;
        font-weight: 700;
    }
    .subtitle {
        color: #555;
        text-align: center;
        margin-bottom: 2rem;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    .year-selector-container {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>📸 Nuestra Historia en Imágenes</h1>", unsafe_allow_html=True)
st.markdown("""
<div class='subtitle'>
Revive los momentos especiales de cada generación que ha pasado por nuestras aulas.<br>
Cada foto cuenta una historia de esfuerzo, amistad y crecimiento.
</div>
""", unsafe_allow_html=True)

# Configuración de imágenes por año
# Aquí puedes agregar las fotos para cada año
fotos_por_año = {
    "2024": [
        {"ruta": "imgs/background7.jpg", "titulo": "Foto 1 - 2024"},
        {"ruta": "imgs/background8.jpg", "titulo": "Foto 2 - 2024"},
    ],
    "2023": [
        {"ruta": "imgs/background9.jpg", "titulo": "Foto 1 - 2023"},
        {"ruta": "imgs/background10.jpg", "titulo": "Foto 2 - 2023"},
    ],
    "2022": [
        {"ruta": "imgs/background11.png", "titulo": "Foto 1 - 2022"},
         {"ruta": "imgs/background12.png", "titulo": "Foto 2 - 2022"},
    ],
    # Agrega más años según necesites
}

# Selector de año
st.markdown("<div class='year-selector-container'>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    años_disponibles = list(fotos_por_año.keys())
    año_seleccionado = st.selectbox(
        "📅 Selecciona el año:",
        años_disponibles,
        index=0,
        help="Elige el año para ver las fotos de esa generación"
    )
st.markdown("</div>", unsafe_allow_html=True)

# Obtener fotos del año seleccionado
fotos_año = fotos_por_año.get(año_seleccionado, [])

if fotos_año:
    st.markdown(f"### 🎓 Generación {año_seleccionado}")
    st.markdown(f"*{len(fotos_año)} {'foto' if len(fotos_año) == 1 else 'fotos'} disponible{'s' if len(fotos_año) > 1 else ''}*")
    
    # Convertir imágenes a base64
    imagenes_base64 = []
    for foto in fotos_año:
        img_base64 = get_base64_image(foto["ruta"])
        if img_base64:
            # Detectar tipo de imagen por extensión
            ext = Path(foto["ruta"]).suffix.lower()
            mime_type = "image/jpeg"
            if ext == ".png":
                mime_type = "image/png"
            elif ext == ".webp":
                mime_type = "image/webp"
            imagenes_base64.append({
                "data": img_base64,
                "mime": mime_type,
                "titulo": foto["titulo"]
            })
    
    # Crear carrusel grande
    if imagenes_base64:
        slides_html = ""
        for i, img in enumerate(imagenes_base64):
            slides_html += f'<div class="slide"><img src="data:{img["mime"]};base64,{img["data"]}" alt="{img["titulo"]}" /><div class="caption">{img["titulo"]}</div></div>\n'
        
        dots_html = ""
        for i in range(len(imagenes_base64)):
            dots_html += f'<span class="dot {"active" if i == 0 else ""}" data-index="{i}"></span>'
        
        carousel_html = f"""
        <style>
        .big-carousel {{
            position: relative;
            overflow: hidden;
            border-radius: 16px;
            background: #f0f0f0;
            box-shadow: 0 4px 16px rgba(0,0,0,0.15);
        }}
        .big-carousel .slides {{
            display: flex;
            transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        .big-carousel .slide {{
            min-width: 100%;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .big-carousel img {{
            width: 100%;
            height: 500px;
            object-fit: contain;
            display: block;
        }}
        .big-carousel .caption {{
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
            color: white;
            padding: 2rem 1.5rem 1rem;
            font-size: 1.2rem;
            font-weight: 600;
            text-align: center;
        }}
        .big-carousel .nav {{
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            width: 100%;
            display: flex;
            justify-content: space-between;
            pointer-events: none;
            padding: 0 1rem;
        }}
        .big-carousel .nav button {{
            pointer-events: auto;
            background: rgba(255,255,255,0.95);
            border: none;
            padding: 1rem 1.2rem;
            border-radius: 50%;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            cursor: pointer;
            font-size: 24px;
            font-weight: bold;
            color: #1a365d;
            transition: all 0.3s ease;
        }}
        .big-carousel .nav button:hover {{
            background: white;
            transform: scale(1.1);
            box-shadow: 0 6px 16px rgba(0,0,0,0.3);
        }}
        .big-carousel .dots {{
            text-align: center;
            padding: 1.5rem 0;
            background: rgba(255,255,255,0.9);
        }}
        .big-carousel .dot {{
            display: inline-block;
            width: 14px;
            height: 14px;
            background: #ccc;
            border-radius: 50%;
            margin: 0 6px;
            cursor: pointer;
            transition: all 0.3s ease;
        }}
        .big-carousel .dot:hover {{
            background: #999;
            transform: scale(1.2);
        }}
        .big-carousel .dot.active {{
            background: #1a365d;
            width: 16px;
            height: 16px;
        }}
        .counter {{
            position: absolute;
            top: 1rem;
            right: 1rem;
            background: rgba(0,0,0,0.7);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.9rem;
            z-index: 10;
        }}
        </style>
        <div class="big-carousel" id="bigCarousel">
          <div class="counter" id="counter">1 / {len(imagenes_base64)}</div>
          <div class="slides" id="bigSlides">
            {slides_html}
          </div>
          <div class="nav">
            <button id="prevBtn">&#10094;</button>
            <button id="nextBtn">&#10095;</button>
          </div>
          <div class="dots" id="bigDots">
            {dots_html}
          </div>
        </div>
        <script>
        (function() {{
            const slides = document.getElementById('bigSlides');
            const dots = document.querySelectorAll('#bigDots .dot');
            const counter = document.getElementById('counter');
            const totalSlides = {len(imagenes_base64)};
            let index = 0;
            let autoplayInterval;
            
            function update() {{
                slides.style.transform = 'translateX(' + (-index * 100) + '%)';
                dots.forEach(d => d.classList.remove('active'));
                if (dots[index]) dots[index].classList.add('active');
                counter.textContent = (index + 1) + ' / ' + totalSlides;
            }}
            
            function nextSlide() {{
                index = (index + 1) % totalSlides;
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
            
            document.getElementById('prevBtn').addEventListener('click', () => {{
                stopAutoplay();
                index = (index - 1 + totalSlides) % totalSlides;
                update();
                startAutoplay();
            }});
            
            document.getElementById('nextBtn').addEventListener('click', () => {{
                stopAutoplay();
                index = (index + 1) % totalSlides;
                update();
                startAutoplay();
            }});
            
            dots.forEach(d => d.addEventListener('click', e => {{
                stopAutoplay();
                index = parseInt(e.target.dataset.index);
                update();
                startAutoplay();
            }}));
            
            // Teclado
            document.addEventListener('keydown', (e) => {{
                if (e.key === 'ArrowLeft') {{
                    stopAutoplay();
                    index = (index - 1 + totalSlides) % totalSlides;
                    update();
                    startAutoplay();
                }} else if (e.key === 'ArrowRight') {{
                    stopAutoplay();
                    index = (index + 1) % totalSlides;
                    update();
                    startAutoplay();
                }}
            }});
            
            // Touch support
            let startX = 0;
            slides.addEventListener('touchstart', (e) => {{
                stopAutoplay();
                startX = e.touches[0].clientX;
            }});
            slides.addEventListener('touchend', (e) => {{
                const dx = e.changedTouches[0].clientX - startX;
                if (dx < -50) {{
                    index = (index + 1) % totalSlides;
                    update();
                }} else if (dx > 50) {{
                    index = (index - 1 + totalSlides) % totalSlides;
                    update();
                }}
                startAutoplay();
            }});
            
            // Pausar autoplay al pasar mouse
            document.getElementById('bigCarousel').addEventListener('mouseenter', stopAutoplay);
            document.getElementById('bigCarousel').addEventListener('mouseleave', startAutoplay);
        }})();
        </script>
        """
        
        st_components.html(carousel_html, height=620, scrolling=False)
    else:
        st.warning(f"⚠️ No se pudieron cargar las imágenes del año {año_seleccionado}")
else:
    st.info(f"📭 No hay fotos disponibles para el año {año_seleccionado}")


# Instrucciones para agregar más fotos
#st.markdown("---")
#with st.expander("ℹ️ Cómo agregar más fotos"):
    #st.markdown("""
    ### Instrucciones para agregar fotos:
    
    #1. **Sube las imágenes** a la carpeta `imgs/` de tu proyecto
    #2. **Edita el archivo** `pages/comunidad.py`
    #3. **Busca la sección** `fotos_por_año` (alrededor de la línea 60)
    #4. **Agrega las rutas** de las nuevas fotos en el año correspondiente:
    
    #```python
    #"2024": [
    #    {"ruta": "imgs/tu_foto.jpg", "titulo": "Descripción de la foto"},
    #    {"ruta": "imgs/otra_foto.png", "titulo": "Otra descripción"},
    #],
    #```
    
    #5. **Guarda el archivo** y recarga la página
    
    #**Formatos soportados:** JPG, PNG, WEBP
   # """)

# Footer
st.markdown("""
<div class='footer'>
    <h3 style='color: #ffffff;'>Escuela Secundaria Federal "Benemérito de las Américas"</h3>
    <p>© 2026 - Formando jóvenes para un mejor futuro</p>
    <p>Zona Escolar 15, Sector 5 | Todos los derechos reservados</p>
    <p>Pagina diseñada por: M.I. José Alberto Payán Marta</p>
</div>
""", unsafe_allow_html=True)