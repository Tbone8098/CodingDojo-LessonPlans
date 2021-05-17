from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

db = 'loginReg'

class User:
    def __init__(self, data):
        self.id = data['id']

# C
    @classmethod
    def new(cls, info):
        query = "INSERT INTO users (first_name, last_name, email, pw_hash) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(pw_hash)s)"
        data = {
            "first_name" : info['first_name'],
            "last_name" : info['last_name'],
            "email" : info['email'],
            "pw_hash" : info['pw_hash'],
        }
        new_user_id = connectToMySQL(db).query_db(query, data)

        query = "SELECT * FROM users WHERE id = %(new_user_id)s"
        data = {
            "new_user_id": new_user_id
        }
        new_user = connectToMySQL(db).query_db(query, data)[0]
        return new_user

    
# R
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        all_users = connectToMySQL(db).query_db(query)
        return all_users

    @classmethod
    def get_one(cls, id):
        query = 'SELECT * FROM users WHERE id = %(users_id)s;'
        data = {
            "users_id": id
        }
        one_user = connectToMySQL(db).query_db(query, data)[0]
        return one_user
    
    @classmethod
    def get_one_by_email(cls, email):
        query = "SELECT * FROM users WHERE email = %(email)s"
        data = {
            "email": email
        }
        return connectToMySQL(db).query_db(query, data)
        
# U
    @classmethod
    def update_one():
        pass

# D
    @classmethod
    def delete_one():
        pass

    # @staticmethod
    # def user_validation(form_data):
    #     is_valid = True
    #     errors = {}
    #     if len(form_data['first_name']) < 3:
    #         is_valid = False
    #         errors['first_name'] = "first name must be greater than 3 characters"
    #     if len(form_data['last_name']) < 3:
    #         is_valid = False
    #         errors['last_name'] = "last name must be greater than 3 characters"
    #     if len(form_data['email']) < 3:
    #         is_valid = False
    #         errors['email'] = "email must be greater than 3 characters"
    #     if len(form_data['pw']) < 8:
    #         is_valid = False
    #         errors['pw'] = "password must be greater than 3 characters"
    #     if form_data['pw'] != form_data['confirm_pw']:
    #         errors['confirm_pw'] = "passwords do not match"
    #     session['errors'] = errors
    #     return is_valid
    
    @staticmethod
    def user_validation(form_data):
        is_valid = True
        if len(form_data['first_name']) < 3:
            is_valid = False
            flash("first name must be greater than 3 characters")
        if len(form_data['last_name']) < 3:
            is_valid = False
            flash("last name must be greater than 3 characters")
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(form_data['email']):
            is_valid = False
            flash("Invalid email address")
        if len(form_data['email']) < 3:
            is_valid = False
            flash("email must be greater than 3 characters")
        if len(form_data['pw']) < 8:
            is_valid = False
            flash("password must be greater than 8 characters")
        if form_data['pw'] != form_data['confirm_pw']:
            flash("passwords do not match")
        return is_valid
