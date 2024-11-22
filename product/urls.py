from django.urls import path
from devcommerce.urls import router
from .views import ProductView

router.register('product', ProductView)

urlpatterns = [
]