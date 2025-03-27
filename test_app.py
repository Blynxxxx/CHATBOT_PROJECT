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

    @patch('app.FAISS')  # Mock the FAISS vector store
    @patch('app.os.path.exists')  # Mock checking if a file exists
    def test_create_vector_store_existing(self, mock_exists, mock_faiss):
        # Simulate that the vector store already exists
        mock_exists.return_value = True
        mock_store = MagicMock()
        mock_faiss.load_local.return_value = mock_store

        # Call the function to create or load the vector store
        vector_store = create_vector_store("dummy_path.pdf", ["chunk1"], "mock_embeddings")

        # Assert that the loaded vector store is returned
        self.assertEqual(vector_store, mock_store)
        mock_faiss.load_local.assert_called_once()  # Verify that load_local was called

    @patch('app.FAISS')  # Mock the FAISS vector store again
    @patch('app.os.path.exists')  # Mock checking if a file exists
    def test_create_vector_store_new(self, mock_exists, mock_faiss):
        # Simulate that the vector store does not exist
        mock_exists.return_value = False
        mock_store = MagicMock()
        mock_faiss.from_texts.return_value = mock_store

        # Call the function to create a new vector store
        vector_store = create_vector_store("dummy_path.pdf", ["chunk1"], "mock_embeddings")

        # Assert that the new vector store is created and saved
        self.assertEqual(vector_store, mock_store)
        mock_faiss.from_texts.assert_called_once_with(["chunk1"], embedding="mock_embeddings")
        mock_store.save_local.assert_called_once()  # Verify that save_local was called

    @patch('app.GoogleGenerativeAI')  # Mock the LLM class
    def test_generate_response(self, mock_llm):
        # Simulate the LLM generating a response
        mock_llm.return_value.run.return_value = "This is a response."
        docs = ["doc1", "doc2"]  # Sample documents
        query = "What is this?"  # Sample query

        # Call the function to generate a response
        response = generate_response(mock_llm, docs, query)

        # Assert that the response matches the expected output
        self.assertEqual(response, "This is a response.")
        mock_llm.return_value.run.assert_called_once()  # Verify that run was called

# Run the tests when the script is executed
if __name__ == '__main__':
    unittest.main()