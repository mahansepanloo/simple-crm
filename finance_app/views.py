from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, exceptions
from finance_app.models import Cart, Account, Transaction, Payment, PaymentReview, PaymentSource, ManagerApproval, Cheque, PaymentType, FinalApprove
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import UpdateAPIView
from finance_app.serializers import (
    CartCreateSerializer, CartDetailSerializer, CartListSerializer, AccountCreateSerializer, AccountDetailSerializer, 
    AccountListSerializer, TransactionCreateSerializer, TransactionDetailSerializer, TransactionListSerializer, CustomerDeleteSerializer,
    EditStatusTransactionSerializer, CloneAccountSerializer, CloneCartSerializer, FinanceMangerTransactions, TransactionSerializers,
    ChequeListSerializer, ChequeDetailSerializer, ChequeCreatedSerializer, FinalApproveListSerializer, FinalApproveDetailSerializer, FinalApproveCreatedSerializer,
    ManagerApprovallListSerializer, ManagerApprovalDetailSerializer, ManagerApprovalCreateSerializer, PaymentReviewDetailSerializer, PaymentCreatedSerializer,
    PaymentReviewListSerializer, PaymentReviewCreateSerializer, PaymentDetailSerializer, PaymentListSerializer)
from config.prototype import Prototype 
from config.importfile import HandleFile
from django.core.exceptions import ValidationError  
from django.utils import timezone  


class CartViewset(ModelViewSet):
    queryset = Cart.objects.all().order_by("-id")
    serializer_class = CartCreateSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["branch", "status", "account"]
    search_fields = ["card_number"]
    ordering_fields = ["created_at", "updated_at"]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
        
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        transactions = Transaction.objects.filter(cart=instance)
        transaction_serializer = TransactionSerializers(transactions, many=True)
        serializer = CartDetailSerializer(instance)
        response_data = serializer.data
        response_data['transactions'] = transaction_serializer.data
        return Response(response_data)

    def get_serializer_class(self):
        # Use different serializers for different actions
        if self.action == "list":
            return CartListSerializer
        return super().get_serializer_class()


class AccountsViewset(ModelViewSet):
    queryset = Account.objects.all().order_by("-id")
    serializer_class = AccountCreateSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["status"]
    search_fields = ["username", "account_code", "dep_number", "organization_code"]
    ordering_fields = ["created_at", "updated_at"]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
    def get_serializer_class(self):
        # Use different serializers for different actions
        if self.action == "list":
            return AccountListSerializer
        elif self.action == "retrieve":
            return AccountDetailSerializer
        return super().get_serializer_class()


class MultipleDeleteCartView(APIView):
    """
    A view for get list ids and deleting  cart.
    """

    serializer_class = CustomerDeleteSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *arg, **kwargs):
        ids = request.data.get('ids')    
        if not isinstance(ids, list):  
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)
        id_cart = Cart.objects.filter(id__in=ids)
        if id_cart.exists():
            id_cart.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"messages:not found cart"}, status=status.HTTP_400_BAD_REQUEST)


class MultipleDeleteAccountView(APIView):
    """
    A view for get list ids and deleting  accounts.
    """

    serializer_class = CustomerDeleteSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *arg, **kwargs):
        ids = request.data.get('ids')    
        if not isinstance(ids, list):  
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)
        id_cart = Account.objects.filter(id__in=ids)
        if id_cart.exists():
            id_cart.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"messages:not found account"}, status=status.HTTP_400_BAD_REQUEST
        )


class TransactionViewset(ModelViewSet):
    queryset = Transaction.objects.all().order_by("-id")
    serializer_class = TransactionCreateSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["status", "transaction_type", "cart"]
    search_fields = [ "cart__card_number", "system_message", "amount"]
    ordering_fields = ["created_at", "updated_at", "amount"]

    def get_serializer_class(self):
        
        if self.request.user.groups.filter(name="finance").exists():
            return FinanceMangerTransactions
        if self.action == "list":
            return TransactionListSerializer
        elif self.action == "retrieve":
            return TransactionDetailSerializer
        return super().get_serializer_class()


    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
        
    def perform_destroy(self, instance):
        if instance.status == 0 :
            instance.delete()
        else:
            raise exceptions.ValidationError(
                    {"status": "You can't delete status of this transaction"}
                )        
        
    
    def perform_update(self, serializer):  
        if serializer.instance.status == 0:  
            serializer.save()
        else:
            raise exceptions.ValidationError(
                    {"status": "You can't update status of this transaction"}
                )
        

