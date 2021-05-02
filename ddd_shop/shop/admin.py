from django.contrib import admin
from ddd_shop.shop.models import Store

# Register your models here.
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):

    list_display = ["name","location"]
    fields = ["name","location"]
 