'''
[동적 URL]
- '라우팅'이라고도 불린다.
<converter : variable_name> 형식으로 써주면 된다.
ex) 유저 아이디와 유저 비밀번호를 받아서 출력해주는 페이지

[HTML 렌더링]
- 렌더링이란?
    => 웹 브라우저의 엔진이 해석해서 보여주는 것
'''

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

# 동적 URL
@app.route('/user/<user_id>/<user_pw>')
def user(user_id, user_pw):
    return 'ID : {}, PW: {}'.format(user_id, user_pw)
    #return f'ID : {user_id}, PW: {user_pw}'

# HTML 렌더링
@app.route('/html')
def html():
    return '''
    <h1> 안녕하세요 </h1>
    <a href="https://www.naver.com">네이버</a>
    '''

if __name__ == '__main__':
    app.run(debug=True, port=6060)