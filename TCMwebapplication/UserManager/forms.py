from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth import authenticate

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'user_type', 'username', 'PhoneNo', 'Address', 'TCM_ID', 'password1', 'password2']


    def clean_password2(self):
        # Check that the two password fields match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The two password fields didn’t match.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CustomUserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=(('sales_person', 'Sales Person'),
                                           ('sales_manager', 'Sales Manager'),
                                           ('accountant', 'Accountant'),
                                           ('admin', 'Admin')))
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        user_type = cleaned_data.get('user_type')
        if email and password and user_type:
            user = authenticate(email=email, password=password, user_type=user_type)
            if not user:
                raise forms.ValidationError('Invalid email or password')
        return cleaned_data