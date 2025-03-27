import unittest
from unittest.mock import patch, MagicMock
import os
from app import extract_text_from_pdf, split_text, initialize_embeddings, create_vector_store, generate_response

class TestOrientationChatbot(unittest.TestCase):

    @patch('app.PdfReader')  # Mock the PdfReader class to simulate PDF reading
    def test_extract_text_from_pdf_valid(self, mock_pdf_reader):
        # Create a mock page that simulates extracting text from a PDF
        mock_page = MagicMock()
        mock_page.extract_text.return_value = "Test extracted text."
        mock_pdf_reader.return_value.pages = [mock_page]

        # Call the function with a dummy PDF path
        result = extract_text_from_pdf("dummy_path.pdf")

        # Assert that the extracted text matches the expected output
        self.assertEqual(result, "Test extracted text.")

    @patch('app.PdfReader')  # Mock the PdfReader again for a different test
    def test_extract_text_from_pdf_no_text(self, mock_pdf_reader):
        # Configure the mock to return None for extracted text
        mock_page = MagicMock()
        mock_page.extract_text.return_value = None
        mock_pdf_reader.return_value.pages = [mock_page]

        # Call the function with a dummy PDF path
        result = extract_text_from_pdf("dummy_path.pdf")

        # Assert that the function returns an empty string when no text is found
        self.assertEqual(result, "")

    def test_split_text(self):
        # Test the text splitting function with a sample text
        text = "This is a test text that needs to be split into chunks."
        chunks = split_text(text)
        
        # Assert that the output is as expected (the original text in this case)
        self.assertEqual(chunks, ["This is a test text that needs to be split into chunks."])

    @patch('app.GoogleGenerativeAIEmbeddings')  # Mock the embeddings class
    @patch('app.os.getenv')  # Mock the environment variable retrieval
    def test_initialize_embeddings(self, mock_getenv, mock_embeddings):
        # Simulate getting an API key from environment variables
        mock_getenv.return_value = "fake_api_key"
        embeddings = initialize_embeddings()
        
        # Assert that the embeddings are initialized and not None
        self.assertIsNotNone(embeddings)



# Run the tests when the script is executed
if __name__ == '__main__':
    unittest.main()