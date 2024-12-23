from rest_framework.viewsets import ModelViewSet
from service_app.models import Agents, DevicePrice, Device, Case, CaseApprove, CaseReceive, CaseSend, CaseSupervisorApprove, Note, Swap
from rest_framework.permissions import IsAuthenticated
from service_app.serializers import (
                                    AgentDetailSerializer, AgentListSerializer, AgentsCreateSerializer, DeviceCreatePriceSerializer,
                                    DeviceListPriceSerializer, DeviceDetailPriceSerializer,  
                                    DeviceCreateSerializer, DeviceDEtailSerializer, DeviceListSerializer, MultipleDeleteSerializer,
                                    CaseCreateSerializer, CaseListSerializer, CaseDetailSerializer, 
                                    CaseApproveCreateSerializer, CaseApproveDetailSerializer, CaseApproveListSerializer,
                                    CaseReceiveCreateSerializer, CaseReceiveDetailSerializer, CaseReceiveListSerializer,
                                    CaseSendCreateSerializer, CaseSendDetailSerializer, CaseSendListSerializer,
                                    CaseSupervisorDetailSerializer, CaseSupervisorCreateSerializer, CaseSupervisorListSerializer,
                                    CloneAgentsSerializers, CloneDeviceSerializer, CloneDevicePriceSerializer,
                                    CloneCaseSerializer, NoteCreateSerializer, NoteListSerializer, NoteDetailSerializer,    
                                    SwapCreateSerializer, SwapDetailSerializer, SwapListSerializer, AprrovedCompletedSerializer, AprrovedSawSerializer
                                    )

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from config.prototype import Prototype
from config.importfile import HandleFile
from django.core.exceptions import ValidationError  
from rest_framework.generics import UpdateAPIView
from django.utils import timezone  




class AgentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Agents.objects.all().order_by("-id")
    serializer_class = AgentsCreateSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["status"]
    search_fields = ["full_name", "business_number", "title"]
    filterset_fields = ["agent_type", "city"]


    def get_serializer_class(self):
        # Use different serializers for different actions
        if self.action == "list":
            return AgentListSerializer
        elif self.action == "retrieve":
            return AgentDetailSerializer
        return super().get_serializer_class()
        

class DevicePriceViewSet(ModelViewSet):
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["inter_price", "microtel_price", "memory"]
    search_fields = ["model_code", "factory_model" , "commercial_model", "memory", "microtel_price", "inter_price"]
    filterset_fields = ["color", "inter_price", "microtel_price", "memory"]
    permission_classes = [IsAuthenticated]
    queryset = DevicePrice.objects.all().order_by("-id")
    serializer_class = DeviceCreatePriceSerializer
    

    def get_serializer_class(self):
        # Use different serializers for different actions
        if self.action == "list":
            return DeviceListPriceSerializer
        elif self.action == "retrieve":
            return DeviceDetailPriceSerializer
        return super().get_serializer_class()


class DeviceViewSet(ModelViewSet):
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["created_by", "brand_model", "model_name", "serial_number", "purchase_date"]
    search_fields = [ "model_name", "serial_number", "imei", "brand_code", "commercial_model", "serial_number",]
    filterset_fields = ["brand", "color", "guarantee", "brand_model", "memory"]
    permission_classes = [IsAuthenticated]
    queryset = Device.objects.all().order_by("-id")
    serializer_class = DeviceCreateSerializer
    
    def get_serializer_class(self):
        # Use different serializers for different actions
        if self.action == "list":
            return DeviceListSerializer
        elif self.action == "retrieve":
            return DeviceDEtailSerializer
        return super().get_serializer_class()


    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class MultipleDeleteAgents(APIView):
    """  
    A view for get list ids and deleting  agent.  
    """  
    permission_classes = [IsAuthenticated]
    serializer_class = MultipleDeleteSerializer

    def post(self, request, *args, **kwargs):
        ids = request.data.get('ids')    
        if not isinstance(ids, list):  
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)
        list_agent = Agents.objects.filter(id__in=ids)
        if list_agent.exists():
            list_agent.delete()
            return Response({"message": "Deleted successfully"}, status=status.HTTP_200_OK)
        return Response({"detail": "No agents found for the provided IDs."}, status=status.HTTP_404_NOT_FOUND) 
    
    
