from django.http import (
    HttpRequest,
    HttpResponseBadRequest,
    HttpResponseForbidden,
    JsonResponse,
    HttpResponse,
)

from .models import Post
from django.contrib.auth.models import User
from .serializers import PostsSerializer


def post_list(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        tags = request.GET.getlist("tag")

        posts = Post.objects.all()
        for tag in tags:
            posts = posts.filter(tags__name=tag)

        serializer = PostsSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponseBadRequest()


def user_posts(request: HttpRequest, userid: int):
    print(userid)
    print(User.objects.get(id=userid))
    if not request.user == User.objects.get(id=userid):
        return HttpResponseForbidden()
    else:
        data = {"posts": list(Post.objects.all().filter(author__id=userid).values())}
        return JsonResponse(data)


def new_post(request: HttpRequest):
    if request.user.is_authenticated:
        if request.method == "POST":
            print(request.POST["title"])
            newpst = Post(
                author=request.user,
                title=request.POST["title"],
                content=request.POST["file"],
            )
            print(newpst)
            newpst.save()

            return JsonResponse({"result": "success!"})
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseForbidden()
