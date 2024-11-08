from django.shortcuts import render

def home(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'home/index.html', {'menu_items': menu_items})