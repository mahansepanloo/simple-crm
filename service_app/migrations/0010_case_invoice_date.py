# Generated by Django 5.1.3 on 2024-12-10 06:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0009_alter_case_jobtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='invoice_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
