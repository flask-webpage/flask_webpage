'''
[기존에 있던 Bootstrap 연결해보기]
'''

from flask import Flask, render_template
app = Flask(__name__)

# 메인 화면
@app.route('/')
@app.route('/main')
def main():
    return render_template('main.html')

# 커버 화면
@app.route('/cover')
def cover():
    return render_template('cover.html')

# 실제 블로그 화면
@app.route('/index')
def index():
    return render_template('index.html')

# 블로그 테스트 화면 (깨져서 나옴)
@app.route('/index_test')
def index_test():
    return render_template('index_test.html')

# 사진첩
@app.route('/album')
def album():
    return render_template('album.html')

# 테스트 화면
@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)