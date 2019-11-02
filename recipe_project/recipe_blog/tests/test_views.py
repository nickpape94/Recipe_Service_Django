from django.test import TestCase, Client
from django.urls import reverse
from recipe_blog.models import Post
from django.contrib.auth.models import User
from users.models import Profile
import json


class TestViews(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username="Jake")
        self.post1 = Post.objects.create(recipe="Cat", description="j",
                                         cuisine="Turkish", ingredients="1 cat",
                                         method="stir", author=self.user1)
        self.client = Client()
        self.postlist_url = reverse('recipe-blog-home')
        self.searchlist_url = reverse('search')
        self.userpostlist_url = reverse('user-posts', args=['Jake'])
        self.postdetaillist_url = reverse('post-detail', args=[1])

    def test_project_postlist_GET(self):
        response = self.client.get(self.postlist_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_blog/home.html')

    def test_project_searchlist_GET(self):
        response = self.client.get(self.searchlist_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_blog/post_list.html')

    def test_project_userpostlist_GET(self):
        response = self.client.get(self.userpostlist_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_blog/user_posts.html')

    def test_project_postdetaillist_GET(self):
        response = self.client.get(self.postdetaillist_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_blog/post_detail.html')
