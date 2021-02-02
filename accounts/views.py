from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()


    total_customers = customers.count() #ordenes totales
    total_orders = orders.count() #ordenes totales

    delivered = orders.filter(status ='Delivered').count()
    pending = orders.filter(status ='Pending').count()

    context = {'orders': orders, 'customers': customers,
    'total_orders': total_orders, 'total_customers':total_customers,
    'delivered': delivered, 'pending':pending } 
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products':products})
    





def customer(request,pk):
    
    customer = Customer.objects.get(id = pk)
    orders = customer.order_set.all() #llama todas las ordenes
    total_orders = orders.count()
    context = {'customer': customer,
                'orders': orders,
                'total_orders': total_orders}
    
    return render(request,'accounts/customer.html', context)


def createOrder(request):
    context = {}
    return render(request,'accounts/order_form.html', context)

def test_view(request):
    return render(request,'accounts/test.html')