from django.db import models

from apps.accountsapp.models import CustomUser


class Post(models.Model):
    """Post model"""
    text = models.TextField(max_length=512)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
