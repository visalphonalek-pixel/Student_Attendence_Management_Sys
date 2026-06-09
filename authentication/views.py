import jwt
from datetime import datetime, timedelta, timezone
from django.conf import settings
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse


def generate_access_token(user):
    now = datetime.now(timezone.utc)
    payload = {
        "user_id": user.id,
        "username": user.username,
        "token_type": "access",
        "iat": now,
        "exp": now + timedelta(minutes=30),
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is None or not user.is_active:
            return render(request, "authentication/login.html", {
                "error": "Invalid username or password"
            })

        token = generate_access_token(user)
        response = redirect("/dashboard/")
        response.set_cookie(
            "access_token",
            token,
            httponly=True,
            samesite="Lax"
        )
        return response

    return render(request, "authentication/login.html")


def logout_view(request):
    response = redirect("/login/")
    response.delete_cookie("access_token")
    return response