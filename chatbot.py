from router import route
from rag import rag_answer
from sql_agent import sql_answer
from recommendation import recommend
from translation import translate
from langchain_mistralai import ChatMistralAI

from config import MISTRAL_API_KEY

llm = ChatMistralAI(
    model="mistral-large-latest",
    api_key=MISTRAL_API_KEY
)

def chatbot(query):

    r = route(query)

    if "rag" in r:
        return rag_answer(query)

    elif "sql" in r:
        return sql_answer(query)

    elif "recommend" in r:
        return recommend(query)

    elif "translate" in r:
        return translate(query)

    else:
        return llm.invoke(query).content