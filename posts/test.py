from posts.models import Post
from django.test import TestCase

# Create your tests here.


class TestPosts(TestCase):
    def setUp(self) -> None:
        Post.objects.create(
            title="My test post",
            description="This is a post generated for testing porpouses",
            content="<h1>Title</h1>\n<h3>Subtittle</h3>\n<p>This is a paragraph!</p>",
            icon="noicon",
        )

    def test_post_post(self):
        p = Post.objects.get(title="My test post")
        self.assertEqual(p.icon, "noicon")
