from rest_framework import serializers

from cart.models import Cart
from goods.models import Good
from goods.serializers import GoodDetailSerializer, GoodListSerializer


class CartSerizlizers(serializers.Serializer):
    # good = GoodListSerializer()
    id = serializers.IntegerField(read_only=True)
    good = serializers.PrimaryKeyRelatedField(required=True, queryset=Good.objects.all())
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    good_num = serializers.IntegerField(required=True, label='数量', min_value=1,
                                        error_messages={
                                            'min_value': '商品数量不能小于一',
                                            'required': '请选择商品数量'
                                        })
    checked = serializers.BooleanField(default=True)

    def create(self, validated_data):
        instance, created = Cart.objects.update_or_create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.good_num = validated_data['good_num']
        instance.checked = validated_data['checked']
        instance.save()
        return instance


class CartListSerizlizers(serializers.ModelSerializer):
    good = GoodListSerializer()

    class Meta:
        model = Cart
        fields = '__all__'


class CartEditSerializers(serializers.ModelSerializer):
    good = serializers.PrimaryKeyRelatedField(required=True, queryset=Good.objects.all())

    class Meta:
        model = Cart
        fields = '__all__'
