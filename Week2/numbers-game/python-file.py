from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)

app.secret_key = 'supersecret1'

@app.route('/')
def index():
    try:
        session['guess']
    except KeyError:
        session['guess'] = 0

    generate_random()
    return render_template('index.html')

@app.route('/post', methods=['POST'])
def post():
    if request.form['action'] == "guess":
        session['guess'] = int(request.form['guess'])
    elif request.form['action'] == "reset":
        session.pop('guess')
        session.pop('random')
        generate_random()
    return redirect('/')

def generate_random():
    try:
        session['random']
    except KeyError:
        session['random'] = random.randrange(1, 101)

app.run(port=5001, debug=True)
