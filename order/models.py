from datetime import datetime

from django.db import models

# Create your models here.
from account.models import User
from address.models import Address
from goods.models import Good


class Order(models.Model):
    pay_status = models.CharField('支付状态',max_length=30)
    order_sn = models.CharField('订单号', max_length=30, unique=True, null=True, blank=True)
    trade_no = models.CharField('贸易号', max_length=30, unique=True, null=True, blank=True)
    pay_time = models.DateTimeField('支付时间', auto_now=True, null=True, blank=True)
    finishDate = models.DateTimeField('订单完成时间', auto_now=True)
    post_script = models.CharField(max_length=200, null=True, blank=True)
    order_total = models.IntegerField('订单总计')
    close_time = models.DateTimeField('订单关闭时间', default=datetime.now())
    address = models.CharField('收件地址', max_length=100)
    singer_name = models.CharField('收件人', max_length=30)
    singer_mobile = models.CharField('收件人电话', max_length=100)
    created = models.DateTimeField('创建时间', auto_now_add=True)
    updated = models.DateTimeField('更新时间', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='Order')

    class Meta:
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name
        ordering = ['-created']


class OrderGoods(models.Model):
    price = models.IntegerField('销售价格')
    goods_num = models.IntegerField('商品数量')
    created = models.DateField('创建时间', auto_now_add=True)
    updated = models.DateField('更新时间', auto_now=True)
    good = models.ForeignKey(Good, on_delete=models.CASCADE, related_name='good')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='goods')

    class Meta:
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name
