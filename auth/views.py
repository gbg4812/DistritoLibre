from django.contrib.auth import login, authenticate, logout
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseForbidden,
    JsonResponse,
)
from django.http.response import HttpResponseNotAllowed
from .serializers import UserSrializer
import enum
# Create your views here.


class StateCodes(enum.IntEnum):
    OPERATION_SUCCESSFUL = 0
    ALTERNATIVE_OPERATION = 1
    BAD_DATA = 2
    OPERATION_FAILURE = 3


def new_state_response(state: StateCodes, message: str | None = None):
    return {"state": state, "message": message}


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            serializer = UserSrializer(user)
            return JsonResponse(serializer.data)

        return HttpResponseForbidden()

    return HttpResponseBadRequest()


def logout_view(request: HttpRequest):
    logout(request)
    return JsonResponse(new_state_response(StateCodes.OPERATION_SUCCESSFUL))


def user_info(request: HttpRequest):
    if request.method == "GET" and request.user.is_authenticated:
        user = UserSrializer(request.user)
        return JsonResponse(user.data)
    return HttpResponseBadRequest()
