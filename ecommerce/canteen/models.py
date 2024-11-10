from django.db import models
from django.db import models

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('veg', 'Vegetarian'),
        ('nonveg', 'Non-Vegetarian')
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=6, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)

    def __str__(self):
        return self.name
