from django.urls import path

from cart.views import CartViewSet, CartEditView

urlpatterns = [
    path('cartEdit/', CartEditView.as_view()),
    path('', CartViewSet.as_view())
]
