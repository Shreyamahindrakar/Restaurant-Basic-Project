from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import get_object_or_404, render, redirect
from .forms import OrderForm
from .models import RestaurantOrder

def order_page(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            sr_no = form.cleaned_data['sr_no']
            user = form.cleaned_data['user']
            item_name = form.cleaned_data['item_name']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            instruction = form.cleaned_data['instruction']
            date = form.cleaned_data['date']
            
            # Check for duplicate order for the same user, item, and date
            if RestaurantOrder.objects.filter(user=user, item_name=item_name, date=date).exists():
                return render(request, 'order/order.html', {
                    'form': form,
                    'error': "Order already exists for this item, user, and date."
                })
            else:
                RestaurantOrder.objects.create(
                    sr_no=sr_no,
                    user=user,
                    item_name=item_name,
                    price=price,
                    quantity=quantity,
                    instruction=instruction,
                    date=date
                )
                return redirect('order_list')
    else:
        form = OrderForm()
    
    return render(request, 'order/order.html', {'form': form})

def order_list(request):
    restaurantorders = RestaurantOrder.objects.all()
    return render(request, 'order/order_list.html', {'restaurantorders': restaurantorders})

def edit_order(request, pk):
    order = get_object_or_404(RestaurantOrder, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'order/edit_order.html', {'form': form, 'order': order})

@csrf_exempt
def update_quantity(request, pk):
    if request.method == 'POST':
        try:
            order = get_object_or_404(RestaurantOrder, pk=pk)
            data = json.loads(request.body)
            action = data.get('action')

            if action == 'increase':
                order.quantity += 1
            elif action == 'decrease' and order.quantity > 1:
                order.quantity -= 1
            else:
                return JsonResponse({'success': False, 'message': 'Invalid operation or minimum quantity reached.'})

            order.save()
            return JsonResponse({'success': True})
        
        except RestaurantOrder.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Order not found.'})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})
