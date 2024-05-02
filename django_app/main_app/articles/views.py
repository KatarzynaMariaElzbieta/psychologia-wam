from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from articles.forms import SignUpForm, LoginForm


def index(request):
    """Main view generating"""
    return render(request, "base.html")


class SignUp(View):
    """Registration view"""

    def get(self, request):
        """Registration form display"""
        form = SignUpForm()
        return render(request, "sign-up.html", {"form": form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data["user_name"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(
                user_name, password=password, first_name=first_name, last_name=last_name
            )
            if user is not None:
                if user.is_authenticated:
                    login(self.request, user)
            return render(request, "my-data.html", {"user": user})
        return render(request, 'sign-up.html', {'form': form})


class Login(View):
    """System Login Form.
    In order to log in, you need to fill in the 'LoginForm' form with your login and password.
    If you enter a non-existent login or an incorrect password, the message "Login error. Try again."
    If the correct data is entered, the user is redirected to the home page.
    """

    def get(self, request):
        if request.user.is_anonymous:
            form = LoginForm()
            print(request.user.username)
            return render(request, "sign-in.html", {"form": form})
        else:
            print("else")
            return redirect("/")

    def post(self, request):
        form = LoginForm(request.POST)
        ctx = {"form": form}
        if form.is_valid():
            username = form.cleaned_data["login"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_authenticated:
                    login(self.request, user)
                    return redirect("/")
            form = LoginForm()
            ctx["notlog"] = "Błąd logowania. Spróbuj jeszcze raz."
            ctx["form"] = form
        return render(request, "sign-in.html", ctx)


def logoutView(request):
    """ Logging out of the application. After logging out, it takes you to a page with a from form to log in."""
    logout(request)
    return redirect(reverse("signin"))
