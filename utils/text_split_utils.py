from langchain.text_splitter import RecursiveCharacterTextSplitter


class TextChunker:
    def __init__(self, input_text):
        """
        Initializes the TextChunker class with the text to be split.

        :param input_text: The string of text that needs to be split into chunks.
        """
        self.input_text = input_text

    def split_into_chunks(self):
        """
        Splits the input text into manageable chunks using the RecursiveCharacterTextSplitter.

        :return: A list of text chunks split according to the specified chunk size and overlap.
        """
        # Initialize the text splitter with specified chunk size, overlap, and length function
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1024,  # Maximum number of characters per chunk
            chunk_overlap=200,  # Number of overlapping characters between consecutive chunks
            length_function=len  # Function used to determine the length of the text
        )

        # Split the input text into chunks using the splitter
        text_chunks = splitter.split_text(self.input_text)
        return text_chunks