from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics

from address.models import Address
from address.serializers import AddressSerializers


class AddressListView(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      generics.GenericAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        request.data["user_id"] = request.user.id
        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        request.data["user_id"] = request.user.id
        return super().partial_update(request, *args, **kwargs)


class AddressDetailView(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        request.data["user_id"] = request.user.id
        return super().partial_update(request, *args, **kwargs)

    def delete(self, request, pk):
        return self.destroy(request)
