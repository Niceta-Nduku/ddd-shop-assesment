from django.apps import AppConfig

from django.utils.translation import gettext_lazy as _

class BranchConfig(AppConfig):
    name = 'ddd_shop.branch'

    verbose_name = _("Branch")

    def ready(self):
        try:
            import ddd_shop.branch.signals  # noqa F401
        except ImportError:
            pass
