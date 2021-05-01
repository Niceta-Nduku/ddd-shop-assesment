from django.contrib import admin
from ddd_shop.branch.models import Store

# Register your models here.
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):

    list_display = ["name","location","owner"]
    fields = ["name","location",("owner")]
 