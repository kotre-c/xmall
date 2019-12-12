from django.db import models


# Create your models here.
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
