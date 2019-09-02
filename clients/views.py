from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from . import api_calls
import requests
import json
import datetime
import time
import dateutil.parser


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

    def render_to_response(self, context, **response_kwargs):
        # pendo api
        pendo_result = api_calls.pendo_data()
        context['pendo_data'] = pendo_result

        # jira api
        jira_result = api_calls.jira_data()
        context['jira_data'] = jira_result['issues']

        return super().render_to_response(context, **response_kwargs)


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
        'client_qaresults'
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
        'client_qaresults'
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
