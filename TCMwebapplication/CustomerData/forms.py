from django import forms
from CustomerData.models import Customer_data

class Customer_Form(forms.ModelForm):
    class Meta:
        model = Customer_data
        fields = ['Name','PhoneNo','Email','Location','Product','Model_Description','Product_Value','Reason_of_leaving','Revisit_date']



