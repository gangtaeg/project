from fastapi import FastAPI
from scraper import scrape_python_doc
from translator import translate_text

app = FastAPI()

@app.get("/translate")
async def translate(query: str):
    content = scrape_python_doc(query)
    translated = translate_text(content)
    return {"result": translated}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)