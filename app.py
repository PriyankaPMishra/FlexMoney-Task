# importing all the required libraries and methods
from flask import Flask, render_template, request, redirect, url_for 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# initializing the Flask App
app = Flask(__name__)
# configuring the database named 'db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'hjshjhdah kjshkjdhjs'
db = SQLAlchemy(app)


# creating the user class
class user(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True)
    name = db.Column(db.String(200))
    age = db.Column(db.Integer)
    phone = db.Column(db.Integer)
    batch = db.Column(db.Integer)
    enrollment_date = db.Column(db.String, default=date.today)

# creating the payment class
class payment(db.Model):
    payment_id = db.Column(db.Integer, primary_key=True)
    paid_user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    amt = db.Column(db.Integer, default=500)
    payment_status = db.Column(db.Boolean)


'''
Routes for all the operations
'''
# Route to display user records
@app.route('/view_users', methods=['GET'])
def view_users():
    # Fetch all user records from the database
    users = user.query.all()
    return render_template('view_users.html', users=users)


@app.route('/', methods=['GET','POST'])
def form():
    if request.method=='POST':
        # get the details filled by the user from the enrollment form
        name = request.form.get("name")
        email = request.form.get("email")
        age = request.form.get("age")
        phone = request.form.get("phone")
        batch = request.form.get("batch")
        enrollment_date = request.form.get("enrollment_date")

        if not enrollment_date:
            enrollment_date = date.today()
        print(f"Form Data: {email}, {name}, {age}, {phone}, {batch}, {enrollment_date}")  # Debug print

        # add the new user's details in the database
        new_user = user(email=email, name=name, age=age, phone=phone,
                        batch=batch, enrollment_date=enrollment_date)
        print(f"New User Object: {new_user.__dict__}")  # Debug print

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("make_payment"))

    return render_template('index.html')
        
        
# payment form page
@app.route('/payment', methods=['GET', 'POST'])
def make_payment():
    if request.method == 'POST':
        last_added_user = user.query.order_by(user.user_id.desc()).first()
        
        if last_added_user:
            # Get the user_id of the last added user
            paid_user_id = last_added_user.user_id

            # Retrieve other form data (amount, etc.)
            amt = request.form.get("amt")

            print(f"Form Data: {paid_user_id}, {amt}") 

        # add the details as a new entry in the database
        new_payment = payment(paid_user_id=paid_user_id, amt=amt, payment_status=True)
        print(f"New User Object: {new_payment.__dict__}")
        db.session.add(new_payment)
        db.session.commit()

        return redirect(url_for("complete_payment"))

    return render_template('payment.html')


# payment confirmation page
@app.route('/payment_done', methods=['GET', 'POST'])
def complete_payment():
    return render_template('confirmation.html')

# for back to home (enrollment form) button
@app.route('/home')
def back_to_home():
    return redirect(url_for('form'))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)