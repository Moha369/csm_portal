from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from jira.client import JIRA
import requests
import json


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
    '''
        This view will hold infomation from Pendo / Salesforce and Jira
        using their APIs to display the infomation.
    '''
    model = Post
    template_name = 'clients/post_detail.html'

    # Test API ---

    def coindesk(self):
        response = requests.get(
            'https://api.coindesk.com/v1/bpi/currentprice.json')
        data = response.json()
        return data['disclaimer']

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context['base'] = self.coindesk()
        return context

    #  Salesforce API ---
    #  Pendo API ---
    #  Jira Cloud API ---
    def jira_tickets(self):
        jira = JIRA(options={'server': 'https://pixalate.atlassian.net'},
                    basic_auth=('paulb@pixalate.com', 'iqKaAYoiFfbY8P3uVrA6AEBB'))
        issue = jira.issue('CS-2917')
        return issue

    def get_jira_context(self, *args, **kwargs):
        context = super(PostDetailView, self).get_jira_context(
            **args, **kwargs)
        context['jira_data'] = self.jira_tickets()
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        'client_name',
        'client_ID',
        'client_password',
        'client_products',
        'client_notes',
        'client_FTP',
        'client_API_login',
        'client_API_password',
        'client_linkedinurl',
        'client_salesforceurl',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = [
        'client_name',
        'client_ID',
        'client_password',
        'client_products',
        'client_notes',
        'client_FTP',
        'client_API_login',
        'client_API_password',
        'client_linkedinurl',
        'client_salesforceurl',
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
