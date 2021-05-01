from django.db import models
from users.models import StoreAttendant

class StoreItem(models.Model):

    name = models.CharField(max_length=50)
    decription = models.CharField(max_length=100)  # extra information
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Sales(models.Model):
    item = models.ForeignKey(to=StoreItem,on_delete=DO_NOTHING)
    amount = models.FloatField()
    comment = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return f'{self.item},{self.amount}'

class SaleFile(models.Model):

    uploadTime = models.DateTimeField()
    attendant = models.ForeignKey(StoreAttendant, on_delete=models.DO_NOTHING)
    # fileName = models.FileField(upload_to=) #TODO: determine upload location

