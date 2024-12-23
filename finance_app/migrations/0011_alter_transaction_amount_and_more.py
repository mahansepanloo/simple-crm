# Generated by Django 5.1.3 on 2024-12-17 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0010_alter_transaction_updated_status_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='updated_status_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
