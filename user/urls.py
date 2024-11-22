from django.urls import path
from devcommerce.urls import router
from .views import UserView

router.register('user', UserView)

urlpatterns = [
]