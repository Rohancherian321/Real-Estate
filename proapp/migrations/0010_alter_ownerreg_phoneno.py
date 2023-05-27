# Generated by Django 3.2 on 2022-03-08 15:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proapp', '0009_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownerreg',
            name='phoneno',
            field=models.IntegerField(validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Phone No'),
        ),
    ]
