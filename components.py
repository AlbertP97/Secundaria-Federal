# components.py
import streamlit as st

def navbar():
    """Navbar con navegación nativa de Streamlit"""
    st.markdown("""
    <style>
    .navbar {
        background: linear-gradient(135deg, #f8f9fa, #e9ecef);
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        border: 1px solid #dee2e6;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .nav-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 1rem;
        flex-wrap: wrap;
    }
    .nav-button {
        background: transparent;
        border: 1px solid #dee2e6;
        color: #495057;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        cursor: pointer;
        transition: all 0.3s ease;
        font-weight: 500;
        text-decoration: none;
        display: inline-block;
    }
    .nav-button:hover {
        background: rgba(255,255,255,0.8);
        color: #1a5276;
        border-color: #1a5276;
        transform: translateY(-2px);
    }
    .nav-active {
        background: #1a5276;
        color: white !important;
        border-color: #1a5276;
        box-shadow: 0 2px 4px rgba(26, 82, 118, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Definir páginas
    pages = {
        "🏠 Inicio": "app.py",
        "📚 Oferta Educativa": "pages/ofertas.py", 
        "👥 Comunidad": "pages/comunidad.py",
        "📅 Calendario": "pages/calendario.py",
        "📋 Requisitos": "pages/requisitos.py",
        "📞 Contacto": "pages/contacto.py"
    }
    
    # Obtener página actual
    current_page = st.session_state.get('current_page', 'app.py')
    
    # Crear navbar con botones
    nav_items = []
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    with col1:
        if st.button("🏠 Inicio", use_container_width=True):
            st.session_state.current_page = "app.py"
            st.switch_page("app.py")
    
    with col2:
        if st.button("📚 Oferta", use_container_width=True):
            st.session_state.current_page = "pages/ofertas.py"
            st.switch_page("pages/ofertas.py")
    
    with col3:
        if st.button("👥 Comunidad", use_container_width=True):
            st.session_state.current_page = "pages/comunidad.py"
            st.switch_page("pages/comunidad.py")
    
    with col4:
        if st.button("📅 Calendario", use_container_width=True):
            st.session_state.current_page = "pages/calendario.py"
            st.switch_page("pages/calendario.py")
    
    with col5:
        if st.button("📋 Requisitos", use_container_width=True):
            st.session_state.current_page = "pages/requisitos.py"
            st.switch_page("pages/requisitos.py")
    
    with col6:
        if st.button("📞 Contacto", use_container_width=True):
            st.session_state.current_page = "pages/contacto.py"
            st.switch_page("pages/contacto.py")
    
    return current_page