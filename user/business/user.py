import bcrypt
from user.data.models.models import Users, Token_Blocklist
from user.data.dto.output_login import OutputLogin





class UserService:
    
    def __init__(self, user_dal, access_tokens_dal, refresh_dal):
        self.user_dal = user_dal
        self.access_tokens_dal = access_tokens_dal
        self.refresh_dal = refresh_dal

    def get_user_by_email_or_username(self, email=None, username=None):
        return self.user_dal.get_user_by_emain_or_username(email, username)

    def get_existing_user(self, email=None, username=None):
        return self.user_dal.get_user_by_email_or_username(email=email, username=username)
    
    def create_user(self, new_user: Users):
        return self.user_dal.create_user(new_user=new_user)

    def sign_up_user(self, email, username, password):
        existing_user = self.get_existing_user(email=email, username=username)
        if existing_user:
            raise ValueError("User already exists")

        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        
        new_user = Users(
            email=email,
            username=username,
            password=hashed_password.decode('utf-8'),  # bcrypt returns bytes, decode to str
        )

        new_user = self.create_user(new_user=new_user)

        user = OutputLogin(email=new_user.email, username=new_user.username, user_id=new_user.user_id)
        access_token, refresh_token = self.create_tokens(user)
        user.access_token = access_token
        user.refresh_token = refresh_token

        return user
    
    def delete_user (self, email):
        user = self.get_user_by_email_or_username(email)
        if not user:
            raise ValueError("User does not exist!")
        
        self.user_dal.delete_user_data(user.user_id)
    
    def request_password_reset(self, email:str):
        existing_user = self.get_user_by_email_or_username(email)
        if not existing_user:
            raise ValueError("User does not exist!")
        
        


        
