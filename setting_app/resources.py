from import_export import resources  
from setting_app.models import Brand, BrandSetting, Color, Employer, Guarantee, Swaptype, RefundType, PaymentType, PaymentSource

class BrandResource(resources.ModelResource):  
    class Meta:  
        model = Brand  


class BrandSettingResource(resources.ModelResource):  
    class Meta:  
        model = BrandSetting


class ColorResource(resources.ModelResource):  
    class Meta:  
        model = Color


class EmployerResource(resources.ModelResource):  
    class Meta:  
        model = Employer


class GuaranteeResource(resources.ModelResource):  
    class Meta:  
        model = Guarantee


class SwaptypeResource(resources.ModelResource):
    class Meta:
        models = Swaptype


class RefundTypeResource(resources.ModelResource):
    class Meta:
        model = RefundType
        
        
class PaymentTypeResource(resources.ModelResource):
    class Meta:
        model = PaymentType

class PaymentSourceResource(resources.ModelResource):
    class Meta:
        model = PaymentSource