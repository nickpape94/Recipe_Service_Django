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

    def test_postlist_url_resolves(self):
        url = reverse('recipe-blog-home')
        self.assertEquals(resolve(url).func.view_class, PostListView)

    def test_searchlist_url_resolves(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func.view_class, SearchListView)

    def test_userpostlist_url_resolves(self):
        url = reverse('user-posts', args=['some user'])
        self.assertEquals(resolve(url).func.view_class, UserPostListView)

    def test_postdetail_url_resolves(self):
        url = reverse('post-detail', args=[2])
        self.assertEquals(resolve(url).func.view_class, PostDetailView)

    def test_postcreate_url_resolves(self):
        url = reverse('post-create')
        self.assertEquals(resolve(url).func.view_class, PostCreateView)

    def test_postupdate_url_resolves(self):
        url = reverse('post-update', args=[1])
        self.assertEquals(resolve(url).func.view_class, PostUpdateView)

    def test_postdelete_url_resolves(self):
        url = reverse('post-delete', args=[3])
        self.assertEquals(resolve(url).func.view_class, PostDeleteView)
