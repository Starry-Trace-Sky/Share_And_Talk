from django.apps import AppConfig


class SoftConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'soft'
    verbose_name = '软件'
