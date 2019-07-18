from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post


@login_required
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'clients/home.html', context)


def about(request):
    return render(request, 'clients/about.html', {'title': 'about!!'})


def links(request):
    return render(request, 'clients/links.html', {'title': 'links!!'})
