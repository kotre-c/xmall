from rest_framework import serializers

from home.models import NavList, Panel, Panelcontent


class NavListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavList
        fields = "__all__"


class PanelcontentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panelcontent
        fields = '__all__'


class PanelSerializer(serializers.ModelSerializer):
    panelContents = PanelcontentSerializer(many=True)

    class Meta:
        model = Panel
        fields = '__all__'
