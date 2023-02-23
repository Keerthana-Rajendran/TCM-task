from django import forms
from .models import Signin



#for admin signup
class Signin_Form(forms.ModelForm):
    class Meta:
        model = Signin
        fields = ['Name','Email', 'PhoneNo', 'Role','Address','TCM_ID','Set_Password']
        widgets = {
        'password': forms.PasswordInput()
        }
