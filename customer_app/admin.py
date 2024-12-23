from django.contrib.admin import register
from customer_app.models import Customer
from import_export.admin import ImportExportModelAdmin  
from .resources import CustomerResource  


@register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    resource_class = CustomerResource  
    list_display = ["full_name", "accounting_code", "gspn_id", "gspn_name"]
    search_fields = ["full_name", "accounting_code", "gspn_id", "gspn_name"]
    readonly_fields = ["created_at", "updated_at"]
