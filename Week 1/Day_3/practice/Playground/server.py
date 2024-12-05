from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def play():
    return render_template('index.html', num_boxes=4, color='blue')

@app.route('/<int:num>')
def play_count(num):
    return render_template('index.html', num_boxes=num, color='blue')


@app.route('/<int:num>/<color>')
def play_count_color(num, color):
    return render_template('index.html', num_boxes=num, color=color)

if __name__=='__main__':
    app.run(debug=True)
