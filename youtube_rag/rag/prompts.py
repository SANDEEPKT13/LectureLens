
from langchain_core.prompts import ChatPromptTemplate


def get_rag_prompt():

    prompt = ChatPromptTemplate.from_template(
        """
        You are a helpful AI YouTube research assistant.

        Answer the user's question using ONLY the
        context provided below.

        If the answer is not available in the context,
        clearly say that the video does not provide
        enough information.

        Do not make up information.

        Context:
        {context}

        Question:
        {question}

        Answer:
        """
    )

    return prompt
