from django.apps import AppConfig

from django.utils.translation import gettext_lazy as _

class ShopConfig(AppConfig):
    name = 'ddd_shop.shop'

    verbose_name = _("Shop")

    def ready(self):
        try:
            import ddd_shop.shop.signals  # noqa F401
        except ImportError:
            pass
