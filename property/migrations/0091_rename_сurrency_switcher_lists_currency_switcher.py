# Generated by Django 4.2.1 on 2023-07-18 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0090_alter_lists_сurrency_switcher_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lists',
            old_name='сurrency_switcher',
            new_name='currency_switcher',
        ),
    ]
