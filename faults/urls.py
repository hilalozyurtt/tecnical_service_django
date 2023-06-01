from django.urls import path
from . import views

urlpatterns = [
    path("",  views.index, name="home_page"),
    path("products",  views.index, name="home_page"),
    path("customers", views.customers, name="customers_page"),
    path("customers/create_customers", views.create_customers, name="create_customers"),
    path("customers/<slug:slug>", views.customer_update, name="customers_update"),
    path("customers/<slug:slug>/detail", views.customer_details, name="customers_details"),
    path("products/create_products", views.create_products, name="create_products"),
    path("products/<slug:slug>", views.product_update, name="product_update"),
    path("customers/<slug:slug>/delete", views.delete_customer, name="delete_customer"),
    path("product/<slug:slug>/delete", views.delete_product, name="delete_product"),
]
