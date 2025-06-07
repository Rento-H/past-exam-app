from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    universities = os.listdir('data')
    return render_template('index.html', universities=universities)

@app.route('/<univ>')
def faculties(univ):
    path = os.path.join('data', univ)
    faculties = os.listdir(path)
    return render_template('faculties.html', univ=univ, faculties=faculties)

@app.route('/<univ>/<faculty>')
def departments(univ, faculty):
    path = os.path.join('data', univ, faculty)
    departments = os.listdir(path)
    return render_template('departments.html', univ=univ, faculty=faculty, departments=departments)

@app.route('/<univ>/<faculty>/<department>')
def years(univ, faculty, department):
    path = os.path.join('data', univ, faculty, department)
    years = os.listdir(path)
    return render_template('years.html', univ=univ, faculty=faculty, department=department, years=years)

@app.route('/<univ>/<faculty>/<department>/<year>')
def exams(univ, faculty, department, year):
    path = os.path.join('data', univ, faculty, department, year)
    pdfs = [f for f in os.listdir(path) if f.endswith('.pdf')]
    return render_template('exams.html', univ=univ, faculty=faculty, department=department, year=year, pdfs=pdfs)

@app.route('/pdf/<path:filepath>')
def pdf_view(filepath):
    full_path = os.path.join('data', filepath)
    directory = os.path.dirname(full_path)
    filename = os.path.basename(full_path)
    return send_from_directory(directory, filename)

if __name__ == '__main__':
    app.run(debug=True)
