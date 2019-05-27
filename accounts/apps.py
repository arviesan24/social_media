from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        from actstream import registry
        # register `User` model for acstream signals
        registry.register(self.get_model('User'))
        # register signals for the app
        from . import signals
