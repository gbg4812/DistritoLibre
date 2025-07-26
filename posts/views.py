import json
from django.http import (
    HttpRequest,
    HttpResponseBadRequest,
    HttpResponseForbidden,
    HttpResponseServerError,
    JsonResponse,
    HttpResponse,
)
from django.views.decorators.http import require_GET, require_POST, require_http_methods

from postsauth.auth_decorators import new_state_response, StateCodes, login_required
from .models import Post, TagBuilding, Tag
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
                return HttpResponse(new_state_response(StateCodes.OPERATION_SUCCESSFUL))
            else:
                return HttpResponseForbidden()
    except Post.DoesNotExist:
        return HttpResponseBadRequest(
            new_state_response(StateCodes.BAD_DATA, "Post does not exist")
        )
    return HttpResponseServerError()


@require_POST
@login_required
def new_post(request: HttpRequest):
    data = json.loads(request.body)
    author = request.user
    title = data["title"]
    newpst, _ = Post.objects.update_or_create(title=title, author=author)
    newpst.content = data["content"]
    newpst.description = data["description"]
    newpst.icon = data["icon"]
    for tagobj in data["tags"]:
        print(tagobj)
        tag = Tag.objects.get(name=tagobj["name"])
        newpst.tags.add(tag)

    print("Adding new post ", newpst)
    newpst.save()

    return HttpResponse(new_state_response(StateCodes.OPERATION_SUCCESSFUL))


@require_GET
def buildings_view(request: HttpRequest) -> HttpResponse:
    tag = request.GET["tag"]
    if len(tag) > 0:
        tag_btags = TagBuilding.objects.filter(post__tags__name=tag).values(
            "name", "icon"
        )

        result = list(tag_btags)

        return JsonResponse({"btags": result})
    return HttpResponseBadRequest(
        new_state_response(StateCodes.BAD_DATA, "Tag not provided")
    )
