from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all_dojos()
    return render_template("home.html", dojos = dojos)

@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    data={
        "dojo_name" : request.form['dojo_name']
    }
    Dojo.create_dojo(data)
    return redirect('/dojos')


