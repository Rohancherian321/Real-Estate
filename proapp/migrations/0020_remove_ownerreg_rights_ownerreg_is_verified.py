# Generated by Django 4.1.3 on 2023-05-24 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proapp', '0019_property_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ownerreg',
            name='rights',
        ),
        migrations.AddField(
            model_name='ownerreg',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
