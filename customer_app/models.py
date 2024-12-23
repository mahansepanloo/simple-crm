from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from config.enums import GenderEnum

class Customer(models.Model):
    full_name = models.CharField(max_length=300, verbose_name=_("Full Name"))
    accounting_code = models.CharField(
        max_length=100, verbose_name=_("Accounting Code"), unique=True
    )
    gspn_id = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("GSPN ID")
    )
    gspn_name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("GSPN Name")
    )
    gender = models.CharField(
        max_length=10,
        choices=GenderEnum,
        default="M",
    )
    account_name = models.CharField(
        max_length=300, null=True, blank=True, verbose_name=_("Account Name")
    )
    email = models.EmailField(
        max_length=300, null=True, blank=True, verbose_name=_("Email")
    )
    home_phone = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Home Phone")
    )
    business_phone = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Bussiness Phone")
    )
    mobile_phone = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Mobile Phone")
    )
    fax = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("Fax"))
    address = models.TextField(null=True, blank=True, verbose_name=_("Address"))
    postal_code = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Postal Code")
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="customer_created_by",
        null=True, blank=True
    )

    def __str__(self) -> str:
        return self.full_name
    
    


    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")
