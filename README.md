# PDF Extractor and Question Answering System

This project is a Flask-based web application that allows users to upload PDF files, extract their content, and ask questions based on the extracted text. The system uses PyMuPDF for text extraction and integrates with the Groq API for question answering.

## Features

- Upload PDF files and extract their text content.
- Ask questions strictly based on the uploaded PDF content.
- Provides accurate answers or responds with "I don't know" if the answer is not found in the PDF.

## Prerequisites

- Python 3.7 or higher
- Install the required dependencies using `pip install -r requirements.txt`.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd pdf_extractor
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the Groq API key in the `pdf_main.py` file:
   ```python
   client = groq.Groq(api_key="your_api_key_here")
   ```

## Usage

1. Run the Flask application:
   ```bash
   python pdf_contain_extractor/pdf_main.py
   ```

2. Open your browser and navigate to `http://127.0.0.1:5000`.

3. Upload a PDF file and ask questions based on its content.

## API Endpoints

### `/upload` (POST)
- Upload a PDF file.
- **Request**: Multipart form data with a file field.
- **Response**: JSON message confirming upload and processing.

### `/ask` (POST)
- Ask a question based on the uploaded PDF content.
- **Request**: JSON with a `question` field.
- **Response**: JSON with the answer or an error message.

## Notes

- Ensure the Groq API key is valid and has access to the required model.
- The application strictly answers questions based on the uploaded PDF content.

## License

This project is licensed under the MIT License. See the LICENSE file for details.