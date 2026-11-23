
def get_retriever(vector_store, k=4):
    """
    Create a retriever from the Chroma vector store.
    """

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k}
    )

    return retriever


def retrieve_documents(retriever, question: str):
    """
    Retrieve relevant documents for a user question.
    """

    documents = retriever.invoke(question)

    return documents
