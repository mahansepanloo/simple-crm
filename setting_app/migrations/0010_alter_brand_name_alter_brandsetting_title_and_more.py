# Generated by Django 5.1.3 on 2024-12-11 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting_app', '0009_sevenconfig'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='brandsetting',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='employer',
            name='imei',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='guarantee',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='swaptype',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
