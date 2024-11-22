from django.contrib import admin
from .models import Order, OrderItem


# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'status', 'grand_total', 'payment_status', 'is_send_email')
    search_fields = ('user__username',)
    list_filter = ('status', 'payment_status')
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
