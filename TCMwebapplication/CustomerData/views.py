from django.shortcuts import render,redirect
from CustomerData.models import Customer_data
from CustomerData.forms import Customer_Form
from django.http import HttpResponse

# Create your views here.

# <-------for register customer data------>

def Create_CustomerData(request):

    cusDict = {
        'cusForm': Customer_Form()
    }
    if request.method == 'POST':
        cusForm = Customer_Form(request.POST)
        if cusForm.is_valid():
            cusForm.save(commit = True)
        else:
             cusDict = {
                'cusForm': Customer_Form()
            }  
    return render(request, 'Customer/createcus.html', context = cusDict)

# <------- for read customer data------->

def Read_CustomerData(request):

    customer = Customer_data.objects.all().filter()
    print(len(customer))
    return render(request,'Customer/cusview.html', {'customer': customer})

#<--------for delete customer data------->

def delete_customer(request, pk):

    customer = Customer_data.objects.get(id = pk)
    customer.delete()
    return Read_CustomerData(request)

#<------- for update customer data-------->

def update_customer(request, pk):

    customer = Customer_data.objects.get(id = pk)
    customerForm = Customer_Form(instance = customer)

    cusDict = {
        'cusForm': customerForm
    }

    if request.method == 'POST':
        customerForm = Customer_Form(request.POST, instance = customer)

        if customerForm.is_valid():
            customer = customerForm.save(commit = True)
            customer.save()
        else:
            cusDict = {
                       'cusForm': customerForm()
                    }
                   
            return render(request, 'Customer/updatecus.html', context = cusDict)     
    return render(request, 'Customer/updatecus.html', context = cusDict)
           

#<------- for search customer data------>

def search_customer_view(request):
    customer = ""
    if request.GET.get("query"):
        customer = Customer_data.objects.filter(Name = request.GET.get("query"))
    return render(request, 'Customer/cusview.html', {'customer': customer})