# Generated by Django 4.2.1 on 2023-06-05 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0039_remove_overview_buy_nums_properties_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]