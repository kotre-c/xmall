# Generated by Django 3.0 on 2019-12-17 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_auto_20191217_1559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='userId',
            new_name='user',
        ),
    ]