from django.contrib.auth.decorators import login_required
from django.http import (
    HttpRequest,
    HttpResponseBadRequest,
    HttpResponseForbidden,
    HttpResponseServerError,
    JsonResponse,
    HttpResponse,
)
from django.views.decorators.http import require_GET, require_POST, require_http_methods

from postsauth.views import StateCodes, new_state_response
from .models import Post, TagBuilding
from .serializers import PostsSerializer
from django.db.models import Count


@require_GET
def post_list(request: HttpRequest) -> HttpResponse:
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


@require_http_methods(["GET", "DELETE"])
def post(request: HttpRequest, id: int) -> HttpResponse:
    try:
        query = Post.objects.get(pk=id)

        post = PostsSerializer(query)

        if request.method == "GET":
            return JsonResponse(post.data)
        if request.method == "DELETE":
            if request.user.is_authenticated and request.user == query.author:
                query.delete()
                return JsonResponse(new_state_response(StateCodes.OPERATION_SUCCESSFUL))
            else:
                return HttpResponseForbidden()
    except Post.DoesNotExist:
        return HttpResponseBadRequest(
            new_state_response(StateCodes.BAD_DATA, "Post does not exist")
        )
    return HttpResponseServerError()


@require_POST
@login_required()
def new_post(request: HttpRequest):
    author = request.user
    title = request.POST["title"]
    newpst = Post.objects.update_or_create(title=title, author=author)
    newpst[0].content = request.POST["content"]
    newpst[0].description = request.POST["description"]
    newpst[0].icon = request.POST["icon"]
    print("Adding new post ", newpst)
    newpst[0].save()

    return JsonResponse(new_state_response(StateCodes.OPERATION_SUCCESSFUL))


@require_GET
def buildings_view(request: HttpRequest) -> HttpResponse:
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
    return HttpResponseBadRequest(
        new_state_response(StateCodes.BAD_DATA, "Tag not provided")
    )
