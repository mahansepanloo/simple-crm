# Generated by Django 5.1.3 on 2024-12-10 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0002_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='dep_number',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.CharField(max_length=100),
        ),
    ]
