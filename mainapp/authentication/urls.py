from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls


router = DefaultRouter()
router.register('products', views.ProductView,basename="product")
router.register('orders', views.OrderView,basename="order")
router.register('payments', views.PaymentView,basename="payment")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('docs/',include_docs_urls(title = "drf crud")),
    path('schema',get_schema_view(title="django crud" ,description="this is django drf for crud", version='1.0.0'),name='openapi-schema'),
]
