from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from setting_app.models import Brand, BrandSetting, Color, Employer, Guarantee, Swaptype, RefundType, PaymentType,PaymentSource
from setting_app.serializers import (BrandCreateSerializer, BrandDetailSerializer, BrandListSerializer, BrandSettingCreateSerializer, 
                                    BrandSettingListSerializer, EmployerCreateSerializer, EmployerDetailSerializer, EmployerListSerializer,
                                    GuaranteeCreateSerializer, GuaranteeDetailSerializer, GuaranteeListSerializer, SwaptypeCreateSerializer,
                                    SwaptypeDetailSerializer, SwaptypeListSerializer,BrandSettingDetailSerializer,
                                    ColorCreateSerializer, ColorDetailSerializer, ColorListSerializer, CloneBrandSerializer, CloneBrandSettingSerializer
                                    ,CloneColorSerializer, CloneEmployerSerializer, CloneGuaranteeSerializer, CloneSwaptypeSerializer, RefundCreateSerializer,
                                    RefundDetailSerializer, RefundListSerializer, PeymentTypeListSerializer, PeymentTypeDetailSerializer, PaymentTypeCreateSerializers,
                                    MultipleDeleteSerializer, PaymentSourceCreateSerializer, PaymentSourceListSerializer, PaymentSourceDetailSerializer,
                                    )
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from config.prototype import Prototype
from config.importfile import HandleFile
from django.core.exceptions import ValidationError  



class BrandViewSet(ModelViewSet):

    queryset = Brand.objects.all().order_by("-id")
    permission_classes = [IsAuthenticated]
    serializer_class = BrandCreateSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["created_at"]
    search_fields = ["name"]

    def get_serializer_class(self):
        # Use different serializers for different actions
        if self.action == "list":
            return BrandListSerializer
        elif self.action == "retrieve":
            return BrandDetailSerializer
        return super().get_serializer_class()


    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class BrandSettingViewSet(ModelViewSet):
    queryset = BrandSetting.objects.all().order_by("-id")
    permission_classes = [IsAuthenticated]
    serializer_class = BrandSettingCreateSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["created_at"]
    search_fields = ["title"]
    filterset_fields = ["brand"]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_serializer_class(self):
        # Use different serializers for different actions
        if self.action == "list":
            return BrandSettingListSerializer
        elif self.action == "retrieve":
            return BrandSettingDetailSerializer
        return super().get_serializer_class()


class ColorViewSet(ModelViewSet):
    queryset = Color.objects.all().order_by("-id")
    permission_classes = [IsAuthenticated]
    serializer_class = ColorCreateSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["created_at"]
    search_fields = ["name"]

    def get_serializer_class(self):
        # Use different serializers for different actions
        if self.action == "list":
            return ColorListSerializer
        elif self.action == "retrieve":
            return ColorDetailSerializer
        return super().get_serializer_class()


    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    
class EmployerViewSet(ModelViewSet):
    queryset = Employer.objects.all().order_by("-id")
    permission_classes = [IsAuthenticated]
    serializer_class = EmployerCreateSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["created_at", "start_date", "end_date"]
    search_fields = ["name","brand__name", "marketing_employer", "factory_employer","imei"]
    filterset_fields = ["brand"]


    def get_serializer_class(self):
        # Use different serializers for different actions
        if self.action == "list":
            return EmployerDetailSerializer
        elif self.action == "retrieve":
            return EmployerListSerializer
        return super().get_serializer_class()
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class GuaranteeViewSet(ModelViewSet):
    queryset = Guarantee.objects.all().order_by("-id")
    permission_classes = [IsAuthenticated]
    serializer_class = GuaranteeCreateSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["created_at"]
    search_fields = ["title"]
    
    def get_serializer_class(self):
        # Use different serializers for different actions
        if self.action == "list":
            return GuaranteeListSerializer
        elif self.action == "retrieve":
            return GuaranteeDetailSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class SwaptypeViewSet(ModelViewSet):
    queryset = Swaptype.objects.all().order_by("-id")
    serializer_class = SwaptypeCreateSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["created_at"]
    search_fields = ["title"]
    
    def get_serializer_class(self):
        # Use different serializers for different actions
        if self.action == "list":
            return SwaptypeListSerializer
        elif self.action == "retrieve":
            return SwaptypeDetailSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class MultipleDeleteBrand(APIView):
    """  
    A view for get list ids and deleting  Brand.  
    """  
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        ids = request.data.get('ids')    
        if not isinstance(ids, list):  
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)
        id_brand = Brand.objects.filter(id__in=ids)
        if id_brand.exists():
            id_brand.delete()
            return Response({"message": "Brand deleted successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Brand not found."}, status=status.HTTP_404_NOT_FOUND)
 
 
