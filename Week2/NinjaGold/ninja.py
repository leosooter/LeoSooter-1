from flask import Flask, render_template, request, redirect, session
import random, time
app = Flask(__name__)

app.secret_key = 'supersecret'

@app.route('/')
def index():
    try:
        session['activities']
    except KeyError:
        session['activities'] = [["Visit a location to earn gold", "green"]]
    try:
        session['gold']
    except KeyError:
        session['gold'] = 0

    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['place'] == "reset":
        session.pop('activities')
        session.pop('gold')

    elif request.form['place'] == "farm":
        get_money(10,20,"farm")
    elif request.form['place'] == "cave":
        get_money(5,10,"cave")
    elif request.form['place'] == "house":
        get_money(2,5,"house")
    elif request.form['place'] == "casino":
        gamble_money(-50,50)

    return redirect('/')

def get_money(min, max, place):
    gold = random.randrange(min, max + 1)
    date = time.asctime( time.localtime(time.time()) )
    session['gold'] += gold
    msg = "Earned {} gold at the {}! {}".format(gold,place,date)
    session['activities'].append([msg, "green"])

def gamble_money(min, max):
    gold = random.randrange(min, max + 1)
    session['gold'] += gold
    if gold < 0:
        msg = "You lost {} gold at the gambling house!... ouch... ".format(gold)
        session['activities'].append([msg, "red"])
    else:
        msg = "Earned {} gold at the gambling house".format(gold)
        session['activities'].append([msg, "green"])



app.run(port=5001, debug=True)

#session.activities = []
#session.activities.append(["hello", "red"])
