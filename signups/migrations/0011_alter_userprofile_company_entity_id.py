# Generated by Django 4.2.4 on 2023-08-21 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0010_entity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='company_entity_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signups.entity'),
        ),
    ]
