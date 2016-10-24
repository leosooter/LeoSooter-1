from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re, time, datetime

app = Flask(__name__)
app.secret_key = 'supersecret'

bcrypt = Bcrypt(app)

mysql = MySQLConnector(app, 'wall')
email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
name_regex = re.compile(r'^[a-zA-Z]{2,}$')
password_regex = re.compile(r'(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{8,}')

#This is my attempt at creating a flash-like global variable to display messages
#in the form. I want to display messages above the appropriate field and I find
#flash unwieldly as it requires 5 lines of code to display a single error message.
form_msg = {
    'errors' : False,
    'login_success' : "",
    'login_email' : "",
    'login_password' : "",
    'registration_success' : "",
    'first_name' : "",
    'last_name' : "",
    'email' : "",
    'password' : "",
    'confirm_password' : "",
}

@app.route('/')
def index():
    global form_msg
    #Check to see if the form_msg needs to display errors- if not- reset form_msg
    if form_msg['errors'] is False:
        for key in form_msg:
            form_msg[key] = ""
    #Setting form_msg to False if it is True ensures that the message only shows one time
    else:
        form_msg['errors'] = False
    return render_template('index.html', form_msg = form_msg)

@app.route('/login', methods=['POST'])
def login():
    global form_msg
    print "Processing Login-Form///////////////////////////////////////////////////////"
    login_valid = True
    login_form = request.form
    #Loop through form to ensure all fields have a value entered
    for key in login_form:
        print key, login_form[key]
        if len(login_form[key]) is 0:
            form_msg[key] = "This field cannot be empty"
            form_msg['errors'] = True
            login_valid = False
    if login_valid is False:
        return redirect('/')

    #check that email is a valid form
    print "checking email"
    email = request.form['login_email'].lower()
    if not email_regex.match(email):
        form_msg['errors'] = True
        form_msg['login_email'] = "Please enter a valid email."
        return redirect('/')

    #Check that email matches an account in the DB
    print "checking for email in DB"
    query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    data = { 'email' : email}
    user_info = mysql.query_db(query, data)
    if not user_info:
        form_msg['errors'] = True
        form_msg['login_email'] = "We do not have an account for this email. Please enter a different email or register a new account."
        return redirect('/')

    #Check that login_password matches password in DB
    print "checking password"

    password = request.form['login_password']
    if bcrypt.check_password_hash(user_info[0]['password'], password):
        session['user_login'] = user_info[0]['id']
        return redirect('/wall')
    else:
        form_msg['errors'] = True
        form_msg['login_password'] = "Email/Password combination you entered is not a match"
        return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    global form_msg
    print "Processing Register-Form///////////////////////////////////////////////////////"
    register_valid = True
    register_form = request.form
    #Loop through form to ensure all fields have a value entered
    for key in register_form:
        print key, register_form[key], len(register_form[key])
        if len(register_form[key]) is 0:
            form_msg[key] = "This field cannot be empty"
            register_valid = False

    if register_valid is False:
        form_msg['errors'] = True
        return redirect('/')

    first_name = request.form['first_name']
    if not name_regex.match(first_name):
        form_msg['first_name'] = "Name must contain at least 2 characters with no numbers or symbols"
        register_valid = False

    last_name = request.form['last_name']
    if not name_regex.match(last_name):
        form_msg['last_name'] = "Name must contain at least 2 characters with no numbers or symbols"
        register_valid = False

    email = request.form['email'].lower()
    if not email_regex.match(email):
        form_msg['email'] = "Please enter a valid email"
        register_valid = False

    query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    data = { 'email' : email}
    email_in_db = mysql.query_db(query, data)
    if email_in_db:
        form_msg['email'] = "We already show an account for this email. Choose a different email or login."
        form_msg['errors'] = True
        return redirect('/')

    password = request.form['password']
    if not password_regex.match(password):
        #This will add the class 'form_msg' to the exsisting password requirement description
        form_msg['password_class'] = "form_msg"
        register_valid = False

    confirm_password = request.form['confirm_password']
    if not confirm_password == password:
        form_msg['confirm_password'] = "Does not match password"
        register_valid = False

    if register_valid is False:
        form_msg['errors'] = True
        return redirect('/')

    elif register_valid is True:
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) \
        VALUES(:first_name, :last_name, :email, :password, NOW(), NOW() )"
        data = {
            'first_name' : first_name,
            'last_name' : last_name,
            'email' : email,
            'password' : bcrypt.generate_password_hash(password),
        }
        mysql.query_db(query, data)

        query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        data = { 'email' : email}
        user_info = mysql.query_db(query, data)

        session['user_login'] = user_info[0]['id']
        return redirect('/wall')

@app.route('/logout')
def logout():
    if 'user_login' in session:
        session.pop('user_login')
    return redirect('/')

