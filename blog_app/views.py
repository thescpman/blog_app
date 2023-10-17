from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Blog
from .forms import BlogForm
# Create your views here.
def index(request):
    return render(request, 'blog_app/index.html')
@login_required
def blogs(request):
    blog_items = Blog.objects.filter(owner=request.user).order_by('date_added')
    context = {'blogs':blog_items}
    return render(request, 'blog_app/blogs.html', context)
@login_required
def newblog(request):
    if request.method != 'POST':
        #No data submitted; create a blank form
        form = BlogForm()
    else:
        #Post data submitted; process data
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            form.save()
            return redirect('blog_app:blogs')
        
    context = {'form':form}
    return render(request, 'blog_app/new_blog.html', context)
@login_required
def edit_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if blog.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = BlogForm(instance=blog)
    else:
        form = BlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_app:blogs')
    context = {'blog':blog, 'form':form}
    return render(request, 'blog_app/edit_blog.html', context)