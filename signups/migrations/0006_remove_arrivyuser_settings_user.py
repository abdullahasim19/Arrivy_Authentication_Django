# Generated by Django 4.2.4 on 2023-08-21 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0005_rename_settings_arrivyuser_settings_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arrivyuser',
            name='settings_user',
        ),
    ]
