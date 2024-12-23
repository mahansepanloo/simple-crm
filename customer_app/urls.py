from django.urls import path
from rest_framework.routers import DefaultRouter
from customer_app.views import CustomerViewSet,DeleteMultipleCustomersView, CloneCustomerView, ImportCustomerView

router = DefaultRouter()
router.register(r"customers", CustomerViewSet)

urlpatterns = [
    path("multiple_delete/", DeleteMultipleCustomersView.as_view(), name="delete_many_customers"),
    path("clone-customer/<int:id>/", CloneCustomerView.as_view(), name="clone customer"),
    path("import-customer/", ImportCustomerView.as_view(), name="import customer"),

] + router.urls
