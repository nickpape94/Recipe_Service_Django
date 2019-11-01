from django.test import SimpleTestCase
from django.urls import reverse, resolve
from recipe_blog.views import (PostListView,
                               PostDetailView,
                               PostCreateView,
                               PostDeleteView,
                               PostUpdateView,
                               SearchListView,
                               UserPostListView
                               )


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('recipe-blog-home')
        self.assertEquals(resolve(url).func.view_class, PostListView)

    def test_list_url_is_resolved(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func.view_class, SearchListView)

    def test_list_url_is_resolved(self):
        url = reverse('recipe-blog-home')
        self.assertEquals(resolve(url).func.view_class, PostListView)

    def test_list_url_is_resolved(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func.view_class, SearchListView)
