# Generated by Django 5.1.3 on 2024-12-16 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_app', '0005_alter_customer_accounting_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='accounting_code',
            field=models.CharField(max_length=100, unique=True, verbose_name='Accounting Code'),
        ),
    ]
