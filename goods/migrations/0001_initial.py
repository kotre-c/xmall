# Generated by Django 3.0 on 2019-12-09 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salePrice', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('productName', models.CharField(max_length=50, verbose_name='商品名称')),
                ('subTitle', models.CharField(max_length=250)),
                ('productImageBig', models.ImageField(blank=True, null=True, upload_to='media/goods/')),
                ('detail', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
            },
        ),
    ]