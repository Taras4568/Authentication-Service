from django.db import transaction
from django.db.models import Q
from user.data.models.models import Users, Token_Blocklist

class UserDal:
    def get_user_by_email_or_username(self, email=None, username=None):
        return Users.objects.filter(
            Q(email=email) | Q(username=username)
        ).first()
    
    def create_user(self, new_user:Users ):
        new_user.save()
        return new_user
    
    def delete_user(self, user_id: int):
        Users.objects.filter(id=user_id).delete()

    def delete_user_data(self, user_id:int):
        with transaction.atomic():
            Token_Blocklist.objects.filter(user_id=user_id).delete()
            self.delete_user(user_id)

    def get_user_by_id(self, user_id:int):
        return Users.objects.filter(id=user_id).first()
    
    def update_user_password(self, user:Users, new_password:str):
        user.password = new_password
        user.save()
        
    def update_user_name(self, user_id:int, new_username:str):
        user = self.get_user_by_id(user_id)
        if user:
            user.username = new_username
            user.save()
        
    def update_user_email(self, user_id:int, new_email:str):
        user = self.get_user_by_id(user_id)
        if user:
            user.email = new_email
            user.save()
            
