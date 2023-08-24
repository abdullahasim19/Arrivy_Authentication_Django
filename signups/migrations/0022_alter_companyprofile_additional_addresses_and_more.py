# Generated by Django 4.2.4 on 2023-08-24 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0021_alter_companyprofile_image_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='additional_addresses',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='additional_charges',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='auto_logout_after',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='contact_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='custom_webhook_authentication_keys',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='depot_departure_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='filters',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='mileage_unit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='onboarding_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='premium_charges_details',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='qr_settings',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='signups.qrsettingsinfo'),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='ratings_fetch_URL_authentication_keys',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='ratings_fetch_URL_v2_authentication_keys',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='social_links',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='status_priority',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='subscribe_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='task_notifications_settings',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='time_line_filters',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='time_reporting_permissions',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='tombstone_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='ui_filters_settings',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='white_labeling_public_settings',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='white_labeling_settings',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
