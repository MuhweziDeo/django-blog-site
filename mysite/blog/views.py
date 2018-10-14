from django.shortcuts import render
from .models import Post
# Create your views here.
posts=Post.objects.all()
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
  