from django.urls import path

from . import views

urlpatterns = [
    path("", views.post_list),
    path("<int:userid>/", views.user_posts),
    path("new/", views.new_post),
]