class MultipleDeleteBrandSetting(APIView):
    """  
    A view for get list ids and deleting  Brandsetting.  
    """  
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        ids = request.data.get('ids')    
        if not isinstance(ids, list):  
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)
        id_brandsetting = BrandSetting.objects.filter(id__in=ids)
        if id_brandsetting.exists():
            id_brandsetting.delete()
            return Response({"message": "BrandSetting deleted successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "BrandSetting not found."}, status=status.HTTP_404_NOT_FOUND)
        

class MultipleDeleteColor(APIView):
    """  
    A view for get list ids and deleting  Color.  
    """  
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        ids = request.data.get('ids')    
        if not isinstance(ids, list):  
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)
        id_color = Color.objects.filter(id__in=ids)
        if id_color.exists():
            id_color.delete()
            return Response({"message": "Color deleted successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Color not found."}, status=status.HTTP_404_NOT_FOUND)
        
        
class MultipleDeleteEmployer(APIView):
    permission_classes = [IsAuthenticated]

    """    A view for get list ids and deleting  employer.  
"""

    def post(self, request, *args, **kwargs):
        ids = request.data.get('ids')    
        if not isinstance(ids, list):  
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)    
        id_employer = Employer.objects.filter(id__in=ids)
        if id_employer.exists():
            id_employer.delete()
            return Response({"message": "Employer deleted successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Employer not found."}, status=status.HTTP_404_NOT_FOUND)
  
        
class MultipleDeleteGuarantee(APIView):
    """    A view for get list ids and deleting  Guarantee.  
"""
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        ids = request.data.get('ids')    
        if not isinstance(ids, list):  
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)
        id_guarantee = Guarantee.objects.filter(id__in=ids)
        if id_guarantee.exists():
            id_guarantee.delete()
            return Response({"message": "Guarantee deleted successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Guarantee not found."}, status=status.HTTP_404_NOT_FOUND)


class MultipleDeleteSwaptype(APIView):
    permission_classes = [IsAuthenticated]
    """   
          A view for get list ids and deleting  swaptype.  
    """

    def post(self, request, *args, **kwargs):
        ids = request.data.get('ids')    
        if not isinstance(ids, list):  
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)
        id_swaptype = Swaptype.objects.filter(id__in=ids)
        if id_swaptype.exists():
            id_swaptype.delete()
            return Response({"message": "Swaptype deleted successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Swaptype not found."}, status=status.HTTP_404_NOT_FOUND)


class BrandCloneView(APIView):
    serializer_class = CloneBrandSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = CloneBrandSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        brand = Brand.objects.get(id=kwargs['pk'])
        new_brand = Prototype(brand)
        final = new_brand.clone(name=serializer.validated_data.get("name")) 
        final.created_by = request.user        
        final.save()
        return Response("created brand", status=status.HTTP_201_CREATED)
    
    
class BrandSettingCloneView(APIView):
    serializer_class = CloneBrandSettingSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        serializer = CloneBrandSettingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        brand_setting = BrandSetting.objects.get(id=kwargs['pk'])
        new_brand_setting = Prototype(brand_setting)
        final = new_brand_setting.clone(title=serializer.validated_data.get("title"))
        final.created_by = request.user
        final.save()
        return Response("created brand setting", status=status.HTTP_201_CREATED)
    

