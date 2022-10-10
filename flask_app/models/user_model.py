from flask import flash, session
from flask_app.config.mysqlconnection import connectToMySQL
import re



DATABASE = 'login_and_registration_schema'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    def __repr__(self):
        return f'<User: {self.first_name}>'

    @staticmethod
    def validate_registration(form):
        is_valid= True
        if len(form['first_name'])<2:
            flash('First name must be at least two characters', 'first_name')
            is_valid= False
        if len(form['last_name'])<2:
            flash('Last name must be at least two characters','last_name')
            is_valid= False
        if not EMAIL_REGEX.match(form['email']):
            flash ("Invalid email address!",'email')
            is_valid= False
        if len(form['password'])<8:
            flash('Password must be at least eight characters', 'password')
            is_valid=False
        else:
            if form['password'] != form['confirm_password']:
                flash('passwords must match', 'confirm_password')
                is_valid= False
        return is_valid
        
    @staticmethod
    def validate_login(form):
        is_valid= True
        if not EMAIL_REGEX.match(form['email']):
            flash ("Invalid email address!",'log_email')
            is_valid= False
        if len(form['password'])<8:
            flash('Password must be at least eight characters', 'log_password')
            is_valid=False
        return is_valid

    #find by email
    @classmethod
    def find_by_email(cls, data):   
        query = 'SELECT * FROM users WHERE email= %(email)s;'
        results =connectToMySQL(DATABASE).query_db(query, data)
        if len(results)>0:
            return User(results[0])
        return None

        # create a user
    @classmethod
    def save(cls, data):
        # dont need created_at or created_at
        query = 'INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);'
        user_id = connectToMySQL(DATABASE).query_db(query, data)
        return user_id



    # find one user by id
    @classmethod
    def find_by_id(cls, data):
        query = 'SELECT * from users WHERE id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results)> 0:
            return User(results[0])
        return None

    


    # # find all users (no data needed)
    # @classmethod
    # def find_all(cls):
    #     query = 'SELECT * from users;'
    #     results = connectToMySQL(DATABASE).query_db(query)
    #     users = []
    #     for result in results:
    #         users.append(User(result))
    #     return users

    # # find one user by id
    # @classmethod
    # def find_by_id(cls, data):
    #     query = 'SELECT * from users WHERE id = %(id)s;'
    #     results = connectToMySQL(DATABASE).query_db(query, data)
    #     user = User(results[0])
    #     return user

    # # update one user by id
    # @classmethod
    # def find_by_id_and_update(cls, data):
    #     query = 'UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, password = %(password)s WHERE id = %(id)s;'
    #     connectToMySQL(DATABASE).query_db(query, data)
    #     return True

    # # delete one user by id
    # @classmethod
    # def find_by_id_and_delete(cls, data):
    #     query = 'DELETE FROM users WHERE id = %(id)s;'
    #     connectToMySQL(DATABASE).query_db(query, data)
    #     return True