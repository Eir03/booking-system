from django.contrib import admin
from django import apps
from django.db import models

def register_model(model: models.Model) -> models.Model:
    """Регистрирует модель данных в административную панель

    Args:
        model (django.db.models.Model): Класс модели данных в Django

    Returns:
        django.db.models.Model: Модель данных
    """
    admin.site.register(model)
    return model