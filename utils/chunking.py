def bangla_chunk_text(text, size=2):
    sentences = text.split("।")
    sentences = [s.strip() for s in sentences if s.strip()]
    chunks = ['। '.join(sentences[i:i+size]) + "।" for i in range(0, len(sentences), size)]
    return chunks
