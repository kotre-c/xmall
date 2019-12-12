from django.db import models

# Create your models here.
from account.models import User
from goods.models import Good


class Cart(models.Model):
    checked = models.BooleanField()
    created = models.DateField('创建时间', auto_now_add=True)
    updated = models.DateField('更新时间', auto_now=True)
    good_id = models.ForeignKey(Good, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
