from django.test import TestCase
from django.urls import reverse, resolve
from recipe_blog.models import Post
from django.contrib.auth.models import User
from users.models import Profile
from users.forms import UserCreationForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm


class setUp(self):
    self.user1 = User.objects.create_user(username="test")

    def tearDown(self):
        self.user.delete()
