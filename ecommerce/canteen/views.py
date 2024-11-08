from django.shortcuts import render, get_object_or_404
from .models import MenuItem, Order, OrderItem


def home(request):
    # Retrieve available menu items
    menu_items = MenuItem.objects.filter(available=True)
    
    # Retrieve recent orders if user is authenticated, else set to empty list
    recent_orders = Order.objects.filter(student=request.user).order_by('-order_time')[:5] if request.user.is_authenticated else []
    
    return render(request, 'home/index.html', {
        'menu_items': menu_items,
        'recent_orders': recent_orders,
    })

def menu_list(request):
    menu_items = MenuItem.objects.filter(available=True)
    return render(request, 'menu/index.html', {'menu_items': menu_items})

def orders(request):
    """View to list all orders for the logged-in user."""
    user_orders = Order.objects.filter(student=request.user).order_by('-order_time')
    return render(request, 'orders/index.html', {'user_orders': user_orders})

def order_detail(request, order_id):
    """View to display details of a specific order."""
    order = get_object_or_404(Order, id=order_id, student=request.user)
    return render(request, 'orders/detail.html', {'order': order})