class OutputLogin():
    def __init__(self, email:str, user_id:int, username:str, new_user:bool, access_token:str, refresh_token:str):
        self.email = email
        self.user_id = user_id
        self.username = username
        self.new_user = new_user
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.message = "You successfully logged in!"