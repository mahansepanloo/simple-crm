from django.urls import path
from rest_framework.routers import DefaultRouter

from setting_app.views import (BrandViewSet, BrandSettingViewSet, ColorViewSet, EmployerViewSet, GuaranteeViewSet, SwaptypeViewSet,  MultipleDeleteBrand
                            ,MultipleDeleteBrandSetting, MultipleDeleteColor, MultipleDeleteEmployer, MultipleDeleteGuarantee, MultipleDeleteSwaptype,
                            ColorCloneView, EmployerCloneView, GuaranteeCloneView, SwaptypeCloneView, BrandCloneView, BrandSettingCloneView,RefundTypeViewSet, PaymentTypeViewSet,
                            CloneRefundTypeView, ImportRefundTypeView, MultipleDeleteRefundType, ClonePaymentTypeView, ImportPaymentTypeView, MultipleDeletePaymentType, 
                            ImportBrandSettingView, ImportBrandView, ImportColorView, ImportEmployerView, ImportGuaranteeView, ImportSwaptypeView, ImportPaymentSourceView,
                            PaymentSourceViewSet, MultipleDeletePaymentSource)



router = DefaultRouter()
router.register(r"brandsetting", BrandSettingViewSet)
router.register(r"brand", BrandViewSet)
router.register(r"color", ColorViewSet)
router.register(r"employer", EmployerViewSet)
router.register(r"guarantee", GuaranteeViewSet)
router.register(r"swaptype", SwaptypeViewSet)
router.register(r"refund-type", RefundTypeViewSet, basename="refund-type")
router.register(r"payment-type", PaymentTypeViewSet, basename="payment-type")
router.register(r"payment-source", PaymentSourceViewSet, basename="payment-source")


urlpatterns = [
    path("multiple-delete-brand/", MultipleDeleteBrand.as_view(), name="multiple-delete-brand"),
    path("multiple-delete-brandsetting/", MultipleDeleteBrandSetting.as_view(), name="multiple-delete-brandsetting"),
    path("multiple-delete-color/", MultipleDeleteColor.as_view(), name="multiple-delete-color"),
    path("multiple-delete-employer/", MultipleDeleteEmployer.as_view(), name="multiple-delete-employer"),
    path("multiple-delete-guarantee/", MultipleDeleteGuarantee.as_view(), name="multiple-delete-guarantee"),
    path("multiple-delete-swaptype/", MultipleDeleteSwaptype.as_view(), name="multiple-delete-swaptype"),
    path("brand-clone/<int:pk>/", BrandCloneView.as_view(), name="brand-clone"),
    path("brandsetting-clone/<int:pk>/", BrandSettingCloneView.as_view(), name="brandsetting-clone"),
    path("color-clone/<int:pk>/", ColorCloneView.as_view(), name="color-clone"),
    path("employer-clone/<int:pk>/", EmployerCloneView.as_view(), name="employer-clone"),
    path("guarantee-clone/<int:pk>/", GuaranteeCloneView.as_view(), name="guarantee-clone"),
    path("swaptype-clone/<int:pk>/", SwaptypeCloneView.as_view(), name="swaptype-clone"),
    path("import-brand/", ImportBrandView.as_view(), name="import-brand"),
    path("import-brandsetting/", ImportBrandSettingView.as_view(), name="import-brandsetting"),
    path("import-color/", ImportColorView.as_view(), name="import-color"),
    path("import-employer/", ImportEmployerView.as_view(), name="import-employer"),
    path("import-guarantee/", ImportGuaranteeView.as_view(), name="import-guarantee"),
    path("import-swaptype/", ImportSwaptypeView.as_view(), name="import-swaptype"),
    path("import-paymentsource/", ImportPaymentSourceView.as_view(), name="import-paymentsource"),
    path("clone-refund-type/<int:pk>/", CloneRefundTypeView.as_view(), name="clone_refund_type"),
    path("import-refund-type/", ImportRefundTypeView.as_view(), name="import_refund_type"),
    path("multiple-delete-refund-type/", MultipleDeleteRefundType.as_view(), name="delete_many_refund_type"),
    path("clone-payment-type/<int:pk>/", ClonePaymentTypeView.as_view(), name="clone_payment_type"),
    path("import-payment-type/", ImportPaymentTypeView.as_view(), name="import_payment_type"),
    path("multiple-delete-payment-type/", MultipleDeletePaymentType.as_view(), name="delete_many_payment_type"),
    path("multiple-delete-paymentsource/", MultipleDeletePaymentSource.as_view(), name="delete_many_paymentsource")
    
    
    
] + router.urls
