# components.py
import streamlit as st

def navbar():
    """Navbar mejorado con navegación estilizada en el navbar"""
    # CSS global - se ejecuta una sola vez
    st.markdown("""
    <style>
    :root {
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
      padding-top: calc(var(--nav-height) + 80px);
    }

    .sticky-nav {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      z-index: 9999;
      background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
      padding: 8px 20px;
      box-shadow: 0 4px 12px rgba(26, 54, 93, 0.15);
      max-height: 140px;
      overflow-y: auto;
    }
    
    .sticky-nav .brand { 
      text-align: center;
      color: #ffffff;
      margin-bottom: 8px;
      padding-bottom: 8px;
    }
    
    .sticky-nav .nav-title { 
      margin: 0;
      font-size: 1.9rem;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.2;
      letter-spacing: -0.5px;
    }
    
    .sticky-nav .nav-sub { 
      margin: 0;
      font-size: 0.85rem;
      color: rgba(255,255,255,0.85);
      margin-top: 0px;
      font-weight: 500;
    }
    
    .nav-buttons-container {
      display: flex;
      justify-content: center;
      gap: 8px;
      flex-wrap: wrap;
      width: 100%;
    }
    
    .stSelectbox {
      width: 100%;
    }

    .stButton>button {
      background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
      color: #ffffff;
      border: none;
      padding: 10px 20px;
      border-radius: 6px;
      font-weight: 600;
      transition: all 0.3s ease;
      box-shadow: 0 4px 12px rgba(26, 54, 93, 0.15);
    }
    
    .stButton>button:hover {
      background: linear-gradient(135deg, var(--primary-dark) 0%, var(--primary) 100%);
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(26, 54, 93, 0.25);
    }

    .section-title { 
      color: var(--primary);
      border-bottom: 3px solid var(--accent);
      padding-bottom: 10px;
      margin: 2rem 0 1.5rem 0;
      font-weight: 700;
      font-size: 1.5rem;
    }

    .card { 
      background: var(--card-bg);
      padding: 1.5rem;
      border-radius: 8px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
      border-left: 4px solid var(--primary);
      transition: all 0.3s ease;
    }

    .card:hover {
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
      transform: translateY(-2px);
    }

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

    .subtle-muted { 
      color: var(--text-light);
      font-size: 0.95rem;
    }

    hr {
      border-color: var(--border-color);
      margin: 2rem 0;
    }

    a[data-testid="stPageLink"] { 
      color: var(--primary) !important; 
      font-weight: 600;
      text-decoration: none;
      transition: color 0.3s ease;
    }

    a[data-testid="stPageLink"]:hover {
      color: var(--accent) !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Obtener página actual
    current_page = st.session_state.get('current_page', 'app.py')
    
    # Navbar HTML
    st.markdown("""
    <div class='sticky-nav'>
        <div class='brand'>
            <h1 class='nav-title'>Escuela Secundaria Federal</h1>
            <div class='nav-sub'>Benemérito de las Américas</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Contenedor de botones de navegación
    col1, col2, col3 = st.columns([0.5, 5, 0.5])
    
    with col2:
        nav_cols = st.columns(5, gap="small")
        
        with nav_cols[0]:
            if st.button("🏠 Inicio", use_container_width=True, key="nav_inicio"):
                st.session_state.current_page = "app.py"
                st.switch_page("app.py")
        
        with nav_cols[1]:
            if st.button("📚 Oferta", use_container_width=True, key="nav_oferta"):
                st.session_state.current_page = "pages/ofertas.py"
                st.switch_page("pages/ofertas.py")
        
        with nav_cols[2]:
            if st.button("👥 Comunidad", use_container_width=True, key="nav_comunidad"):
                st.session_state.current_page = "pages/comunidad.py"
                st.switch_page("pages/comunidad.py")
        
        with nav_cols[3]:
            if st.button("📋 Requisitos", use_container_width=True, key="nav_requisitos"):
                st.session_state.current_page = "pages/requisitos.py"
                st.switch_page("pages/requisitos.py")
        
        with nav_cols[4]:
            if st.button("📞 Contacto", use_container_width=True, key="nav_contacto"):
                st.session_state.current_page = "pages/contacto.py"
                st.switch_page("pages/contacto.py")

    return current_page