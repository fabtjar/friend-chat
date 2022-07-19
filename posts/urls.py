from django.urls import path

from . import views


urlpatterns = [
    path("<int:message_id>", views.message_details, name="message_details"),
]
