# Generated by Django 4.2.1 on 2023-05-29 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_remove_property_photo_remove_property_photos'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='buildings',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]