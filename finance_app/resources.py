from import_export import resources  
from finance_app.models import Cart, Account, Transaction, FinalApprove, Cheque, ManagerApproval, PaymentReview, Payment

class CartResource(resources.ModelResource):  
    class Meta:  
        model = Cart


class AccountResource(resources.ModelResource):
    class Meta:
        model = Account


class TransactionResource(resources.ModelResource):
    class Meta:
        model = Transaction


class FinalApproveResource(resources.ModelResource):
    class Meta:
        model = FinalApprove


class ChequeResource(resources.ModelResource):
    class Meta:
        model = Cheque


class ManagerApprovalResource(resources.ModelResource):
    class Meta:
        model = ManagerApproval


class PaymentReviewResource(resources.ModelResource):
    class Meta:
        model = PaymentReview


class PaymentResource(resources.ModelResource):
    class Meta:
        model = Payment