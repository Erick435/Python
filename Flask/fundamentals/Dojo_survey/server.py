from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)

app.secret_key = "wsalkjflksjef"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    description = request.form['description']

    return render_template('result.html', name = name, location = location, language = language, description = description)

if __name__ == "__main__":
    app.run(debug = True)