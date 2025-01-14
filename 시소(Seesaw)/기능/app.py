import os
from flask import Flask, render_template

# Flask 앱에서 템플릿 폴더 경로 설정
app = Flask(__name__, template_folder=os.path.join(os.getcwd(), '웹페이지', 'templates'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/technology')
def technology():
    return render_template('technology.html')

@app.route('/dispute')
def dispute():
    return render_template('dispute.html')

@app.route('/features')
def features():
    return render_template('features.html')

if __name__ == '__main__':
    app.run(debug=True)