class MultipleDeleteDevice(APIView):
    """  
    A view for get list ids and deleting  device.  
    """  
    permission_classes = [IsAuthenticated]
    serializer_class = MultipleDeleteSerializer

    def post(self, request, *args, **kwargs):
        ids = request.data.get('ids')    
        if not isinstance(ids, list):  
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)
        list_device = Device.objects.filter(id__in=ids)
        if list_device.exists():
            list_device.delete()
            return Response({"message": "Deleted successfully"}, status=status.HTTP_200_OK)
        return Response({"detail": "No devices found for the provided IDs."}, status=status.HTTP_404_NOT_FOUND)
    

class MultipleDeleteDevicePrice(APIView):
    """  
    A view for get list ids and deleting  devicePrice.  
    """  
    permission_classes = [IsAuthenticated]
    serializer_class = MultipleDeleteSerializer

    def post(self, request, *args, **kwargs):
        ids = request.data.get('ids')    
        if not isinstance(ids, list):  
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)
        list_device = DevicePrice.objects.filter(id__in=ids)
        if list_device.exists():
            list_device.delete()
            return Response({"message": "Deleted successfully"}, status=status.HTTP_200_OK)
        return Response({"detail": "No DevicePrice found for the provided IDs."}, status=status.HTTP_404_NOT_FOUND)


class CaseViewSet(ModelViewSet):
    serializer_class = CaseCreateSerializer
    queryset = Case.objects.all().order_by("-id")
    # permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["created_at","updated_at","invoice_amount", "invoice_date", ]
    search_fields = ["job_number", "customer_statement"]
    filterset_fields = ["jobtype", "customer", "branch", "device", "swaptype"]
    
    def get_serializer_class(self):
        # Use different serializers for different actions
        if self.action == "list":
            return CaseListSerializer
        elif self.action == "retrieve":
            return CaseDetailSerializer
        return super().get_serializer_class()    


    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class MultipleDeleteCase(APIView):
    """  
    A view for get list ids and deleting  case.  
    """  
    permission_classes = [IsAuthenticated]
    serializer_class = MultipleDeleteSerializer

    def post(self, request, *args, **kwargs):
        ids = request.data.get('ids')    
        if not isinstance(ids, list):  
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)
        list_device = Case.objects.filter(id__in=ids)
        if list_device.exists():
            list_device.delete()
            return Response({"message": "Deleted successfully"}, status=status.HTTP_200_OK)
        return Response({"detail": "No case found for the provided IDs."}, status=status.HTTP_404_NOT_FOUND)
    
    
class DevicePriceCloneView(APIView):
    serializer_class = CloneDevicePriceSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = CloneDevicePriceSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        deviceprice = DevicePrice.objects.get(id=kwargs['pk'])
        new_deviceprice = Prototype(deviceprice)
        final = new_deviceprice.clone(model_code=serializer.validated_data.get("model_code")) 
        final.save()
        return Response("created DevicePrice", status=status.HTTP_201_CREATED)
    
    
class DeviceCloneView(APIView):
    serializer_class = CloneDeviceSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = CloneDeviceSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        device = Device.objects.get(id=kwargs['pk'])
        new_device = Prototype(device)
        final = new_device.clone(imei=serializer.validated_data.get("imei")) 
        final.created_by = request.user        
        final.save()
        return Response("created Device", status=status.HTTP_201_CREATED)
    
    
class AgentsCloneView(APIView):
    serializer_class = CloneAgentsSerializers
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = CloneAgentsSerializers(data = request.data)
        serializer.is_valid(raise_exception=True)
        agents = Agents.objects.get(id=kwargs['pk'])
        new_agents = Prototype(agents)
        final = new_agents.clone(business_number=serializer.validated_data.get("business_number")) 
        final.save()
        return Response("created agents", status=status.HTTP_201_CREATED)
    
    
