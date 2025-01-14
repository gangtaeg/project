import matplotlib.pyplot as plt
import os
import json

def generate_chart(data):
    try:
        # 데이터가 비어 있는지 확인
        if not data:
            raise ValueError("입력 데이터가 비어 있습니다.")

        # 항목과 가격을 추출 (항목명과 가격 데이터가 없으면 예외 처리)
        items = [item.get('item') for item in data]
        prices = [item.get('price', '').replace(",", "") for item in data]  # 가격은 문자열로 되어 있을 수 있음

        # 항목과 가격이 모두 유효한 값인지 확인
        if not all(items) or not all(prices):
            raise ValueError("항목명 또는 가격에 유효하지 않은 값이 있습니다.")

        # 가격을 숫자형으로 변환
        try:
            prices = [float(price) for price in prices]
        except ValueError:
            raise ValueError("가격을 숫자 형식으로 변환할 수 없습니다.")

        if not items or not prices:
            raise ValueError("차트를 그리기 위한 데이터가 부족합니다.")

        # 막대 차트 생성
        plt.figure(figsize=(10, 6))  # 차트 크기 설정
        plt.bar(items, prices, color='dodgerblue')  # 파란색 계열로 설정
        plt.xlabel('Item')  # x축 라벨
        plt.ylabel('Price')  # y축 라벨
        plt.title('Market Item Prices')  # 차트 제목
        plt.xticks(rotation=45, ha='right')  # x축 항목 이름 회전
        plt.tight_layout()  # 레이아웃 자동 조정

        # 차트를 이미지 파일로 저장
        save_path = './웹페이지/assets/images/chart.png'
        plt.savefig(save_path, dpi=300)
        plt.close()  # 메모리 해제

        return save_path  # 차트 이미지 저장 경로 반환

    except ValueError as e:
        # 데이터 오류 처리
        print(f"차트 생성 오류: {e}")
        return None  # 오류 발생 시 None 반환
    except Exception as e:
        # 그 외 오류 처리
        print(f"알 수 없는 오류 발생: {e}")
        return None  # 오류 발생 시 None 반환

def create_sample_data():
    file_path = './웹페이지/data/sample_data.json'
    data = {
        "latestPrice": 145,
        "transactions": [
            {"id": 1, "date": "2025-01-01", "buyer": "UserA", "seller": "UserB", "amount": 100, "status": "completed"},
            {"id": 2, "date": "2025-01-02", "buyer": "UserC", "seller": "UserD", "amount": 50, "status": "pending"},
            {"id": 3, "date": "2025-01-03", "buyer": "UserE", "seller": "UserF", "amount": 200, "status": "completed"},
        ]
    }
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)