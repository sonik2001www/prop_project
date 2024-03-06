# Generated by Django 4.2.1 on 2023-07-18 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0092_notuser_alter_lists_currency_switcher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notuser',
            old_name='search',
            new_name='csrf',
        ),
        migrations.AlterField(
            model_name='lists',
            name='currency_switcher',
            field=models.CharField(blank=True, choices=[('HKD', 'HKD'), ('HUF', 'HUF'), ('CZK', 'CZK'), ('NOK', 'NOK'), ('EUR', 'EUR'), ('MXN', 'MXN'), ('BRL', 'BRL'), ('AUD', 'AUD'), ('ZAR', 'ZAR'), ('NZD', 'NZD'), ('KRW', 'KRW'), ('MYR', 'MYR'), ('SEK', 'SEK'), ('CHF', 'CHF'), ('SGD', 'SGD'), ('GBP', 'GBP'), ('INR', 'INR'), ('AED', 'AED'), ('JPY', 'JPY'), ('CAD', 'CAD'), ('CNY', 'CNY'), ('PHP', 'PHP'), ('US', 'US'), ('THB', 'THB'), ('RUB', 'RUB'), ('IDR', 'IDR'), ('ILS', 'ILS'), ('DKK', 'DKK'), ('TRY', 'TRY'), ('PLN', 'PLN')], default='AED', max_length=10, null=True),
        ),
    ]
