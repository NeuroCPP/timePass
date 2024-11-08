from django.db import models
from django.contrib.auth.models import User

# Model for individual food items on the menu
class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('Snacks', 'Snacks'),
        ('Drinks', 'Drinks'),
        ('Meals', 'Meals'),
        ('Desserts', 'Desserts'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Maximum price: 9999.99
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# Model to represent each student's order
class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming user is a student
    order_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Order {self.id} by {self.student.username}"

    # Calculate total price based on OrderItems related to this order
    def calculate_total(self):
        total = sum(item.menu_item.price * item.quantity for item in self.order_items.all())
        self.total_price = total
        self.save()


# Model for individual items within an order
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.menu_item.name}"


# Optional model to represent additional student details if needed
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
