'''
[템플릿 렌더링해서 URL에 연결하기]
- Jinja2 템플릿, 변수, 조건문/반복문을 포함하는 HTML 파일을 렌더링
→ 템플릿에서 변수, 조건문/반복문 쓰기

1. 변수 사용
    {{ 변수명 }}

2. if / for문
    {% if문 %}          {% endif %}
    {% for문 %}         {% endfor %}
'''

from flask import Flask, render_template
app = Flask(__name__)

# 학생 데이터
student_data = {
    1: {"name": "슈퍼맨", "score": {"국어": 90, "수학": 65}},
    2: {"name": "배트맨", "score": {"국어": 75, "영어": 80, "수학": 75}}
}

@app.route('/')
@app.route('/index')
def index():
    return render_template('base_3_main.html', template_students = student_data)

@app.route('/student/<int:id>')
def student(id):
    return render_template('base_3_student.html',
            template_name = student_data[id]['name'],
            template_score = student_data[id]['score'])

if __name__ == '__main__':
    app.run(debug=True)