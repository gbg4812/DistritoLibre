from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login_view),
    path("logout/", views.logout_view),
    path("userinfo/", views.user_info),
    path("register/", views.register_request),
    path("verify/", views.register_code),
]
