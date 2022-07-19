from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    following = models.ManyToManyField("accounts.User", related_name="followed_by")

    def get_absolute_url(self):
        return reverse("profile", kwargs={"username": self.username})
