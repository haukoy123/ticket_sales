# Generated by Django 3.1.7 on 2021-08-23 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='status',
            field=models.CharField(choices=[('ACTIVATE', 'ACTIVATE'), ('INACTIVE', 'INACTIVE')], default='ACTIVATE', max_length=20),
        ),
    ]
