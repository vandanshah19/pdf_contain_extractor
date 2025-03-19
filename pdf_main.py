import os
import fitz  # PyMuPDF for extracting text
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import groq

client = groq.Groq(api_key="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")   # Replace with your API key

app = Flask(__name__)
CORS(app)

upload_folder = "uploads"
os.makedirs(upload_folder, exist_ok=True)

pdf_text = ""

# Function to extract text from PDF
def extractTextFromPdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text("text") for page in doc])
    return text

@app.route("/")
def home():
    return render_template("index.html")  # Serve the frontend

@app.route("/upload", methods=["POST"])
def uploadPdf():
    global pdf_text

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)

    pdf_text = extractTextFromPdf(file_path)

    return jsonify({"message": "File uploaded and processed successfully!"})

@app.route("/ask", methods=["POST"])
def askQuestion():
    global pdf_text
    if not pdf_text:
        return jsonify({"error": "No PDF uploaded yet!"}), 400

    data = request.json
    question = data.get("question", "")

    if not question:
        return jsonify({"error": "No question provided!"}), 400

    response = client.chat.completions.create(
        model="llama3-70b-8192",  # Correct model name for Groq
        messages=[
            {"role": "system", "content": """
                You are an AI assistant that answers questions **strictly based** on the uploaded PDF document.
                If the answer is not explicitly found in the PDF, respond **only** with 'I don't know.' 
                Do not generate answers based on outside knowledge. Stay strictly within the given PDF content.
            """},
            {"role": "user", "content": f"PDF Content: {pdf_text}\n\nQuestion: {question}"}
        ]
    )  

    answer = response.choices[0].message.content
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
