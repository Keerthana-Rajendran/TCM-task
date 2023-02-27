from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE = [
        ('Sales Person', 'Sales Person'),
        ('Sales Manager', 'Sales Manager'),
        ('Accountant', 'Accountant'),
        ('Admin', 'Admin')
    ]
    email = models.EmailField(max_length=254, unique=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE, default='Sales Person')
    username = models.CharField(max_length=100)
    PhoneNo = models.CharField(max_length=20)
    Address = models.CharField(max_length=200)
    TCM_ID = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_type']
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True