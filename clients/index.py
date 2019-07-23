from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Post


@register(Post)
class Post(AlgoliaIndex):
    fields = ('client_name', 'client_ID')
    settings = {'searchableAttributes': ['client_name', 'client_ID']}
    index_name = 'dev_PIXALATECLIENTS'
