from django.apps import AppConfig

class ManageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'manage'

    # def ready(self):
    #     from .app_config import ManageContainer
    #     self.container = ManageContainer()
    #     self.container.wire(modules=[self.name])