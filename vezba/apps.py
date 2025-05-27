from django.apps import AppConfig


class VezbaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vezba'

    def ready(self):
        from . import signals
