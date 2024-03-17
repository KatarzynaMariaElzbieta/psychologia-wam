from django.urls import path

from . import views
from .views import SignUp, Login, logoutView

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", SignUp.as_view(), name="signup"),
    path("", Login.as_view(), name="signin"),
    path("logout/", logoutView, name="logout"),

]