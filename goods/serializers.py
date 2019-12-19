import decimal
import json

from rest_framework import serializers

from goods.models import Good, GoodImage


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        super(DateEncoder, self).default(obj)


class GoodListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    salePrice = serializers.DecimalField(decimal_places=2, max_digits=8)
    productName = serializers.CharField()
    subTitle = serializers.CharField()
    productImageBig = serializers.ImageField()
    created = serializers.DateField()
    stock =serializers.IntegerField()


class GoodImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodImage
        fields = "__all__"


class GoodDetailSerializer(serializers.ModelSerializer):
    image = GoodImageListSerializer(many=True)

    class Meta:
        model = Good
        fields = "__all__"
