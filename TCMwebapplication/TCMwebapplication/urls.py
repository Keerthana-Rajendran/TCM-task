"""TCMwebapplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from UserManager import views as userView
from CustomerData import views as cusView

urlpatterns = [
    path('admin/', admin.site.urls),

  # Path for Usermanager module

    path('',userView.firstpage_view),
    path('signin/',userView.signin_view),
    path('login/',userView.login_view),
    path('home/',userView.home_view),

  # Path for Customer module

    path('addcus/',cusView.Create_CustomerData),
    path('customer/',cusView.Read_CustomerData),
    path('updatecus/<int:pk>',cusView.update_customer),
    path('delcus/<int:pk>',cusView.delete_customer),
    path('searchcus/',cusView.search_customer_view)
   
]


