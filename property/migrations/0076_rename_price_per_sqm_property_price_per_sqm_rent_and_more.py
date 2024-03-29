# Generated by Django 4.2.1 on 2023-06-28 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0075_reviewsoverview_property'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='price_per_sqm',
            new_name='price_per_sqm_rent',
        ),
        migrations.AddField(
            model_name='property',
            name='price_per_sqm_sold',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
