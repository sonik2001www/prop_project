# Generated by Django 4.2.1 on 2023-05-26 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_project_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='off_plan',
            field=models.DateField(blank=True, null=True),
        ),
    ]
