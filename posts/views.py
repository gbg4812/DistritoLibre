from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Post
from .serializers import PostsSerializer


@csrf_exempt
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostsSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)
