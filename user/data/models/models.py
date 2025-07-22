from django.db import models

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    
class Token_Blocklist(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    token = models.CharField(unique=True)
    token_type = models.CharField(max_length=50, choices=[('access', 'Access'), ('refresh', 'Refresh')])
    revoked = models.BooleanField(default=False)
    expires_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now=True)