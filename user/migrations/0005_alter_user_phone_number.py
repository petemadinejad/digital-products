# Generated by Django 3.2 on 2022-08-18 15:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.BigIntegerField(blank=True, error_messages={'invalid': 'Enter a valid phone number. This value may contain only digits.'}, unique=True, validators=[django.core.validators.RegexValidator(message='Enter a valid phone number. This value may contain only digits.', regex='^989[0-3,9]\\d{8}$')], verbose_name='phone number'),
        ),
    ]
