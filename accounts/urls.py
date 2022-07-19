from django.urls import path

from . import views


urlpatterns = [
    path('', views.user_list, name="list_users"),
    path('profile/', views.user_show, name="my_profile"),
    path('profile/<username>', views.user_show, name="profile"),
]
