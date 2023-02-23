from django import forms
from CustomerData.models import Customer_data

class Customer_Form(forms.ModelForm):
    class Meta:
        model = Customer_data
        fields = ['Name','Email','PhoneNo','Product','Model','Product_Value','Reason_of_leaving','Revisit_date']



