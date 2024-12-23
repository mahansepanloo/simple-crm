from service_app.models import Agents, DevicePrice, Device, Case, CaseApprove, CaseReceive, CaseSend, CaseSupervisorApprove, Note, Swap
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from user_app.serializers import UserSerializer
from setting_app.models import Brand, Color, Guarantee, BrandSetting, Swaptype, RefundType, PaymentType
from customer_app.models import Customer
from rest_framework.exceptions import ValidationError



#serializer ForeignKey

class RefundTypeSerializers(ModelSerializer):
    class Meta:
        model = RefundType
        fields = ("id", "title")
        
class PaymentTypeSerializers(ModelSerializer):
    class Meta:
        model = PaymentType
        fields = ("id", "title")

class brandSerializers(ModelSerializer):
    class Meta:
        model = Brand
        fields = ("id", "name")
        
class ColorSerializers(ModelSerializer):
    class Meta:
        model = Color
        fields = ("id", "name")

class GuaranteeSerializers(ModelSerializer):
    class Meta:
        model = Guarantee
        fields = ("id", "title")
        
class BrandSettingSerializers(ModelSerializer):
    class Meta:
        model = BrandSetting
        fields = ("id", "title")


class CustomerSerializers(ModelSerializer):
    class Meta:
        model = Customer
        fields = ("id", "full_name")


class BranchSerializers(ModelSerializer):
    class Meta:
        model = Agents
        fields = ("id", "full_name")
        

class DeviceSerializers(ModelSerializer):
    class Meta:
        model = Device
        fields = ("id", "brand_code")


class SwaptypeSerializers(ModelSerializer):
    class Meta:
        model = Swaptype
        fields = ("id", "title")
        
class CaseSerializers(ModelSerializer):
    class Meta:
        model = Case
        fields = ("id", "job_number")
        
#end




class AgentsCreateSerializer(ModelSerializer):
    class Meta:
        model = Agents
        fields = '__all__'
        read_only_fields = ['id']


class AgentListSerializer(ModelSerializer):
    class Meta:
        model = Agents
        fields = ["id", "agent_type", "full_name","business_number", "title", "status", "manager_name", "city"]
        read_only_fields = ['id']

        

class AgentDetailSerializer(ModelSerializer):
    class Meta:
        model = Agents
        fields = '__all__'
        read_only_fields = ['id'] 
    
    

class DeviceCreatePriceSerializer(ModelSerializer):
    class Meta:
        model = DevicePrice
        fields = '__all__'
        read_only_fields = ['id'] 

        
        
class DeviceListPriceSerializer(ModelSerializer):
    class Meta:
        model = DevicePrice
        fields = ("id", "model_code", "factory_model", "commercial_model", "microtel_price", "inter_price")
        read_only_fields = ['id'] 
        
        
class DeviceDetailPriceSerializer(ModelSerializer):
    class Meta:
        model = DevicePrice
        fields = '__all__'
        read_only_fields = ['id'] 
        
        

class DeviceCreateSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
        read_only_fields = ["id", "created_at", "updated_at", "created_by"]
           

class DeviceListSerializer(ModelSerializer):
    brand = brandSerializers()
    color = ColorSerializers()
    guarantee = GuaranteeSerializers()
    brand_model = BrandSettingSerializers()
    created_by = UserSerializer()
    class Meta:
        model = Device
        fields = ("id", "imei", "brand", "brand_code", "brand_model", "model_name", "commercial_model", "created_by", "color", "guarantee")
        read_only_fields = ["id", "created_at", "updated_at", "created_by"]
        


class DeviceDEtailSerializer(ModelSerializer):
    brand = brandSerializers()
    color = ColorSerializers()
    guarantee = GuaranteeSerializers()
    created_by = UserSerializer()
    brand_model = BrandSettingSerializers()
    class Meta:
        model = Device
        fields = '__all__'
        read_only_fields = ["id", "created_at", "updated_at", "created_by"]


class MultipleDeleteSerializer(serializers.Serializer):
    ids = serializers.ListField()

    
