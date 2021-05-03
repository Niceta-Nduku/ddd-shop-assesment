from django.urls import path
import ddd_shop.sales.urls 
from ddd_shop.store.views import *
from ddd_shop.sales.views import *


app_name = "store"
urlpatterns = [
    path("", view=storeListView.as_view(), name="stores"),
    path("<str:name>/attendants/",view=storeAttendantsView.as_view(),name="attendants"), 
    path("<str:name>/sales", view=allSalesView, name="sales"),
    path("<str:name>", view=storeDetailView.as_view(), name="store-detail"),
]