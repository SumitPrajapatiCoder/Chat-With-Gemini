from django.urls import path
from . import views

urlpatterns = [
    path("", views.chat_view, name="chat"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("clear/", views.clear_chat, name="clear_chat"),
    path("download/txt/", views.download_txt, name="download_txt"),
    path("health/", views.health_check, name="health_check"),
]
