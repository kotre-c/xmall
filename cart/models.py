from django.db import models

# Create your models here.
from account.models import User
from goods.models import Good


class CartManager(models.Manager):
    def update_or_create(self, quantity=1, **kwargs):
        cart, created = self.get_or_create(**kwargs)
        if created:
            cart.good_num = quantity
        else:
            cart.good_num += quantity
        cart.save()
        return cart, created


class Cart(models.Model):
    checked = models.BooleanField(default=True)
    created = models.DateTimeField('创建时间', auto_now_add=True)
    updated = models.DateTimeField('更新时间', auto_now=True)
    good_num = models.PositiveIntegerField('商品数量', default=1)
    good = models.ForeignKey(Good, on_delete=models.CASCADE, null=True, blank=True, related_name='cart')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='cart')

    objects = CartManager()

    class Meta:
        unique_together = ['user', 'good']
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
