# 📘 Multilingual Retrieval-Augmented Generation (RAG) System – Bangla + English

## 👩‍💻 AI Engineer (Level-1) Technical Assessment

This project implements a **Multilingual RAG (Retrieval-Augmented Generation) System** using a Bangla PDF textbook (`HSC26 Bangla 1st Paper`) as the knowledge base. The system accepts queries in both **Bangla and English**, retrieves the most relevant chunks, and uses **OpenAI GPT-3.5** to generate accurate answers.

---

## 📂 Project Structure

```
📁 ai-rag-hsc26
├── main_cleaned .ipynb
├── requirements.txt
├── README.md
├── test_queries.txt
├── sample_outputs/
├── utils/
└── app.py (optional)
```

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/sadianeeha019/ai-rag-hsc26.git
cd ai-rag-hsc26
pip install -r requirements.txt
```

Make sure you export your OpenAI API key:

```bash
export OPENAI_API_KEY=your-key-here
```

---

## 💬 How It Works

1. Extracts and cleans text from the Bangla PDF using `PyMuPDF`
2. Splits the text into 2-sentence chunks using Bangla delimiter `।`
3. Converts chunks into embeddings using multilingual transformer model
4. Stores embeddings into FAISS vector index
5. Accepts a query → embeds → retrieves → answers using OpenAI GPT-3.5

---

## ✅ Mandatory Questions & Detailed Answers

### 1. What method or library did you use to extract the text, and why?
Used `PyMuPDF` (fitz) for structured and efficient Bangla PDF extraction. Some formatting inconsistencies were handled during cleanup.

### 2. What chunking strategy did you choose and why?
2-sentence chunking based on `।` to maintain semantic units for better retrieval accuracy.

### 3. What embedding model did you use and why?
Used `paraphrase-multilingual-MiniLM-L12-v2` (supports 50+ languages including Bangla + English). Lightweight and semantically powerful.

### 4. How are you comparing the query with your stored chunks?
Used `FAISS` with L2 distance for fast similarity search. Embeddings are compared vectorially.

### 5. How do you ensure meaningful comparisons? What if the query is vague?
Same model for query + chunks ensures semantic alignment. If vague, fallback response is returned or low-ranked chunks skipped.

### 6. Do the results seem relevant? What could improve them?
Yes. Could be improved using overlapping chunking, larger embeddings, or fine-tuned Bangla models.

---

## 📄 License
MIT











---

## 🙋 Author

Made by Sadia Sabrin Neha  
GitHub: [sadianeeha019](https://github.com/sadianeeha019)
