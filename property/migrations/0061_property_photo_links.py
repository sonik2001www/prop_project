# Generated by Django 4.2.1 on 2023-06-09 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0060_remove_property_property_features_delete_features_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='photo_links',
            field=models.TextField(blank=True, null=True),
        ),
    ]