from django.db import models
from ddd_shop.users.models import StoreAttendant
from ddd_shop.shop.models import Store

class StoreItem(models.Model):

    name = models.CharField(max_length=50)
    decription = models.CharField(max_length=100)  # extra information
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Sales(models.Model):
    item = models.ForeignKey(to=StoreItem,on_delete=models.DO_NOTHING)
    amount = models.FloatField()
    comment = models.CharField(max_length=200,blank=True,null=True)
    date = models.DateField(auto_created=True)

    def __str__(self):
        return f'{self.item},{self.amount}'

def file_directory_path(instance, filename):
    """
    File path for uploading sale file. 
    "MEDIA_ROOT/<store_name>/<date of Upload>/<uploaddatetime_attendant_fileID>
    """
    extension = filename.split('.')[-1] #file extension
    store = instance.store.name #
    date = instance.date#day of sale
    attendant = instance.attendant.user.username
    date_time = instance.uploadTime 

    filename = '{0}_{1}_{2}.{3}'.format(date_time,attendant,instance.id,extension)
    return '{0}/{1}/{2}'.format(store,date,filename)

class SaleFile(models.Model):

    uploadTime = models.DateTimeField(auto_now=True)
    date = models.DateField(auto_created=True) #date of sale
    store = models.ForeignKey(Store, on_delete=models.DO_NOTHING)
    attendant = models.ForeignKey(StoreAttendant, on_delete=models.DO_NOTHING,null=True)
    fileName = models.FileField(upload_to=file_directory_path)

