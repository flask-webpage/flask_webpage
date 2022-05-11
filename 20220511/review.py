from flask import Flask
app = Flask(__name__)

# 기초 문법(시작하자마자 보이는 인덱스 페이지 → '/')
@app.route('/')
def index():
    return '<h1><a href="/user">유저 메인 페이지로 이동</a></h1>' # 렌더링 → HTML(정확하게는 마크업 언어)를 읽을 수 있음 → h1태그가 정상적으로 반영됨

# 기초 문법2(인덱스 페이지 뒤에 user라는 파라미터를 추가해서 '/user'라는 주소에 접속할 수 있도록 설정)
@app.route('/user')
def user():
    return '<h2>유저 메인 페이지</h2>'

# 라우팅
# 주소 뒤에 '/파라미터' 형식으로 파라미터를 넘겨서 내가 원하는 값을 넘길 수 있도록 설정
@app.route('/user/<string:user_name>/<user_id>/<int:user_number>')
def user_info(user_name, user_id, user_number):
    return f'{user_number}번 학번 / {user_name}님 환영합니다. ({user_id})'

if __name__ == '__main__':
    app.run(debug=True)