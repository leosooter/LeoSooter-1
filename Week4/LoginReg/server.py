from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = 'supersecret'

bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'login_reg')

email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
name_regex = re.compile(r'^[a-zA-Z]{2,}$')
password_regex = re.compile(r'(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{8,}')

@app.route('/')
def index():
    print mysql.query_db("SELECT * FROM users")
    return render_template('index.html')

@app.route('/success')
def success():
    if 'user_login' not in session:
        return redirect('/')
    return render_template('success.html')

@app.route('/register', methods=['POST'])
def register():
    print "Processing Register-Form///////////////////////////////////////////////////////"
    register_valid = True
    register_form = request.form
    #Loop through form to ensure all fields have a value entered
    for key in register_form:
        print key, register_form[key], len(register_form[key])
        if len(register_form[key]) == 0:
            flash("Cannot be empty", key)
            register_valid = False
    #If all fields have values- check to see if fields are valid
    first_name = request.form['fname']
    last_name = request.form['lname']
    email = request.form['email']
    password = request.form['password']
    password_conf = request.form['password-conf']

    #Check to see if first name is valid form
    if not name_regex.match(first_name):
        flash("Name must be at least two characters log with no numbers or symbols", 'fname')
        register_valid = False
    #Check to see if last name is valid form
    if not name_regex.match(last_name):
        flash("Name must be at least two characters log with no numbers or symbols", 'lname')
        register_valid = False
    #Check to see if email is valid form
    if not email_regex.match(email):
        flash("Please enter a valid email", 'email')
        register_valid = False
    #Check to see if password if valid form
    if not password_regex.match(password):
        flash("Please enter a valid password", 'password')
        register_valid = False
    #Check to see if confiration password matches password
    if password != password_conf:
        flash("Does not match", 'password-conf')
        register_valid = False
    #If form fields are invalid or empty- return user to form with error messages
    if register_valid == False:
        return redirect('/')
    #If fields are valid and email is not already in DB- enter new user into DB and send to success page
    elif register_valid == True:
        query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        data = {'email' : email}
        user = mysql.query_db(query, data)
        #if email exists in DB- return user to form with error message
        if user:
            flash("We already have an account for this email. Please choose a different email or login above", 'email')
            return redirect('/')
        #Enter new user into DB
        else:
            encrypted_pw = bcrypt.generate_password_hash(password)
            query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :encrypted_pw, NOW(), NOW() )"
            data = {
                'first_name' : first_name,
                'last_name' : last_name,
                'email' : email,
                'encrypted_pw' : encrypted_pw
            }
            mysql.query_db(query, data)
            flash('True', 'registered')
            return redirect('/')



@app.route('/login', methods=['POST'])
def login():
    print "Processing Login-Form///////////////////////////////////////////////////////"
    login_valid = True
    login_form = request.form
    #Loop through Form to ensure all fields have a value entered
    for key in login_form:
        print key, login_form[key], len(login_form[key])

        if len(login_form[key]) == 0:
            flash("Cannot be empty", key)
            login_valid = False
    email = request.form['login-email']
    password = request.form['login-password']
    #Check to see if email is valid form
    if not email_regex.match(email):
        flash("Please enter a valid email", 'login-email')
        login_valid = False
    #Check to see if password if valid form
    if not password_regex.match(password):
        flash("Please enter a valid password", 'login-password')
        login_valid = False
    #If form fields are invalid or empy- return user to form with error messages
    if login_valid == False:
        return redirect('/')

    #If form fields are valid- check to see if email is in DB and if password matches
    elif login_valid == True:
        query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        data = {'email' : email}
        user = mysql.query_db(query, data)
        #if email exists in DB check to see if password asscociated with it matches the password entered
        if user:
            print "email in DB"
            #If password is a match- send success message and set session['id'] to matching user id.
            if bcrypt.check_password_hash(user[0]['password'], password):
                print "Password matches"
                query = "SELECT * FROM users WHERE email = :email LIMIT 1"
                data = {'email' : email}
                user_id = mysql.query_db(query, data)
                print user_id
                session['user_login'] = user_id
                return redirect('/success')
            #If password is not a match return to form with error message
            else:
                print "Password does not match"
                flash("Incorrect password for the email you entered", 'login-password')
        #If email is not a match return to form with error message
        else:
            flash("We cannot find the email you entered in our records- please try again or create a new account", 'login-email')
        return redirect('/')

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_login')
    return redirect('/')

app.run(debug=True)
