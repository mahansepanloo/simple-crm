# Generated by Django 5.1.3 on 2024-12-23 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loggers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('user_ip', models.GenericIPAddressField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('view', models.CharField(max_length=200)),
                ('view_method', models.CharField(max_length=100)),
                ('request', models.TextField()),
                ('response', models.TextField()),
                ('status_code', models.PositiveIntegerField()),
                ('query_params', models.TextField(blank=True, null=True)),
            ],
        ),
    ]