from rest_framework.serializers import ModelSerializer
from setting_app.models import Brand, BrandSetting, Color, Employer, Guarantee, Swaptype, RefundType, PaymentType, PaymentSource
from user_app.serializers import UserSerializer
from rest_framework import serializers


#serializer ForeignKey

class brandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ("id", "name") 


        
#end

class MultipleDeleteSerializer(serializers.Serializer):
    ids = serializers.ListField()


class BrandCreateSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__" 
        read_only_fields = ["id", "created_at", "updated_at", "created_by"]


class BrandListSerializer(ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = Brand
        fields = ("id", "name", "created_by" )
        read_only_fields = ["id", "created_at", "updated_at", "created_by"]


class BrandDetailSerializer(ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = Brand
        fields = "__all__" 
        read_only_fields = ["id", "created_at", "updated_at", "created_by"]
        

class BrandSettingCreateSerializer(ModelSerializer):
    class Meta:
        model = BrandSetting
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "created_by"]


class BrandSettingListSerializer(ModelSerializer):
    brand = brandSerializer()
    created_by = UserSerializer()
    class Meta:
        model = BrandSetting
        fields = ("id", "brand", "title", "created_by")
        read_only_fields = ["id", "created_at", "updated_at", "created_by"]


class BrandSettingDetailSerializer(ModelSerializer):
    brand = brandSerializer()
    created_by = UserSerializer()
    class Meta:
        model = BrandSetting
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "created_by"]
        
        
class ColorCreateSerializer(ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "created_by"]



    
class ColorListSerializer(ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = Color
        fields = ("id", "name", "created_by" )
        read_only_fields = ["id", "created_at", "updated_at", "created_by"]

        
class ColorDetailSerializer(ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = Color
        fields = "__all__" 
        read_only_fields = ["id", "created_at", "updated_at", "created_by"]
        

class EmployerCreateSerializer(ModelSerializer):
    class Meta:
        model = Employer
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "created_by"]


class EmployerListSerializer(ModelSerializer):
    brand = brandSerializer()
    created_by = UserSerializer()
    class Meta:
        model = Employer
        fields = ("id", "name", "brand", "marketing_employer", "factory_employer", 'imei', "start_date", "end_date", "created_by")
        read_only_fields = ["id", "created_at", "updated_at", "created_by"]


class EmployerDetailSerializer(ModelSerializer):
    brand = brandSerializer()
    created_by = UserSerializer()
    class Meta:
        model = Employer
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "created_by"]
        
        
class GuaranteeCreateSerializer(ModelSerializer):
    class Meta:
        model = Guarantee
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "created_by"]


class GuaranteeListSerializer(ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = Guarantee
        fields = ("id", "title", "created_by" )
        read_only_fields = ["id", "created_at", "updated_at", "created_by"]
        

class GuaranteeDetailSerializer(ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = Guarantee
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "created_by"]
        

class SwaptypeCreateSerializer(ModelSerializer):
    class Meta:
        model = Swaptype
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "created_by"]


class SwaptypeListSerializer(ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = Swaptype
        fields = ("id", "title", "created_by" )
        read_only_fields = ["id", "created_at", "updated_at", "created_by"]


class SwaptypeDetailSerializer(ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = Swaptype
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "created_by"]


class CloneBrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ("name", )


class CloneBrandSettingSerializer(ModelSerializer):
    class Meta:
        model = BrandSetting
        fields = ("title", )
        
        
class CloneColorSerializer(ModelSerializer):
    class Meta:
        model = Color
        fields = ("name", )
        
        
class CloneEmployerSerializer(ModelSerializer):
    class Meta:
        model = Employer
        fields = ("imei", )
        
        
class CloneGuaranteeSerializer(ModelSerializer):
    class Meta:
        model = Guarantee
        fields = ("title", )
        
        
class CloneSwaptypeSerializer(ModelSerializer):
    class Meta:
        model = Swaptype
        fields = ("title", )


class RefundCreateSerializer(ModelSerializer):
    class Meta:
        model = RefundType
        fields = "__all__"
        read_only_fields = ["id", "created_at", "created_by" ]


class RefundListSerializer(ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = RefundType
        fields = ("id", "title", "created_by")
        read_only_fields = ["id", "created_at", "created_by" ]
        

class RefundDetailSerializer(ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = RefundType
        fields = "__all__"
        read_only_fields = ["id", "created_at", "created_by" ]


class PaymentTypeCreateSerializers(ModelSerializer):
    class Meta:
        model = PaymentType
        fields = "__all__"
        read_only_fields = ["id", "created_at", "created_by" ]
        

class PeymentTypeListSerializer(ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = PaymentType
        fields = ("id", "title", "created_by")
        read_only_fields = ["id", "created_at", "created_by" ]
        

class PeymentTypeDetailSerializer(ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = PaymentType
        fields = "__all__"
        read_only_fields = ["id", "created_at", "created_by" ]
        

class PaymentSourceCreateSerializer(ModelSerializer):
    class Meta:
        model = PaymentSource
        fields = "__all__"
        read_only_fields = ["id", "created_at", "created_by" ]


class PaymentSourceListSerializer(ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = PaymentSource
        fields = ("id", "title", "created_by")
        read_only_fields = ["id", "created_at", "created_by" ]


class PaymentSourceDetailSerializer(ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = PaymentSource
        fields = "__all__"
        read_only_fields = ["id", "created_at", "created_by" ]
        