from flask import Flask, render_template
from data import Students


app = Flask (__name__)
Students = Students ()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/students')
def students():
    return render_template('students.html', students = Students)

@app.route('/student/<string:id>/')
def student(id):
    return render_template('student.html', id=id)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug = True)
