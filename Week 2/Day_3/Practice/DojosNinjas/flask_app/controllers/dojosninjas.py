from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/dojos')
def dojos():
    return render_template('dojo.html', dojos=Dojo.get_all())

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {"id": id}
    return render_template('dojo_show.html', dojo=Dojo.get_one_with_ninjas(data))

@app.route('/ninjas')
def new_ninja():
    return render_template('new_ninja.html', dojos=Dojo.get_all())

@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    dojo_id = Ninja.save(request.form)
    return redirect(f'/dojos/{dojo_id}')
