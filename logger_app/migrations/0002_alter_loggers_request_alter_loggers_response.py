# Generated by Django 5.1.3 on 2024-12-23 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loggers',
            name='request',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loggers',
            name='response',
            field=models.TextField(blank=True, null=True),
        ),
    ]
