from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_migrate


@receiver(post_migrate)
def create_groups(sender, **kwargs):
    """Добавляет роли пользователей в систему после того как выполняется миграция данных"""
    Group.objects.get_or_create(name='ADMIN')
    Group.objects.get_or_create(name='TECH-ADMIN')
    Group.objects.get_or_create(name='SERVICE-MANAGER')
    Group.objects.get_or_create(name='RESEPTION')