from django.contrib import admin
from ddd_shop.store.models import Store

# Register your models here.
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):

    list_display = ["name","location"]
    fields = ["name","location"]
 