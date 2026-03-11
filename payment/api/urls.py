from django.urls import path
from .api_rezerpay import *

urlpatterns = [
    path('order/create/',CreateOrderAPIView.as_view(),name='create_order_api'),
    path('order/complete/',TranactionAPIView.as_view(),name='complete_order_api')
]
