from django.db import models
from ddd_shop.users.models import User, StoreOwner


class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    owner = models.ForeignKey(StoreOwner, null=True, blank=True, on_delete=models.PROTECT)#,default=defaultOwner)  # store owner can change
    
