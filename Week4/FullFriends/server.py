from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = 'supersecret'

mysql = MySQLConnector(app, 'friends')
name_regex = re.compile(r'^[a-zA-Z]+$')

@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM users")
    return render_template('index.html', friends = friends)

@app.route('/friends', methods=['POST'])
def create():
    if validate_name(request.form['fname']) and validate_name(request.form['lname']):
        query = "INSERT INTO users (first_name, last_name, created_at, updated_at) VALUES (:first_name, :last_name, NOW(), NOW())"
        data = {
            'first_name' : request.form['fname'],
            'last_name' : request.form['lname']
        }
        mysql.query_db(query, data)
    else:
        flash("Please enter a valid name (no numbers or symbols)")
    return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
    friend_info = mysql.query_db("SELECT first_name, last_name, id FROM users WHERE id = " + id)
    return render_template('friend.html', friend_info = friend_info)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    if validate_name(request.form['fname']) and validate_name(request.form['lname']):
        query = "UPDATE users SET first_name = :first_name, last_name = :last_name, updated_at = NOW() WHERE id =" + id
        data = {
            'first_name' : request.form['fname'],
            'last_name' : request.form['lname']
        }
        mysql.query_db(query, data)
    else:
        friend_info = mysql.query_db("SELECT first_name, last_name, id FROM users WHERE id = " + id)
        flash("Please enter a valid name (no numbers or symbols)")
    return redirect('/')

@app.route('/friends/<id>/delete', methods = ['POST'])
def destroy(id):
    mysql.query_db("DELETE FROM users WHERE id =" + id)
    return redirect('/')

def validate_name(name):
    if name_regex.match(name):
        return True
    else:
        return False

app.run(debug=True)
