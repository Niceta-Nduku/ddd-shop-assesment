from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Get url for store detail view.
        Returns:
            str: URL for store detail.
        """
        return reverse("store:detail", kwargs={"name": self.name})

