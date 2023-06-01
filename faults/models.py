from django.conf import settings
from django.db import models
from django.utils import timezone 
from django.core.validators import MinLengthValidator
from django.utils.text import slugify

class Customer(models.Model):
    name_surname = models.CharField(max_length=200)
    email = models.EmailField(default="", blank=True)
    phone = models.CharField(max_length=11, blank=True)
    address = models.CharField(max_length=200, blank=True)
    record_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(unique=True, db_index=True, blank=True)

    def __str__(self):
        return self.name_surname

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name_surname)
        super().save(*args, **kwargs)
    

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    # Sahipsiz bir ürün eklemek için null=true, blank=true eklenmeli.
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    customer_complaint = models.CharField(max_length=400, blank=True)
    transantions_made = models.TextField(validators= [MinLengthValidator(10)], blank=True)
    record_date = models.DateTimeField(default=timezone.now, blank=True)
    complated_date = models.DateField()
    price = models.DecimalField(max_digits=19, decimal_places=2, blank=True)
    status = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(unique=True, db_index=True, blank=True)

    def __str__(self):
        return f"{self.product_name} {self.customer}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super().save(*args, **kwargs)
    



    