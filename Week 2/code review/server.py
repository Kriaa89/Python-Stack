from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)
app.secret_key = 'keep it safe'

questions = [
    {
        'question': 'What is Flask?',
        'options': ['A web framework for Python', 'A database', 'A JavaScript library', 'A CSS framework'],
        'answer': 'A web framework for Python'
    },
    {
        'question': 'How do you install Flask?',
        'options': ['npm install Flask', 'composer install Flask', 'pipenv install Flask', 'gem install Flask'],
        'answer': 'pipenv install Flask'
    },
    {
        'question': 'Which file is typically the main application file in a Flask project?',
        'options': ['server.py', 'server.html', 'server.js', 'server.yaml'],
        'answer': 'server.py'
    },
    {
        'question': 'Which decorator is used to define a route in Flask?',
        'options': ['@route', '@app.route', '@path', '@flask.route'],
        'answer': '@app.route'
    },
    {
        'question': 'What is the default port Flask runs on?',
        'options': ['3000', '8080', '80', '5000'],
        'answer': '5000'
    }
]

@app.route('/')
def home():
    session['score'] =0
    return render_template("quiz.html", question = questions[0], question_number=0)

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    question_number = int(request.form['question_number'])
    slected_answer = request.form['answer']
    if slected_answer == questions[question_number]['answer']:
        session['score'] += 1
    if question_number +1 <len(questions):
        return render_template("quiz.html", question = questions[question_number+1], question_number = question_number + 1)
    else:
        return redirect('/result')

@app.route('/result')
def result(): 
    score = session.get('score', 0)
    return render_template ('/reshtmlult.', score=score)

app.route("/reset")
def reset():
    session.pop('score' None)

if __name__ == '__main__':
    app.run(debug=True)