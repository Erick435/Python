from flask import Flask, render_template,request, redirect, session
app = Flask(__name__)
app.secret_key = "I am a flask project by Erick Ortega"

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/handle_results', methods = ['POST'])
def receive_form():

    session['full_name'] = request.form['full_name']
    session['maiden_name'] = request.form['mothers_maiden_name']
    session['first_pet'] = request.form['first_pet']
    session['ssn'] = request.form['ssn']
    return redirect('/show_results')

@app.route('/show_results')
def show_results():
    
    return render_template('result.html')


if __name__ == "__main__":
    app.run(debug=True)