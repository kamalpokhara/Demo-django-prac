from django.shortcuts import render

# Create your views here.
# def login_view(req):
#     pass
# def register_view(req):
#     pass
# def logout_view(req):
#     pass

from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Hi " + user.username + ", welcome back!")
            return redirect("articles:home")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("articles:home")


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        gender = request.POST.get("gender")

        if User.objects.filter(
            username=username, email=email, phone=phone, gender=gender
        ).exists():
            messages.error(request, "User with this information already exists.")
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                phone=phone,
                gender=gender,
            )
            login(request, user)
            messages.success(request, "Registration successful! You are now logged in.")
            return redirect("articles:home")
    return render(request, "register.html")
