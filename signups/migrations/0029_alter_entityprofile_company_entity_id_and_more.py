# Generated by Django 4.2.4 on 2023-08-24 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0028_crmserviceinfo_crm_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entityprofile',
            name='company_entity_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_id', to='signups.entity'),
        ),
        migrations.AlterField(
            model_name='entityprofile',
            name='owned_company_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_company_id', to=settings.AUTH_USER_MODEL),
        ),
    ]