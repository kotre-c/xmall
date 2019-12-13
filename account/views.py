from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
import json
# Create your views here.
from django.views.generic.base import View
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

from account.models import User
from account.serializers import DateEncoder, UserSerializer


# class UserListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class UserListView(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_url_kwarg = 'username'
    lookup_field = 'username'

    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
