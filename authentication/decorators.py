import jwt
from django.conf import settings
from django.shortcuts import redirect
from functools import wraps


def jwt_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        token = request.COOKIES.get("access_token")

        if not token:
            return redirect("/login/")

        try:
            payload = jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=["HS256"]
            )
            request.jwt_payload = payload
        except jwt.ExpiredSignatureError:
            return redirect("/login/")
        except jwt.InvalidTokenError:
            return redirect("/login/")

        return view_func(request, *args, **kwargs)
    return wrapper