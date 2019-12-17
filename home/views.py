from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets

from home.models import NavList, Panel
from home.serializers import NavListSerializer, PanelSerializer


class NavListView(generics.ListAPIView):
    queryset = NavList.objects.all()
    serializer_class = NavListSerializer


class HomeListView(generics.ListAPIView):
    queryset = Panel.objects.all()
    serializer_class = PanelSerializer


