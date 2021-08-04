from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from .models import Employees
from django.urls import reverse
from datetime import date

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.
def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    Customer = apps.get_model('customers.Customer')
    all_customers = Customer.objects.all()
    user = request.user
    try:
        log_in_employee = Employees.obnjects.get(user=user)
        except:
            return HttpResponseRedirect(reverse('employee:create'))
        context = {
            'log_in_employee': lod_in_employee,
            'all_custmoers': all_customers,
            }
    return render(request, 'employees/index.html', context)

    #This is to register employee information
def create(request):
    if request.method == "POST":
        user = request.user
        name = request.POST.get('name')
        zip_code = request.POST.get('zip_code')
        new_employee = Employees(user=user, name=name, zip_code=zip_code)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create.html')

def view_daily(request):
    user = request.user
    log_in_employee = Employees.objects.get(user=user)
    Customers = apps.get_model('customers.Customer')
    all_customers = Customers.objects.all()
    current_date = date.today()
    weekday = current_date.strftime('%A')
    my_customers = []
    if request.method == "POST":
        for customer in all_customers:
            if customer.zip_code == logged_in_employee.zipcode and customer.pickup_day == weekday and customer.suspension_start == False or customer.onetime_pickup == weekday:
                my_customers.append(customer)
    return render(request, 'employees/filter.html')
