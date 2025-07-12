# ChatbotForPortfolio
# 🤖 Gemini PDF Chatbot – Portfolio-based AI Assistant

This is an intelligent chatbot built using **Google Gemini Pro (via `google-genai`)**, designed to answer questions based entirely on a user's **portfolio PDF**. It can be used as a personal assistant for interviews, career websites, or even job applications.

---

## 📌 Features

- 🔍 Reads and understands content from a PDF (e.g., resume or portfolio)
- 💬 Answers questions strictly based on the uploaded content
- 🧠 Powered by Google Gemini 2.5 Pro
- 📄 Accepts user-uploaded portfolio/resume in `.pdf` format
- ⚙️ Built in Python using Google Colab
- ☁️ Does **not** require a server or hosting — all free via Colab


---

## 🛠️ Technologies Used

- [Google Gemini API (gemini-2.5-pro)](https://ai.google.dev/)
- `google-genai` SDK
- `PyMuPDF` (`fitz`) for PDF parsing
- Python 3.x
- Google Colab

---

## 🧑‍💻 How It Works

1. Upload your portfolio (e.g., `portfolio.pdf`)
2. The chatbot extracts text from the PDF using `PyMuPDF`
3. When you type a question, the bot:
   - Combines your question with the PDF content
   - Sends it to Gemini
   - Responds based only on the extracted PDF content

---

## 📂 File Structure

📁 Gemini-PDF-Chatbot/
├── portfolio.pdf # Your input PDF (uploaded during runtime)
├── Gemini_PDF_Chatbot.ipynb # Main notebook file (Google Colab)
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🧪 Sample Questions

You can ask the bot:

- What technologies do I use?
- Tell me about my machine learning project.
- Do I have web development experience?
- What mobile applications have I built?
- What are my soft skills?

---

## 🔐 Setup Instructions

1. Open the notebook in Google Colab.
2. Upload your `portfolio.pdf` file.
3. Replace the `YOUR_API_KEY` in the code with your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
4. Run all cells and start chatting!

---

## 🧠 Future Enhancements

- Use vector similarity (FAISS) for better long PDF support
- Add a Gradio or web interface
- Memory across multiple questions (conversation history)
- Support for multiple document sources (PDF + CSV + plain text)

---

## 🤝 Contributing

Pull requests are welcome! Feel free to open issues or suggest features.

---

## 📄 License

This project is open-source and free to use for educational and non-commercial purposes.

---
