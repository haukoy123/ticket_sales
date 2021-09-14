# Generated by Django 3.1.7 on 2021-09-06 02:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0003_auto_20210905_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='company_route',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to=settings.AUTH_USER_MODEL),
        ),
    ]