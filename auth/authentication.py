import jwt

from django.conf import settings
from django.contrib.auth.models import User

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class CustomJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return None

        if not auth_header.startswith("Bearer "):
            raise AuthenticationFailed("Invalid authorization header")

        token = auth_header.split(" ")[1]

        try:
            payload = jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=["HS256"]
            )

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token expired")

        except jwt.InvalidTokenError:
            raise AuthenticationFailed("Invalid token")

        token_type = payload.get("token_type")

        if token_type != "access":
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

        return (user, token)