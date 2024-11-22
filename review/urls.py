from django.urls import path
from devcommerce.urls import router
from .views import ReviewView

router.register('review', ReviewView)

urlpatterns = [
]