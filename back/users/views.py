from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from users import serializers, models
from back import pagination

class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UsersSerializer
    queryset = models.Users.objects.all()
    pagination_class = pagination.MyCustomPagination

class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StoreSerializer
    queryset = models.Store.objects.all()
    pagination_class = pagination.MyCustomPagination

class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductsSerializer
    queryset = models.Products.objects.all()
    pagination_class = pagination.MyCustomPagination

class RequestsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RequestsSerializer
    queryset = models.Requests.objects.all()
    pagination_class = pagination.MyCustomPagination
class ReportsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ReportsSerializer
    queryset = models.Reports.objects.all()
    pagination_class = pagination.MyCustomPagination