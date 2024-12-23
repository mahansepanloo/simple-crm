from django.contrib import admin
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin  
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin  
from user_app.resources import UserResource

admin.site.unregister(User)
@admin.register(User)
class UserAdmin(ImportExportModelAdmin, DefaultUserAdmin):
    resource_class = UserResource