from import_export import resources  
from service_app.models import Device, Agents, DevicePrice, Case, CaseApprove, CaseSend, CaseReceive, CaseSupervisorApprove, Note, Swap


class DeviceResource(resources.ModelResource):  
    class Meta:  
        model = Device  

class AgentsResource(resources.ModelResource):  
    class Meta:  
        model = Agents


class DevicePriceResource(resources.ModelResource):  
    class Meta:  
        model = DevicePrice


class CaseResource(resources.ModelResource):
    class Meta:
        model = Case


class CaseApproveResource(resources.ModelResource):
    class Meta:
        model = CaseApprove
        

class CaseSendResource(resources.ModelResource):
    class Meta:
        model = CaseSend
        
        
class CaseReceiveResource(resources.ModelResource):
    class Meta:
        model = CaseReceive
        
        
class CaseSupervisorApproveResource(resources.ModelResource):
    class Meta:
        model = CaseSupervisorApprove
        

class NoteResource(resources.ModelResource):
    class Meta:
        model = Note
        

class SwapResource(resources.ModelResource):
    class Meta:
        model = Swap
        

