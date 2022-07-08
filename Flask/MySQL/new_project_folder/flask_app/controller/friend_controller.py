from flask_app import app

from flask import render_template, request, redirect
from flask_app.models.friend import Friend

# import the class from friend.py
from flask_app.config.mysqlconnection import connectToMySQL

#route to render all friends
# @app.route("/")
# def index():
#     # call the get all classmethod to get all friends
#     friends = Friend.get_all()
#     print(friends)
#     return render_template("index.html")
            
@app.route('/')
def index():
    friends = Friend.get_all()
    print('*' * 25)
    print(friends)
    print('*' * 25)
    return render_template("index.html", all_friends = friends)

#ROUTE TO CREATE A FRIEND
@app.route('/create', methods=['POST'])
def create_friend():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'occupation' : request.form['occupation']
    }

    Friend.create_friend(data)
    return redirect('/')


#route to render the update form
@app.route('/renderUpdate/<int:id>')
def render_update(id):

    return render_template('update.html', id = id)


#Processing route to update friends
@app.route('/update', methods = ['POST'])
def update_friend():
    data = {
        'id' : request.form['id'],
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'occupation' : request.form['occupation']
    }

    Friend.update_friend(data)
    return redirect('/')


#ROUTE TO DELETE A FRIEND
@app.route('/delete/<int:id>')
def delete_friend(id):

    data = {
        'id' : id
    }

    Friend.delete_friend(data)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)