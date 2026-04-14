from langchain_mistralai import ChatMistralAI
from config import MISTRAL_API_KEY

llm = ChatMistralAI(
    model="mistral-large-latest",
    api_key=MISTRAL_API_KEY
)

products = [
    "iPhone 14 - smartphone premium",
    "Samsung S23 - Android haut de gamme",
    "MacBook Air M2 - laptop léger",
    "Dell XPS 13 - productivité",
    "Sony WH-1000XM5 - casque audio"
]

def recommend(query):

    prompt = f"""
    Tu es un assistant e-commerce.

    Produits :
    {products}

    Question :
    {query}

    Donne 1 à 3 recommandations avec justification.
    """

    return llm.invoke(prompt).content