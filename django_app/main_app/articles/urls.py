from django.urls import path

from . import views
from .views import SignUp, Login, logoutView

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", SignUp.as_view(), name="signup"),
    path("", Login.as_view(), name="signin"),
    path("logout/", logoutView, name="logout"),
    path("add_article/", views.add_article, name="new_article"),
    path("article/<int:id>", views.view_article, name="article"),
    path("articles/", views.article_list, name="articles_list"),
    path("articles/<int:page>/", views.article_list, name="articles_list"),

]