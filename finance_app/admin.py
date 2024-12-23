from django.contrib import admin
from finance_app.models import Cart, Account, Transaction, Payment, PaymentReview, Cheque, FinalApprove, ManagerApproval
from import_export.admin import ImportExportModelAdmin  
from finance_app.resources import (CartResource, AccountResource, TransactionResource, PaymentResource, PaymentReviewResource, 
                                   ChequeResource, FinalApproveResource,    ManagerApprovalResource)


@admin.register(Payment)
class PaymentAdmin(ImportExportModelAdmin):
    readonly_fields = ["created_at", "updated_at"]
    list_display = ["swap_or_refound", "final_amount", "payment_source", "payment_Type"]
    search_fields = ["swap_or_refound", "final_amount", "payment_source", "payment_Type"]
    resource_class = PaymentResource


@admin.register(PaymentReview)
class PaymentReviewAdmin(ImportExportModelAdmin):
    readonly_fields = ["created_at", "updated_at"]
    list_display = ["payment", "status", "created_by"]
    search_fields = ["payment", "status", "created_by"]
    resource_class = PaymentReviewResource


@admin.register(Cheque)
class ChequeAdmin(ImportExportModelAdmin):
    readonly_fields = ["created_at", "updated_at"]
    list_display = ["payment", "status", "created_by"]
    search_fields = ["payment", "status", "created_by"]
    resource_class = ChequeResource


@admin.register(FinalApprove)
class FinalApproveAdmin(ImportExportModelAdmin):
    readonly_fields = ["created_at", "updated_at"]
    list_display = ["payment", "status", "created_by"]
    search_fields = ["payment", "status", "created_by"]
    resource_class = FinalApproveResource


@admin.register(ManagerApproval)
class ManagerApprovalAdmin(ImportExportModelAdmin):
    readonly_fields = ["created_at", "updated_at"]
    list_display = ["payment", "status", "created_by"]
    search_fields = ["payment", "status", "created_by"]
    resource_class = ManagerApprovalResource



@admin.register(Cart)
class CartAdmin(ImportExportModelAdmin):
    readonly_fields = ["created_at", "updated_at"]
    list_display = ["branch", "account", "card_number", "status"]
    search_fields = ["branch", "account", "card_number", "status"]
    resource_class = CartResource


@admin.register(Account)
class AccountAdmin(ImportExportModelAdmin):
    readonly_fields = ["created_at", "updated_at"]
    list_display = ["username", "account_code", "dep_number", "organization_code","status"]
    search_fields = ["username", "account_code", "dep_number", "organization_code","status"]
    resource_class = AccountResource


@admin.register(Transaction)
class TransactionAdmin(ImportExportModelAdmin):
    readonly_fields = ["created_at", "updated_at"]
    list_display = ["cart", "transaction_type", "amount", "status"]
    search_fields = ["cart", "transaction_type", "amount", "status"]
    resource_class = TransactionResource







