from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu_list, name='menu'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
]
    