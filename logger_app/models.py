from django.db import models
from django.contrib.auth.models import User
class Loggers(models.Model):
    user = models.CharField(max_length=100)
    user_ip = models.GenericIPAddressField()
    date = models.DateTimeField(auto_now_add=True)
    view = models.CharField(max_length=200, null=True, blank=True)
    view_method = models.CharField(max_length=100)
    request = models.TextField(null=True, blank=True)
    response = models.TextField(null=True, blank=True)
    status_code = models.PositiveIntegerField()
    query_params = models.TextField(null=True, blank=True)
