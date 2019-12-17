from django.urls import path

from cart.views import CartViewSet

urlpatterns = [
    path('', CartViewSet.as_view())
]
