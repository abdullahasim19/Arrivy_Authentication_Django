# Generated by Django 4.2.4 on 2023-08-24 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0020_delete_group_alter_companyprofile_default_entity_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='image_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
