from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.model_users import User

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/success')
def success():
    if 'uuid' not in session:
        return redirect('/')

    return render_template('success.html')
    
