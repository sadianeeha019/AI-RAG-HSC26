import numpy as np
import faiss
import openai

def build_faiss_index(embeddings):
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings).astype('float32'))
    return index

def search(model, index, query, chunks, top_k=3):
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding).astype('float32'), top_k)
    return [chunks[i] for i in I[0]]

def generate_answer(query, context, api_key):
    openai.api_key = api_key
    prompt = f"""Answer the following question based on the context below.
Respond in the same language as the query.

Context:
{context}

Question:
{query}

Answer:"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response['choices'][0]['message']['content'].strip()
