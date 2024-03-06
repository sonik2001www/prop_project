# Generated by Django 4.2.1 on 2023-05-25 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_facilitiescategory_project_facilities_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='direction',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='floors',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='off_plan',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='overview',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='tower',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='underprised',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='units_num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
