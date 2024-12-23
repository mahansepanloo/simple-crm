from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DevicePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_code', models.CharField(max_length=100)),
                ('factory_model', models.CharField(blank=True, max_length=100, null=True)),
                ('commercial_model', models.CharField(blank=True, max_length=100, null=True)),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
                ('memory', models.CharField(blank=True, max_length=100, null=True)),
                ('microtel_price', models.CharField(blank=True, max_length=100, null=True)),
                ('inter_price', models.CharField(blank=True, max_length=100, null=True)),
            ],),
        migrations.CreateModel(
            name='Agents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_type', models.CharField(choices=[('a', 'agent'), ('b', 'branch')], default='agent')),
                ('full_name', models.CharField(max_length=300, verbose_name='Full Name')),
                ('mobile_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Mobile Number')),
                ('business_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Business Number')),
                ('email', models.EmailField(blank=True, max_length=300, null=True, verbose_name='Email')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('seven_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='Seven Code')),
                ('asc_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='ASC Code')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='City')),
                ('manager_name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Manager Name')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('fax', models.CharField(blank=True, max_length=100, null=True, verbose_name='Fax')),
                ('status', models.CharField(choices=[(0, 'close'), (1, 'open'), (-1, 'pending')], default=0)),
            ],
        ),
    ]
            
