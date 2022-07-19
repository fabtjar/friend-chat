from django.db import models
from django.urls import reverse

from accounts.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Message(Post):
    recipient = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("message_details", kwargs={"message_id": self.id})


class Reply(Post):
    message = models.ForeignKey(Message, related_name="replies", on_delete=models.CASCADE)