class MultipleDeleteTransactionView(APIView):
    """
    A view for get list ids and deleting  transaction.
    """

    serializer_class = CustomerDeleteSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *arg, **kwargs):
        ids = request.data.get('ids')    
        if not isinstance(ids, list):  
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)
        id_cart = Transaction.objects.filter(id__in=ids)
        if id_cart.exists():
            id_cart.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"messages:not found transaction"}, status=status.HTTP_400_BAD_REQUEST
        )


class EditStatusTransactionView(UpdateAPIView):
    queryset = Transaction.objects.all().order_by("-id")
    serializer_class = EditStatusTransactionSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        if serializer.instance.status != 0:
            raise exceptions.ValidationError(
                {"status": "You can't update status of this transaction"}
            )
        obj = serializer.save(updated_status_by=self.request.user, updated_status_at=timezone.now())


class TransactionCloneView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        transactions = Transaction.objects.get(id = kwargs["pk"])
        new_transaction = Prototype(transactions)
        final = new_transaction.clone()
        final.created_by = request.user
        final.save()
        return Response("created transactions", status=status.HTTP_201_CREATED)
    
    
class AccountsCloneView(APIView):
    serializer_class = CloneAccountSerializer
    permission_classes = [IsAuthenticated]

    def post(self,request, *args, **kwargs):
        serilazers = CloneAccountSerializer(data = request.data)
        serilazers.is_valid(raise_exception=True)
        account = Account.objects.get(id=kwargs['pk'])
        new_account = Prototype(account)  
        final = new_account.clone(username=serilazers.validated_data.get("username"),
                          account_code=serilazers.validated_data.get("account_code"))
        final.save()
        return Response("created account", status=status.HTTP_201_CREATED)
    
    
class CartCloneView(APIView):
    serializer_class = CloneCartSerializer
    permission_classes = [IsAuthenticated]

    def post(self,request, *args, **kwargs):
        serilazers = CloneCartSerializer(data = request.data)
        serilazers.is_valid(raise_exception=True)
        cart = Cart.objects.get(id=kwargs['pk'])
        new_account = Prototype(cart)  
        final = new_account.clone(card_number=serilazers.validated_data.get("card_number"))
        final.save()
        return Response("created cart", status=status.HTTP_201_CREATED)

        
class ImportTransactionView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        files = request.FILES['file']  
        app_name = "finance_app"  
        model_name = "Transaction"  
        
        try:  
            a = HandleFile( files, app_name, model_name, request.user)
            a.handle()
            return Response("Successfully uploaded", status=status.HTTP_200_OK)  
        except ValidationError as e:  
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)  
        except Exception as e:  
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
        
        
class ImportCartView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        files = request.FILES['file']  
        app_name = "finance_app"  
        model_name = "Cart"  
        
        try:  
            a = HandleFile( files, app_name, model_name, request.user)
            a.handle()
            return Response("Successfully uploaded", status=status.HTTP_200_OK)  
        except ValidationError as e:  
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)  
        except Exception as e:  
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
 
 
class ImportAccountView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        files = request.FILES['file']  
        app_name = "finance_app"  
        model_name = "Account"  
        
        try:  
            a = HandleFile( files, app_name, model_name, request.user)
            a.handle()
            return Response("Successfully uploaded", status=status.HTTP_200_OK)  
        except ValidationError as e:  
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)  
        except Exception as e:  
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)    


class PaymentReviewViewSet(ModelViewSet):
    queryset = PaymentReview.objects.all().order_by("-id")
    serializer_class = PaymentReviewCreateSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["status"]
    ordering_fields = ["created_at", "updated_at", "status"]

    def get_serializer_class(self):
        if self.action == "list":
            return PaymentReviewListSerializer
        elif self.action == "retrieve":
            return PaymentReviewDetailSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        return super().perform_create(serializer)



class ManageApproveViewSet(ModelViewSet):
    queryset = ManagerApproval.objects.all().order_by("-id")
    serializer_class = ManagerApprovalCreateSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["status"]
    ordering_fields = ["created_at", "updated_at", "status"]

    def get_serializer_class(self, *args, **kwargs):
        if self.action == "list":
            return ManagerApprovallListSerializer
        elif self.action == "retrieve":
            return ManagerApprovalDetailSerializer
        return super().get_serializer_class()
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        return super().perform_create(serializer)
    

class ChequeViewSet(ModelViewSet):
    queryset = Cheque.objects.all().order_by("-id")
    serializer_class = ChequeCreatedSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["status"]
    ordering_fields = ["created_at", "updated_at", "status"]

    def get_serializer_class(self):
        if self.action == "list":
            return ChequeListSerializer
        elif self.action == "retrieve":
            return ChequeDetailSerializer
        return super().get_serializer_class()
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        return super().perform_create(serializer)
    

