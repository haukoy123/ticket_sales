# Generated by Django 3.1.7 on 2021-09-01 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20210823_2241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]