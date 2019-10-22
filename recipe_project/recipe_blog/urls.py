from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="recipe-blog-home"),
    path('about/', views.about, name="recipe-blog-about"),

]
