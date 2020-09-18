from django import forms
from main.models import Product,Category

class Productform(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class Categoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
