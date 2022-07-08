from flask import Flask, render_template
#to import our helpers.py function to this file, we do... 
#from {filename} import {function name}
from helpers import generate_checkerboard

app = Flask(__name__)

@app.route('/')
def checkerboard():
    result = generate_checkerboard(8, 8)
    return render_template('index.html', result = result)

@app.route('/<int:y>')
def checkerboard_2(y):
    result = generate_checkerboard(8, y)
    return render_template("index.html", result = result)



@app.route('/<int:x>/<int:y>')
def checkerboard_3(x, y):
    result = generate_checkerboard(x, y)
    return render_template("index.html", result = result)


if __name__ == "__main__":
    app.run(debug = True)