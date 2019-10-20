from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Nick',
        'title': 'post 1',
        'content': 'first post content',
        'date_posted': '10/10/2019'
    },
    {
        'author': 'Jane',
        'title': 'post 2',
        'content': 'second post content',
        'date_posted': '10/10/2019'
    }


]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'recipe_blog/home.html', context)


def about(request):
    return render(request, 'recipe_blog/about.html', {'title': 'oifdvpiv'})