class FinalApproveViewSet(ModelViewSet):
    queryset = FinalApprove.objects.all().order_by("-id")
    serializer_class = FinalApproveCreatedSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["status"]
    ordering_fields = ["created_at", "updated_at", "status"]

    def get_serializer_class(self):
        if self.action == "list":
            return FinalApproveListSerializer
        elif self.action == "retrieve":
            return FinalApproveDetailSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        return super().perform_create(serializer)


class ImportPaymentREviewView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        files = request.FILES['file']
        app_name = "finance_app"
        model_name = "PaymentReview"

        try:
            a = HandleFile( files, app_name, model_name, request.user)
            a.handle()
            return Response("Successfully uploaded", status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class ImportManagerApprovalView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        files = request.FILES['file']
        app_name = "finance_app"
        model_name = "ManagerApproval"

        try:
            a = HandleFile( files, app_name, model_name, request.user)
            a.handle()
            return Response("Successfully uploaded", status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class ImportChequeView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        files = request.FILES['file']
        app_name = "finance_app"
        model_name = "Cheque"

        try:
            a = HandleFile( files, app_name, model_name, request.user)
            a.handle()
            return Response("Successfully uploaded", status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class ImportFinalApproveView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        files = request.FILES['file']
        app_name = "finance_app"
        model_name = "FinalApprove"

        try:
            a = HandleFile( files, app_name, model_name, request.user)
            a.handle()
            return Response("Successfully uploaded", status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        

class MultipleDeletePaymentReviewView(APIView):
    """
    A view for get list ids and deleting  transaction.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request, *arg, **kwargs):
        ids = request.data.get('ids')    
        if not isinstance(ids, list):  
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)
        id_cart = PaymentReview.objects.filter(id__in=ids)
        if id_cart.exists():
            id_cart.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"messages:not found payment review"}, status=status.HTTP_400_BAD_REQUEST
        )
    
class MultipleDeleteManagerApprovalView(APIView):
    """
    A view for get list ids and deleting  transaction.
    """
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        ids = request.data.get('ids')
        if not isinstance(ids, list):
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)
        id_cart = ManagerApproval.objects.filter(id__in=ids)
        if id_cart.exists():
            id_cart.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"messages:not found payment review"}, status=status.HTTP_400_BAD_REQUEST
        )
    
class MultipleDeleteChequeView(APIView):

    """
    A view for get list ids and deleting  transaction.
    """
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        ids = request.data.get('ids')
        if not isinstance(ids, list):
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)
        id_cart = Cheque.objects.filter(id__in=ids)
        if id_cart.exists():
            id_cart.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"messages:not found payment review"}, status=status.HTTP_400_BAD_REQUEST
        )
    

class MultipleDeleteFinalApproveView(APIView):

    """
    A view for get list ids and deleting  transaction.
    """
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        ids = request.data.get('ids')
        if not isinstance(ids, list):
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)
        id_cart = FinalApprove.objects.filter(id__in=ids)
        if id_cart.exists():
            id_cart.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"messages:not found payment review"}, status=status.HTTP_400_BAD_REQUEST
        )


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all().order_by("-id")
    serializer_class = PaymentCreatedSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = [ "swap_or_refound", "payment_source", "payment_Type", ]
    ordering_fields = ["created_at", "updated_at", "status", "final_amount"]

    def get_serializer_class(self):
        if self.action == "list":
            return PaymentListSerializer
        elif self.action == "retrieve":
            return PaymentDetailSerializer
        return super().get_serializer_class()
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        return super().perform_create(serializer)
    

class ImportPaymentView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        files = request.FILES['file']
        app_name = "finance_app"
        model_name = "Payment"
        try:
            a = HandleFile( files, app_name, model_name, request.user)
            a.handle()
            return Response("Successfully uploaded", status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        

class MultipleDeletePaymentView(APIView):
    """
    A view for get list ids and deleting  transaction.
    """
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        ids = request.data.get('ids')
        if not isinstance(ids, list):
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)
        id_cart = Payment.objects.filter(id__in=ids)
        if id_cart.exists():
            id_cart.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"messages:not found payment review"}, status=status.HTTP_400_BAD_REQUEST
        )


class PaymentCloneView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        transactions = Payment.objects.get(id = kwargs["pk"])
        new_transaction = Prototype(transactions)
        final = new_transaction.clone()
        final.created_by = request.user
        final.save()
        return Response("created transactions", status=status.HTTP_201_CREATED)