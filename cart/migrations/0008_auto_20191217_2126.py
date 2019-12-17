# Generated by Django 3.0 on 2019-12-17 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0013_good_productimagebig'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0007_auto_20191217_1618'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='cart',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='cart',
            name='checked',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='good',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='goods.Good'),
        ),
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together={('user', 'good')},
        ),
    ]
