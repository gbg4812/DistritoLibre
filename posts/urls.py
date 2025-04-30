from django.urls import path

from . import views

urlpatterns = [
    path("", views.post_list),
    path("btags/", views.buildings_view),
    path("new/", views.new_post),
    path("detail/<str:title>/", views.post),
]
