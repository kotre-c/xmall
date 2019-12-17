from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.
class Good(models.Model):
    salePrice = models.DecimalField('价格', null=True, blank=True, decimal_places=2, max_digits=8)
    productName = models.CharField('商品名称', max_length=50)
    subTitle = models.CharField('标题', max_length=250, null=True, blank=True, )
    productImageBig = models.ImageField('图片', max_length=100, null=True, blank=True, upload_to='goods/')
    detail = RichTextUploadingField('详情')
    created = models.DateField('创建时间', auto_now_add=True)
    updated = models.DateField('更新时间', auto_now=True)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    stock = models.IntegerField('库存')

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.productName

    def to_json(self):
        return {"a": self.salePrice}


class GoodImage(models.Model):
    image = models.ImageField('图片', max_length=100, null=True, blank=True, upload_to='goods/wp/')
    created = models.DateField('创建时间', auto_now_add=True)
    updated = models.DateField('更新时间', auto_now=True)
    good_id = models.ForeignKey('Good', on_delete=models.CASCADE, null=True, blank=True, related_name='image')

    class Meta:
        verbose_name = '商品轮播图'
        verbose_name_plural = verbose_name


class Category(models.Model):
    name = models.CharField('类别名称', max_length=50)
    created = models.DateField('创建时间', auto_now_add=True)
    updated = models.DateField('更新时间', auto_now=True)
    slug = models.CharField(max_length=120)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name
