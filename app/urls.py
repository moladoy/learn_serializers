
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import ProductView

router = DefaultRouter()
router.register('product', ProductView, 'product')

urlpatterns = [
    path('', include(router.urls))
]