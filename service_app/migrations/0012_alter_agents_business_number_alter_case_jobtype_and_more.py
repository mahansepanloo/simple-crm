# Generated by Django 5.1.3 on 2024-12-11 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0011_alter_device_brand_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agents',
            name='business_number',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Business Number'),
        ),
        migrations.AlterField(
            model_name='case',
            name='jobtype',
            field=models.IntegerField(choices=[(0, 'seven'), (1, 'gspn')], unique=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='imei',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='deviceprice',
            name='model_code',
            field=models.CharField(max_length=100, unique=True, verbose_name='Model Code'),
        ),
    ]
