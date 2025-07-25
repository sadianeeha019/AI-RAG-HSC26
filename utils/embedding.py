from sentence_transformers import SentenceTransformer

def load_model():
    model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    return model

def embed_chunks(model, chunks):
    return model.encode(chunks, show_progress_bar=True)
