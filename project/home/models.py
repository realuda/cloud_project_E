from django.db import models

class User:
    def __init__(self):
        self.user_id = None
        self.usr_name = None
        self.user_email = None
        self.user_pw = None
    
    @classmethod
    def create_from_request(cls, request_data):
        user = User()
        user.user_email = request_data['email']
        user.user_pw = request_data['passwd']
        if 'username' in request_data: 
            user.user_name = request_data['username']
        
        return user    

# Create your models here.
