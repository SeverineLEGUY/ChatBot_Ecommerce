from langchain_mistralai import ChatMistralAI
from config import MISTRAL_API_KEY

llm = ChatMistralAI(
    model="mistral-large-latest",
    api_key=MISTRAL_API_KEY
)

def route(query):

    prompt = f"""
    Tu dois répondre UNIQUEMENT par un mot parmi :
    rag, sql, recommend, translate

    Question : {query}
    """

    result = llm.invoke(prompt).content.lower().strip()

    if "rag" in result:
        return "rag"
    elif "sql" in result:
        return "sql"
    elif "recommend" in result:
        return "recommend"
    elif "translate" in result:
        return "translate"
    else:
        return "rag"
