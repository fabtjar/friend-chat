from django.forms.models import ModelForm

from .models import Message, Reply


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["title", "text"]


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ["title", "text"]
