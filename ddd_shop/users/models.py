from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class StoreItem(models.Model):

    name = models.CharField(max_length=50)
    decription = models.CharField(max_length=100)  # extra information
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)


class User(AbstractUser):
    """Default user for ddd_shop."""

    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class StoreOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    items = models.ManyToManyField(StoreItem, blank=True)
    # defaultOwner = User.objects.get(username='SuperAdmin')
    owner = models.ForeignKey(StoreOwner, null=True, on_delete=models.PROTECT)#,default=defaultOwner)  # store owner can change


class StoreAttendant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)


# class SaleFile(models.Model):

#     uploadTime = models.DateTimeField()
#     defaultStore = Store.objects.create(name='Imara Daima DDD', location='Imara Daima')
#     # if store is deleted does all data?
#     store = models.ForeignKey(Store, default=defaultStore, on_delete=models.CASCADE)
#     defaultAttendant = User.objects.get(username='defaultAttendant')  # a dafault attendant
#     attendant = models.ForeignKey(StoreAttendant, default=defaultAttendant, on_delete=models.PROTECT)
# #     # fileName = models.FileField(upload_to=) #TODO: determine upload location

