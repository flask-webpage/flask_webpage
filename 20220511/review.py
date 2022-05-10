from flask import Flask, render_template
app = Flask(__name__)

# 기초 문법
@app.route('/')
def index():
    return '<h1>Hello World</h1>'

# 기초 문법2
@app.route('/user')
def user():
    return '<h2>유저 메인 페이지</h2>'

# 라우팅
@app.route('/user/<user_name>/<user_id>')
def user_info(user_name, user_id):
    return f'{user_name}님 환영합니다. {user_id}'

if __name__ == '__main__':
    app.run(debug=True)