import asyncio
from fastapi import FastAPI
from translator import translate_text

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello world"}

def scrape_python_doc(query: str) -> str:
    url = f'https://docs.python.org/3/library/{query}.html'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find('div', {'class': 'body'}).text
        return content
    else:
        return '문서를 찾을 수 없습니다.'

    return f"Documentation cotent for {query}"

async def main():
    query = input("검색할 Python 모듈 함수를 입력하세요: ")
    content = scrape_python_doc(query)

    translated = await translated_docs/python-{query}.txt'

    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(translated)

    print(f'{query} 도움말이 번역되어 {file_name}에 저장되었습니다.')

if __name__ == "__main__":
    asyncio.run(main())