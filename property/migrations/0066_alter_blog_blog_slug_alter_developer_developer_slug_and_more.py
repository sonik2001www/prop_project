# Generated by Django 4.2.1 on 2023-06-13 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0065_blog_blog_slug_developer_developer_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_slug',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='developer',
            name='developer_slug',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='overview',
            name='overview_slug',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_slug',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_slug',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]
