from django.shortcuts import render
from .models import MenuItem

def home(request):
    veg_items = MenuItem.objects.filter(category='veg')
    non_veg_items = MenuItem.objects.filter(category='nonveg')
    return render(request, 'home/index.html', {"veg_items": veg_items, "non_veg_items": non_veg_items})