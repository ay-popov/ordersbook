from django.urls import path

from .views import MeView, LoginView, LogoutView

app_name = "myauth"

urlpatterns = [

    # Страница после авторизации
    path("me/", MeView, name="me"),

    path("login/", LoginView.as_view(), name="login"),

    path("logout/", LogoutView.as_view(), name="logout"),
]