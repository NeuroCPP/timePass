from django.shortcuts import render

def home(request):
    return render(request, 'canteen/templates/home/index.html')