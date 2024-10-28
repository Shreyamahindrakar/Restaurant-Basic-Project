from django.urls import path
from .views import order_page,order_list,edit_order,update_quantity

urlpatterns = [
    path('',order_page,name='order'),
    path('order/list/', order_list, name='order_list'),
    path('order/edit/<int:pk>/', edit_order, name='edit_order'),
    
    path('order/update_quantity/<int:pk>/', update_quantity, name='update_quantity')
]
