from flask import Flask, request, render_template, jsonify
import fitz  # PyMuPDF
import os
import google.generativeai as genai

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# ⚠️ IMPORTANT: Replace with your actual API key
GEMINI_API_KEY = "AIzaSyAP46oJCMgdEqFGr0GBt3o0F3e37f4dXyA"  # Replace this with your API key

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Global variable to store extracted text
pdf_text = ""

def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def load_default_pdf():
    """Load the default PDF file on startup"""
    global pdf_text
    default_pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], 'Hi.pdf')
    if os.path.exists(default_pdf_path):
        try:
            pdf_text = extract_text_from_pdf(default_pdf_path)
            print(f"✅ Successfully loaded Hi.pdf - {len(pdf_text)} characters extracted")
        except Exception as e:
            print(f"❌ Error loading Hi.pdf: {str(e)}")
    else:
        print("⚠️ Hi.pdf not found in uploads folder")

def get_gemini_response(question, context=""):
    """Generate response using Gemini API with PDF context"""
    try:
        if context:
            prompt = (
                f"You are a knowledgeable assistant helping someone learn about a portfolio. "
                f"Here is the relevant information:\n\n{context[:4000]}\n\n"
                f"Question: {question}\n\n"
                f"Instructions:\n"
                f"- Answer naturally and conversationally, as if you're explaining to a colleague\n"
                f"- Use the information provided to give accurate, helpful responses\n"
                f"- Don't mention 'the document', 'the text', or 'based on the provided information'\n"
                f"- Speak directly about the topics as if you have first-hand knowledge\n"
                f"- If you cannot answer from the given information, simply say 'I don't have that information available'\n"
                f"- Keep responses concise but informative"
            )
        else:
            prompt = f"Answer this question naturally and helpfully: {question}"
        
        # Generate a response using Gemini
        response = model.generate_content(prompt)
        
        return response.text.strip()
        
    except Exception as e:
        return f"Error generating response: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def index():
    global pdf_text
    response = None

    if request.method == "POST":
        # Handle user question
        question = request.form.get("question")
        if question:
            if pdf_text:
                # Use PDF context with Gemini
                response = get_gemini_response(question, pdf_text[:4000])
            else:
                # Use Gemini without PDF context
                response = "Sorry, no PDF is loaded. Please restart the app."
            
            if not response:
                response = "Sorry, I couldn't generate a response."

    return render_template("index.html", response=response)

if __name__ == "__main__":
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    
    # Load the default PDF file on startup
    load_default_pdf()
    
    print("🤖 Gemini PDF Chatbot Flask App is starting...")
    app.run(debug=True)
