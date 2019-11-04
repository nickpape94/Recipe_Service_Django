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
    ('East European', 'EAST EUROPEAN'),
    ('French', 'FRENCH'),
    ('Greek', 'GREEK'),
    ('Indian', 'INDIAN'),
    ('Italian', 'ITALIAN'),
    ('Japanese', 'JAPANESE'),
    ('Korean', 'KOREAN'),
    ('Mexican', 'MEXICAN'),
    ('North African', 'NORTH AFRICAN'),
    ('Pakistani', 'PAKISTANI'),
    ('Portuguese', 'PORTUGUESE'),
    ('South American', 'SOUTH AMERICAN'),
    ('Spanish', 'SPANISH'),
    ('Thai', 'THAI'),
    ('Turkish', 'TURKISH'),
    ('Other', 'OTHER')
)


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

    class Meta:
        verbose_name_plural = "posts"

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
