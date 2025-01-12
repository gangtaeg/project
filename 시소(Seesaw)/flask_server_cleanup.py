from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from datetime import datetime

app = Flask(__name__)
Bootstrap(app)

# Mock function for crawling and saving data
def perform_crawling():
    # Simulated crawling process
    crawled_data = [
        {'item': '맥북 프로', 'price': 1000},
        {'item': '패딩', 'price': 2000},
    ]
    save_data(crawled_data)
    return crawled_data

# Mock function to save data
def save_data(data):
    print("Data saved:", data)

# Mock function to manage data
def get_saved_data():
    return [
        {'item': '맥북 프로', 'price': 1000},
        {'item': '패딩', 'price': 2000},
    ]

# 메인 페이지
@app.route('/')
def main():
    return render_template('main.html')

# 시작하기 버튼 액션
@app.route('/start', methods=['POST'])
def start():
    crawled_data = perform_crawling()
    return render_template('crawled_data.html', data=crawled_data)

# 카테고리
@app.route('/category')
def category():
    return render_template('category.html')

# 카테고리 - no1~no12
today = datetime.now()

def get_results(keyword):
    return [{'keyword': keyword, 'price': 1000}, {'keyword': keyword, 'price': 2000}]  # Mock data

@app.route('/no<int:no>')
def category_no(no):
    keywords = {
        1: '맥북 프로', 2: '패딩', 3: '노트북', 4: '의자', 5: '아이폰',
        6: '아이패드', 7: '캠핑', 8: '냉장고', 9: '컴퓨터', 10: '자전거',
        11: '에어팟', 12: '모니터'
    }
    keyword = keywords.get(no, '기타')
    results = get_results(keyword)
    return render_template('mongo.html', data=results)

# 분쟁 해결 페이지
@app.route('/dispute')
def dispute():
    return redirect('https://safedeal52.github.io/')

# 저장된 데이터 관리 페이지
@app.route('/manage')
def manage():
    data = get_saved_data()
    return render_template('manage_data.html', data=data)

# 지도 페이지 연결
@app.route('/map')
def map():
    return render_template('kakaomap.html')

# JSON 파일
@app.route('/json')
def json():
    return render_template('data.json')

# 메일 발송 페이지
@app.route('/mail', methods=['GET'])
def mailtest():
    return render_template('mail_test.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        price = request.form['price']
        email = request.form['email']
        print(username, price, email)
        return 'done!'
    return render_template('mail_test.html')

if __name__ == '__main__':
    app.run(debug=True)