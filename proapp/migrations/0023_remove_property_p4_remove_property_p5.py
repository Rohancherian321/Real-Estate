# Generated by Django 4.1.3 on 2023-05-24 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proapp', '0022_remove_property_oid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='p4',
        ),
        migrations.RemoveField(
            model_name='property',
            name='p5',
        ),
    ]
