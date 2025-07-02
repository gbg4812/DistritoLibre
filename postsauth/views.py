from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import UserManager, User
from django.contrib.auth.password_validation import validate_password
from django.conf import settings
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseForbidden,
    JsonResponse,
)
from django.views.decorators.http import require_POST, require_GET
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

from postsauth.models import DistritoLibreUser
from .serializers import UserSrializer
import enum
import json
# Create your views here.


class StateCodes(enum.IntEnum):
    OPERATION_SUCCESSFUL = 0
    ALTERNATIVE_OPERATION = 1
    BAD_DATA = 2
    OPERATION_FAILURE = 3


def new_state_response(state: StateCodes, message: str | None = None):
    return {"state": state, "message": message}


@require_POST
def login_view(request: HttpRequest) -> HttpResponse:
    data: dict = json.loads(request.body)
    username = data["username"]
    password = data["password"]
    print(username, password)

    user = authenticate(request, password=password, username=username)
    if user is not None:
        login(request, user)
        serializer = UserSrializer(user)
        return JsonResponse(serializer.data)

    return HttpResponseForbidden()


@require_POST
@login_required()
def logout_view(request: HttpRequest):
    logout(request)
    return JsonResponse(new_state_response(StateCodes.OPERATION_SUCCESSFUL))


@require_GET
@login_required()
def user_info(request: HttpRequest):
    if request.user.is_authenticated:
        user = UserSrializer(request.user)
        return JsonResponse(user.data)
    return HttpResponseBadRequest()


@require_POST
def register_request(request: HttpRequest):
    data: dict = json.loads(request.body)
    username = data["username"]
    password = data["password"]
    email = data["email"]

    try:
        validate_password(password)
        code = settings.OTP_OBJECT.now()

        user = User.objects.create_user(
            username=username, password=password, email=email, email_code=code
        )
        user.validate_unique()
        user.is_active = False
        user.save()

        send_mail(
            "Distrito Libre CONFIRMATION CODE",
            f"Your code is: <h1>{code}</h1>",
            settings.EMAIL_ADDRESS,
            [email],
            html_message=f"Your code is: <h1>{code}</h1>",
        )
        return JsonResponse(
            new_state_response(StateCodes.OPERATION_SUCCESSFUL, "Code Required")
        )
    except ValidationError:
        return HttpResponseBadRequest(
            new_state_response(StateCodes.BAD_DATA, "Username exists or wrong password")
        )


@require_POST
def register_code(request: HttpRequest):
    data: dict = json.loads(request.body)
    code = data["code"]
    username = data["username"]
    code = settings.OTP_OBJECT.now()
    user = User.objects.get(username=username)

    if settings.OTP_OBJECT.verify(code) and user.distritolibreuser.code == code:
        user.is_active = True
        return HttpResponse(new_state_response(StateCodes.OPERATION_SUCCESSFUL))
    return HttpResponseBadRequest(
        new_state_response(StateCodes.BAD_DATA, "Bad verification code")
    )
