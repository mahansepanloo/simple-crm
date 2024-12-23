from service_app.views import (AgentViewSet, DevicePriceViewSet, DeviceViewSet, MultipleDeleteDevice,CaseCloneView,AgentsCloneView,
                               DeviceCloneView,MultipleDeleteAgents, MultipleDeleteDevicePrice, CaseViewSet, MultipleDeleteCase, DevicePriceCloneView,
                               ImportAgentsView,ImportCaseView, ImportDevicePriceView, ImportDeviceView, CaseSendViewSet, CaseReceiveViewSet,
                               CaseSupervisorApproveViewSet, CaseApproveViewSet, ImportCaseApproveView, ImportCaseReceiveView, 
                               ImportCaseSupervisorApproveView, ImportCaseSendView, MultipleDeleteCaseApprove, MultipleDeleteCaseReceive, 
                               MultipleDeleteCaseSend, MultipleDeleteCaseSupervisorApprove, MultipleDeleteNote, NoteCloneView, NoteViewSet, DownloadNote,
                                SwapViewSet, SawApproveView, ImportSwapView, MultipleDeleteSwap,
                               AprrovedCompletedView,AprrovedCompletedView)
from rest_framework.routers import DefaultRouter
from django.urls import path


router = DefaultRouter()
router.register(r'agent', AgentViewSet, basename='agent')
router.register(r'device-price', DevicePriceViewSet, basename='device-price')
router.register(r'device', DeviceViewSet, basename='device-price-list')
router.register(r"case", CaseViewSet, basename="case")
router.register(r"case-send", CaseSendViewSet, basename="case-send")
router.register(r"case-receive", CaseReceiveViewSet, basename="case-receive")
router.register(r"case-supervisor-approve", CaseSupervisorApproveViewSet, basename="case-supervisor-approve")
router.register(r"case-approve", CaseApproveViewSet, basename="case-approve")
router.register(r"note", NoteViewSet, basename="note")
router.register(r"swap", SwapViewSet, basename="swap")




urlpatterns = [
    path("multiple-delete-device/", MultipleDeleteDevice.as_view(), name="delete_many_device"),
    path("multiple-delete-agent/", MultipleDeleteAgents.as_view(), name="delete_many_agent"),
    path("multiple-delete-device-price/", MultipleDeleteDevicePrice.as_view(), name="delete_many_device_price"),
    path("multiple-delete-case/", MultipleDeleteCase.as_view(), name="delete_many_case"),
    path("clone-device/<int:pk>/", DeviceCloneView.as_view(), name="clone_device"),
    path("clone-agent/<int:pk>/", AgentsCloneView.as_view(), name="clone_agent"),
    path("clone-case/<int:pk>/", CaseCloneView.as_view(), name="clone_case"),
    path("clone-device-price/<int:pk>/", DevicePriceCloneView.as_view(), name="clone_device_price"),
    path("import-agents/", ImportAgentsView.as_view(), name="import_agents"),
    path("import-case/", ImportCaseView.as_view(), name="import_case"),
    path("import-device-price/", ImportDevicePriceView.as_view(), name="import_device_price"),
    path("import-device/", ImportDeviceView.as_view(), name="import_device"),
    path("import-case-approve/", ImportCaseApproveView.as_view(), name="import_case_approve"),
    path("import-case-receive/", ImportCaseReceiveView.as_view(), name="import_case_receive"),
    path("import-case-supervisor-approve/", ImportCaseSupervisorApproveView.as_view(), name="import_case_supervisor_approve"),
    path("import-case-send/", ImportCaseSendView.as_view(), name="import_case_send"),
    path("multiple-delete-case-approve/", MultipleDeleteCaseApprove.as_view(), name="delete_many_case_approve"),
    path("multiple-delete-case-receive/", MultipleDeleteCaseReceive.as_view(), name="delete_many_case_receive"),
    path("multiple-delete-case-send/", MultipleDeleteCaseSend.as_view(), name="delete_many_case_send"),
    path("multiple-delete-case-supervisor-approve/", MultipleDeleteCaseSupervisorApprove.as_view(), name="delete_many_case_supervisor_approve"),
    path("multiple-delete-note/", MultipleDeleteNote.as_view(), name="delete_many_note"),
    path("clone-note/<int:pk>/", NoteCloneView.as_view(), name="clone_note"),
    path("download-note/<int:pk>/", DownloadNote.as_view(), name="download_note"),
    path("saw-approve/<int:pk>/", SawApproveView.as_view(), name="saw_approve"),
    path("import-swap/", ImportSwapView.as_view(), name="import_swap"),
    path("multiple-delete-swap/", MultipleDeleteSwap.as_view(), name="delete_many_swap"),
    path("completed-Approve/<int:pk>/", AprrovedCompletedView.as_view(), name="Aprroved_Completed"),
    
    
] + router.urls