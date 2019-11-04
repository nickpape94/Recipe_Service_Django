from django.test import TestCase, Client
from django.urls import reverse
from recipe_blog.models import Post
from django.contrib.auth.models import User
from users.models import Profile
import json


class TestViews(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username="Jake")
        self.post1 = Post.objects.create(recipe="Pie", description="foo",
                                         cuisine="Turkish", ingredients="bar",
                                         method="stir", author=self.user1)
        self.client = Client()
        self.postlist_url = reverse('recipe-blog-home')
        self.searchlist_url = reverse('search')
        self.userpostlist_url = reverse('user-posts', args=['Jake'])

    def test_project_postlist_GET(self):
        response = self.client.get(self.postlist_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_blog/home.html')
