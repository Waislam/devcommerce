from django.contrib.auth.models import AbstractUser, Group
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    """
    Represents a custom user model extending Django's AbstractUser
    with additional metadata for creation and updates.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    updated_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
