from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say_name(name):
    print(name)
    return f"Hi  {name}!"

@app.route('/repeat/<int:num>/<word>')
def repeat(num, word):
    return (word + ' ') * num

app.run(debug=True, host="localhost", port=8000)
    