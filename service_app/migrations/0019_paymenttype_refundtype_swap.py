# Generated by Django 5.1.3 on 2024-12-18 08:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0018_alter_note_attachment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paymenttype_created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RefundType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='refundtype_created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Swap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('swap_or_refund', models.IntegerField(blank=True, choices=[(0, 'swap'), (1, 'refund')], null=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('required_amount', models.IntegerField(blank=True, null=True)),
                ('amount_of_additions', models.IntegerField(blank=True, null=True)),
                ('Amountـofـdeduction', models.IntegerField(blank=True, null=True)),
                ('final_amount', models.IntegerField(blank=True, null=True)),
                ('sawapprove', models.BooleanField(default=False)),
                ('sawapprove_date', models.DateTimeField(blank=True, null=True)),
                ('send_to_financial', models.BooleanField(default=False)),
                ('send_date', models.DateTimeField(blank=True, null=True)),
                ('financial_approved_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('case', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='swap_case', to='service_app.case')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='swap_created_by', to=settings.AUTH_USER_MODEL)),
                ('financial_approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='swap_financial_approved_by', to=settings.AUTH_USER_MODEL)),
                ('new_device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='swap_new_device', to='service_app.device')),
                ('peyment_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='swap_payment_type', to='service_app.paymenttype')),
                ('refund_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='swap_refund_type', to='service_app.refundtype')),
                ('sawapprove_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='swap_approved_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
