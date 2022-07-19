from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.core.exceptions import BadRequest

from posts.forms import MessageForm

from .models import User


def user_show(request, username=None):
    if username is None:
        if request.user.is_authenticated:
            username = request.user.username
        else:
            return redirect("account_login")
    user = get_object_or_404(User, username=username)
    messages = user.received_messages.all()

    if request.method == "POST":
        if not request.user.is_authenticated:
            login_url = reverse("account_login")
            return redirect(f"{login_url}?next={request.path}")
        if request.user == user:
            raise BadRequest("Cannot message yourself.")
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.created_by = request.user
            message.recipient = user
            message.save()
            return redirect(user)
    else:
        form = MessageForm()

    return render(
        request,
        "accounts/profile.html",
        {
            "user": user,
            "form": form,
            "messages": messages,
        }
    )


def user_list(request):
    users = User.objects.all()
    return render(request, "accounts/list_users.html", {"users": users})
