from flask import Flask, render_template, request, redirect, session
app = Flask (__name__)

app.secret_key = 'This is my secret key :^)'

@app.route('/')
def index():

    if 'refreshed' not in session:
        session['refreshed'] = 1
    else: 
        session['refreshed'] += 1
    return render_template('index.html')


@app.route('/count', methods=['post'])
def refreshed():
    
    if request.form['change'] == 'click':
        session['refreshed'] += 1
    elif request.form['change'] == 'reset':
        session['refreshed'] = 0
        return redirect('/destroy_session')

    return redirect('/')

@app.route('/destroy_session')
def delete():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)