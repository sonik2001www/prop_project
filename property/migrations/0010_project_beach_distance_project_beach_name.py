# Generated by Django 4.2.1 on 2023-05-26 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_remove_developer_starting_price_project_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='beach_distance',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='beach_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]