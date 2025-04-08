# Generated by Django 5.2 on 2025-04-08 02:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airliner', '0004_alter_plane_manufacture_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
