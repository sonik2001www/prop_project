# Generated by Django 4.2.1 on 2023-06-05 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0044_alter_question_for_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewsoverview',
            name='average',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]