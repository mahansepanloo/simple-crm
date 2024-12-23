import csv
from django.apps import apps
from django.core.exceptions import ValidationError
from io import TextIOWrapper
from django.db import models


class HandleFile:
    def __init__(self, files, app_name, model_name, user):
        self.files = files
        self.app_name = app_name
        self.model_name = model_name
        self.user = user

    def handle(self):
        HandleCsv(self.files, self.app_name, self.model_name, self.user).handle()


class HandleCsv:
    def __init__(self, files, app_name, model_name, user):
        self.files = files
        self.app_name = app_name
        self.model_name = model_name
        self.user = user

    def handle(self):
        model = apps.get_model(self.app_name, self.model_name)

        if model is None:
            raise ValidationError(f"Model '{self.model_name}' does not exist in app '{self.app_name}'.")

        fields = [field.name for field in model._meta.get_fields()]

        csv_file = TextIOWrapper(self.files.file, encoding='utf-8')
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)

        for row in headers:
            if row not in fields:
                raise ValidationError(f"Header '{row}' does not exist in the {self.model_name}.")

        foreign_keys = {
            field.name: field.related_model for field in model._meta.get_fields() if isinstance(field, models.ForeignKey)
        }

        for row in csv_reader:
            data = dict(zip(headers, row))
            self._handle_foreign_keys(data, foreign_keys)

            if data.get('id'):
                obj = model.objects.update_or_create(id=data['id'], defaults=data)
            else:
                data.pop('id', None) 
                obj = model.objects.create(**data, created_by=self.user)

    def _handle_foreign_keys(self, data, foreign_keys):
        for key, related_model in foreign_keys.items():
            if key in data:
                try:
                    data[key] = related_model.objects.get(id=data[key])
                except related_model.DoesNotExist:
                    raise ValidationError(f"{related_model.__name__} with id {data[key]} does not exist.")
