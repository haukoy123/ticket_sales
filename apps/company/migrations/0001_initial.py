# Generated by Django 3.1.7 on 2021-08-23 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('UNLOCK', 'UNLOCK'), ('LOCK', 'LOCK')], default='UNLOCK', max_length=20)),
            ],
            options={
                'db_table': 'company',
            },
        ),
    ]