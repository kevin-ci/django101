from django.urls import path

from . import views

urlpatterns = [
    path("", views.view_blogs, name="index"),
    path("create_blog", views.create_blog, name="create"),
]