from django.contrib import admin
from .models import Post
from django.forms import TextInput, Textarea
from django.db import models


# class YourModelAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.CharField: {'widget': TextInput(attrs={'size': '20'})},
#         models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
#     }


# admin.site.register(Post, YourModelAdmin)

admin.site.register(Post)
