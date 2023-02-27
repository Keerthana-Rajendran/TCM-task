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
from Dashboard import views as dashView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Path for Usermanager module
    path('login/', userView.login_view, name='login'),
    path('',userView.firstpage_view),
    path('signin/',userView.signin_view),
    # path('login/',userView.login_view),
    path('base/',userView.base_view),
    path('home/',userView.home_view, name='home'),
    path('logout/', userView.logout_view, name='logout'),

    # Path for Customer module

    path('addcus/',cusView.create_customer_data),
    path('customer/',cusView.read_customer_data),
    path('updatecus/<int:pk>',cusView.update_customer, name = 'updatecus'),
    path('delcus/<int:pk>',cusView.delete_customer, name = 'delcus'),
    path('searchcus/',cusView.search_customer_view),

    # Path for Customer module
    path('dashboard/', dashView.line_chart, name='line_chart'),

]


