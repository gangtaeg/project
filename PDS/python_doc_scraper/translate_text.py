import asyncio
from translator import translate_text  # 비동기 번역 함수
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

def scrape_python_doc(query: str) -> str:
    # 가상의 문서 내용 반환 (실제 스크래핑 대신)
    return f"Documentation content for {query}"

async def main():
    query = input("검색할 Python 모듈 함수를 입력하세요: ")
    content = scrape_python_doc(query)

    # 번역 함수 호출
    translated = await translate_text(content)  # 비동기 호출 시 await 사용

    # 번역 결과를 파일에 저장
    file_name = f'translated_docs/python-{query}.txt'
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(translated)  # translated는 문자열로 반환됨

    print(f"'{query}' 도움말이 번역되어 {file_name}에 저장되었습니다.")

if __name__ == "__main__":
    asyncio.run(main())  # asyncio로 비동기 함수 실행