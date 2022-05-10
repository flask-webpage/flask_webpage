from flask import Flask, render_template
app = Flask(__name__)

# 템플릿 렌더링
student_data = {
    100 : {'name': '김철수', 'score' : {'국어' : 100, '수학' : 100, '영어' : 100}},
    200 : {'name': '박영희', 'score' : {'국어' : 90, '수학' : 90, '영어' : 90}},
    300 : {'name': '홍길동', 'score' : {'국어' : 80, '수학' : 80, '영어' : 80}},
    400 : {'name': '이지은', 'score' : {'국어' : 70, '수학' : 70, '영어' : 70}}
}

@app.route('/')
def index():
    return render_template('score_main.html', template_student = student_data)

@app.route('/score/<int:student_id>')
def score(student_id):
    return render_template('score_student.html',
            name = student_data[student_id]['name'],
            score = student_data[student_id]['score'])

if __name__ == '__main__':
    app.run(debug=True)