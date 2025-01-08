async def translate_large_text(content, chunk_size=5000):
    chunks = [content[i:i + chunk_size] for i in range(0, len(content), chunk_size)]
    translated_chunks = []
    for chunk in chunks:
        translated = await translate_text(chunk)
        translated_chunks.append(translated)
    return ''.join(translated_chunks)

@app.get("/translate")
async def translate(query: str):
    content = scrape_python_doc(query)
    translated = await translate_large_text(content)
    return {"result": translated}