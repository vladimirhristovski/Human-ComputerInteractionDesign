from django.apps import AppConfig


class EstateShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'estate_shop'

    def ready(self):
        from . import signals
