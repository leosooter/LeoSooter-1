from flask import Flask, render_template, request, redirect, flash

import re, datetime
from datetime import datetime

app = Flask(__name__)

app.secret_key = 'supersecret'

email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
password_regex = re.compile(r'(?=.*[0-9])(?=.*[A-Z])')

@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def create_user():
    print "Recieved Form"
    #store form values so that they can be preserved if form redirects with errors
    flash(request.form['email'], 'email_value')
    flash(request.form['first-name'], 'fname_value')
    flash(request.form['last-name'], 'lname_value')
    flash(request.form['date-of-birth'], 'dob_value')

    #form information is stored as condition/message pairs. If the statement evaluates to true, the input is invalid and the message is displayed.
    #first condition checks to see if input has values entered, second condition varries by input
    user_form = {
        'first_name' : [
            [ eval(str( len(request.form['first-name']) == 0) ) , "Must enter a first name."],
            [ eval(str( str.isalpha(str(request.form['first-name'])) is not True )), "First name cannot contain any numbers."],
            ],
        'last_name' : [
            [ eval(str( len(request.form['last-name']) == 0) ) , "Must enter a last name."],
            [ eval(str( str.isalpha(str(request.form['last-name'])) is not True )), "Last name cannot contain any numbers."],
            ],
        'email' : [
            [ eval(str( len(request.form['email']) == 0) ) , "Must enter an email"],
            [ eval(str( str(email_regex.match(request.form['email'])) == "None" )), "Must enter a valid email"],
            ],
        'date_of_birth' : [
            [ eval(str( len(request.form['date-of-birth']) == 0) ) , "Must enter a date of birth"],
            [ validate_date( request.form['date-of-birth'] ) , "Must enter a valid date- mm/dd/yyyy - before today's date"],
            ],
        'password' : [
            [ eval(str( len(request.form['password']) == 0) ) , "Must enter a password"],
            [ eval(str( str(password_regex.match(request.form['password'])) == "None" )), "Password must contain at least one uppercase letter and at least one number."],
            ],
        'confirm_password' : [
            [ eval(str( len(request.form['confirm-password']) == 0) ) , "Please re-enter your password to confirm"],
            [ eval(str( request.form['password'] != request.form['confirm-password'] )), "Does not match."],
            ],
    }
    if validate_form(user_form):
        flash("", "valid")
        print "Form is valid"



    return redirect('/')
# function to evaluate the date input- returns true if the date is invalid or after today's date
def validate_date(date1):
    try:
        #check that date can be properly formatted
        user_date = datetime.strptime( date1 , '%Y-%m-%d')
        #check that the date is not greater than or equal to current date
        now_date = datetime.strftime(datetime.now(), '%Y-%m-%d')
        now_date = datetime.strptime(now_date , '%Y-%m-%d')
        if user_date >= now_date:
            return True
        else:
            return False
    except:
        return True

#loops through condition/message pairs in form dictionary
#returns true if all inputs are valid
def validate_form(form):
    valid = True
    for key, value in form.items():
        for condition in value:
            if condition[0]:
                valid = False
                flash(condition[1], key)
                print condition[1]
                break
    return valid

app.run(port=5001, debug=True)
