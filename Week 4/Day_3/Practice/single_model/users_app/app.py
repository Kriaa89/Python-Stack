
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('index.html', all_users=users)

@app.route('/add_user', methods=('GET', 'POST'))
def add_user():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        age = request.form['age']

        conn = get_db_connection()
        conn.execute('INSERT INTO users (first_name, last_name, email_address, age) VALUES (?, ?, ?, ?)',
                    (first_name, last_name, email, age))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)