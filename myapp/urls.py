from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    # ... existing URL patterns ...
    path('', include(router.urls)),
]