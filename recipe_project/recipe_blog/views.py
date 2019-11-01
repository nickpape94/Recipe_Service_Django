from itertools import chain
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'recipe_blog/home.html', context)


class SearchListView(ListView):
    model = Post
    template_name = 'recipe_blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    # def get_template_names(self):
    #     return ['recipe_blog/post_list.html']

    def get_queryset(self):
        query = self.request.GET.get('q')
        pollist = Post.objects.all().order_by('-date_posted')
        if query:
            pollist = pollist.filter(
                Q(recipe__icontains=query) |
                Q(cuisine__icontains=query)
            )

        return(pollist)


class PostListView(ListView):
    model = Post
    template_name = 'recipe_blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'recipe_blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['image', 'recipe', 'description',
              'cuisine', 'ingredients', 'method']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['image', 'recipe', 'description',
              'cuisine', 'ingredients', 'method']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'recipe_blog/about.html', {'title': 'About'})
