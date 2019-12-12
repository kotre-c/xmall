from django.db import models

# Create your models here.
from account.models import User


class Address(models.Model):
    name = models.CharField('收货人', max_length=20)
    tel = models.CharField('电话号码', max_length=11)
    address = models.CharField('收获地址', max_length=150)
    created = models.DateField('创建时间', auto_now_add=True)
    updated = models.DateField('更新时间', auto_now=True)
    is_default = models.BooleanField(default=False)

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '收获地址'
        verbose_name_plural = verbose_name
