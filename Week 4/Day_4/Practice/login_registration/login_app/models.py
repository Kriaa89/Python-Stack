from django.db import models
import re
import bcrypt
from datetime import datetime

class UserManager(models.Manager):
    def validate_registration(self, postData):
        errors = {}
        # first name validation
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters"

        # last name validation 
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters"
        
        # email validation 
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address"
        if User.objects.filter(email=postData['email']).exists():
            errors['email'] = "Email already in use"

        # password validation 
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        if postData['password'] != postData['confirm_password']:
            errors['password'] = "Passwords do not match"
        try:
            birthday = datetime.strptime(postData['birthday'], "%Y-%m-%d")
            age = (datetime.now() - birthday).days // 365
            if age < 13:
                errors['birthday'] = "You must be at least 13 years old to register"
        except ValueError:
            errors['birthday'] = "Invalid date format for birthday"
        return errors
    
    def validate_login(self, postData):
        errors = {}
        user = User.objects.filter(email=postData['email'])
        if not user:
            errors['login'] = "Invalid email/password combination"
        elif not bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
            errors['login'] = "Invalid email/password combination"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    birthday = models.DateField()
    objects = UserManager()
