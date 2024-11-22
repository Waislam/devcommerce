from django.urls import path
from devcommerce.urls import router
from .views import OrderView, CartView



# router = routers.DefaultRouter()

router.register('cart', CartView)
router.register('order', OrderView)

urlpatterns = []