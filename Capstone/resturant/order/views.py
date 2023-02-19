from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .order import Order
from meal.models import Meal

# Create your views here.

def add_to_order(request, meal_id):
    order = Order(request)
    order.add(meal_id)
    
    return render(request, 'order/menu_order.html')

def update_order(request, meal_id, action):
    order = Order(request)
    
    if action == 'increment':   
        order.add(meal_id, 1, True)
    else:
        order.add(meal_id, -1, True)
        
    meal = Meal.objects.get(pk=meal_id)
    
    item = {
        'meal': {
            'id': meal.id,
            'name': meal.name,
            'image': meal.image,
            'price': meal.price,
        },
        'total_price': meal.quantity * meal.price,
        'quantity': meal.quantity,
    }
    
    response = render(request, 'order/partials/meal_item.html', {'item': item})
    response['HX-Trigger'] = 'update-menu-order'
    return response

@login_required
def order(request):
    return render(request, 'order/order.html')

def hx_menu_order(request):
    return render(request, 'order/menu_order.html')