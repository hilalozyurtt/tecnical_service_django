from django import forms
from .models import Customer, Product
from django.forms import widgets

class CustomerForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        
        self.fields['record_date'].widget.attrs['value'] = ''
     
    class Meta:
        model = Customer
        fields = ['name_surname', 'email', 'phone', 'address', 'record_date', 'status']
        labels = {
            "name_surname": "Ad Soyad",
            "email": "Email",
            "phone": "Telefon ",
            "address": "Adres",
            "record_date": "Kayıt Tarihi",
            "status": "Durum",
        }

class ProductForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        
        self.fields['record_date'].widget.attrs['value'] = ''
        self.fields['complated_date'].widget.attrs['value'] = ''

    class Meta:
        model = Product
        exclude = ['slug',]

