from rest_framework import serializers

from home.models import NavList, Panel


class NavListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavList
        fields = "__all__"


class PanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panel
        fields = '__all__'