class CaseCreateSerializer(ModelSerializer):
    class Meta:
        model = Case
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "created_by"]
        
        
class CaseListSerializer(ModelSerializer):
    customer = CustomerSerializers()
    branch = BranchSerializers()
    device = DeviceSerializers()
    swaptype = SwaptypeSerializers()
    class Meta:
        model = Case
        fields = ("id", "jobtype", "customer", "branch", "device", "swaptype", "job_number",
                  "invoice_date", "invoice_amount", "customer_statement" )
        read_only_fields = ["id", "created_at", "updated_at", "created_by"]


class CaseDetailSerializer(ModelSerializer):
    customer = CustomerSerializers()
    branch = BranchSerializers()
    device = DeviceSerializers()
    swaptype = SwaptypeSerializers()
    created_by = UserSerializer()
    class Meta:
        model = Case
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "created_by"]


class CloneDevicePriceSerializer(ModelSerializer):
    class Meta:
        model = DevicePrice
        fields = ("model_code",  )
        

class CloneAgentsSerializers(ModelSerializer):
    class Meta:
        model = Agents
        fields = ("business_number", )
        
        
class CloneDeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = ("imei", )
        
        
class CloneCaseSerializer(ModelSerializer):
    class Meta:
        model = Case
        fields = ("job_number", )


class CaseSendCreateSerializer(ModelSerializer):
    class Meta:
        model = CaseSend
        fields = "__all__"
        read_only_fields = ["id", "created_at", "created_by"]


class CaseSendListSerializer(ModelSerializer):
    case = CaseSerializers()
    created_by = UserSerializer()

    class Meta:
        model = CaseSend
        fields = ("id", "case", "status", "created_by")
        read_only_fields = ["id", "created_at", "created_by"]
        
        
class CaseSendDetailSerializer(ModelSerializer):
    created_by = UserSerializer()
    case = CaseSerializers()
    class Meta:
        model = CaseSend
        fields = "__all__"
        read_only_fields = ["id", "created_at", "created_by"]
        

class CaseApproveCreateSerializer(ModelSerializer):
    class Meta:
        model = CaseApprove
        fields = "__all__"
        read_only_fields = ["id", "created_at", "created_by"]


class CaseApproveListSerializer(ModelSerializer):
    created_by = UserSerializer()
    case = CaseSerializers()
    class Meta:
        model = CaseApprove
        fields = ("id", "case", "status", "created_by")
        read_only_fields = ["id", "created_at", "created_by"]


class CaseApproveDetailSerializer(ModelSerializer):
    created_by = UserSerializer()
    case = CaseSerializers()
    class Meta:
        model = CaseApprove
        fields = "__all__"
        read_only_fields = ["id", "created_at", "created_by"]


class CaseReceiveCreateSerializer(ModelSerializer):
    class Meta:
        model = CaseReceive
        fields = "__all__"
        read_only_fields = ["id", "created_at", "created_by"]
        

class CaseReceiveListSerializer(ModelSerializer):
    created_by = UserSerializer()
    case = CaseSerializers()
    class Meta:
        model = CaseReceive
        fields = ("id", "case", "status", "created_by")
        read_only_fields = ["id", "created_at", "created_by"]
        
        
class CaseReceiveDetailSerializer(ModelSerializer):
    created_by = UserSerializer()
    case = CaseSerializers()
    class Meta:
        model = CaseReceive
        fields = "__all__"
        read_only_fields = ["id", "created_at", "created_by"]
        
        
class CaseSupervisorCreateSerializer(ModelSerializer):
    class Meta:
        model = CaseSupervisorApprove
        fields = "__all__"
        read_only_fields = ["id", "created_at", "created_by"]
        

class CaseSupervisorListSerializer(ModelSerializer):
    created_by = UserSerializer()
    case = CaseSerializers()
    class Meta:
        model = CaseSupervisorApprove
        fields = ("id", "case", "status", "created_by")
        read_only_fields = ["id", "created_at", "updated_at", "created_by"]
        

