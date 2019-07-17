from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'clients/home.html', context)


def about(request):

    return render(request, 'clients/about.html', {'title': 'about!!'})

