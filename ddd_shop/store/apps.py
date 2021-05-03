from django.apps import AppConfig

from django.utils.translation import gettext_lazy as _

class ShopConfig(AppConfig):
    name = 'ddd_shop.store'

    verbose_name = _("store")

    def ready(self):
        try:
            import ddd_shop.store.signals  # noqa F401
        except ImportError:
            pass
