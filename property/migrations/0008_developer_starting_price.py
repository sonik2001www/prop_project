# Generated by Django 4.2.1 on 2023-05-26 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_facilitiescategory_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='starting_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]
