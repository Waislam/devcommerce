from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer
from django.core.cache import cache


# Create your views here.

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, ]
    search_fields = ['name', ]

    def get_permissions(self):
        permissions = super().get_permissions()
        if self.request.method.lower() == 'get':
            return []
        return permissions

    def get_authenticators(self):
        auth = super().get_authenticators()
        if self.request.method.lower() == 'get':
            return []
        return auth

    def list(self, request, *args, **kwargs):
        cache_key = 'product_list'
        cached_data = cache.get(cache_key)

        if cached_data is not None:
            return Response(cached_data)

        response = super().list(request, *args, **kwargs)
        cache.set(cache_key, response.data, timeout=60 * 20)

        return response
