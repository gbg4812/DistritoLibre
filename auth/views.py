from django.contrib.auth import login, authenticate, logout
from django.http import (
    HttpRequest,
    HttpResponseBadRequest,
    HttpResponseForbidden,
    JsonResponse,
)
from django.http.response import HttpResponseNotAllowed
from .serializers import UserSrializer
# Create your views here.


def login_view(request: HttpRequest):
    username = request.POST["username"]
    password = request.POST["password"]

    print(username)
    print(password)

    user = authenticate(request, password=password, username=username)
    if user is not None:
        login(request, user)
        serializer = UserSrializer(user)
        return JsonResponse(serializer.data)
    else:
        return HttpResponseForbidden()


def logout_view(request: HttpRequest):
    logout(request)
