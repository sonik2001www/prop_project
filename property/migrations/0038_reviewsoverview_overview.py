# Generated by Django 4.2.1 on 2023-06-05 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0037_alter_reviewsoverview_facilities_on_site_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewsoverview',
            name='overview',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='property.overview'),
        ),
    ]
