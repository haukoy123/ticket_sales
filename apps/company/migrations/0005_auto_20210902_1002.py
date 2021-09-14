# Generated by Django 3.1.7 on 2021-09-02 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_vehicle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=100, null=True)),
                ('province_begins', models.TextField(blank=True, max_length=50, null=True)),
                ('province_ends', models.TextField(blank=True, max_length=50, null=True)),
                ('departure_time', models.TimeField(blank=True, null=True)),
                ('time_ends', models.TimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'route',
            },
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='color',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_type',
            field=models.CharField(choices=[('Sleeping car', 'Sleeping car'), ('Normal car', 'Normal car')], default='Normal car', max_length=100),
        ),
    ]