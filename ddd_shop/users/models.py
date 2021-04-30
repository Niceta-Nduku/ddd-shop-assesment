from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for ddd_shop."""

    ADMIN = 1
    STOREOWNER = 2 
    STOREATTENDANT = 3

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

# class StoreOwner(models.Model):
# user = models.
#email

# 

#     def __str__(self):
#         return f

# class StoreAttendant(models.Model):

#     def

#class Store(models.Model):

