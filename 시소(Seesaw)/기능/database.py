import json

def fetch_data():
    try:
        # sample_data.json 파일을 읽어서 데이터 반환
        with open('./웹페이지/data/sample_data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # 파일이 존재하지 않으면 오류 메시지를 출력하고 빈 데이터를 반환
        print("오류: 'sample_data.json' 파일을 찾을 수 없습니다.")
        return {}  # 빈 데이터 반환
    except json.JSONDecodeError:
        # JSON 파싱 중 오류가 발생하면 오류 메시지를 출력
        print("오류: 'sample_data.json' 파일의 내용이 올바르지 않습니다.")
        return {}  # 빈 데이터 반환
    except Exception as e:
        # 그 외의 예기치 않은 오류 처리
        print(f"알 수 없는 오류 발생: {e}")
        return {}  # 빈 데이터 반환