class CaseCloneView(APIView):
    serializer_class = CloneCaseSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = CloneCaseSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        case = Case.objects.get(id=kwargs['pk'])
        new_case = Prototype(case)
        final = new_case.clone(job_number=serializer.validated_data.get("job_number")) 
        final.created_by = request.user
        final.save()
        return Response("created case", status=status.HTTP_201_CREATED)
    
    
 
class ImportDevicePriceView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        files = request.FILES['file']  
        app_name = "service_app"  
        model_name = "DevicePrice"  
        
        try:  
            a = HandleFile( files, app_name, model_name, request.user)
            a.handle()
            return Response("Successfully uploaded", status=status.HTTP_200_OK)  
        except ValidationError as e:  
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)  
        except Exception as e:  
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
        
        
class ImportAgentsView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        files = request.FILES['file']  
        app_name = "service_app"  
        model_name = "Agents"  
        
        try:  
            a = HandleFile(files, app_name, model_name, request.user)
            a.handle()
            return Response("Successfully uploaded", status=status.HTTP_200_OK)  
        except ValidationError as e:  
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)  
        except Exception as e:  
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
 
 
class ImportDeviceView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        files = request.FILES['file']  
        app_name = "service_app"  
        model_name = "Device"  
        
        try:  
            a = HandleFile(files, app_name, model_name, request.user)
            a.handle()
            return Response("Successfully uploaded", status=status.HTTP_200_OK)  
        except ValidationError as e:  
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)  
        except Exception as e:  
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)    


 
class ImportCaseView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        files = request.FILES['file']  
        app_name = "service_app"  
        model_name = "Case"  
        
        try:  
            a = HandleFile(files, app_name, model_name, request.user)
            a.handle()
            return Response("Successfully uploaded", status=status.HTTP_200_OK)  
        except ValidationError as e:  
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)  
        except Exception as e:  
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
        

class CaseApproveViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = CaseApprove.objects.all().order_by("-id")
    serializer_class = CaseApproveCreateSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["status", "date", "created_at"]
    search_fields = ['case']
    filterset_fields = ["status", "case"]


    def get_serializer_class(self):
        if self.action == "list":
            return CaseApproveListSerializer
        elif self.action == "retrieve":
            return CaseApproveDetailSerializer
        return super().get_serializer_class()
    
    
class CaseSupervisorApproveViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = CaseSupervisorApprove.objects.all().order_by("-id")
    serializer_class = CaseSupervisorCreateSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["status", "date", "created_at"]
    search_fields = ['case']
    filterset_fields = ["status", "case"]


    def get_serializer_class(self):
        if self.action == "list":
            return CaseSupervisorListSerializer
        elif self.action == "retrieve":
            return CaseSupervisorDetailSerializer
        return super().get_serializer_class()
    

class CaseSendViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = CaseSend.objects.all().order_by("-id")
    serializer_class = CaseSendCreateSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["status", "date", "created_at"]
    search_fields = ['case']
    filterset_fields = ["status", "case"]


    def get_serializer_class(self):
        if self.action == "list":
            return CaseSendListSerializer
        elif self.action == "retrieve":
            return CaseSendDetailSerializer
        return super().get_serializer_class()
    

class CaseReceiveViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = CaseReceive.objects.all().order_by("-id")
    serializer_class = CaseReceiveCreateSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["status", "date", "created_at"]
    search_fields = ['case']
    filterset_fields = ["status", "case"]
    
    
    def get_serializer_class(self):
        if self.action == "list":
            return CaseReceiveListSerializer
        elif self.action == "retrieve":
            return CaseReceiveDetailSerializer
        return super().get_serializer_class()
    

