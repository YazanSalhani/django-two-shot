from django.shortcuts import render, redirect
from accounts.forms import LogInForm, SignUPForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
# Create your views here.
def login(request):
    if request.method =="POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(
                request,
                username=username,
                password=password)

            if user is not None:
                auth_login(request, user,)
                return redirect("home")
    else:
        form = LogInForm()
    context = {
        "form": form
    }

    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("login")


def signup(request):
    if request.method == "POST":
        form =SignUPForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_confirmation = form.cleaned_data["password_confirmation"]

            if password == password_confirmation:
                user = User.objects.create_user(
                    username,
                    password=password,
                )
                auth_login(request, user)
                return redirect("home")
            else:
                form.add_error("password", "the passwords do not match")

    else:
        form = SignUPForm()
    context = {
        "form": form
    }
    return render(request, "accounts/signup.html", context)
