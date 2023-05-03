from django.db import models
from uuid import uuid4

# Create your models here.

class Users(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid4, editable = False)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    date_of_birth = models.DateField(default=None, null=True, blank=True)
    GENDER = (
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other'),
        )
    gender = models.CharField(max_length = 1, choices = GENDER)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    ROLES = (
        ('READONLY', 'READONLY'),
        ('SUPERUSER', 'SUPERUSER'),
        ('ADMIN', 'ADMIN'),
    )
    roles = models.CharField(max_length=255, choices = ROLES, default = 'READONLY')
    email = models.EmailField(max_length=70, blank=True, unique=True)


class Store (models.Model):
    owner = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='email')
    name = models.CharField(max_length = 255, unique=True)
    street = models.CharField(max_length=100)
    number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class Products (models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, to_field='name')
    drinks = models.JSONField(default=list, blank=True, null=True)
    foods = models.JSONField(default=list, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)