from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register('products', views.ProductView,basename="product")
router.register('orders', views.OrderView,basename="order")
router.register('payments', views.PaymentView,basename="payment")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
