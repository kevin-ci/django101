from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm

def view_blogs(request):
    blogs = Blog.objects.all()
    context = { "blogs": blogs }
    return render(request, 'blog/index.html', context)

def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BlogForm()
        context = {"form" : form}
        return render(request, 'blog/create_blog.html', context)