from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<string:name>')
def output(name):
    return "Hi " + name


@app.route('/repeat/<int:num>/<string:word>')
def repeatword(num, word):
    output = ' '
    for i in range(0, num):
        output += f"<p>{word}</p>"

    return output

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)
