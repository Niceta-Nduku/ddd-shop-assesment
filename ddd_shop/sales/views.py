from ddd_shop.sales.models import *
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, TemplateView, FormView
from .forms import UploadFileForm
User = get_user_model()


class SaleUploadView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, FormView):

    template_name = "templates/store/salesUpload.html"
    success_message = _("Sale uploaded")
    form_class = None  # in
    wrong_file_format = "Please upload a .csv or .xlsx file"
    # success_url = # return to store view

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            filename = request.FILES['file']
            if filename.lower().endswith('.xlsx', '.csv'):
                form.save()
            else:
                return self.form_invalid(form)  # reload and request proper file
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class SaleUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """ 
    View to modify sale file
    """
    success_message = _("Sale modified")
    model = SaleFile

    def get_object(self):
        return self.request.salefile


class showArchivedFiles(LoginRequiredMixin):
    """
    View for opening archived files
    """
    #access only for store owner and admin
    pass


class CommentView(LoginRequiredMixin, DetailView):
    """
    View for making a comment on a sale
    """
    # acess for store owner only
    pass


class allSalesView(LoginRequiredMixin):
    """
    View to see all sales in a store
    """
    pass


class salesDetailView(LoginRequiredMixin, DetailView):
    """
    View for a sale item 
    """
    # view to looking at a single sale item filter
    pass

class totalSaleView(LoginRequiredMixin, DetailView):
    """
    View for the total sale of an item
    """

