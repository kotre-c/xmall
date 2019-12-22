from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics, mixins
from rest_framework.response import Response

from cart.models import Cart
from cart.serializers import CartSerizlizers, CartListSerizlizers, CartEditSerializers


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


class CartEditView(mixins.UpdateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartEditSerializers
    pagination_class = None

    def get(self, request, *args, **kwargs):
        queryset = Cart.objects.all()
        checkedAll = False
        for i in queryset:
            if i.checked:
                var = checkedAll == True
        if checkedAll:
            Cart.objects.all().update(checked=False)
        else:
            Cart.objects.all().update(checked=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        queryset = Cart.objects.filter(checked=True, user=self.request.user).delete()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
