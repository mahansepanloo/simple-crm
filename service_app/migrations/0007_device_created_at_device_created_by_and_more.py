# Generated by Django 5.1.3 on 2024-12-08 13:28

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0006_alter_device_imei'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='device',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='device_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='device',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
