from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
import requests
import json
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
    #  Salesforce API ---

    #  Jira Cloud API ---
    def jira_tickets(self):
        jira_url = 'https://pixalate.atlassian.net/rest/api/2/search?jql=project=CS'

        jira_r = requests.get(jira_url, auth=(
            'paulb@pixalate.com', 'iqKaAYoiFfbY8P3uVrA6AEBB'))

        data = jira_r.json()

        # client_name = ['client_name']
        # client_ID = ['client_ID']

        client_name = 'Fox TV'
        client_ID = 'tv'

        for ticket in data['issues']:
            ticket_number = ticket['key']
            summary = ticket['fields']['summary']
            # assignee = ticket['fields']['assignee']['name']
            status = ticket['fields']['status']['name']
            updated = dateutil.parser.parse(ticket['fields']['updated'])
            ticket_url = 'https://pixalate.atlassian.net/browse/' + \
                ticket['key']
            client = ticket['fields']['customfield_10907'][0]['value']

            if status != 'Closed' and client_name in client or client_ID.upper() in client:

                ticket_dict = {
                    'ticket_number': ticket_number,
                    'summary': summary,
                    # 'assignee': assignee,
                    'status': status,
                    'updated': updated,
                    'url': ticket_url,
                    'client_id': client
                }

                return ticket_dict

    def get_jira_context(self, **kwargs):
        context = super(PostDetailView, self).get_jira_context(**kwargs)
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
