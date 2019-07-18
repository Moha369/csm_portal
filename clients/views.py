from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


@login_required
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'clients/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'clients/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['client_ID']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        'client_name',
        'client_ID',
        'client_products',
        'client_password',
        'client_FTP',
        'client_API_login',
        'client_API_password',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = [
        'client_name',
        'client_ID',
        'client_products',
        'client_password',
        'client_FTP',
        'client_API_login',
        'client_API_password',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'clients/about.html', {'title': 'about!!'})


def links(request):
    return render(request, 'clients/links.html', {'title': 'links!!'})
