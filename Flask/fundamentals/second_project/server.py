from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/another_route')
def another_route():
    return"This is another route!!! :D"

@app.route('/test/<route_data>')
def test_data(route_data):
    return f"The route data that was passed in was {route_data}"

@app.route('/multiply/<int:x>/<int:y>')
def multiply_two_number(x, y):
    return render_template("multiply.html",
    x_on_template = x, y = y, result = x * y)

@app.route('/multiplication_table/<int:x>/<int:y>')
def multiplication_table(x,y):
    #generate data
    results = []

    new_row = ["X"]
    for k in range(0, x + 1):
        new_row.append(k)
    results.append(new_row)

    for i in range(0, y + 1):
        new_row = [i]
        for j in range(0, x + 1):
            new_row.append(i * j)
        results.append(new_row)
        
    print(results)

    return render_template("multitable.html",
    x = x, y = y, results = results)

if __name__ == "__main__":
    app.run(debug= True)
