from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.conf import settings
from django.db.models import Q
from users.models import Profile


CUISINE_CHOICES = (
    ('African', 'AFRICAN'),
    ('American', 'AMERICAN'),
    ('British', 'BRITISH'),
    ('Caribbean', 'CARIBBEAN'),
    ('Chinese', 'CHINESE'),
    ('Other', 'OTHER')
)


class PostQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(recipe__icontains=query) |
                         Q(cuisine__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()
        return qs


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class Post(models.Model):
    image = models.ImageField(default='no_photo.jpg',
                              upload_to='media/recipe_pics', blank=True)
    recipe = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    cuisine = models.CharField(
        max_length=50, choices=CUISINE_CHOICES, default='Other')
    ingredients = models.TextField(unique=True)
    method = models.TextField(unique=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = PostManager()

    def __str__(self):
        return self.recipe

    def get_absolute_url(self):
        return reverse('recipe-blog-home')

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
