from django.db import models
from datetime import datetime
from email.policy import default
from enum import auto 
from django.utils import timezone

# Create your models here.

class Customer_data(models.Model):

    
    type = [('Vivo Mobile','Vivo Mobile'),
    ('Redmi Mobile','Redmi Mobile'),('Home Applicances','Home Applicances')]

    type = [('Out of stock','Out of stock'),
    ('Pricing','Pricing'),('EMI availability','EMI availability'),('EMI Ineligibility','EMI Ineligibility')]

    Name = models.CharField(max_length = 25)
    Email = models.EmailField(max_length = 40)
    PhoneNo = models.IntegerField()
    Product = models.CharField(max_length = 20,choices = type)
    Model = models.TextField(max_length = 150)
    Product_Value = models.IntegerField()
    Reason_of_leaving = models.CharField(max_length = 20, choices = type)
    Revisit_date = models.DateField(default = datetime.now())

    
