# Generated by Django 4.2.4 on 2023-08-21 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0004_alter_arrivyuser_iscompany_alter_arrivyuser_sso_only'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arrivyuser',
            old_name='settings',
            new_name='settings_user',
        ),
    ]