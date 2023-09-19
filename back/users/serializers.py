from rest_framework import serializers
from . import models

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Users
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Store
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Products
        fields = '__all__'
        
class RequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Requests
        fields = '__all__'
class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reports
        fields = '__all__'
