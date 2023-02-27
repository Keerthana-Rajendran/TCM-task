from django import forms
from CustomerData.models import Customer_data

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer_data
        fields = ['Name', 'PhoneNo', 'Email', 'Location', 'Product', 'Model_Description', 'Product_Value', 'Reason_of_leaving', 'Revisit_date']
        widgets = {
          'Location': forms.Textarea(attrs={'rows':3, 'cols':15}),
          'Model_Description': forms.Textarea(attrs={'rows':3, 'cols':15}),
        }



