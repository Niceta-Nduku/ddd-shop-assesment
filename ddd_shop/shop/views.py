from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UserPassesTestMixin,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    DetailView,
    FormView,
    ListView,
    RedirectView,
    TemplateView,
    UpdateView,
)

from ddd_shop.sales.models import *

from ..decorators import *


class storeDetailView(LoginRequiredMixin,DetailView,UserPassesTestMixin):
    """
    Main Store View  
    """
    model = Store

    slug_field = "name"
    slug_url_kwarg = "name"

    def test_func(self):
        return not self.request.user.is_attendant


class storeAttendantsView(LoginRequiredMixin,ListView):
    """
    View to List of all attendants in a store
    """
    model = StoreAttendant
    # TODO filter by current store
    # def get_queryset(self):
    #     pass

# @method_decorator(owner_only)
class storeListView(LoginRequiredMixin,ListView):
    """
    View to see all stores
    """
    model = Store
    def test_func(self):
        return not self.request.user.is_attendant


class storesListOwnerView(LoginRequiredMixin,ListView):
    """
    View for Owner to see all stores
    """
    model = Store

    def test_func(self):
        return not self.request.user.is_attendant