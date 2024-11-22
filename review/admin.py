from django.contrib import admin
from .models import Review


# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at')
    search_fields = ('user__username', 'product__name')
    list_filter = ('product',)


admin.site.register(Review, ReviewAdmin)