class CaseSupervisorDetailSerializer(ModelSerializer):
    created_by = UserSerializer()
    case = CaseSerializers()
    class Meta:
        model = CaseSupervisorApprove
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "created_by"]
        
        
class NoteCreateSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"
        read_only_fields = ["id", "created_at", "created_by"]
        
    def validate(self, data):
        if data.get("note") is None and data.get("attachment") is None:
            raise ValidationError("one field must be required")
        return super().validate(data)

    
class NoteListSerializer(ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = Note
        fields = ("id", "note", "attachment", "created_by")
        read_only_fields = ["id", "created_at", "created_by"]


class NoteDetailSerializer(ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = Note
        fields = "__all__"
        read_only_fields = ["id", "created_at", "created_by", ]
        

class SwapCreateSerializer(ModelSerializer):
    class Meta:
        model = Swap
        fields = "__all__"
        read_only_fields = ["id", "created_at", "created_by", "sawapprove", "sawapprove_date", "sawapprove_by", 
                            "send_to_financial", "send_date", "financial_approved_by", "financial_approved_at" ]

    def validate(self, data):
        if (data.get("swap_or_refund") == 0 and data.get("refund_type") is None) or (data.get("swap_or_refund") == 0 and data.get("payment_type") is None):
            raise ValidationError('must choose refund type and payment type')
        elif data.get("swap_or_refund") == 0 and data.get ("new_device") is not None:
            raise ValidationError("can not chose new device")
        elif (data.get("swap_or_refund") == 1 and data.get("refund_type") is not None) or (data.get("swap_or_refund") == 1 and data.get("payment_type") is not None):   
            raise ValidationError("can not chose refund and payment")
        elif data.get("swap_or_refund") == 1 and data.get("new_device") is None:
            raise ValidationError('must choose new_device ')
        return super().validate(data)
                
        
class SwapListSerializer(ModelSerializer):
    created_by = UserSerializer()
    case = CaseSerializers()
    refund_type = RefundTypeSerializers()
    payment_type = PaymentTypeSerializers()
    class Meta:
        model = Swap
        fields = ("id", "case", "created_by", "refund_type", "payment_type")
        read_only_fields = ["id", "created_at", "created_by", "sawapprove", "sawapprove_date", "sawapprove_by", 
                            "send_to_financial", "send_date", "financial_approved_by", "financial_approved_at" ]
              
              
class SwapDetailSerializer(ModelSerializer):
    created_by = UserSerializer()
    case = CaseSerializers()
    refund_type = RefundTypeSerializers()
    payment_type = PaymentTypeSerializers()
    sawapprove_by = UserSerializer()
    financial_approved_by = UserSerializer()
    new_device = DeviceSerializers()
    class Meta:
        model = Swap
        fields = "__all__"
        read_only_fields = ["id", "created_at", "created_by", "sawapprove", "sawapprove_date", "sawapprove_by", 
                            "send_to_financial", "send_date", "financial_approved_by", "financial_approved_at" ]


class AprrovedSawSerializer(ModelSerializer):
    class Meta:
        model = Swap
        fields = ("sawapprove",)
        extra_kwargs = {
            "sawapprove":{"required":True} 
            }
        read_only_fields = ["id", "created_at", "created_by", "case", "swap_or_refund", "refund_type", "payment_type", "Description", 
                            "new_device", "required_amount", "amount_of_additions", "Amountـofـdeduction", "final_amount",
                            "send_to_financial", "send_date", "financial_approved_by", "financial_approved_at"]
        
        
class AprrovedCompletedSerializer(ModelSerializer):
    class Meta:
        model = Swap
        fields = ("send_to_financial",)
        extra_kwargs = {
            "send_to_financial":{"required":True} 
            }
        read_only_fields = ["id", "created_at", "created_by", "case", "swap_or_refund", "refund_type", "payment_type", "Description", 
                            "new_device", "required_amount", "amount_of_additions", "Amountـofـdeduction", "final_amount",
                            "sawapprove",]