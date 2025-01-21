from django.urls import path
from apps.main.views import products
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]