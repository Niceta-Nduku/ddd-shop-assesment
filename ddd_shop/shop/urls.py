from django.urls import path
import ddd_shop.sales.urls 
from ddd_shop.shop.views import *
from ddd_shop.sales.views import *


app_name = "shop"
urlpatterns = [
    path("", view=storeListView.as_view(), name="stores"),
    path("<str:name>/attendants/",view=storeAttendantsView.as_view(),name="attendants"), 
    path("<str:name>/sales", view=allSalesView, name="sales"),
    path("<str:name>/sales/<int:year>/<int:month>/<int:day>",view =storeSales),
    path("<int:pk>", view=storeDetailView, name="store-detail"),
]