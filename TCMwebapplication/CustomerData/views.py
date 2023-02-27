from django.shortcuts import render,redirect
from CustomerData.models import Customer_data
from CustomerData.forms import CustomerForm
from django.contrib.auth.decorators import login_required
from UserManager.decorators import user_type_required

@login_required
@user_type_required(['Sales Manager', 'Admin'])
def create_customer_data(request):
    """for register customer data"""

    cusDict = {
        'cusForm': CustomerForm()
    }

    if request.method == 'POST':
        cusForm = CustomerForm(request.POST)
        if cusForm.is_valid():
            cusForm.save(commit = True)
        else:
             cusDict = {
                'cusForm': CustomerForm()
            }  
    return render(request, 'Customer/createcus.html', context = cusDict)


@login_required
@user_type_required(['Sales Manager', 'Admin'])
def read_customer_data(request):
    """for read customer data"""

    customer = Customer_data.objects.all().filter()
    print(len(customer))
    return render(request,'Customer/cusview.html', {'customer': customer})

@login_required
@user_type_required(['Sales Manager', 'Admin'])
def delete_customer(request, pk):
    """for delete customer data"""

    customer = Customer_data.objects.get(id = pk)
    customer.delete()
    return read_customer_data(request)

@login_required
@user_type_required(['Sales Manager', 'Admin'])
def update_customer(request, pk):
    """for update customer data"""

    customer = Customer_data.objects.get(id = pk)
    customerForm = CustomerForm(instance = customer)

    cusDict = {
        'cusForm': customerForm
    }

    if request.method == 'POST':
        customerForm = CustomerForm(request.POST, instance = customer)

        if customerForm.is_valid():
            customer = customerForm.save(commit = True)
            customer.save()
        else:
            cusDict = {
                       'cusForm': customerForm()
                    }
                   
            return render(request, 'Customer/updatecus.html', context = cusDict)     
    return render(request, 'Customer/updatecus.html', context = cusDict)
           
@login_required
@user_type_required(['Sales Manager', 'Admin'])
def search_customer_view(request):
    """for search customer data"""

    customer = ""
    if request.GET.get("query"):
        customer = Customer_data.objects.filter(Name = request.GET.get("query"))
    return render(request, 'Customer/cusview.html', {'customer': customer})