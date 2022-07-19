from django.core.exceptions import BadRequest
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ReplyForm
from .models import Message


def message_details(request, message_id):
    message = get_object_or_404(Message, id=message_id)

    if request.method == "POST":
        if not request.user.is_authenticated:
            raise BadRequest
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.message = message
            reply.created_by = request.user
            reply.save()
            return redirect(message)
    else:
        form = ReplyForm()

    return render(request, "messages/message.html", {"message": message, "form": form})

