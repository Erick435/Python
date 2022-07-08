from flask import Flask, render_template, request, redirect, session
app = Flask (__name__)

app.secret_key = 'This is my secret key :^)'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['post'])
def create_user():
#print statements appear in the terminal check for info
    print("Got Post Info")
    print(request.form['name'])
    print(request.form['email'])
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    #never render a temlate on a POST request
    #we will re-direct it to our index route
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('show.html')



if __name__ == "__main__":
    app.run(debug = True)