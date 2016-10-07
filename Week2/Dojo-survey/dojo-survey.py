from flask import Flask, render_template, request, redirect

app = Flask(__name__)

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

   return render_template('result.html', name= name, location= location, fav_lang= fav_lang, comments= comments)

app.run(port=5001, debug=True)