@app.route('/wall')
def wall():
    if 'user_login' in session:

        query = "SELECT id, first_name, last_name FROM users WHERE id = :user_id LIMIT 1"
        data = { 'user_id' : session['user_login']}
        user_info = mysql.query_db(query, data)[0]
        #I used updated_at rather than created_at in my queries. Currently these will always be the same sa there is no 'update' feature but I wanted to create queries that would account for that if it was added.
        message_info = mysql.query_db("SELECT CONCAT(first_name, ' ', last_name) AS message_author, messages.id, messages.user_id, message AS message_text, DATE_FORMAT(messages.updated_at, '%r') AS message_time, CASE WHEN DATE(messages.updated_at) = CURDATE() THEN 'Today' WHEN DATE(messages.updated_at) >= DATE_SUB(CURDATE(), INTERVAL 6 DAY) THEN DATE_FORMAT(messages.updated_at, '%W') ELSE DATE_FORMAT(messages.updated_at,'%M %d %Y') END AS message_date, CASE WHEN ( DATE(messages.updated_at) = CURDATE() ) AND ( DATE(messages.updated_at) >= DATE_SUB(CURDATE(),INTERVAL 30 MINUTE) ) THEN 'True' ELSE 'False' END AS under_time_limit FROM messages JOIN users ON users.id = messages.user_id ORDER BY messages.updated_at DESC")

        comment_info = mysql.query_db("SELECT CONCAT(first_name, ' ', last_name) AS comment_author, comments.id, comments.user_id, comment AS comment_text, comments.message_id, DATE_FORMAT(comments.updated_at, '%r') AS comment_time, CASE WHEN DATE(comments.updated_at) = CURDATE() THEN 'Today' WHEN DATE(comments.updated_at) >= DATE_SUB(CURDATE(), INTERVAL 6 DAY) THEN DATE_FORMAT(comments.updated_at, '%W') ELSE DATE_FORMAT(comments.updated_at,'%M %d %Y') END AS comment_date FROM comments JOIN users ON users.id = comments.user_id ")

        return render_template('wall.html', user_info = user_info, message_info = message_info, comment_info = comment_info)
    #If user does not have a session['user_login'] assigned- send them back to index.html
    else:
        return redirect('/')

@app.route('/message', methods=['POST'])
def message():
    if 'user_login' in session:
        message = request.form['message']
        print "validating message: " , message
        if len(message) > 0:
            print "Inserting message into DB"
            query = "INSERT INTO messages (message, user_id, created_at, updated_at) \
            VALUES (:message, :user_id, NOW(), NOW() )"
            data = {
                'message' : message,
                'user_id' : session['user_login']
            }
            mysql.query_db(query, data)
            return redirect('/wall')
        else:
            print "No message"
            return redirect('/wall')
    else:
        print "No user_login id"
        return redirect('/')

@app.route('/comment', methods=['POST'])
def comment():
    msg_id = int(request.form['msg_id'])
    print "message_id = ", msg_id
    if 'user_login' in session:
        comment = request.form['comment']
        print "validating comment"
        if len(comment) > 0:
            print "inserting comment into DB"
            query = "INSERT INTO comments (comment, user_id, message_id, created_at, updated_at) \
            VALUES (:comment, :user_id, :message_id, NOW(), NOW() )"
            data = {
                'comment' : comment,
                'user_id' : session['user_login'],
                'message_id' : msg_id,
            }
            for key in data:
                print key, data[key]

            mysql.query_db(query, data)
            return redirect('/wall')
        else:
            print "No message"
            return redirect('/wall')
    else:
        print "No user_login id"
        return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    #I am assuming here that the 30 minute limit on deleting messages is more of
    #a UI thing- like gmail's 'undo' feature, rather than a security issue.
    #Someone could look at the HTML and figure out how to delete a message after the time-limit.
    #If this was a security issue I would need to run a second query and compare the time the message was created
    #to the current time in this function.
    #This function is only concerned with making sure the message id is valid and that the
    #user is authorized to delete the message.
    print "delete route"
    delete_id = int(request.form['delete_id'])
    print "delete_id = ", delete_id, " type = ", type(delete_id)
    #Check to make sure the message exists in the DB and that it was created by the user
    query = "SELECT user_id FROM messages WHERE id = :delete_id"
    data = { 'delete_id' : delete_id }
    message_user_id = int(mysql.query_db(query,data)[0]['user_id'])
    #If it is valid and created by user, delete message
    if message_user_id == session['user_login']:
        print "Message found and id belongs to user- deleting now."
        query = "DELETE FROM messages WHERE id = :delete_id"
        data = {'delete_id' : delete_id }
        mysql.query_db(query, data)
    else:
        print "Delete message not found in DB"

    return redirect('/wall')

app.run(debug=True)
