# Generated by Django 4.2.1 on 2023-05-29 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0018_property_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='photo_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
