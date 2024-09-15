from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings



class VectorStoreHandler:
    def __init__(self):
        """
        Initializes the VectorStoreHandler class and sets up the embeddings.
        """
        self.embedding_model = OpenAIEmbeddings()  # Initialize the OpenAI embeddings model

    def create_embeddings(self, text_chunks):
        """
        Embeds the given text chunks and saves them to a persistent Chroma database.

        :param text_chunks: A list of text chunks to be embedded.
        """
        # Create a Chroma vector store from the provided text chunks
        Chroma.from_texts(
            text_chunks,  # The list of text chunks to embed
            self.embedding_model,  # The embedding model to use
            persist_directory="../data/chroma_db"  # Directory where the vector store will be saved
        )

    def get_retriever(self):
        """
        Loads the Chroma vector store from disk and sets up a retriever for querying.

        :return: A retriever object configured to search the vector store.
        """
        # Load the Chroma vector store from the specified directory
        vector_store = Chroma(
            persist_directory="../data/chroma_db",  # Directory containing the saved vector store
            embedding_function=self.embedding_model  # Embedding function to use for retrieval
        )
        # Set up the retriever with search parameters (e.g., top 20 results)
        retriever = vector_store.as_retriever(search_kwargs={"k": 20})
        return retriever
