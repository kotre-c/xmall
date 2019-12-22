# Generated by Django 3.0 on 2019-12-19 07:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '0001_initial'),
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderId', models.CharField(max_length=30, unique=True, verbose_name='订单号')),
                ('orderStatus', models.IntegerField(verbose_name='支付状态')),
                ('orderTotal', models.IntegerField(verbose_name='订单总计')),
                ('post_script', models.CharField(blank=True, max_length=200, null=True)),
                ('createDate', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('closeDate', models.DateTimeField(auto_now=True, verbose_name='订单关闭时间')),
                ('finishDate', models.DateTimeField(auto_now=True, verbose_name='订单完成时间')),
                ('payDate', models.DateTimeField(auto_now=True, verbose_name='支付时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Order', to='address.Address')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Order', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '订单详情',
                'verbose_name_plural': '订单详情',
            },
        ),
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salePrice', models.IntegerField(verbose_name='销售价格')),
                ('productNum', models.IntegerField(verbose_name='商品数量')),
                ('created', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('good_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Good')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order')),
            ],
            options={
                'verbose_name': '订单商品',
                'verbose_name_plural': '订单商品',
            },
        ),
    ]
