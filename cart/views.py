from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics, mixins

from cart.models import Cart
from cart.serializers import CartSerizlizers, CartListSerizlizers


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerizlizers
    pagination_class = None

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return CartListSerizlizers
        else:
            return self.serializer_class
