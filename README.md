# ChatBot_Ecommerce
# 🛍️ AI E-commerce Assistant

## 🤖 Chatbot intelligent e-commerce (RAG + SQL + Recommandation + Traduction)

---

## 🎯 Objectif du projet

Ce projet simule un **assistant e-commerce intelligent** capable de :

- 🔎 répondre à des questions produits via RAG
- 🗄️ interroger une base de données SQL (produits, stock, prix)
- 🛍️ recommander des produits personnalisés
- 🌍 traduire des descriptions produits
- 🔀 router automatiquement les requêtes vers le bon module IA

---

## 🚀 Cas d’usage métier

Ce chatbot peut être utilisé pour :

- améliorer l’expérience client sur un site e-commerce
- réduire les demandes du support client
- faciliter la découverte produit
- automatiser les réponses commerciales
- internationaliser les contenus produits

---

## 🏗️ Architecture du projet

## 🧠 Fonctionnalités

### 🔎 RAG (Retrieval Augmented Generation)
- Recherche sémantique dans un catalogue produit
- Embeddings HuggingFace + FAISS

---

### 🗄️ SQL Agent
- Base de données SQLite e-commerce
- Requêtes sur :
  - stock
  - prix
  - produits

---

### 🛍️ Recommandation produit
- Suggestions personnalisées selon le besoin utilisateur
- Basé sur un LLM (Mistral)

---

### 🌍 Traduction
- Traduction de descriptions produits
- Support multilingue

---

### 🔀 Router intelligent
- Classification automatique des intentions :
  - RAG
  - SQL
  - Recommendation
  - Translation

---

## 🛠️ Stack technique

- Python 🐍
- Streamlit 🎨
- LangChain 🧠
- Mistral AI 🤖
- FAISS 🔎
- SQLite 🗄️
- Pandas 📊
- HuggingFace Embeddings 🤗

---

## 📁 Structure du projet
```
ai-ecommerce-chatbot/
│
├── app.py # Interface Streamlit
├── chatbot.py # Orchestrateur IA
├── router.py # Classification intent
│
├── rag.py # RAG (FAISS)
├── sql_agent.py # Requêtes SQL
├── sql_setup.py # Initialisation base SQLite
├── recommendation.py # Moteur de recommandation
├── translator.py # Traduction
│
├── data/
│ ├── ecommerce.db
│ ├── products.csv
│ └── docs.txt
│
├── requirements.txt
└── README.md
```

## 🚀 Améliorations possibles
- Ajout mémoire conversationnelle
- Migration vers LangGraph
- Vector DB (Weaviate / Pinecone)
- Déploiement cloud (Streamlit Cloud / AWS)
