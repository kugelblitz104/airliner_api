# Generated by Django 5.2 on 2025-04-08 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airliner', '0003_alter_planemodel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plane',
            name='manufacture_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
