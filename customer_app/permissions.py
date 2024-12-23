from rest_framework import permissions




class IsSupporter(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and  request.user.groups.filter(name='support').exists()
    
    
class IsFinance(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and  request.user.groups.filter(name='finance').exists()
         


class CanEditSupport(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated and  request.user.groups.filter(name='support').exists():
            return request.method in ['GET', 'PATCH', 'PUT']
        return False


class CanViewSupport(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.user.is_authenticated and  request.user.groups.filter(name='support').exists():
            return request.method in ['GET']
        return False
    
    
class CanDeleteSupport(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.groups.filter(name='support').exists():
            return request.method in ['GET', "DELETE"]
        return False
    
    
class CanCreatedSupport(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.groups.filter(name='support').exists():
            return request.method in ["POST"]
        return False






class CanEditFinance(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.groups.filter(name='finance').exists():
            return request.method in ['GET', 'PATCH', 'PUT']
        return False


class CanViewFinance(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.groups.filter(name='finance').exists():
            return request.method in ['GET']
        return False
    
    
class CanDeleteFinance(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.groups.filter(name='finance').exists():
            return request.method in ['GET', "DELETE"]
        return False
    
    
class CanCreatedFinance(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.groups.filter(name='finance').exists():
            return request.method in ["POST"]
        return False
    


    

