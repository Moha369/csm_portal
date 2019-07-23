from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import requests


class Post(models.Model):
    client_name = models.CharField(max_length=100)
    client_ID = models.CharField(max_length=100)
    client_password = models.CharField(max_length=100)
    client_products = models.CharField(max_length=100, default="")
    client_FTP = models.CharField(max_length=100)
    client_API_login = models.CharField(max_length=100)
    client_API_password = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


'''
Code block for the use of API's.
Pendo API to allow tracking of dashboard useage
Saleforces API to allow placement of things such as a contract dates
'''

# Pendo API
# url = f'https://app.pendo.io/api/v1/visitor/{client_ID}/history'
# params = {
#     "starttime": "1506341326000"
# }
# headers = {
#     'x-pendo-integration-key': "PENDO_API_KEY",
#     'content-type': "application/x-www-form-urlencoded"
# }
# response = requests.get(url, headers=headers, params=params)
