# Generated by Django 3.0 on 2019-12-17 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_panel_panelcontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panelcontent',
            name='panel_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='panelContents', to='home.Panel'),
        ),
    ]