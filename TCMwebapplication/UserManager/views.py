from django.http import HttpResponse
from django.shortcuts import render ,redirect
from .models import CustomUser
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.templatetags.static import static
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

# Create your views here.

def firstpage_view(request):
    return render(request,'UserManager/Firstpage.html')

# asas46833
def signin_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user = form.save(commit=False)
            # Merge user_type if user already exists
            try:
                existing_user = CustomUser.objects.get(email=user.email)
                existing_user.user_type = user.user_type
                existing_user.save()
                return redirect('home')
            except CustomUser.DoesNotExist:
                pass
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request,'UserManager/Signin.html', { 'form': form })


# def login_view(request):
#     form = LoginForm()
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             name = form.data.get('Name')
#             password = form.data.get('Set_Password')
#             role = form.data.get('Role')
#             user = Signin.objects.all().filter(Name=name, Set_Password=password,Role=role)
#             user_dict = user.values()[0]
#             if user_dict.get('Name') == name and user_dict.get('Set_Password') and user_dict.get('Role') == role:
#                 return redirect('home')
#         else:
#             print(form.errors)
#     return render(request,'UserManager/login.html',{ 'form':form })

def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            # Authenticate user
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'], user_type=form.cleaned_data['user_type'])

            if user is not None:
                # Check if user has the correct user type
                if user.user_type.replace(' ', '_').lower() == form.cleaned_data['user_type']:
                    login(request, user)
                    return redirect('home')
                else:
                    form.add_error('user_type', 'Invalid user type')
    else:
        form = CustomUserLoginForm()
    return render(request,'UserManager/login.html',{ 'form':form })


# def login_view(request): T:TY638yJp7H7Jh
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request,'UserManager/login.html',{ 'form':form })

def logout_view(request):
    logout(request)
    # redirect to a success page
    return redirect('/')

def base_view(request):
    return render(request, 'UserManager/navbar.html')

def home_view(request):
    return render(request,'UserManager/Homepage.html')







