# Generated by Django 3.2 on 2022-08-18 17:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='A required field. At least 32 characters long or fewer letter, Letters or digits .', max_length=32, unique=True, validators=[django.core.validators.RegexValidator(message='Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.', regex='^[\\w.@+-]+$')], verbose_name='username'),
        ),
    ]
