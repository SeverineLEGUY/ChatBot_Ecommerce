from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_mistralai import ChatMistralAI

# LLM
llm = ChatMistralAI(model="mistral-large-latest")


# 1. Construction de la base RAG
def build_rag():

    with open("data/docs.txt", "r", encoding="utf-8") as f:
        text = f.read()

    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    docs = splitter.create_documents([text])

    embeddings = HuggingFaceEmbeddings()

    vectorstore = FAISS.from_documents(docs, embeddings)

    return vectorstore.as_retriever()


# 2. Initialisation retriever (chargé une seule fois)
retriever = build_rag()


# 3. Fonction principale RAG
def rag_answer(query: str):

    docs = retriever.get_relevant_documents(query)

    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
    Tu es un assistant e-commerce.

    Utilise uniquement ce contexte :

    {context}

    Question : {query}

    Réponds de manière claire et concise.
    """

    return llm.invoke(prompt).content
