from django.apps import AppConfig

from django.utils.translation import gettext_lazy as _

class SalesConfig(AppConfig):
    name = 'ddd_shop.sales'
    verbose_name = _("Sales")

    def ready(self):
        try:
            import ddd_shop.sales.signals  # noqa F401
        except ImportError:
            pass