from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post




# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'HOME'
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts' # This is the name of the context object that will be used in the template
    ordering = ['-date_posted'] # This is the order in which the posts will be displayed


class PostDetailView(DetailView):
    model = Post
    

def about(request):
    return render(request, 'blog/about.html',{'title': 'ABOUTTT'})