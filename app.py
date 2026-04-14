# import streamlit as st
# from chatbot import chatbot   

# st.title(" AI E-commerce Assistant")

# query = st.text_input("Pose ta question")

# if query:
#     response = chatbot(query)
#     st.write(response)


import streamlit as st
from chatbot import chatbot

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(
    page_title="AI E-commerce Assistant",
    page_icon="🛍️",
    layout="wide"
)

# -----------------------
# SIDEBAR
# -----------------------
with st.sidebar:
    st.title("🛍️ AI Assistant")
        
    st.markdown("---")
    st.markdown("###  FONCTIONNALITES")
    st.markdown("- RAG produits")
    st.markdown("- SQL (stock, prix)")
    st.markdown("- Recommandation")
    st.markdown("- Traduction")

    st.markdown("---")
    st.info("Projet IA - démonstration LLM")

# -----------------------
# TITLE
# -----------------------
st.title("💬 Assistant E-commerce Intelligent")

st.caption("Pose une question produit, stock, recommandation ou traduction")

# -----------------------
# CHAT HISTORY
# -----------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Affichage historique
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# -----------------------
# EXEMPLES CLIQUABLES
# -----------------------
st.markdown("### 💡 Exemples rapides")

col1, col2, col3 = st.columns(3)

if col1.button("📦 Produits en stock"):
    st.session_state.user_input = "Quels produits sont en stock ?"

if col2.button("💻 Recommandation laptop"):
    st.session_state.user_input = "Je cherche un laptop puissant à moins de 1200€"

if col3.button("🌍 Traduction"):
    st.session_state.user_input = "Translate: high quality noise cancelling headphones”"

# -----------------------
# INPUT USER
# -----------------------
user_input = st.chat_input("Pose ta question ici...")

# gestion bouton exemples
if "user_input" in st.session_state:
    user_input = st.session_state.user_input
    del st.session_state.user_input

# -----------------------
# CHAT LOGIC
# -----------------------
if user_input:

    # user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    # bot response
    with st.chat_message("assistant"):
        with st.spinner("🤖 Analyse de la demande..."):
            response = chatbot(user_input)
            st.write(response)

    st.session_state.messages.append({"role": "assistant", "content": response})