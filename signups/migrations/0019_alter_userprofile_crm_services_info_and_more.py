# Generated by Django 4.2.4 on 2023-08-22 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0018_alter_entity_allow_status_notifications_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='crm_services_info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='signups.crmserviceinfo'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='samsara_integration_info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='signups.oldexternalintegration'),
        ),
    ]