class ImportCaseApproveView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        files = request.FILES['file']  
        app_name = "service_app"  
        model_name = "CaseApprove"  
        
        try:  
            a = HandleFile(files, app_name, model_name, request.user)
            a.handle()
            return Response("Successfully uploaded", status=status.HTTP_200_OK)  
        except ValidationError as e:  
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)  
        except Exception as e:  
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)   
        
        
class ImportCaseSupervisorApproveView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        files = request.FILES['file']
        app_name = "service_app"
        model_name = "CaseSupervisorApprove"

        try:
            a = HandleFile(files, app_name, model_name, request.user)
            a.handle()
            return Response("Successfully uploaded", status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class ImportCaseSendView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        files = request.FILES['file']
        app_name = "service_app"
        model_name = "CaseSend"
        try:
            a = HandleFile(files, app_name, model_name, request.user)
            a.handle()
            return Response("Successfully uploaded", status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ImportCaseReceiveView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        files = request.FILES['file']
        app_name = "service_app"
        model_name = "CaseReceive"

        try:
            a = HandleFile(files, app_name, model_name, request.user)
            a.handle()
            return Response("Successfully uploaded", status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class MultipleDeleteCaseApprove(APIView):
    """  
    A view for get list ids and deleting  case.  
    """  
    permission_classes = [IsAuthenticated]
    serializer_class = MultipleDeleteSerializer

    def post(self, request, *args, **kwargs):
        ids = request.data.get('ids')    
        if not isinstance(ids, list):  
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)
        list_device = CaseApprove.objects.filter(id__in=ids)
        if list_device.exists():
            list_device.delete()
            return Response({"message": "Deleted successfully"}, status=status.HTTP_200_OK)
        return Response({"detail": "No caseApprove found for the provided IDs."}, status=status.HTTP_404_NOT_FOUND)
 
 
class MultipleDeleteCaseSend(APIView):
    """  
    A view for get list ids and deleting  case.  
    """  
    permission_classes = [IsAuthenticated]
    serializer_class = MultipleDeleteSerializer

    def post(self, request, *args, **kwargs):
        ids = request.data.get('ids')    
        if not isinstance(ids, list):  
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)
        list_device = CaseSend.objects.filter(id__in=ids)
        if list_device.exists():
            list_device.delete()
            return Response({"message": "Deleted successfully"}, status=status.HTTP_200_OK)
        return Response({"detail": "No CaseSend found for the provided IDs."}, status=status.HTTP_404_NOT_FOUND)
    
class MultipleDeleteCaseReceive(APIView):
    """
    A view for get list ids and deleting  case.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = MultipleDeleteSerializer
    
    def post(self, request, *args, **kwargs):
        ids = request.data.get('ids')
        if not isinstance(ids, list):
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)
        list_device = CaseReceive.objects.filter(id__in=ids)
        if list_device.exists():
            list_device.delete()
            return Response({"message": "Deleted successfully"}, status=status.HTTP_200_OK)
        return Response({"detail": "No CaseReceive found for the provided IDs."}, status=status.HTTP_404_NOT_FOUND)


class MultipleDeleteCaseSupervisorApprove(APIView):
    """
    A view for get list ids and deleting  case.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = MultipleDeleteSerializer

    def post(self, request, *args, **kwargs):
        ids = request.data.get('ids')
        if not isinstance(ids, list):
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)
        list_device = CaseSupervisorApprove.objects.filter(id__in=ids)
        if list_device.exists():
            list_device.delete()
            return Response({"message": "Deleted successfully"}, status=status.HTTP_200_OK)
        return Response({"detail": "No CaseSupervisorApprove found for the provided IDs."}, status=status.HTTP_404_NOT_FOUND)


class NoteViewSet(ModelViewSet):
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["created_at"]
    permission_classes = [IsAuthenticated]
    queryset = Note.objects.all().order_by("-id")
    serializer_class = NoteCreateSerializer
    
    def get_serializer_class(self):
        # Use different serializers for different actions
        if self.action == "list":
            return NoteListSerializer
        elif self.action == "retrieve":
            return NoteDetailSerializer
        return super().get_serializer_class()  
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        return super().perform_create(serializer)
 

