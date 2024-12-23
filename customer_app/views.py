from rest_framework.permissions import IsAuthenticated 
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from customer_app.models import Customer
from customer_app.serializers import (CustomerCreateSerializer,
                                      CustomerDetailSerializer,
                                      CustomerListSerializer,
                                      CustomerDeleteSerializer,CloneCustomerSerializer)
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from config.prototype import Prototype 
from config.importfile import HandleFile
from django.core.exceptions import ValidationError  


class CustomerViewSet( ModelViewSet):
    """
    A viewset for viewing and editing customer instances.

    retrieve:
    Return the given customer.

    list:
    Return a list of all the existing customers.

    create:
    Create a new customer instance.

    update:
    Update an existing customer instance.

    partial_update:
    Partially update an existing customer instance.

    destroy:
    Delete an existing customer instance.
    """

    queryset = Customer.objects.all().order_by("-id")
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerCreateSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["created_at"]
    search_fields = ["full_name", "account_name"]
    filterset_fields = ["gender"]
    

    def get_serializer_class(self):
        # Use different serializers for different actions
        if self.action == "list":
            return CustomerListSerializer
        elif self.action == "retrieve":
            return CustomerDetailSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        # Save the created_by field with the current user
        serializer.save(created_by=self.request.user)


class DeleteMultipleCustomersView(APIView):  
    """  
    A view for get list ids and deleting  customers.  
    """  
    permission_classes = [IsAuthenticated]  
    serializer_class = CustomerDeleteSerializer  

    def post(self, request, *args, **kwargs):  
        ids = request.data.get('ids')    
        if not isinstance(ids, list):  
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)
        deleted_count= Customer.objects.filter(id__in=ids)
        if deleted_count.exists():
            deleted_count.delete()  
            return Response({"detail": f"{deleted_count} customers deleted successfully."},status=status.HTTP_204_NO_CONTENT)    
        return Response({"detail": "No customers found for the provided IDs."}, status=status.HTTP_404_NOT_FOUND) 
    
    
class CloneCustomerView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        serilazers = CloneCustomerSerializer(data=request.data)
        serilazers.is_valid(raise_exception=True)
        customer = Customer.objects.get(id=kwargs['id'])       
        prototype = Prototype(customer)  
        new_customer = prototype.clone(  
            accounting_code=serilazers.validated_data.get("accounting_code"),  
            full_name=serilazers.validated_data.get("full_name"),  
        )  
        new_customer.created_by = request.user
        new_customer.save()
        return Response('Customer created successfully', status=status.HTTP_201_CREATED)

        
class ImportCustomerView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        files = request.FILES['file']  
        app_name = "customer_app"  
        model_name = "Customer"  
        
        try:  
            a = HandleFile( files, app_name, model_name, request.user)
            a.handle()
            return Response("Successfully uploaded", status=status.HTTP_200_OK)  
        except ValidationError as e:  
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)  
        except Exception as e:  
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)