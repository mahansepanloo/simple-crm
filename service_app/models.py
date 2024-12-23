from django.db import models
from django.utils.translation import gettext_lazy as _
from config.enums import AGENT_TYPE_CHOICES, SWAP_OR_REFUND,STATUS_CHOICES, JOB_TYPE
from setting_app.models import Brand, Color, Guarantee, BrandSetting, RefundType, PaymentType
from django.contrib.auth.models import User
from customer_app.models import Customer
from setting_app.models import Swaptype




class DevicePrice(models.Model):
    model_code = models.CharField(
        max_length=100, verbose_name=_("Model Code"), unique=True
    )
    factory_model = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Factory Model")
    )
    commercial_model = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Commercial Model")
    )
    color = models.ForeignKey(
        Color, on_delete = models.CASCADE, related_name= "device_price_color",null=True, blank=True, verbose_name=_("Color")
    )
    memory = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Memory")
    )
    microtel_price = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Microtel Price")
    )
    inter_price = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Inter Price")
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True
)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True
)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="device_price_created_by",
        null=True, blank=True
    )

    
    
    

class Agents(models.Model):
    agent_type = models.CharField(choices=AGENT_TYPE_CHOICES, default="A")
    full_name = models.CharField(
        max_length=300, verbose_name=_("Full Name")
    )
    mobile_number = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Mobile Number")
    )
    business_number = models.CharField(
        max_length=100, verbose_name=_("Business Number"), unique=True
    )
    email = models.EmailField(
        max_length=300, null=True, blank=True, verbose_name=_("Email")
    )
    title = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Title")
    )
    seven_code = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Seven Code")
    )
    asc_code = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("ASC Code")
    )
    city = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("City")
    )
    manager_name = models.CharField(
        max_length=300, null=True, blank=True, verbose_name=_("Manager Name")
    )
    address = models.TextField(
        null=True, blank=True, verbose_name=_("Address")
    )
    fax = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Fax")
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True
)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True
)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="agents_created_by",
        null=True, blank=True
    )


class Device(models.Model):
    imei = models.CharField(
        max_length=100, unique=True
    )
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name="device_brand"
    )
    brand_code = models.CharField(
        max_length=100, null=True, blank=True
    )
    brand_model = models.ForeignKey(
        BrandSetting, on_delete = models.CASCADE, related_name="device_brand_model"
    )
    model_name = models.CharField(
        max_length=100, null=True, blank=True
    )
    commercial_model = models.CharField(
        max_length=100, null=True, blank=True
    )
    description = models.TextField(
        null=True, blank=True
    )
    serial_number = models.CharField(
        max_length=100, null=True, blank=True
    )
    color = models.ForeignKey(
        Color, on_delete=models.CASCADE, related_name="device_color"
    )
    memory = models.CharField(
        max_length=100, null=True, blank=True
    )
    purchase_date = models.DateTimeField(
        null=True, blank=True
    )
    guarantee = models.ForeignKey(
        Guarantee, on_delete=models.CASCADE, related_name="device_guarantee"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="device_created_by",
        null=True, blank=True
    )

    
class Case(models.Model):
    jobtype = models.IntegerField(choices = JOB_TYPE)
    customer = models.ForeignKey(
        Customer, on_delete = models.CASCADE, related_name = "case_customer"
        )
    branch = models.ForeignKey(
        Agents, on_delete=models.CASCADE, related_name = "case_branch"
    )
    device = models.ForeignKey(
        Device, on_delete = models.CASCADE, related_name = "case_device"
    )
    swaptype = models.ForeignKey(
        Swaptype, on_delete = models.CASCADE, related_name = "case_swaptype" 
    )
    job_number = models.CharField(max_length = 200, unique=True)
    invoice_date = models.DateTimeField()
    invoice_amount = models.CharField(max_length = 200)
    customer_statement = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="case_created_by",
        null=True, blank=True
    )
    
    def __str__(self):
        return self.job_number


class CaseApprove(models.Model):
    case = models.OneToOneField(
        Case, on_delete = models.CASCADE, related_name = "case_approve_case"
    )
    status = models.BooleanField()
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="case_approve_created_by",
        null=True, blank=True
    )

    def __str__(self):
        return self.case.job_number
    
    
class CaseSend(models.Model):
    case = models.OneToOneField(
        Case, on_delete = models.CASCADE, related_name = "case_send_case"
    )
    status = models.BooleanField()
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="case_send_created_by",
        null=True, blank=True
    )

    def __str__(self):
        return self.case.job_number
    
    
class CaseReceive(models.Model):
    case = models.OneToOneField(
        Case, on_delete = models.CASCADE, related_name = "case_receive_case"
    )
    status = models.BooleanField()
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="case_receive_created_by",
        null=True, blank=True
    )
    
    def __str__(self):
        return self.case.job_number


class CaseSupervisorApprove(models.Model):
    case = models.OneToOneField(
        Case, on_delete = models.CASCADE, related_name = "case_supervisor_approve_case"
    )
    status = models.BooleanField()
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="case_supervisor_approve_created_by",
        null=True, blank=True
    )
    
    def __str__(self):
        return self.case.job_number
    
    
class Note(models.Model):
    attachment = models.FileField(null= True, blank=True, upload_to='%Y-%m-%d')
    note = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="note_created_by",
        null=True, blank=True
    )


class Swap(models.Model):
    case = models.ForeignKey(
        Case, on_delete = models.CASCADE, related_name = "swap_case"
    )
    swap_or_refund = models.IntegerField(choices=SWAP_OR_REFUND, null=True, blank=True)
    refund_type = models.ForeignKey(RefundType, on_delete=models.CASCADE, related_name="swap_refund_type", null=True, blank=True)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE, related_name="swap_payment_type", null=True, blank=True)
    Description = models.TextField(null=True, blank=True)
    new_device = models.ForeignKey(
        Device, on_delete=models.CASCADE, related_name="swap_new_device", null=True, blank=True
    )
    required_amount = models.IntegerField(null=True, blank=True)
    amount_of_additions = models.IntegerField(null=True, blank=True)
    Amountـofـdeduction = models.IntegerField(null=True, blank=True)
    final_amount = models.IntegerField(null=True, blank=True)
    sawapprove = models.BooleanField(default=False)
    sawapprove_date = models.DateTimeField(null=True, blank=True)
    sawapprove_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="swap_approved_by",
        null=True, blank=True
    )
    send_to_financial = models.BooleanField(default=False)
    send_date = models.DateTimeField(null=True, blank=True)
    financial_approved_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="swap_financial_approved_by",
        null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="swap_created_by",
        null=True, blank=True
    )



