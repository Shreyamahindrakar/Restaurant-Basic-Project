from django import forms
from .models import RestaurantOrder
from django.contrib.auth.models import User

class OrderForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=True, label="Select User")
    date = forms.DateField(widget=forms.SelectDateWidget, label="Order Date")

    class Meta:
        model = RestaurantOrder
        fields = ['sr_no', 'user', 'item_name', 'price', 'quantity', 'instruction', 'date']
