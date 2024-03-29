# Generated by Django 3.0 on 2019-12-18 03:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='收货人')),
                ('tel', models.CharField(max_length=11, verbose_name='电话号码')),
                ('address', models.CharField(max_length=150, verbose_name='收货地址')),
                ('created', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('is_default', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '收货地址',
                'verbose_name_plural': '收货地址',
            },
        ),
    ]
