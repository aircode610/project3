from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signin", views.signin, name="signin"),
    path("verify", views.verify, name="verify"),
    path("add_user", views.add_user, name="add_user"),
    path("login", views.login, name="login"),
    path("login_user", views.login_user, name="login_user"),
    path("logout", views.logout, name="logout"),
    path("order", views.order, name="order")
]
