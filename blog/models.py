from os import times_result
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.forms.widgets import Media


def user_directory(instance, filename):
    return 'user_{0}/{1}'.format(instance.uploader.username, filename)

class Post(models.Model):
  title = models.CharField(max_length=300)
  description = models.TextField(blank=True, null=True)
  uploader = models.ForeignKey(User, on_delete=models.CASCADE)
  date_created = models.DateTimeField(auto_now_add=True)
  image = models.FileField(blank=True,upload_to=user_directory, null=True)
  url = models.CharField(max_length=500, blank=True, null= True)



