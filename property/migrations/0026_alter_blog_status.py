# Generated by Django 4.2.1 on 2023-06-01 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0025_category_tag_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(blank=True, choices=[('hot', 'Hot'), ('new', 'New')], max_length=25, null=True),
        ),
    ]