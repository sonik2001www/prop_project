# Generated by Django 4.2.1 on 2023-06-05 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0043_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='for_table',
            field=models.CharField(blank=True, choices=[('Overview', 'Overview')], max_length=100, null=True),
        ),
    ]
