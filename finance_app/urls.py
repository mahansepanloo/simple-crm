from django.urls import path
from rest_framework.routers import DefaultRouter
from finance_app.views import (CartViewset, AccountsViewset, TransactionViewset, 
                    MultipleDeleteCartView, MultipleDeleteAccountView, MultipleDeleteTransactionView, EditStatusTransactionView,
                    TransactionCloneView, AccountsCloneView, CartCloneView,ImportAccountView, ImportTransactionView, ImportCartView,
                    ImportPaymentREviewView, PaymentReviewViewSet, MultipleDeletePaymentReviewView, ManageApproveViewSet, ImportManagerApprovalView, 
                    MultipleDeleteManagerApprovalView, ChequeViewSet, ImportChequeView, MultipleDeleteChequeView, FinalApproveViewSet, ImportFinalApproveView,
                    MultipleDeleteFinalApproveView, PaymentCloneView, PaymentViewSet, ImportPaymentView, MultipleDeletePaymentView,
                    )

router = DefaultRouter()
router.register(r"cart", CartViewset)
router.register(r"accounts", AccountsViewset)
router.register(r"transaction", TransactionViewset)
router.register(r"payment_review", PaymentReviewViewSet)
router.register(r"manager_approval", ManageApproveViewSet)
router.register(r"cheque", ChequeViewSet)
router.register(r"final_approve", FinalApproveViewSet)
router.register(r"payment", PaymentViewSet)


urlpatterns = [
    path("multiple_delete-cart/", MultipleDeleteCartView.as_view(), name="delete_many_cart"),
    path("multiple_delete-account/", MultipleDeleteAccountView.as_view(), name="delete_many_account"),
    path("multiple_delete-transaction/", MultipleDeleteTransactionView.as_view(), name="delete_many_transaction"),
    path("edit-status/<int:pk>/", EditStatusTransactionView.as_view(), name="delete_many_customer"),
    path("clone-cart/<int:pk>/", CartCloneView.as_view(), name="clone_cart"),
    path("clone-account/<int:pk>/", AccountsCloneView.as_view(), name="clone_account"),
    path("clone-transaction/<int:pk>/", TransactionCloneView.as_view(), name="clone_transaction"),
    path("import-account/", ImportAccountView.as_view(), name="import_account"),
    path("import-transaction/", ImportTransactionView.as_view(), name="import_transaction"),
    path("import-cart/", ImportCartView.as_view(), name="import_cart"),
    path("import-payment-review/", ImportPaymentREviewView.as_view(), name="import_payment_review"),
    path("import-manager-approval/", ImportManagerApprovalView.as_view(), name="import_manager_approval"),
    path("import-cheque/", ImportChequeView.as_view(), name="import_cheque"),
    path("import-final-approve/", ImportFinalApproveView.as_view(), name="import_final_approve"),
    path("import-payment/", ImportPaymentView.as_view(), name="import_payment"),
    path("multiple_delete-payment-review/", MultipleDeletePaymentReviewView.as_view(), name="delete_many_payment_review"),
    path("multiple_delete-manager-approval/", MultipleDeleteManagerApprovalView.as_view(), name="delete_many_manager_approval"),
    path("multiple_delete-cheque/", MultipleDeleteChequeView.as_view(), name="delete_many_cheque"),
    path("multiple_delete-final-approve/", MultipleDeleteFinalApproveView.as_view(), name="delete_many_final_approve"),
    path("multiple_delete-payment/", MultipleDeletePaymentView.as_view(), name="delete_many_payment"),
    path("clone-payment/<int:pk>/", PaymentCloneView.as_view(), name="clone_payment"),
    

    



] + router.urls
