import asyncio
import requests
from fastapi import FastAPI
from bs4 import BeautifulSoup
from translator import translate_text

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":  "Hello world"}

# 비동기 main 함수
async def main():
    query = input("검색할 python 모듈 함수를 입력하세요: ")
    content = scrape_python_doc(query)
    translated = await translate_text(content)  # await 추가
    file_name = f'translated_docs/python-{query}.txt'
    
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(translated)
    
    print(f'{query} 도움말이 번역되어 {file_name}에 저장되었습니다.')

# 동기 함수에서 비동기 translate_text 호출
def sync_translate(query: str):
    content = scrape_python_doc(query)
    translated = asyncio.run(translate_text(content))  # asyncio.run() 사용
    file_name = f'translated_docs/python-{query}.txt'
    
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(translated)

# 문서 스크래핑 함수
def scrape_python_doc(query: str) -> str:
    url = f'https://docs.python.org/3/library/{query}.html'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find('div', {'class': 'body'}).text
        return content
    else:
        return '문서를 찾을 수 없습니다.'

@app.get("/translate")
async def translate(query: str):
    content = scrape_python_doc(query)
    translated = await translate_text(content)  # await 추가
    return {"result": translated}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)

    # 동기 실행 부분 수정
    query = input("검색할 Python 모듈 함수를 입력하세요: ")
    sync_translate(query)