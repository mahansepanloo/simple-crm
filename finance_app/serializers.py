from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from finance_app.models import Cart, Account, Transaction, Payment, PaymentReview, PaymentSource, ManagerApproval, Cheque, PaymentType, FinalApprove
from service_app.models import Agents
from finance_app.models import Account
from user_app.serializers import UserSerializer

#serializer ForeignKey
class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = ("id", "swap_or_refound")

class PaymentSourceSerializer(ModelSerializer):
    class Meta:
        model = PaymentSource
        fields = ("id", "title")


class PaymentTypeSerializer(ModelSerializer):
    class Meta:
        model = PaymentType
        fields = ("id", "title")


class BranchSerializer(ModelSerializer):
    class Meta:
        model = Agents
        fields = ('id', "full_name")
        read_only_fields = ['id']
        
class AccountSerializers(ModelSerializer):
    class Meta:
        model = Account
        fields = ("id", "username")
        
        
class CartSerializers(ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id',"card_number")
        
        
class TransactionSerializers(ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = Transaction
        fields = ("id", "transaction_type", "amount", "status", "created_by")

        
#end


class CartCreateSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        read_only_fields = ['id', "created_at", "updated_at", "created_by"]


class CartListSerializer(ModelSerializer):
    branch = BranchSerializer()
    account = AccountSerializers()
    created_by = UserSerializer()
    
    class Meta:
        model = Cart
        fields = ("id","branch", "account", "card_number", "status", "created_at", "created_by")
        read_only_fields = ['id', "created_at", "updated_at", "created_by"]
        
        
class CartDetailSerializer(ModelSerializer):
    branch = BranchSerializer()
    account = AccountSerializers()
    created_by = UserSerializer()
    
    class Meta:
        model = Cart
        fields = '__all__'
        read_only_fields = ['id', "created_at", "updated_at", "created_by"]


class AccountCreateSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        read_only_fields = ['id', "created_at", "updated_at", "created_by"]
        
        
class AccountDetailSerializer(ModelSerializer):
    created_by = UserSerializer()    
    class Meta:
        model = Account
        fields = ("id", "username","account_code", "dep_number", "organization_code", "status", "created_at", "created_by")
        read_only_fields = ['id', "created_at", "updated_at", "created_by"]
        
        
class AccountListSerializer(ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = Account
        fields = '__all__'
        read_only_fields = ['id', "created_at", "updated_at", "created_by"]


class TransactionCreateSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ['id', "created_at", "updated_at", "created_by", "status", "system_message", "updated_status_by", "updated_status_at"]
        
    def validate(self, data):
        if data.get("transaction_type") == "charge" and data.get("amount") is None:
            raise serializers.ValidationError("Amount is required for charge transaction.")
        elif data.get("transaction_type") == "decharge" and data.get("amount") is not None:
            raise serializers.ValidationError("Amount is not allowed for decharge transaction.")
        return super().validate(data)



class TransactionDetailSerializer(ModelSerializer):
    cart = CartSerializers()
    created_by = UserSerializer()
    updated_status_by = UserSerializer()
    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ['id', "created_at", "updated_at", "created_by", "status", "system_message", "transaction_type", "updated_status_by", "updated_status_at"]
        extra_kwargs = {
            'cart': {'required' : False},
            'amount': {'required' : False},
            'transaction_type': {'required' : False},
            'status': {'required' : False},
        }



        
class TransactionListSerializer(ModelSerializer):
    cart = CartSerializers()
    created_by = UserSerializer()
    class Meta:
        model = Transaction
        fields = ("id", "cart", "created_by", "transaction_type", "amount", "status")
        read_only_fields = ['id', "created_at", "updated_at", "created_by", "updated_status_by", "updated_status_at"]
    
    
class CustomerDeleteSerializer(serializers.Serializer):
    ids =  serializers.ListField()
    
    
class EditStatusTransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('status', "updated_status_at")
        read_only_fields = ['id', "created_at", "updated_at", "created_by", "updated_status_by"]

        
        
class CloneAccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ("username", "account_code")
        

class CloneCartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ("card_number", )
        
        
        
        
class FinanceMangerTransactions(ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = ['id', "created_at", "updated_at", "created_by", "updated_status_by", "updated_status_at"]
        
        
class TransactionCartSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = ("id", "transaction_type", "amount", "status", "created_at")
        read_only_fields = ['id', "created_at", "updated_at", "created_by", "updated_status_by", "updated_status_at"]


class PaymentCreatedSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
        read_only_fields = ['id', "created_at", "updated_at", "created_by"]


class PaymentDetailSerializer(ModelSerializer):
    created_by = UserSerializer()
    payment_source = PaymentSourceSerializer()
    payment_Type = PaymentTypeSerializer()
    class Meta:
        model = Payment
        fields = "__all__"
        read_only_fields = ['id', "created_at", "updated_at", "created_by"]


class PaymentListSerializer(ModelSerializer):
    payment_source = PaymentSourceSerializer()
    payment_Type = PaymentTypeSerializer()
    class Meta:
        model = Payment
        fields = ("id", "swap_or_refound", "payment_source", "payment_Type", "created_at")
        read_only_fields = ['id', "created_at", "updated_at", "created_by"]


class PaymentReviewCreateSerializer(ModelSerializer):
    class Meta:
        model = PaymentReview
        fields = "__all__"
        read_only_fields = ['id', "created_at", "updated_at", "created_by"]


class PaymentReviewListSerializer(ModelSerializer):
    created_by = UserSerializer()
    payment = PaymentSerializer()
    class Meta:
        model = PaymentReview
        fields = ("id", "payment", "created_by", "created_at", "status")
        read_only_fields = ['id', "created_at", "updated_at", "created_by"]


class PaymentReviewDetailSerializer(ModelSerializer):
    created_by = UserSerializer()
    payment = PaymentSerializer()
    class Meta:
        model = PaymentReview
        fields = "__all__"
        read_only_fields = ['id', "created_at", "updated_at", "created_by"]



class ManagerApprovalCreateSerializer(ModelSerializer):
    class Meta:
        model = ManagerApproval
        fields = "__all__"
        read_only_fields = ['id', "created_at", "updated_at", "created_by"]


class ManagerApprovalDetailSerializer(ModelSerializer):
    created_by = UserSerializer()
    payment = PaymentSerializer()
    class Meta:
        model = ManagerApproval
        fields = "__all__"
        read_only_fields = ['id', "created_at", "updated_at", "created_by"]


class ManagerApprovallListSerializer(ModelSerializer):
    created_by = UserSerializer()
    payment = PaymentSerializer()
    class Meta:
        model = ManagerApproval
        fields = ("id", "payment", "created_by", "created_at", "status")
        read_only_fields = ['id', "created_at", "updated_at", "created_by"]


class FinalApproveCreatedSerializer(ModelSerializer):
    class Meta:
        model = FinalApprove
        fields = "__all__"
        read_only_fields = ['id', "created_at", "updated_at", "created_by"]



class FinalApproveDetailSerializer(ModelSerializer):
    created_by = UserSerializer()
    payment = PaymentSerializer()
    class Meta:
        model = FinalApprove
        fields = "__all__"
        read_only_fields = ['id', "created_at", "updated_at", "created_by"]


class FinalApproveListSerializer(ModelSerializer):
    created_by = UserSerializer()
    payment = PaymentSerializer()
    class Meta:
        model = FinalApprove
        fields = ("id", "payment", "created_by", "created_at", "status")
        read_only_fields = ['id', "created_at", "updated_at", "created_by"]


class ChequeCreatedSerializer(ModelSerializer):
    class Meta:
        model = Cheque
        fields = "__all__"
        read_only_fields = ['id', "created_at", "updated_at", "created_by"]


class ChequeListSerializer(ModelSerializer):
    created_by = UserSerializer()
    payment = PaymentSerializer()
    class Meta:
        model = Cheque
        fields = ("id", "payment", "created_by", "created_at", "status")
        read_only_fields = ['id', "created_at", "updated_at", "created_by"]


class ChequeDetailSerializer(ModelSerializer):
    created_by = UserSerializer()
    payment = PaymentSerializer()
    class Meta:
        model = Cheque
        fields = "__all__"
        read_only_fields = ['id', "created_at", "updated_at", "created_by"]
