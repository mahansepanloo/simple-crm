from service_app.models import DevicePrice, Agents, Device, Case, CaseApprove, CaseSend, CaseReceive, CaseSupervisorApprove, Note, Swap
from django.contrib.admin import register
from import_export.admin import ImportExportModelAdmin  
from service_app.resources import( DevicePriceResource, AgentsResource, DeviceResource, CaseResource,
                                  CaseApproveResource, CaseSendResource, CaseReceiveResource, CaseSupervisorApproveResource, NoteResource, SwapResource, 
                                  )


@register(DevicePrice)
class DevicePriceAdmin(ImportExportModelAdmin):
    list_display = ["model_code", "factory_model", "microtel_price", "inter_price"]
    search_fields = ["model_code", "factory_model"]
    resource_class = DevicePriceResource  



@register(Agents)
class AgentsAdmin(ImportExportModelAdmin):
    list_display = ["full_name", "agent_type"]
    search_fields = ["full_name"]
    resource_class = AgentsResource  


@register(Device)
class DeviceAdmin(ImportExportModelAdmin): 
    readonly_fields = ["created_at", "updated_at"]
    list_display = ["imei", "brand", "brand_code", "brand_model","model_name", "commercial_model", "serial_number", "color", "memory", "guarantee" ]
    search_fields = ["imei", "brand", "brand_code", "brand_model","model_name", "commercial_model", "serial_number", "color", "memory", "guarantee" ]
    resource_class = DeviceResource  


@register(Case)
class CaseAdmin(ImportExportModelAdmin):
    readonly_fields = ["created_at", "updated_at"]
    list_display = ["customer_statement", "invoice_amount", "invoice_date","job_number", "swaptype", "device", "branch", "customer", "jobtype" ]
    search_fields = ["customer_statement", "invoice_amount", "invoice_date","job_number", "swaptype", "device", "branch", "customer", "jobtype" ]
    resource_class = CaseResource


@register(CaseApprove)
class CaseApproveAdmin(ImportExportModelAdmin):
    readonly_fields = ["created_at"]
    list_display = ["case", "status", "date"]
    search_fields = ["case", "status", "date"]
    resource_class = CaseApproveResource
    

@register(CaseSend)
class CaseSendAdmin(ImportExportModelAdmin):
    readonly_fields = ["created_at"]
    list_display = ["case", "status", "date"]
    search_fields = ["case", "status", "date"]
    resource_class = CaseSendResource
    

@register(CaseReceive)
class CaseReceiveAdmin(ImportExportModelAdmin):
    readonly_fields = ["created_at"]
    list_display = ["case", "status", "date"]
    search_fields = ["case", "status", "date"]
    resource_class = CaseReceiveResource
    
    
@register(CaseSupervisorApprove)
class CaseSupervisorApproveAdmin(ImportExportModelAdmin):
    readonly_fields = ["created_at"]
    list_display = ["case", "status", "date"]
    search_fields = ["case", "status", "date"]
    resource_class = CaseSupervisorApproveResource


@register(Note)
class NoteAdmin(ImportExportModelAdmin):
    readonly_fields = ["created_at"]
    list_display = ["note", "attachment"]
    search_fields = [ "note", "attachment"]
    resource_class = NoteResource
    

@register(Swap)
class SwapAdmin(ImportExportModelAdmin):
    readonly_fields = ["created_at"]
    list_display = ["swap_or_refund", "case"]
    search_fields = ["swap_or_refund"]
    resource_class = SwapResource
    
