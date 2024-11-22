from django.contrib.auth import get_user_model
from django.db import models
from product.models import Product

User = get_user_model()


# Create your models here.

class Review(models.Model):
    """
    Represents a product review created by a user.
    Each review includes the user, the product reviewed, the review text,
    and a timestamp indicating when the review was created.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.product.name}"
