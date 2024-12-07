from flask import render_template, redirect, request
from flask_app import app 
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/new_ninja")
def new_ninjas():
    dojos = Dojo.get_all()
    return render_template("new_ninjas.html", dojos=dojos)

@app.route("/create_ninja", methods=["POST"])
def create_ninja():
    Ninja.save(request.form)
    return redirect("/dojos")
