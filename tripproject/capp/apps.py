from django.apps import AppConfig


class CappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'capp'



class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals