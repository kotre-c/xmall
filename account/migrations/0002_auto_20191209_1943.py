# Generated by Django 3.0 on 2019-12-09 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(null=True, upload_to='media/img/user/', verbose_name='图片'),
        ),
    ]