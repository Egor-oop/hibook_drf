from django.db import models

from apps.accountsapp.models import CustomUser


class Post(models.Model):
    """Post model"""
    
    text = models.TextField(max_length=512, blank=False, null=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
