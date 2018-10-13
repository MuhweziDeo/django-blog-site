from django.shortcuts import render
# Create your views here.
posts = [
    {
        'author': 'dee',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'August 27,2018'
    },

    {
        'author': 'dee2',
        'title': 'Blog Post 2',
        'content': 'second Post content',
        'date_posted': 'August 7,2018'
    }

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
