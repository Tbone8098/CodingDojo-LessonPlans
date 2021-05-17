from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.model_users import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/user/create', methods=['POST'])
def create_user():
    is_valid = User.user_validation(request.form)
    if is_valid:
        hash_pw = bcrypt.generate_password_hash(request.form['pw'])
        print(hash_pw)
        info = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email'],
            "pw_hash": hash_pw,
        }
        new_user = User.new(info)
        print(new_user)
        session['uuid'] = new_user['id']
        return redirect('/success')
    else:
        return redirect('/')

@app.route('/user/login', methods=['POST'])
def login():
    user = User.get_one_by_email(request.form['email'])
    if len(user) < 1:
        print("user not found")
        flash("Invalid login credentials")
    else:
        print("user found")
        if not bcrypt.check_password_hash(user[0]['pw_hash'], request.form['pw']):
            print("passwords don't match")
            flash("Invalid login credentials")
        else:
            session['uuid'] = user[0]['id']
            return redirect('/success')

    return redirect('/')

@app.route('/user/logout')
def logout():
    session.clear()
    return redirect('/')