# Generated by Django 3.0 on 2019-12-09 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20191209_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='created',
            field=models.DateField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='good',
            name='detail',
            field=models.TextField(verbose_name='详情'),
        ),
        migrations.AlterField(
            model_name='good',
            name='productImageBig',
            field=models.ImageField(blank=True, null=True, upload_to='media/goods/', verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='good',
            name='subTitle',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='good',
            name='updated',
            field=models.DateField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.CreateModel(
            name='Goodimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/goods/wp/', verbose_name='图片')),
                ('created', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('good_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.Good')),
            ],
            options={
                'verbose_name': '商品轮播图',
                'verbose_name_plural': '商品轮播图',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='类别名称')),
                ('created', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('slug', models.CharField(max_length=120)),
                ('parent_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.Category')),
            ],
            options={
                'verbose_name': '商品分类',
                'verbose_name_plural': '商品分类',
            },
        ),
    ]