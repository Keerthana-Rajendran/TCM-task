from django.shortcuts import render,redirect
from .models import Signin
from django.contrib.auth.models import Group
from .forms import Signin_Form

# Create your views here.

def firstpage_view(request):
    return render(request,'UserManager/Firstpage.html')


def signin_view(request):
    form = Signin_Form()
    if request.method == 'POST':
        form = Signin_Form(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()

            """
            user.Set_password(user.Set_password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            return redirect("login")
            """

    return render(request,'UserManager/Signin.html', { 'form':form })


def login_view(request):
    form = Signin_Form()
    if request.method == 'POST':
        form = Signin_Form(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
    return render(request,'UserManager/login.html',{ 'form':form })

def home_view(request):
    return render(request,'UserManager/Homepage.html')





