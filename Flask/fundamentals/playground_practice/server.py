from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def first():
    return render_template("index.html", num = 3, color = "#9fc5f8")

@app.route('/play/<int:num>')
def second(num):
    return render_template("index.html", num = num, color = "#9fc5f8")

@app.route('/play/<int:num>/<string:color>')
def third(num, color):
    return render_template("index.html", num = num, color = color)

if __name__ == "__main__":
    app.run(debug = True)