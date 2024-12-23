from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from customer_app.models import Customer
from user_app.serializers import UserSerializer





class CustomerCreateSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at", "created_by"]


class CustomerDetailSerializer(ModelSerializer):
    created_by = UserSerializer()

    class Meta:
        model = Customer
        fields = "__all__"


class CustomerListSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "id",
            "full_name",
            "mobile_phone",
            "business_phone",
            "gspn_id",
            "gspn_name",
            "created_at",
            "accounting_code"
            
        ]


class CustomerDeleteSerializer(serializers.Serializer):
    ids =  serializers.ListField()
    
    
class CloneCustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ("accounting_code", "full_name")
        extra_kwargs = {
            "accounting_code":{"required":True}
            
        } 
