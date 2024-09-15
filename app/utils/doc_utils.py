from PyPDF2 import PdfReader


class PDFHandler:
    def __init__(self, pdf_files):
        """
        Initializes the PDFHandler class with a  of PDF file paths.

        :param pdf_files: A list of paths to the PDF files to be read.
        """
        self.pdf_file_l = pdf_files if isinstance(pdf_files, list) else [pdf_files]


    def extract_text_from_pdfs(self):
        """
        Extracts text from all pages of each PDF file in the provided list.

        :return: A string containing the concatenated text of all pages from all PDFs.
        """
        complete_text = ""  # Initialize an empty string to store the extracted text
        for file in self.pdf_file_l:
            reader = PdfReader(file)  # Create a PdfReader object for the current file
            for page in reader.pages:
                # Extract text from the current page
                page_text = page.extract_text()  
                # Append the extracted text to complete_text if it's not None
                if page_text:  
                    complete_text += page_text
        return complete_text