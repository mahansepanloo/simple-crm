from django.contrib.admin import  register
from setting_app.models import Brand, BrandSetting, Color, Employer, Guarantee, Swaptype, SevenConfig, RefundType, PaymentType, PaymentSource
from import_export.admin import ImportExportModelAdmin  
from setting_app.resources import (BrandResource, BrandSettingResource, ColorResource, EmployerResource, SwaptypeResource, GuaranteeResource, PaymentTypeResource,
                                  RefundTypeResource, PaymentSourceResource)


@register(Brand)
class BrandAdmin(ImportExportModelAdmin): 
    resource_class = BrandResource  
    list_display = ["name"]
    search_fields = ["name"]
    readonly_fields = ["created_at", "updated_at"]


@register(BrandSetting)
class BrandSettingAdmin(ImportExportModelAdmin):
    resource_class = BrandSettingResource
    list_display = ["brand", "title"]
    search_fields = ["brand", "title"]
    readonly_fields = ["created_at", "updated_at"]


@register(Color)
class ColorAdmin(ImportExportModelAdmin):
    resource_class = ColorResource
    list_display = ["name"]
    search_fields = ["name"]
    readonly_fields = ["created_at", "updated_at"]
    
    
@register(Employer)
class EmployerAdmin(ImportExportModelAdmin):
    resource_class = EmployerResource
    list_display = ["name", "brand", "marketing_employer", "factory_employer", "imei"]
    search_fields = ["name", "brand", "marketing_employer", "factory_employer", "imei"]
    readonly_fields = ["created_at", "updated_at"]
    

@register(Swaptype)
class SwaptypeAdmin(ImportExportModelAdmin):
    resource_class = SwaptypeResource
    list_display = ['title']
    search_fields = ['title']
    readonly_fields = ["created_at", "updated_at"]
    
    
@register(Guarantee)
class GuaranteeAdmin(ImportExportModelAdmin):
    resource_class = GuaranteeResource
    list_display = ['title']
    search_fields = ['title']
    readonly_fields = ["created_at", "updated_at"]
    


@register(SevenConfig)
class SevenConfigAdmin(ImportExportModelAdmin):
    pass


@register(PaymentType)
class PaymentTypeAdmin(ImportExportModelAdmin):
    readonly_fields = ["created_at"]
    list_display = ["title"]
    search_fields = ["title"]
    resource_class = PaymentTypeResource
    

@register(RefundType)
class RefundTypeAdmin(ImportExportModelAdmin):
    readonly_fields = ["created_at"]
    list_display = ["title"]
    search_fields = ["title"]
    resource_class = RefundTypeResource


@register(PaymentSource)
class PaymentSourceAdmin(ImportExportModelAdmin):
    readonly_fields = ["created_at"]
    list_display = ["title"]
    search_fields = ["title"]
    resource_class = PaymentSourceResource