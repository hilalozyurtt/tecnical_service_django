from datetime import date
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render
from faults.forms import CustomerForm, ProductForm
from faults.models import Customer, Product
from django.http.response import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {
        "products": products
    })

def customers(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {
        "customers": customers
    })

def customer_update(request, slug):
    customer = get_object_or_404(Customer, slug=slug)
    customer_form = CustomerForm(instance=customer)

    if request.method == "POST":
        customer_form = CustomerForm(request.POST, instance=customer)
        if customer_form.is_valid():
            customer = customer_form.save(commit=False)
            customer.save()
            return HttpResponseRedirect(reverse("customers_page"))

    return render(request, 'customer_update.html', {
    "customer": customer,
    "customer_form": customer_form,
})

def create_customers(request):
    customer_form = CustomerForm()

    if request.method == "POST":
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer = customer_form.save(commit=False)
            customer.save()
            return HttpResponseRedirect(reverse("customers_page"))

    return render(request, 'create_customers.html', {
        "customer_form": customer_form
    })

def customer_details(request, slug):
    customer = get_object_or_404(Customer, slug=slug)
    #product = Product.objects.filter(customer = customer.id)
    return render(request, 'customer_details.html', {
        "customer": customer,
        "products": customer.product_set.all(),
    })

def create_products(request):
    product_form = ProductForm()

    if request.method == "POST":
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.save()
            return HttpResponseRedirect(reverse("home_page"))

    return render(request, 'create_products.html',{
        "product_form": product_form
    } )

def product_update(request, slug):
    product = get_object_or_404(Product, slug=slug)
    product_form = ProductForm(instance=product)

    if request.method == "POST":
        product_form = ProductForm(request.POST, instance=product)
        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.save()
            return HttpResponseRedirect(reverse("home_page"))

    return render(request, 'product_update.html', {
        "product": product,
        "product_form":product_form
    })

def delete_customer(request, slug):
    customer = get_object_or_404(Customer, slug=slug)

    if request.method == "POST":
        customer.delete()
        return HttpResponseRedirect(reverse("customers_page"))

    return render(request, 'delete_customer.html', {
        "customer": customer
    })

def delete_product(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.method == "POST":
        product.delete()
        return HttpResponseRedirect(reverse("home_page"))

    return render(request, 'delete_product.html', {
        "product": product
    })
