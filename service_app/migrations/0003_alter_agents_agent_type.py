# Generated by Django 5.1.3 on 2024-12-02 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0002_alter_agents_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agents',
            name='agent_type',
            field=models.CharField(choices=[('A', 'agent'), ('B', 'branch')], default='A'),
        ),
    ]
