from functools import wraps
import json

from django.http import HttpRequest, HttpResponseForbidden
import enum


class StateCodes(enum.IntEnum):
    OPERATION_SUCCESSFUL = 0
    ALTERNATIVE_OPERATION = 1
    BAD_DATA = 2
    OPERATION_FAILURE = 3


def new_state_response(state: StateCodes, message: str | None = None):
    return json.dumps({"state": state, "message": message})


def login_required(view):
    @wraps(view)
    def wrapper(request: HttpRequest, *args, **kwds):
        if request.user.is_authenticated:
            return view(request, *args, **kwds)
        else:
            return HttpResponseForbidden(
                new_state_response(StateCodes.BAD_DATA, "User must be loged in!")
            )

    return wrapper
