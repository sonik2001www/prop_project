# Generated by Django 4.2.1 on 2023-06-05 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0035_delete_answer_alter_reviewsoverview_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id_answer', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('answer', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Answer Overview',
                'verbose_name_plural': 'Answers Overview',
            },
        ),
    ]
