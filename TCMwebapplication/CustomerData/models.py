from django.db import models
from datetime import datetime

# Create your models here.

class Customer_data(models.Model):

    type = [
        ('Mobile -> Brand', 'Mobile -> Brand'),
        ('Accessories', 'Accessories'),
        ('Home Applicances', 'Home Applicances'),
        ('AC', 'AC'),
        ('IT', 'IT'),
        ('Small Home Applicances', 'Small Home Applicances'),
        ('TV', 'TV'),
        ('Others', 'Others')
    ]

    options = [
        ('Out of stock', 'Out of stock'),
        ('Discontinued product', 'Discontinued product'),
        ('Pricing', 'Pricing'),
        ('EMI availability', 'EMI availability'),
        ('EMI Ineligibility', 'EMI Ineligibility'),
        ('Window Shopper', 'Window Shopper'),
        ('Upcoming Product Enquiry', 'Upcoming Product Enquiry'),
        ('Outdated offers','Oudated offers'),
        ('Unspecified', 'Unspecified'),
        ('Others', 'Others')
    ]

    Name = models.CharField(max_length = 25)
    PhoneNo = models.IntegerField()
    Email = models.EmailField(max_length = 40)
    Location = models.TextField(max_length = 100)
    Product = models.CharField(max_length = 30,choices = type)
    Model_Description = models.TextField(max_length = 100)
    Product_Value = models.IntegerField()
    Reason_of_leaving = models.CharField(max_length = 30, choices = options)
    Revisit_date = models.DateField(default = datetime.now())

    
