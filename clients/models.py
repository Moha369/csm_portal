from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    client_name = models.CharField(max_length=100)
    client_ID = models.CharField(max_length=100)
    client_linkedinurl = models.CharField(
        max_length=150, default="Linkedin Profile...")
    client_salesforceurl = models.CharField(
        max_length=150, default="Salesforce Profile...")
    client_password = models.CharField(max_length=100, default="***")
    client_products = (
        ('Analytics', 'Analytics Only'),
        ('Datafeeds', 'Datafeeds Only'),
        ('Analytics, Datafeeds', 'Analytics & Datafeeds'),
        ('MRT', 'Media Ratings Tool'),
    )
    client_products = models.CharField(max_length=100, choices=client_products)

    client_notes = models.TextField(default="Notes Here...")
    client_FTP = models.CharField(max_length=100, default="ftp://")
    client_API_login = models.CharField(max_length=100, default="")
    client_API_password = models.CharField(max_length=100, default="")
    date_posted = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
