from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', rows=8, cols=8, color1='red', color2='black')

@app.route('/<int:rows>')
def set_rows(rows):
    return render_template('index.html', rows=rows, cols=8, color1='red', color2='black')

@app.route('/<int:rows>/<int:cols>')
def set_rows_cols(rows, cols):
    return render_template('index.html', rows=rows, cols=cols, color1='red', color2='black')

@app.route('/<int:rows>/<int:cols>/<string:color1>/<string:color2>')
def set_rows_cols_color1_color2(rows, cols, color1, color2):
    return render_template('index.html', rows=rows, cols=cols, color1=color1, color2=color2)

if __name__ == '__main__':
    app.run(debug=True)
