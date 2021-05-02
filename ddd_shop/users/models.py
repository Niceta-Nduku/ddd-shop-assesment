from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from ddd_shop.shop.models import Store


class User(AbstractUser):
    """Default user for ddd_shop."""
    
    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None
    last_name = None

    is_owner = models.BooleanField(
        _('owner status'),
        default=False,
        help_text="Designates whether this user is the owner of a store",
    )
    is_attendant = models.BooleanField(
        _('attendant status'),
        default=False,
        help_text="Designates whether this user is a store attendant",
    )

    def get_absolute_url(self):
        """Get url for user's detail view.
        Returns:
            str: URL for user detail.
        """
        return reverse("users:detail", kwargs={"username": self.username})

    def __str__(self):
        return self.name


class StoreOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    store = models.ManyToManyField(to=Store, blank=True)  # made this to prevent circular import


class StoreAttendant(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(to=Store, on_delete=models.DO_NOTHING)