class NoteCloneView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        note = Note.objects.get(id=kwargs['pk'])
        note = Prototype(note)
        final = note.clone() 
        final.save()
        return Response("created note", status=status.HTTP_201_CREATED)


class MultipleDeleteNote(APIView):
    """
    A view for get list ids and deleting  case.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = MultipleDeleteSerializer
    
    def post(self, request, *args, **kwargs):
        ids = request.data.get('ids')
        if not isinstance(ids, list):
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)
        list_device = Note.objects.filter(id__in=ids)
        if list_device.exists():
            list_device.delete()
            return Response({"message": "Deleted successfully"}, status=status.HTTP_200_OK)
        return Response({"detail": "No note found for the provided IDs."}, status=status.HTTP_404_NOT_FOUND)
    
    
from django.http.response import HttpResponse  
class DownloadNote(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):    
        try:
            note = Note.objects.get(id=kwargs["pk"])
        except Note.DoesNotExist:
            return Response({"detail": "Note not found"}, status=status.HTTP_404_NOT_FOUND)
        file_path = note.attachment.path
        file = open(file_path, 'r', encoding='utf-8')
        file_content = file.read()
        response = HttpResponse(file_content, content_type='text/plain')
        response['Content-Disposition'] = f'attachment; filename="{f"{note.created_at}74852951skjghfygsd{note.id}"}"'
        return response
    
    
class SwapViewSet(ModelViewSet):
    ordering_fields = ["final_amount", "amount_of_additions", "created_at", "sawapprove_date", "approved_at", "send_date", "created_at" ]
    search_fields = ['case']
    filterset_fields = ["swap_or_refund", "refund_type", "payment_type", "new_device", "sawapprove", "send_to_financial"]
    
    permission_classes = [IsAuthenticated]
    queryset = Swap.objects.all().order_by("-id")
    serializer_class = SwapCreateSerializer
    
    def get_serializer_class(self):
        # Use different serializers for different actions
        if self.action == "list":
            return SwapListSerializer
        elif self.action == "retrieve":
            return SwapDetailSerializer
        return super().get_serializer_class()  
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        return super().perform_create(serializer)


# class CloneSwapView(APIView):
#     permission_classes = [IsAuthenticated]
    
#     def get(self, request, *args, **kwargs):
#         swap = Swap.objects.get(id=kwargs['pk'])
#         swap = Prototype(swap)
#         final = swap.clone()
#         final.save()
#         return Response("created swap", status=status.HTTP_201_CREATED)
    
    
class ImportSwapView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *arg, **kwargs):
        files = request.FILES['file']
        app_name = "service_app"
        model_name = "Swap"

        try:
            a = HandleFile(files, app_name, model_name, request.user)
            a.handle()
            return Response("Successfully uploaded", status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
class MultipleDeleteSwap(APIView):
    """
    A view for get list ids and deleting  case.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = MultipleDeleteSerializer

    def post(self, request, *args, **kwargs):
        ids = request.data.get('ids')
        if not isinstance(ids, list):
            return Response({"message": "Invalid input. 'ids' should be a list."}, status=status.HTTP_400_BAD_REQUEST)
        list_device = Swap.objects.filter(id__in=ids)
        if list_device.exists():
            list_device.delete()
            return Response({"message": "Deleted successfully"}, status=status.HTTP_200_OK)
        return Response({"detail": "No swap found for the provided IDs."}, status=status.HTTP_404_NOT_FOUND)
    

class SawApproveView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Swap.objects.all()
    serializer_class = AprrovedSawSerializer

    def perform_update(self, serializer):
        serializer.save(sawapprove_by=self.request.user, sawapprove_date = timezone.now())
        return super().perform_update(serializer)
    
    
class AprrovedCompletedView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Swap.objects.all()
    serializer_class = AprrovedCompletedSerializer
    
    def perform_update(self, serializer):
        serializer.save(financial_approved_by=self.request.user, send_date = timezone.now())
        return super().perform_update(serializer)