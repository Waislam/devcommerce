from itertools import product

from django.contrib.auth import get_user_model
from django.db import models

from product.models import Product

# Create your models here.

User = get_user_model()


class Cart(models.Model):
    """
    Represents a shopping cart belonging to a user, with status and total cost.
    """
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('ordered', 'Ordered')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, editable=False)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, editable=False)

    def __str__(self):
        return self.product.name

class Order(models.Model):
    """
    Represents an order placed by a user, with shipping details, payment status, and order status.
    """
    STATUS_CHOICES = [
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('shipped', 'Shipped'),
    ]
    PAYMENT_STATUS = [
        ('pending', 'Pending'),
        ('completed', 'Completed')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='processing')
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, editable=False)
    shipping_address = models.TextField(null=True, blank=True)
    payment_status = models.CharField(max_length=20, default='pending', choices=PAYMENT_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_send_email = models.BooleanField(default=False)


class OrderItem(models.Model):
    """
    Represents an item in an order, linking to a product and storing its quantity and price details.
    """
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, editable=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, editable=False)

    def __str__(self):
        return self.product.name
