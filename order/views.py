from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from order.models import Order
from order.serializers import OrderSerizlizer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerizlizer
    # pagination_class = None

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return CartListSerizlizers
    #     else:
    #         return self.serializer_class
