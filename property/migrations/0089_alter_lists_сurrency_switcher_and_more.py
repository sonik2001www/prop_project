# Generated by Django 4.2.1 on 2023-07-14 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0088_lists_сurrency_switcher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lists',
            name='сurrency_switcher',
            field=models.CharField(blank=True, choices=[('US', 'US'), ('AED', 'AED')], default='AED', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='rent_price',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='sold_price',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
