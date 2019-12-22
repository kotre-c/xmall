from rest_framework import serializers

from goods.models import Good
from goods.serializers import GoodSerializer
from order.models import Order, OrderGoods


class OrderGoodsListSerializer(serializers.ModelSerializer):
    good = GoodSerializer(read_only=True)

    class Meta:
        model = OrderGoods
        fields = "__all__"


class OrderSerizlizer(serializers.ModelSerializer):
    goods = OrderGoodsListSerializer(many=True)
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Order
        fields = "__all__"
