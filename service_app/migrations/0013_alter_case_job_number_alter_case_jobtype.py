# Generated by Django 5.1.3 on 2024-12-11 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0012_alter_agents_business_number_alter_case_jobtype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='job_number',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='jobtype',
            field=models.IntegerField(choices=[(0, 'seven'), (1, 'gspn')]),
        ),
    ]