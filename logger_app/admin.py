from django.contrib import admin
from  logger_app.models import Loggers
from import_export.admin import ImportExportModelAdmin  
from logger_app.resources import LoggerResource


@admin.register(Loggers)
class LoggerAdmin(ImportExportModelAdmin):
    list_display = ["user", "user_ip", "date", "view", "view_method", "status_code"]
    search_fields = ["user", "user_ip", "date", "view", "view_method", "status_code"]
    resource_class = LoggerResource