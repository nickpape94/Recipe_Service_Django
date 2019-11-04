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
        self.userpostlist1_url = reverse('user-posts', args=['James'])
        self.postdetaillist_url = reverse('post-detail', args=[1])
        self.postcreatelist_url = reverse('post-create')
        self.postdeletelist_url = reverse('post-delete', args=[1])

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

    def test_project_postcreatelist_POST_new_post(self):

        self.user2 = User.objects.create_user(username="Jerry")
        self.post2 = Post.objects.create(recipe="Milkshake", description="foo",
                                         cuisine="Italian", ingredients="oof",
                                         method="Wisk", author=self.user2)

        response = self.client.post(self.postcreatelist_url, {
            'recipe': "Milkshake",
            'description': "foo",
            'cuisine': "Italian",
            'ingredients': "bar",
            'method': "Wisk",
            'author': self.user2
        }
        )

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.user2.username, "Jerry")
        self.assertEquals(self.post2.recipe, "Milkshake")

    def test_project_detail_DELETE_delete_post(self):

        self.user3 = User.objects.create_user(username="James")
        self.post3 = Post.objects.create(recipe="Apple pie", description="apple",
                                         cuisine="British", ingredients="apple",
                                         method="Bake it", author=self.user3)

        # response = self.client.delete(self.postcreatelist_url, {
        #     'recipe': "Milkshake",
        #     'description': "foo",
        #     'cuisine': "Italian",
        #     'ingredients': "bar",
        #     'method': "Wisk",
        #     'author': self.user2
        # }
        # )
        new_post = self.post1
        response = self.client.delete(self.postdeletelist_url)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(new_post.recipe.count("Pie"), 1)
