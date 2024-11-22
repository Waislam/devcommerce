from django.db import models


# Create your models here.
class Product(models.Model):
    """
    Represents a product with details such as name, description, price, image,
    stock quantity, and stock status.
    """
    STOCK_STATUS_CHOICES = [
        ('low_stock', 'Low Stock'),
        ('in_stock', 'In Stock'),
        ('out_of_stock', 'Out of Stock'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    quantity = models.IntegerField(default=0)
    stock_status = models.CharField(max_length=20, choices=STOCK_STATUS_CHOICES, default='in_stock')

    def __str__(self):
        return self.name
