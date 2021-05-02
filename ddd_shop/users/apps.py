from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "ddd_shop.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import ddd_shop.users.sipgnals  # noqa F401
        except ImportError:
            pass
