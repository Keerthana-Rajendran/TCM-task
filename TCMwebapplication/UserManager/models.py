from django.db import models

# Create your models here.

class Signin(models.Model):
    
    type = [('SalesManager1','SalesManager1'),('SalesManager2','SalesManager2'),('SalesExecutive1','SalesExecutive1'),('SalesExecutive2','SalesExecutive2')]

    Name = models.CharField(max_length = 50)
    Email = models.EmailField(max_length = 50)
    PhoneNo = models.IntegerField()
    Role = models.CharField(max_length = 20, choices = type)
    Address = models.CharField(max_length = 100)
    TCM_ID = models.CharField(max_length = 20)
    Set_Password = models.CharField(max_length = 20)
