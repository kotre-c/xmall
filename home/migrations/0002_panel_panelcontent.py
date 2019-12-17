# Generated by Django 3.0 on 2019-12-17 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0013_good_productimagebig'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('type', models.IntegerField()),
                ('sort_order', models.IntegerField()),
                ('position', models.IntegerField()),
                ('limit_num', models.IntegerField()),
                ('status', models.IntegerField()),
                ('created', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '首页面板',
                'verbose_name_plural': '首页面板',
            },
        ),
        migrations.CreateModel(
            name='Panelcontent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('sort_order', models.IntegerField()),
                ('full_url', models.ImageField(blank=True, max_length=120, null=True, upload_to='home/')),
                ('pic_url', models.ImageField(blank=True, null=True, upload_to='home/')),
                ('pic_url2', models.ImageField(blank=True, null=True, upload_to='home/')),
                ('pic_url3', models.ImageField(blank=True, null=True, upload_to='home/')),
                ('good_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='goods.Good')),
                ('panel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='panels', to='home.Panel')),
            ],
            options={
                'verbose_name': '面板内容',
                'verbose_name_plural': '面板内容',
            },
        ),
    ]