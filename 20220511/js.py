from flask import Flask, render_template
app = Flask(__name__)

# 자바스크립트 기초 1(변수 및 함수 선언, if문, for문, console.log)
@app.route('/')
@app.route('/basic0')
def basic0():
    return render_template('js_0.html')

# 자바스크립트 기초 2(document.getElementById, click event)
@app.route('/basic1')
def basic1():
    return render_template('js_1.html')

# 자바스크립트 기초 3(getElementById, getElementsByClassName, getElementsByName)
@app.route('/basic2')
def basic2():
    return render_template('js_2.html')

# 자바스크립트 기초 4(document, click event)
@app.route('/basic3')
def basic3():
    return render_template('js_3.html')

if __name__ == '__main__':
    app.run(debug=True)