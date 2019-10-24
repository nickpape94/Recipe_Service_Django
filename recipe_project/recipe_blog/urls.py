from django.urls import path
from .views import PostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name="recipe-blog-home"),
    path('about/', views.about, name="recipe-blog-about"),

]
