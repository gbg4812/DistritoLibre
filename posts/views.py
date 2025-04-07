from django.http import JsonResponse
from .models import Post
from .serializers import PostsSerializer


def post_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostsSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)
