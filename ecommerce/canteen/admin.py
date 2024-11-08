from django.contrib import admin
from .models import MenuItem, Order, OrderItem, StudentProfile

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'available')
    list_filter = ('category', 'available')
    search_fields = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'status', 'total_price', 'order_time')
    list_filter = ('status', 'order_time')
    search_fields = ('student__username',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'menu_item', 'quantity')
    search_fields = ('menu_item__name',)

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number')
    search_fields = ('user__username',)
