from celery import shared_task
from .models import Product
from django.conf import settings


@shared_task(name='check_product_stock')
def check_product_stock(product_id):
    product = Product.objects.filter(id=product_id).first()
    if product:
        if product.quantity == 0:
            product.stock_status = 'out_of_stock'
            product.save()
        elif 0 > product.quantity <= settings.THRESHOLD_QUANTITY:
            product.stock_status = 'low_stock'
            product.save()