class ColorCloneView(APIView):
    serializer_class = CloneColorSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = CloneColorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        color = Color.objects.get(id=kwargs['pk'])
        new_color = Prototype(color)
        final = new_color.clone(name=serializer.validated_data.get("name"))
        final.created_by = request.user
        final.save()
        return Response("created color", status=status.HTTP_201_CREATED)
    

class EmployerCloneView(APIView):
    serializer_class = CloneEmployerSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        serializer = CloneEmployerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        employer = Employer.objects.get(id=kwargs['pk'])
        new_employer = Prototype(employer)
        final = new_employer.clone(imei=serializer.validated_data.get("imei"))
        final.created_by = request.user
        final.save()
        return Response("created employer", status=status.HTTP_201_CREATED)
    
    
class GuaranteeCloneView(APIView):
    serializer_class = CloneGuaranteeSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = CloneGuaranteeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        guarantee = Guarantee.objects.get(id=kwargs['pk'])
        new_guarantee = Prototype(guarantee)
        final = new_guarantee.clone(title=serializer.validated_data.get("title"))
        final.created_by = request.user
        final.save()
        return Response("created guarantee", status=status.HTTP_201_CREATED)
    
    
class SwaptypeCloneView(APIView):
    serializer_class = CloneSwaptypeSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        serializer = CloneSwaptypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        swaptype = Swaptype.objects.get(id=kwargs['pk'])
        new_swaptype = Prototype(swaptype)
        final = new_swaptype.clone(title=serializer.validated_data.get("title"))
        final.created_by = request.user
        final.save()
        return Response("created swaptype", status=status.HTTP_201_CREATED)


class ImportBrandView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        files = request.FILES['file']  
        app_name = "setting_app"  
        model_name = "Brand"  
        
        try:  
            a = HandleFile( files, app_name, model_name, request.user)
            a.handle()
            return Response("Successfully uploaded", status=status.HTTP_200_OK)  
        except ValidationError as e:  
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)  
        except Exception as e:  
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)    


class ImportBrandSettingView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        files = request.FILES['file']  
        app_name = "setting_app"  
        model_name = "BrandSetting"  
        
        try:  
            a = HandleFile( files, app_name, model_name, request.user)
            a.handle()
            return Response("Successfully uploaded", status=status.HTTP_200_OK)  
        except ValidationError as e:  
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)  
        except Exception as e:  
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class ImportColorView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        files = request.FILES['file']  
        app_name = "setting_app"  
        model_name = "Color"  
        
        try:  
            a = HandleFile( files, app_name, model_name, request.user)
            a.handle()
            return Response("Successfully uploaded", status=status.HTTP_200_OK)  
        except ValidationError as e:  
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)  
        except Exception as e:  
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)  


class ImportEmployerView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        files = request.FILES['file']  
        app_name = "setting_app"  
        model_name = "Employer"  
        
        try:  
            a = HandleFile( files, app_name, model_name, request.user)
            a.handle()
            return Response("Successfully uploaded", status=status.HTTP_200_OK)  
        except ValidationError as e:  
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)  
        except Exception as e:  
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)      
        
        
class ImportGuaranteeView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        files = request.FILES['file']  
        app_name = "setting_app"  
        model_name = "Guarantee"  
        
        try:  
            a = HandleFile( files, app_name, model_name, request.user)
            a.handle()
            return Response("Successfully uploaded", status=status.HTTP_200_OK)  
        except ValidationError as e:  
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)  
        except Exception as e:  
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR) 


class ImportSwaptypeView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        files = request.FILES['file']  
        app_name = "setting_app"  
        model_name = "Swaptype"  
        
        try:  
            a = HandleFile( files, app_name, model_name, request.user)
            a.handle()
            return Response("Successfully uploaded", status=status.HTTP_200_OK)  
        except ValidationError as e:  
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)  
        except Exception as e:  
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
        
        

class RefundTypeViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = RefundType.objects.all().order_by("-id")
    serializer_class =  RefundCreateSerializer
    search_fields = ["title"]
    ordering_fields = ["created_at"]
    
    
    def get_serializer_class(self):
        # Use different serializers for different actions
        if self.action == "list":
            return RefundListSerializer
        elif self.action == "retrieve":
            return RefundDetailSerializer
        return super().get_serializer_class()  
 
        
        
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        return super().perform_create(serializer)
    

