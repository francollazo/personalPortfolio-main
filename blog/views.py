from django.shortcuts import render, get_object_or_404
from .models import Project

def all_blogs(request):
    blogs = Project.objects.all()
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})

def blog_list(request):
    blogs = Project.objects.all()  # Select all
    return render(request, 'blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Project, id=blog_id)  # Select by ID
    return render(request, 'blog_detail.html', {'blog': blog})