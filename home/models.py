from django.db import models

# Create your models here.
from goods.models import Good


class NavList(models.Model):
    name = models.CharField('名称', max_length=120, null=True, blank=True)
    panelId = models.PositiveIntegerField(default=0)
    type = models.PositiveIntegerField(default=0)
    sortOrder = models.PositiveIntegerField(default=0)
    fullUrl = models.CharField(max_length=120)
    picUrl = models.CharField(max_length=120)
    created = models.DateField('创建时间', auto_now_add=True)
    updated = models.DateField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '导航栏'
        verbose_name_plural = verbose_name


class Panel(models.Model):
    name = models.CharField(max_length=120)
    type = models.IntegerField()
    sort_order = models.IntegerField()
    position = models.IntegerField()
    limit_num = models.IntegerField()
    status = models.IntegerField()
    created = models.DateField('创建时间', auto_now_add=True)
    updated = models.DateField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '首页面板'
        verbose_name_plural = verbose_name


class Panelcontent(models.Model):
    name = models.CharField(max_length=120),
    type = models.IntegerField()
    sort_order = models.IntegerField()
    full_url = models.ImageField(upload_to='home/', max_length=120, null=True, blank=True)
    pic_url = models.ImageField(upload_to='home/', max_length=100, null=True, blank=True)
    pic_url2 = models.ImageField(upload_to='home/', max_length=100, null=True, blank=True)
    pic_url3 = models.ImageField(upload_to='home/', max_length=100, null=True, blank=True)
    good_id = models.ForeignKey(Good, models.CASCADE, null=True, blank=True, related_name='goods')
    panel_id = models.ForeignKey(Panel, models.CASCADE, related_name='panels')

    class Meta:
        verbose_name = '面板内容'
        verbose_name_plural = verbose_name
