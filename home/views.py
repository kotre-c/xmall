from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from home.models import NavList
from home.serializers import NavListSerializer


class NavListView(generics.ListAPIView):
    queryset = NavList.objects.all()
    serializer_class = NavListSerializer
