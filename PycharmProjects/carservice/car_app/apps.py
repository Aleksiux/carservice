from django.apps import AppConfig


class CarAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'car_app'

    def ready(self):
        from .signals import create_profile, save_profile



