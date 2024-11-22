from django.contrib import admin
from .models import Product


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'stock_status')
    search_fields = ('name',)
    list_filter = ('stock_status',)


admin.site.register(Product, ProductAdmin)
