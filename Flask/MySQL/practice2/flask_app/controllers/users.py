from flask_app import app

from flask import render_template, redirect, request
from flask_app.models.user import User

from flask_app.config.mysqlconnection import connectToMySQL

@app.route('/')
def home():
    return redirect('/users')

@app.route('/users')
def index():
    users = User.get_all()
    print('*' * 50)
    print('*' * 50)
    print(users)
    print('*' * 50)
    print('*' * 50)
    return render_template('read.html', all_users = users)

# CREATING A USER ==================
@app.route('/users/new')
def render_create():    

    return render_template('create.html')

@app.route('/create', methods = ['POST'])
def create_user():
    # data = {
    #     'first_name' : request.form['first_name'],
    #     'last_name' : request.form['last_name'],
    #     'email' : request.form['email']
    # }
    # User.create_user(data)

    User.create_user(request.form)
    return redirect('/users')

# UPDATING A USER=============

@app.route('/users/<int:id>/edit')
def render_update(id):
    data = {
        'id' : id
    }
    # users = User.read_one(data)
    return render_template('update.html', users = User.read_one(data))

# READ THE ONE USER ========================

@app.route('/users/<int:id>')
def read_one(id):
    data = {
        'id' : id
    }
    # users = User.read_one(data)
    return render_template('read_one.html', users = User.read_one(data))

# PROCESSING THE UPDATE ================
@app.route('/update', methods = ['POST'])
def update_user():
    
    # data = {
    #     'id' : id,
    #     'first_name' : request.form['first_name'],
    #     'last_name' : request.form['last_name'],
    #     'email' : request.form['email'],
    # }
    User.update_user(request.form)
    return redirect('/users')

# DELETING A USER==========================

@app.route('/delete/<int:id>')
def delete_user(id):
    data = {
        'id' : id
    }
    User.delete_user(data)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug = True)