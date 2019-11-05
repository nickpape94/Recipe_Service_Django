import json
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from django.test import TestCase
from recipe_blog.models import Post
from django.contrib.auth.models import User
from users.models import Profile
# from . import models
from django.db.models import CharField, TextField, ForeignKey


class TestModels(TestCase):

    def setUp(self):
        user1 = User.objects.create_user(username="Jake")
        Post.objects.create(recipe="Pie", description="foo",
                                   cuisine="Turkish", ingredients="bar",
                                   method="stir", author=user1)

    def test_post_creation(self):
        post = Post.object.get(id=1)
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(post.__str__(), post.recipe)

    def test_string_representation(self):
        post = Post(recipe="Fries")
        self.assertEquals(str(post), post.recipe)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Post._meta.verbose_name_plural), "posts")

    def test_post_creation(self):
        post = Post.objects.get(id=1)
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(post.__str__(), post.recipe)

    # Testing model fields

    def test_recipe_field(self):
        post = Post.objects.get(id=1)
        field = Post._meta.get_field('recipe')
        self.assertTrue(isinstance(field, CharField))

    def test_description_field(self):
        post = Post.objects.get(id=1)
        field = Post._meta.get_field('description')
        self.assertTrue(isinstance(field, CharField))

    def test_cuisine_field(self):
        post = Post.objects.get(id=1)
        field = Post._meta.get_field('cuisine')
        self.assertTrue(isinstance(field, CharField))

    def test_ingredients_field(self):
        post = Post.objects.get(id=1)
        field = Post._meta.get_field('ingredients')
        self.assertTrue(isinstance(field, TextField))

    def test_method_field(self):
        post = Post.objects.get(id=1)
        field = Post._meta.get_field('method')
        self.assertTrue(isinstance(field, TextField))

    def test_author_field(self):
        post = Post.objects.get(id=1)
        field = Post._meta.get_field('author')
        self.assertTrue(isinstance(field, ForeignKey))

    # Testing models

    def test_recipe_label(self):
        post = Post.objects.get(id=1)
        expected_post_recipe = post.recipe
        self.assertEquals(expected_post_recipe, "Pie")

    def test_description_label(self):
        post = Post.objects.get(id=1)
        expected_post_description = post.description
        self.assertEquals(expected_post_description, "foo")

    def test_recipe_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('recipe').verbose_name
        self.assertEquals(field_label, 'recipe')

    def test_name_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('recipe').max_length
        self.assertEquals(max_length, 200)

    def test_get_absolute_url(self):
        post = Post.objects.get(id=1)
        self.assertEquals(post.get_absolute_url(), '/')

    def test_str_equal_to_title(self):
        post = Post.objects.get(id=1)
        self.assertEquals(str(post), post.recipe)
