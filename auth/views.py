import jwt

from datetime import datetime, timedelta, timezone

from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import AuthenticationFailed


def generate_access_token(user):
    now = datetime.now(timezone.utc)

    payload = {
        "user_id": user.id,
        "username": user.username,
        "token_type": "access",
        "iat": now,
        "exp": now + timedelta(minutes=30),
    }

    token = jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm="HS256"
    )

    return token


def generate_refresh_token(user):
    now = datetime.now(timezone.utc)

    payload = {
        "user_id": user.id,
        "username": user.username,
        "token_type": "refresh",
        "iat": now,
        "exp": now + timedelta(days=7),
    }

    token = jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm="HS256"
    )

    return token


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {
                    "message": "Username and password are required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(
            username=username,
            password=password
        )

        if user is None:
            return Response(
                {
                    "message": "Invalid username or password"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        if not user.is_active:
            return Response(
                {
                    "message": "User account is disabled"
                },
                status=status.HTTP_403_FORBIDDEN
            )

        access_token = generate_access_token(user)
        refresh_token = generate_refresh_token(user)

        return Response(
            {
                "access": access_token,
                "refresh": refresh_token
            },
            status=status.HTTP_200_OK
        )


class RefreshTokenAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        refresh_token = request.data.get("refresh")

        if not refresh_token:
            return Response(
                {
                    "message": "Refresh token is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            payload = jwt.decode(
                refresh_token,
                settings.SECRET_KEY,
                algorithms=["HS256"]
            )

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Refresh token expired")

        except jwt.InvalidTokenError:
            raise AuthenticationFailed("Invalid refresh token")

        token_type = payload.get("token_type")

        if token_type != "refresh":
            raise AuthenticationFailed("Invalid token type")

        user_id = payload.get("user_id")

        if not user_id:
            raise AuthenticationFailed("Invalid token payload")

        try:
            user = User.objects.get(id=user_id)

        except User.DoesNotExist:
            raise AuthenticationFailed("User not found")

        if not user.is_active:
            raise AuthenticationFailed("User account is disabled")

        new_access_token = generate_access_token(user)

        return Response(
            {
                "access": new_access_token
            },
            status=status.HTTP_200_OK
        )