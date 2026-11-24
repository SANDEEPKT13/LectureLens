
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

from youtube_rag.config import GROQ_API_KEY, GROQ_MODEL

from youtube_rag.rag.prompts import get_rag_prompt


def get_llm():

    if not GROQ_API_KEY:
        raise ValueError("Groq API key not found in .env")

    llm = ChatGroq(
        model=GROQ_MODEL,
        temperature=0,
        api_key=GROQ_API_KEY
    )
    # temperature = 0 (Strict / Deterministic):
    # The model almost always picks the #1 highest-probability word ("blue"). If you ask the exact same question 10 times, you get nearly the exact same answer every time.
    return llm


def create_rag_chain():

    llm = get_llm()

    prompt = get_rag_prompt()

    output_parser = StrOutputParser()   #Converts the model's response into a plain Python string.

    rag_chain = prompt | llm | output_parser   # lcel LangChain Expression Language

    return rag_chain



def generate_answer(retrieved_docs, question, rag_chain):

    # Combine retrieved document chunks
    context = "\n\n".join(
        doc.page_content for doc in retrieved_docs
    )

    # Pass context and question to the chain
    answer = rag_chain.invoke({
        "context": context,
        "question": question
    })

    return answer

