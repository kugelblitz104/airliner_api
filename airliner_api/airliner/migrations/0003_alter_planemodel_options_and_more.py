# Generated by Django 5.2 on 2025-04-08 02:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airliner', '0002_planemodel_seattype_alter_country_options_address_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='planemodel',
            options={'ordering': ['manufacturer', 'name'], 'verbose_name_plural': 'Models'},
        ),
        migrations.RemoveField(
            model_name='plane',
            name='manufacturing_year',
        ),
        migrations.AddField(
            model_name='plane',
            name='manufacture_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='plane',
            name='airport',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='airliner.airport'),
        ),
    ]
