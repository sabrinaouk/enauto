# Generated by Django 4.2.7 on 2023-11-21 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VMS', '0007_vmcreatespec_remove_vms_spec_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vmcreatespec',
            name='placement',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='VMS.vmplacementspec'),
        ),
    ]
