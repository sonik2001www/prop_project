# Generated by Django 4.2.1 on 2023-06-14 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0070_property_agent_property_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='condo_name',
            new_name='property_name',
        ),
    ]
