'''
[기본적인 flask 사용법]
'''

from flask import Flask     # 1. flask 클래스를 가져온다.
app = Flask(__name__)       # 2. 플라스크 객체를 생성한다. (__name__은 현재 실행 중인 모듈 이름을 전달하는 것이다.)

@app.route('/')             # 3. 기본서버 127.0.0.1:5000 뒤에 붙는 주소를 적어준다.
def index():                # 4. 위의 주소를 호출 시 보여 줄 것을 함수로 작성해 준다. 중복되지 않도록만 적어주면된다.
    return 'Hello world'    # 5. 문자열이 출력된다.

@app.route('/login')
def login():
    return 'login'

@app.route('/logout')
def logout():
    return 'logout'

if __name__ == '__main__':  # 6. 다른데서 부르면 실행하지 마라는 뜻이다.
    app.run(debug=True, port=80)     # 1) debug=True : 수정할 경우 수정사항을 바로 반영해서 재시작(기본값은 false) / 2) port : 포트변호 변경(기본값은 5000)