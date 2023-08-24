# Generated by Django 4.2.4 on 2023-08-24 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0027_alter_companyprofile_custom_integrations'),
    ]

    operations = [
        migrations.AddField(
            model_name='crmserviceinfo',
            name='crm_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='samsara_integration_info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='signups.oldexternalintegration'),
        ),
        migrations.AlterField(
            model_name='crmserviceinfo',
            name='crm_type',
            field=models.IntegerField(blank=True, choices=[(4005, 'Pipedrive')], null=True),
        ),
        migrations.AlterField(
            model_name='oldexternalintegration',
            name='samsara_access_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='oldexternalintegration',
            name='samsara_group_ids',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]