class ImportRefundTypeView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        files = request.FILES['file']
        app_name = "setting_app"
        model_name = "RefundType"
        try:
            a = HandleFile(files, app_name, model_name, request.user)
            a.handle()
            return Response("Successfully uploaded", status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class MultipleDeleteRefundType(APIView):
    """
    A view for get list ids and deleting  case.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = MultipleDeleteSerializer
    def post(self, request, *args, **kwargs):
        ids = request.data.get('ids')
        if not isinstance(ids, list):
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)
        list_device = RefundType.objects.filter(id__in=ids)
        if list_device.exists():
            list_device.delete()
            return Response({"message": "Deleted successfully"}, status=status.HTTP_200_OK)
        return Response({"detail": "No refund type found for the provided IDs."}, status=status.HTTP_404_NOT_FOUND)

class CloneRefundTypeView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        refund_type = RefundType.objects.get(id=kwargs['pk'])
        refund_type = Prototype(refund_type)
        final = refund_type.clone()
        final.save()
        return Response("created refund type", status=status.HTTP_201_CREATED)
    
    
    
    

class PaymentTypeViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PaymentType.objects.all().order_by("-id")
    serializer_class = PaymentTypeCreateSerializers
    search_fields = ["title"]
    ordering_fields = ["created_at"]


    def get_serializer_class(self):
        # Use different serializers for different actions
        if self.action == "list":
            return PeymentTypeListSerializer
        elif self.action == "retrieve":
            return PeymentTypeDetailSerializer
        return super().get_serializer_class()  



    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        return super().perform_create(serializer)
    

class ClonePaymentTypeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        payment_type = PaymentType.objects.get(id=kwargs['pk'])
        payment_type = Prototype(payment_type)
        final = payment_type.clone()
        final.save()
        return Response("created payment type", status=status.HTTP_201_CREATED)
    

class ImportPaymentTypeView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        files = request.FILES['file']
        app_name = "setting_app"
        model_name = "PaymentType"
        try:
            a = HandleFile(files, app_name, model_name, request.user)
            a.handle()
            return Response("Successfully uploaded", status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
        
class MultipleDeletePaymentType(APIView):
    """
    A view for get list ids and deleting  case.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = MultipleDeleteSerializer
    
    def post(self, request, *args, **kwargs):
        ids = request.data.get('ids')
        if not isinstance(ids, list):
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)
        list_device = PaymentType.objects.filter(id__in=ids)
        if list_device.exists():
            list_device.delete()
            return Response({"message": "Deleted successfully"}, status=status.HTTP_200_OK)
        return Response({"detail": "No payment type found for the provided IDs."}, status=status.HTTP_404_NOT_FOUND)


class PaymentSourceViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PaymentSource.objects.all().order_by("-id")
    serializer_class = PaymentSourceCreateSerializer
    search_fields = ["title"]
    ordering_fields = ["created_at"]

    def get_serializer_class(self):
        # Use different serializers for different actions
        if self.action == "list":
            return PaymentSourceListSerializer
        elif self.action == "retrieve":
            return PaymentSourceDetailSerializer
        return super().get_serializer_class()
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        return super().perform_create(serializer)


class ImportPaymentSourceView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        files = request.FILES['file']
        app_name = "setting_app"
        model_name = "PaymentSource"
        try:
            a = HandleFile(files, app_name, model_name, request.user)
            a.handle()
            return Response("Successfully uploaded", status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)


class MultipleDeletePaymentSource(APIView):
    """
    A view for get list ids and deleting  case.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = MultipleDeleteSerializer

    def post(self, request, *args, **kwargs):
        ids = request.data.get('ids')
        if not isinstance(ids, list):
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)
        list_device = PaymentSource.objects.filter(id__in=ids)
        if list_device.exists():
            list_device.delete()
            return Response({"message": "Deleted successfully"}, status=status.HTTP_200_OK)
        return Response({"detail": "No payment source found for the provided IDs."}, status=status.HTTP_404_NOT_FOUND)