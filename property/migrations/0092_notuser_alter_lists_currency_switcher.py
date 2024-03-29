# Generated by Django 4.2.1 on 2023-07-18 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0091_rename_сurrency_switcher_lists_currency_switcher'),
    ]

    operations = [
        migrations.CreateModel(
            name='notUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.CharField(blank=True, max_length=200, null=True)),
                ('currency_switcher', models.CharField(blank=True, default='AED', max_length=10, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='lists',
            name='currency_switcher',
            field=models.CharField(blank=True, choices=[('BRL', 'BRL'), ('MYR', 'MYR'), ('SGD', 'SGD'), ('DKK', 'DKK'), ('AUD', 'AUD'), ('CNY', 'CNY'), ('IDR', 'IDR'), ('TRY', 'TRY'), ('CHF', 'CHF'), ('CAD', 'CAD'), ('HUF', 'HUF'), ('SEK', 'SEK'), ('NOK', 'NOK'), ('JPY', 'JPY'), ('CZK', 'CZK'), ('US', 'US'), ('AED', 'AED'), ('PHP', 'PHP'), ('INR', 'INR'), ('EUR', 'EUR'), ('HKD', 'HKD'), ('RUB', 'RUB'), ('ZAR', 'ZAR'), ('NZD', 'NZD'), ('MXN', 'MXN'), ('THB', 'THB'), ('GBP', 'GBP'), ('KRW', 'KRW'), ('PLN', 'PLN'), ('ILS', 'ILS')], default='AED', max_length=10, null=True),
        ),
    ]
