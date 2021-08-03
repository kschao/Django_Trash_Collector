from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Customer
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user

    try:
        # This line inside the 'try' will return the customer record of the logged-in user if one exists
        logged_in_customer = Customer.objects.get(user=user)
        context = {
            'logged_in_customer': logged_in_customer
        }
    except:
        # TODO: Redirect the user to a 'create' function to finish the registration process if no customer record found
       return HttpResponseRedirect(reverse('customers:register'))

    # It will be necessary while creating a Customer/Employee to assign request.user as the user foreign key

    print(user)
    return render(request, 'customers/index.html', context)

# User info registration
def create(request):
    if request.method == "POST":
        user = request.user
        name = request.POST.get('name')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        weekly_pickup_day = request.POST.get('weekly_pickup_day')
        new_customer = Customer(user=user, name=name, address=address, zip_code=zip_code, weekly_pickup_day=weekly_pickup_day)
        new_customer.save()
        return HttpResponseRedirect (reverse('customer:details'))
    else:
        return render(request, 'customer/create.html')
    
def detail(request, customer_id):
    customer_from_db = Customer.objects.get(pk=customer_id)
    return render(request, 'customer/detail.html', {'customer': customer_from_db})

def edit(request, customer_id):
    customer_from_db = Customer.objects.get(pk=customer_id)
    if request.method == 'POST':
        customer_from_db.name = request.POST.get('name')
        customer_from_db.address = request.POST.get('address')
        customer_from_db.zip_code = request.POST.get('zip_code')
        customer_from_db.weekly_pickup_day = request.POST.get('weekly_pickup_day')
        customer_from_db.one_time_pickup = request.POST.get('one_time_pickup')
        return HttpResponseRedirect(reverse('customer:index'))
    else:
        return render(request, 'customer/edit.html')


