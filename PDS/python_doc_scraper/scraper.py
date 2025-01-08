import requests
from bs4 import BeautifulSoup

def scrape_python_doc(query):
    url = f'https://docs.python.org/3/library/{query}.html'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find('div', {'class': 'body'}).text
        return content
    else:
        return '문서를 찾을 수 없습니다.'