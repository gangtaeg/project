import requests
from bs4 import BeautifulSoup

def crawl_market_data():
    try:
        url = "https://example-market.com"  # 실제 마켓 URL로 수정 필요
        response = requests.get(url)
        response.raise_for_status()  # HTTP 오류가 있을 경우 예외 발생
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 크롤링 로직 예시: 예시 데이터로 상품명과 가격 추출
        market_data = []
        items = soup.find_all('div', class_='item')  # 예시: 'item' 클래스의 div 찾기
        
        if not items:
            raise ValueError("크롤링할 데이터가 없습니다.")  # 데이터가 없으면 예외 처리

        for item in items:
            name = item.find('h2').text.strip() if item.find('h2') else "Unknown"  # 상품명 추출
            price = item.find('span', class_='price').text.strip() if item.find('span', class_='price') else "0"  # 가격 추출
            market_data.append({"item": name, "price": price})
        
        if not market_data:
            raise ValueError("크롤링된 데이터가 비어 있습니다.")
        
        return market_data

    except requests.exceptions.RequestException as e:
        # 네트워크 요청 관련 예외 처리
        return {"error": "웹 페이지 요청 중 오류가 발생했습니다.", "details": str(e)}
    except ValueError as e:
        # 데이터가 없거나 잘못된 경우
        return {"error": "크롤링 데이터 처리 오류", "details": str(e)}
    except Exception as e:
        # 그 외 일반적인 오류 처리
        return {"error": "알 수 없는 오류 발생", "details": str(e)}

def get_sample_data():
    try:
        data = crawl_market_data()
        
        if "error" in data:
            raise ValueError(data["error"])  # 크롤링 오류 발생 시 처리
        
        # 거래 내역 예시
        return {
            "latestPrice": 145,
            "transactions": [
                {
                    "id": 1,
                    "date": "2025-01-01",
                    "buyer": "UserA",
                    "seller": "UserB",
                    "amount": 100,
                    "status": "completed"
                },
                {
                    "id": 2,
                    "date": "2025-01-02",
                    "buyer": "UserC",
                    "seller": "UserD",
                    "amount": 50,
                    "status": "pending"
                },
                {
                    "id": 3,
                    "date": "2025-01-03",
                    "buyer": "UserE",
                    "seller": "UserF",
                    "amount": 200,
                    "status": "completed"
                }
            ]
        }
    
    except ValueError as e:
        return {"error": "샘플 데이터 로딩 실패", "details": str(e)}
    except Exception as e:
        return {"error": "알 수 없는 오류 발생", "details": str(e)}