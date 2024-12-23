# Generated by Django 5.1.3 on 2024-12-11 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0007_merge_20241210_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_code',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='card_number',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
