# Generated by Django 4.2.1 on 2023-06-09 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0055_alter_project_property_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='project_name',
            new_name='condo_name',
        ),
    ]
