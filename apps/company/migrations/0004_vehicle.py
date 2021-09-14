# Generated by Django 3.1.7 on 2021-09-02 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20210901_0927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liceicnse_plates', models.CharField(blank=True, max_length=20, null=True)),
                ('color', models.TextField(blank=True, max_length=20, null=True)),
                ('vehicle_type', models.TextField(choices=[('Sleeping car', 'Sleeping car'), ('Normal car', 'Normal car')], default='Normal car', max_length=100)),
                ('number_seat', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('ACTIVATE', 'ACTIVATE'), ('INACTIVE', 'INACTIVE')], default='ACTIVATE', max_length=20)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
            options={
                'db_table': 'vehicle',
                'ordering': ['company'],
            },
        ),
    ]
