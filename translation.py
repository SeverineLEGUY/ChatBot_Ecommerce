from langchain_mistralai import ChatMistralAI
from config import MISTRAL_API_KEY

llm = ChatMistralAI(
    model="mistral-large-latest",
    api_key=MISTRAL_API_KEY
)

def translate(text):

    prompt = f"""
    Traduis en français :

    {text}
    """

    return llm.invoke(prompt).content