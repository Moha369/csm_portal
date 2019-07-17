from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    client_name = models.CharField(max_length=100)
    client_ID = models.CharField(max_length=100)
    client_password = models.CharField(max_length=100)
    client_FTP = models.CharField(max_length=100)
    client_API_login = models.CharField(max_length=100)
    client_API_password = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.client_name

