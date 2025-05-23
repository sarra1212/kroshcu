import streamlit as st
from pathlib import Path
import base64

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "current_page" not in st.session_state:
    st.session_state.current_page = "Dashboard"

USERS = {"sarra.hajjeji37@gmail.com": "sarra12/12/2003"}


def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

LOGO_PATH = "logo_kroschu.png"
logo_b64 = get_base64(LOGO_PATH) if Path(LOGO_PATH).exists() else ""

st.set_page_config(
    page_title="KROSCHU BI",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="collapsed"
)


st.markdown(f"""
<style>
#MainMenu, header, footer {{visibility: hidden;}}
.stApp {{ 
    background: #f8fafc;
    display: flex;
    justify-content: center;
    align-items: center;
}}

.login-container {{
    background: 
        linear-gradient(rgba(255,255,255,0.93), 
        rgba(255,255,255,0.93)),
        url(data:image/png;base64,{logo_b64}) center/cover no-repeat;
    width: 400px;
    padding: 2.5rem;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(106,13,173,0.1);
    margin: auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
}}

.login-title {{
    color: #6A0DAD;
    font-size: 2rem;
    text-align: center;
    margin-bottom: 2rem;
}}

.stButton > button {{
    background: #6A0DAD !important;
    color: white !important;
    width: 100%;
    padding: 0.8rem;
    border: none;
    border-radius: 8px;
    transition: all 0.3s !important;
}}

.stButton > button:hover {{
    background: #4A0D8A !important;
    transform: scale(1.02);
}}

.input-field {{
    margin: 1.5rem 0;
}}

.input-field input {{
    width: 100%;
    padding: 0.8rem;
    border: 2px solid #e2e8f0;
    border-radius: 8px;
}}

.sidebar .stButton button {{
    width: 100%;
    text-align: left;
    margin: 5px 0;
    transition: all 0.3s !important;
}}

.sidebar .stButton button:hover {{
    transform: translateX(10px);
}}

.footer {{
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background: #6A0DAD;
    color: white;
    text-align: center;
    padding: 0.8rem;
    font-size: 0.9rem;
}}
</style>
""", unsafe_allow_html=True)


if not st.session_state.logged_in:
    st.markdown("""
    <div class="login-container">
        <div class="login-title">KROSCHU BI</div>
    """, unsafe_allow_html=True)
    
    email = st.text_input("Adresse email")
    password = st.text_input("Mot de passe", type="password")
    
    if st.button("Se connecter"):
        if USERS.get(email) == password:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Identifiants incorrects")
    
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()


with st.sidebar:
    st.markdown("## Navigation")
    
    if st.button("📊 Tableau de bord", use_container_width=True):
        st.session_state.current_page = "Dashboard"
    
    if st.button("🔮 Prédictions", use_container_width=True):
        st.session_state.current_page = "Prédictions"
    
    if st.button("🔑 Changer mot de passe", use_container_width=True):
        st.session_state.current_page = "Changer mot de passe"
    
    st.markdown("---")
    
    if st.button("🚪 Déconnexion", use_container_width=True):
        st.session_state.logged_in = False
        st.rerun()

if st.session_state.current_page == "Dashboard":
    st.markdown("<div style='text-align:center; color:#6A0DAD; font-size:1.8rem; margin:2rem 0;'>Tableau de bord</div>", unsafe_allow_html=True)
    st.write("""
    <iframe 
        src="https://app.powerbi.com/reportEmbed?reportId=b539f81f-c727-4556-8d5d-5752fe1e5144&autoAuth=true&ctid=1158e2d5-dc24-41ad-abce-62841076dbde"
        style="width:100%; height:75vh; border:none;"
    ></iframe>
    """, unsafe_allow_html=True)

elif st.session_state.current_page == "Prédictions":
    st.markdown("<div style='text-align:center; color:#6A0DAD; font-size:1.8rem; margin:2rem 0;'>Prévisions du profit </div>", unsafe_allow_html=True)
    st.image("70.png" if Path("70.png").exists() else "https://via.placeholder.com/800x400", use_container_width=True)
    st.image("75.png" if Path("75.png").exists() else "https://via.placeholder.com/800x400", use_container_width=True)

elif st.session_state.current_page == "Changer mot de passe":
    st.markdown("<div style='text-align:center; color:#6A0DAD; font-size:1.8rem; margin:2rem 0;'>Changer mot de passe</div>", unsafe_allow_html=True)
    with st.form("change_pass"):
        old_pass = st.text_input("Ancien mot de passe", type="password")
        new_pass = st.text_input("Nouveau mot de passe", type="password")
        confirm_pass = st.text_input("Confirmer le mot de passe", type="password")
        
        if st.form_submit_button("Valider"):
            if new_pass != confirm_pass:
                st.error("Les mots de passe ne correspondent pas")
            elif USERS["sarra.hajjeji37@gmail.com"] != old_pass:
                st.error("Ancien mot de passe incorrect")
            else:
                USERS["sarra.hajjeji37@gmail.com"] = new_pass
                st.success("Mot de passe mis à jour !")
                st.session_state.current_page = "Dashboard"
                st.rerun()


st.markdown("""
<div class='footer'>
    © 2025 KROSCHU BI - Tous droits réservés
</div>
""", unsafe_allow_html=True)
