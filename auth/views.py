from django.contrib.auth import login, logout, authenticate
from django.http import HttpRequest, HttpResponseBadRequest, HttpResponseRedirect
# Create your views here.


def login_view(request: HttpRequest):
    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, password=password, username=username)
    if user != None:
        login(request, user)
        return HttpResponseRedirect("/")
    else:
        return HttpResponseBadRequest()
