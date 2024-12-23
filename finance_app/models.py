from django.db import models
from django.contrib.auth.models import User
from service_app.models import Agents
from config.enums import STATUS_CHOICES_ACCOUNT, STATUS_TRANSACTION, STATUS_TYPE, SWAP_OR_REFUND
from setting_app.models import PaymentType, PaymentSource


class Account(models.Model):
    username = models.CharField(max_length=255, unique=True)
    account_code = models.CharField(max_length=255, unique=True)
    dep_number = models.CharField(max_length=255)
    organization_code = models.CharField(max_length=255)
    status = models.IntegerField(choices=STATUS_CHOICES_ACCOUNT, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="account_created_by"
    )

    def __str__(self):
        return self.account_code
    

class Cart(models.Model):
    branch = models.ForeignKey(
        Agents, on_delete=models.CASCADE, related_name="cart_branch"
    )
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="cart_account"
    )
    card_number = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES_ACCOUNT, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cart_created_by"
    )

    def __str__(self):
        return self.card_number
    

class Transaction(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="transaction_cart"
    )
    transaction_type = models.CharField(choices=STATUS_TYPE, max_length=100, default='charge')
    amount = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    system_message = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS_TRANSACTION, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="transaction_created_by"
    )
    updated_status_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="transaction_updated_by", null=True, blank=True
    )
    updated_status_at = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return self.cart.account.username


class Payment(models.Model):
    swap_or_refound = models.IntegerField(choices=SWAP_OR_REFUND)
    final_amount = models.IntegerField(null=True, blank=True)
    payment_source = models.ForeignKey(
        PaymentSource, on_delete=models.CASCADE, related_name="payment_payment_source"
    )
    payment_Type = models.ForeignKey(
        PaymentType, on_delete=models.CASCADE, related_name="payment_payment_type"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="payment_created_by"
    )


class PaymentReview(models.Model):
    payment = models.ForeignKey(
        Payment, on_delete=models.CASCADE, related_name="payment_review_payment"
    )
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="payment_review_created_by", null=True, blank=True
    )


class ManagerApproval(models.Model):
    payment = models.ForeignKey(
        Payment, on_delete=models.CASCADE, related_name="manage_approval_payment"
    )
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="manage_approval_created_by"
    )


class Cheque(models.Model):
    payment = models.ForeignKey(
        Payment, on_delete=models.CASCADE, related_name="cheque_payment"
    )
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cheque_created_by"
    )


class FinalApprove(models.Model):
    payment = models.ForeignKey(
        Payment, on_delete=models.CASCADE, related_name="final_approve_payment"
    )
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="final_approve_created_by"
    )

    