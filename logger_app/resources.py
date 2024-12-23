from import_export import resources  
from logger_app.models import Loggers


class LoggerResource(resources.ModelResource):
    class Meta:
        model = Loggers