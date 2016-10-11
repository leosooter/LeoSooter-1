from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)

app.secret_key = 'supersecret'

@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def create_user():
    print "Recieved Form"
    name = request.form['name']
    location = request.form['location']
    fav_lang = request.form['fav-lang']
    comments = request.form['comments']
    valid = True
    if len(name) == 0:
        flash("You must enter a name.")
        valid = False
    if len(comments) == 0:
        flash("You must enter a comment")
        valid = False
    elif len(comments) > 120:
        flash("Comments cannot be more than 120 characters")
        valid = False
    if valid == False:
        return render_template('index.html')
    else:
        return render_template('result.html', name= name, location= location, fav_lang= fav_lang, comments= comments)

app.run(port=5001, debug=True)
