from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = 'keep it safe'

@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template('index.html', count=session['counter'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)