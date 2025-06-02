import enum
from django.http import (
    HttpRequest,
    HttpResponseBadRequest,
    HttpResponseForbidden,
    JsonResponse,
    HttpResponse,
)

from .models import Post, Tag, TagBuilding
from django.contrib.auth.models import User
from .serializers import PostsSerializer
from django.db.models import F, Count


class StateCodes(enum.IntEnum):
    OPERATION_SUCCESSFUL = 0
    ALTERNATIVE_OPERATION = 1
    BAD_DATA = 2
    OPERATION_FAILURE = 3


def new_state_response(state: StateCodes, message: str | None = None):
    return {"state": state, "message": message}


def post_list(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        tags = request.GET.getlist("tag")

        ntags = len(tags)

        posts = Post.objects.all()
        if ntags > 0:
            result = (
                posts.filter(tags__name__in=tags)
                .annotate(count=Count("tags"))
                .filter(count=ntags)
            )
        else:
            result = posts

        serializer = PostsSerializer(result, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponseBadRequest()


def post(request: HttpRequest, title: str) -> HttpResponse:
    query = Post.objects.get(title__iexact=title)
    post = PostsSerializer(query)
    if request.method == "GET":
        return JsonResponse(post.data)
    if request.method == "DELETE":
        if request.user.is_authenticated and request.user == query.author:
            query.delete()
            return JsonResponse(new_state_response(StateCodes.OPERATION_SUCCESSFUL))
        else:
            return HttpResponseForbidden()
    return HttpResponseBadRequest()


def new_post(request: HttpRequest):
    if request.user.is_authenticated:
        if request.method == "POST":
            newpst = Post(
                author=request.user,
                title=request.POST["title"],
                content=request.POST["content"],
                description=request.POST["description"],
                icon=request.POST["icon"],
            )
            print("Adding new post ", newpst)
            newpst.save()

            return JsonResponse(new_state_response(StateCodes.OPERATION_SUCCESSFUL))
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseForbidden()


def buildings_view(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        tag = request.GET["tag"]
        if len(tag) > 0:
            btags = TagBuilding.objects.all()
            tag_btags = (
                Post.objects.filter(tags__name=tag)
                .filter(tags__in=btags)
                .values_list("tags", flat=True)
                .distinct()
            )

            result = list(btags.filter(name__in=tag_btags).values("name", "icon"))

            return JsonResponse({"btags": result})
    return HttpResponseBadRequest()
