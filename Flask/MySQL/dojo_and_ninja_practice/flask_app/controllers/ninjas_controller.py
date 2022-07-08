from flask_app import app
from flask import render_template, redirect, session, request


from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
@app.route('/ninja')
def ninjas():
    dojos = Dojo.get_all_dojos()

    return render_template('/create.html', dojos = dojos)



@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age'],
        "dojo_id" : request.form['dojo_id']
    }
    Ninja.create_ninja(data)
    
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def ninjas_in_dojo(id):
    data = {
        'id' : id
    }
    single_dojo = Ninja.ninjas_in_dojo(data)
    return render_template('/show_ninja.html', all_dojos = single_dojo)

