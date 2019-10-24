from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView)
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'recipe_blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'recipe_blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['recipe', 'description']


def about(request):
    return render(request, 'recipe_blog/about.html', {'title': 'About'})
